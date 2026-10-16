/**
 * MIMAC-2026 Pyodide Web Worker (benchmark/pyodide-worker.js)
 * Executes FabSimulator inside browser WebAssembly via Pyodide.
 */
/* global importScripts, loadPyodide */

let pyodide = null;
let isInitialized = false;

function postStatus(stage, details) {
  self.postMessage({ type: "status", stage, details });
}

async function initPyodide() {
  if (isInitialized) return;

  postStatus("loading-pyodide", "Fetching Pyodide WASM runtime from CDN...");
  try {
    importScripts("https://cdn.jsdelivr.net/pyodide/v0.27.7/full/pyodide.js");
  } catch (err) {
    throw new Error("Failed to load Pyodide CDN script: " + err.message);
  }

  try {
    pyodide = await loadPyodide({
      indexURL: "https://cdn.jsdelivr.net/pyodide/v0.27.7/full/",
    });
  } catch (err) {
    throw new Error("Failed to initialize Pyodide runtime: " + err.message);
  }

  postStatus("installing-simpy", "Installing simpy & initializing numpy...");
  try {
    await pyodide.loadPackage(["numpy", "micropip"]);
    const micropip = pyodide.pyimport("micropip");
    try {
      const localWheelUrl = new URL(
        "vendor/simpy-4.1.1-py3-none-any.whl",
        self.location.href,
      ).href;
      await micropip.install(localWheelUrl);
    } catch (wheelErr) {
      console.warn(
        "Could not load local simpy wheel, falling back to micropip.install('simpy')",
        wheelErr,
      );
      await micropip.install("simpy");
    }
  } catch (err) {
    throw new Error("Failed to install Python dependencies: " + err.message);
  }

  postStatus(
    "loading-model",
    "Fetching MIMAC-2026 simulator and fab configuration...",
  );
  try {
    const filesToFetch = [
      { url: "simulator/fab_config.json", path: "/fab_config.json" },
      {
        url: "simulator/mimac2026/__init__.py",
        path: "/mimac2026/__init__.py",
      },
      {
        url: "simulator/mimac2026/baselines.py",
        path: "/mimac2026/baselines.py",
      },
      { url: "simulator/mimac2026/events.py", path: "/mimac2026/events.py" },
      { url: "simulator/mimac2026/gym_api.py", path: "/mimac2026/gym_api.py" },
      { url: "simulator/mimac2026/metrics.py", path: "/mimac2026/metrics.py" },
      { url: "simulator/mimac2026/model.py", path: "/mimac2026/model.py" },
      { url: "simulator/mimac2026/sim.py", path: "/mimac2026/sim.py" },
    ];

    try {
      pyodide.FS.mkdir("/mimac2026");
    } catch (e) {
      // directory might already exist
    }

    for (const f of filesToFetch) {
      const fileUrl = new URL(f.url, self.location.href).href;
      const resp = await fetch(fileUrl);
      if (!resp.ok) {
        throw new Error(`HTTP ${resp.status} fetching ${f.url}`);
      }
      const text = await resp.text();
      pyodide.FS.writeFile(f.path, text, { encoding: "utf8" });
    }

    // Set up sys.path and pre-load config
    pyodide.runPython(`
import sys
if "/" not in sys.path:
    sys.path.insert(0, "/")

from mimac2026.model import FabConfig
from mimac2026.sim import FabSimulator
import json

_fab_config = FabConfig.from_file("/fab_config.json")
`);
    isInitialized = true;
  } catch (err) {
    throw new Error("Failed to load simulator files into WASM: " + err.message);
  }
}

self.onmessage = async (e) => {
  const data = e.data;
  if (!data || data.type !== "run") return;

  const { policy, seed } = data;
  const startTime = performance.now();

  try {
    if (!isInitialized) {
      await initPyodide();
    }

    postStatus(
      "running",
      "Running simulation in WASM (10-day warmup + 60-day run)...",
    );

    pyodide.globals.set("_run_policy", policy);
    pyodide.globals.set("_run_seed", parseInt(seed, 10));

    const pyRunCode = `
_sim = FabSimulator(
    config=_fab_config,
    dispatcher=_run_policy,
    seed=int(_run_seed),
    warmup_days=10.0,
    run_length_days=60.0
)
_metrics = _sim.run()

json.dumps({
    "policy": _run_policy,
    "seed": int(_run_seed),
    "mean_cycle_time_days": float(_metrics.mean_cycle_time_days),
    "mean_tardiness_days": float(_metrics.mean_tardiness_days),
    "throughput_wafers_per_day": float(_metrics.throughput_wafers_per_day),
    "mean_wip": float(_metrics.mean_wip),
    "bottleneck_utilization": float(_metrics.bottleneck_utilization),
    "completed_lots": int(_metrics.completed_lots),
    "runtime_sec": float(_metrics.runtime_sec)
})
`;

    const resultJson = pyodide.runPython(pyRunCode);
    const result = JSON.parse(resultJson);
    const totalWallSec = (performance.now() - startTime) / 1000;
    result.wall_clock_sec = totalWallSec;

    self.postMessage({ type: "success", result });
  } catch (err) {
    self.postMessage({
      type: "error",
      stage: isInitialized ? "running" : "init",
      error: err.message || String(err),
    });
  }
};
