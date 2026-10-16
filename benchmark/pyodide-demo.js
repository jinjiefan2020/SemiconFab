/**
 * MIMAC-2026 In-Browser Pyodide Demo Controller (benchmark/pyodide-demo.js)
 * Manages Web Worker lifecycle, state machine, metric rendering, and session history.
 */

(function () {
  "use strict";

  const POLICY_DESCRIPTIONS = {
    fifo: {
      en: "First-In, First-Out (SPEC §5.1): Priority given to lots with earliest queue entry timestamp.",
      zh: "先进先出（规范 §5.1）：优先派发最早进入当前工步等待队列的晶圆批次。",
    },
    spt: {
      en: "Shortest Processing Time (SPEC §5.2): Lowest step processing duration; ties broken by FIFO.",
      zh: "最短加工时间（规范 §5.2）：优先派发当前工步耗时最短的批次；工步耗时相同时按 FIFO 决序。",
    },
    edd: {
      en: "Earliest Due Date (SPEC §5.3): Earliest assigned order due date; ties broken by FIFO.",
      zh: "最早交期（规范 §5.3）：优先派发承诺交付日期最近的批次；相同时按 FIFO 决序。",
    },
    cr: {
      en: "Critical Ratio (SPEC §5.4): CR = (due_date - current_time) / remaining_workload. Late lots (CR < 0) are strictly prioritized over on-time lots.",
      zh: "临界比例（规范 §5.4）：CR = (交期 - 当前时间) / 剩余工时。拖期批次 (CR < 0) 获得绝对最高优先级，拖期最严重者先排。",
    },
  };

  let worker = null;
  let currentState = "idle";
  let workerIsInitialized = false;
  let timerInterval = null;
  let runStartTime = 0;
  let runIndex = 0;
  const historyRuns = [];

  function formatNumber(val, decimals = 2) {
    if (val === null || val === undefined || isNaN(val)) return "-";
    return Number(val).toLocaleString(undefined, {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals,
    });
  }

  function initWorker() {
    if (worker) return worker;

    try {
      worker = new Worker("benchmark/pyodide-worker.js");
    } catch (err) {
      handleError("Worker initialization failed: " + err.message, "init");
      return null;
    }

    worker.onmessage = (e) => {
      const data = e.data;
      if (!data) return;

      if (data.type === "status") {
        setState(data.stage, data.details);
      } else if (data.type === "success") {
        workerIsInitialized = true;
        handleSuccess(data.result);
      } else if (data.type === "error") {
        handleError(data.error || "Unknown worker error", data.stage);
      }
    };

    worker.onerror = (err) => {
      handleError(err.message || "Web Worker execution error", currentState);
    };

    return worker;
  }

  function setState(state, details) {
    currentState = state;
    const runBtn = document.getElementById("demo-run-btn");
    const statusBox = document.getElementById("demo-status-box");
    const statusTextEn = document.getElementById("demo-status-text-en");
    const statusTextZh = document.getElementById("demo-status-text-zh");
    const progressBar = document.getElementById("demo-progress-bar");
    const spinner = document.getElementById("demo-spinner");
    const errorBox = document.getElementById("demo-error-box");

    if (errorBox) errorBox.style.display = "none";

    if (state === "idle") {
      if (runBtn) runBtn.disabled = false;
      if (statusBox) statusBox.style.display = "none";
      if (progressBar) progressBar.style.width = "0%";
      stopTimer();
    } else if (state === "loading-pyodide") {
      if (runBtn) runBtn.disabled = true;
      if (statusBox) statusBox.style.display = "block";
      if (spinner) spinner.style.display = "block";
      if (statusTextEn)
        statusTextEn.textContent =
          "Loading Pyodide runtime (~10MB) from jsdelivr CDN...";
      if (statusTextZh)
        statusTextZh.textContent =
          "正在从 jsdelivr CDN 加载 Pyodide WebAssembly 运行时（约 10MB）...";
      if (progressBar) progressBar.style.width = "25%";
    } else if (state === "installing-simpy") {
      if (runBtn) runBtn.disabled = true;
      if (statusBox) statusBox.style.display = "block";
      if (spinner) spinner.style.display = "block";
      if (statusTextEn)
        statusTextEn.textContent =
          "Installing simpy & initializing numpy in WASM...";
      if (statusTextZh)
        statusTextZh.textContent =
          "正在 WASM 环境中安装 simpy 并初始化 numpy...";
      if (progressBar) progressBar.style.width = "50%";
    } else if (state === "loading-model") {
      if (runBtn) runBtn.disabled = true;
      if (statusBox) statusBox.style.display = "block";
      if (spinner) spinner.style.display = "block";
      if (statusTextEn)
        statusTextEn.textContent =
          "Loading MIMAC-2026 simulator and fab configuration...";
      if (statusTextZh)
        statusTextZh.textContent =
          "正在加载 MIMAC-2026 仿真模型与晶圆厂物理配置...";
      if (progressBar) progressBar.style.width = "75%";
    } else if (state === "running") {
      if (runBtn) runBtn.disabled = true;
      if (statusBox) statusBox.style.display = "block";
      if (spinner) spinner.style.display = "block";
      if (progressBar) progressBar.style.width = "88%";
      startTimer();
    } else if (state === "done") {
      if (runBtn) runBtn.disabled = false;
      if (spinner) spinner.style.display = "none";
      if (progressBar) progressBar.style.width = "100%";
      stopTimer();
    } else if (state === "error") {
      if (runBtn) runBtn.disabled = false;
      if (spinner) spinner.style.display = "none";
      stopTimer();
    }
  }

  function startTimer() {
    stopTimer();
    runStartTime = Date.now();
    updateRunningStatus();
    timerInterval = setInterval(updateRunningStatus, 500);
  }

  function stopTimer() {
    if (timerInterval) {
      clearInterval(timerInterval);
      timerInterval = null;
    }
  }

  function updateRunningStatus() {
    const elapsed = Math.round((Date.now() - runStartTime) / 1000);
    const statusTextEn = document.getElementById("demo-status-text-en");
    const statusTextZh = document.getElementById("demo-status-text-zh");
    if (statusTextEn) {
      statusTextEn.textContent = `Running simulation in browser WASM (10-day warmup + 60-day run)... ${elapsed}s elapsed (typically 15–45s)`;
    }
    if (statusTextZh) {
      statusTextZh.textContent = `正在浏览器 WASM 中运行仿真（10 天预热 + 60 天运行）... 已耗时 ${elapsed} 秒（通常耗时 15–45 秒）`;
    }
  }

  function handleSuccess(result) {
    setState("done");
    const statusBox = document.getElementById("demo-status-box");
    const statusTextEn = document.getElementById("demo-status-text-en");
    const statusTextZh = document.getElementById("demo-status-text-zh");
    const duration = result.wall_clock_sec
      ? result.wall_clock_sec.toFixed(1)
      : result.runtime_sec.toFixed(1);

    if (statusBox) statusBox.style.display = "block";
    if (statusTextEn) {
      statusTextEn.innerHTML = `<strong>Simulation finished in ${duration}s!</strong> (Simulated runtime: ${result.runtime_sec.toFixed(1)}s, ${result.completed_lots} lots completed)`;
    }
    if (statusTextZh) {
      statusTextZh.innerHTML = `<strong>仿真完成，总耗时 ${duration} 秒！</strong>（仿真内部耗时 ${result.runtime_sec.toFixed(1)} 秒，共完工 ${result.completed_lots} 批次）`;
    }

    renderMetrics(result);
    addToHistory(result);
  }

  function handleError(errorMsg, stage) {
    setState("error");
    showError(errorMsg);
  }

  function showError(msg) {
    const errorBox = document.getElementById("demo-error-box");
    const errorDetail = document.getElementById("demo-error-detail");
    const statusBox = document.getElementById("demo-status-box");
    if (statusBox) statusBox.style.display = "none";
    if (errorBox) {
      errorBox.style.display = "block";
      if (errorDetail) errorDetail.textContent = msg;
    }
  }

  function renderMetrics(res) {
    const resultsContainer = document.getElementById("demo-results");
    if (resultsContainer) resultsContainer.style.display = "block";

    document.getElementById("metric-cycle-time").textContent =
      formatNumber(res.mean_cycle_time_days, 2) + " d";
    document.getElementById("metric-tardiness").textContent =
      formatNumber(res.mean_tardiness_days, 2) + " d";
    document.getElementById("metric-throughput").textContent =
      formatNumber(res.throughput_wafers_per_day, 1) + " w/d";
    document.getElementById("metric-wip").textContent =
      formatNumber(res.mean_wip, 1) + " lots";
    document.getElementById("metric-bottleneck").textContent =
      (res.bottleneck_utilization * 100).toFixed(2) + "%";
    document.getElementById("metric-completed-lots").textContent =
      res.completed_lots.toLocaleString() + " lots";
    document.getElementById("metric-runtime").textContent =
      (res.wall_clock_sec
        ? res.wall_clock_sec.toFixed(1)
        : res.runtime_sec.toFixed(1)) + " s";
  }

  function addToHistory(res) {
    runIndex++;
    const runItem = { index: runIndex, ...res };
    historyRuns.unshift(runItem);

    const emptyHint = document.getElementById("demo-history-empty");
    const tbody = document.getElementById("demo-history-tbody");
    if (emptyHint) emptyHint.style.display = "none";
    if (tbody) {
      const row = document.createElement("tr");
      row.style.animation = "fadeIn 0.3s ease";
      row.innerHTML = `
        <td><strong>#${runItem.index}</strong></td>
        <td><span class="badge-tag badge-warning" style="text-transform: uppercase; font-size: 11px;">${runItem.policy}</span></td>
        <td><code>${runItem.seed}</code></td>
        <td><strong>${formatNumber(runItem.mean_cycle_time_days, 2)} d</strong></td>
        <td>${formatNumber(runItem.mean_tardiness_days, 2)} d</td>
        <td>${formatNumber(runItem.throughput_wafers_per_day, 1)}</td>
        <td>${formatNumber(runItem.mean_wip, 1)}</td>
        <td>${(runItem.bottleneck_utilization * 100).toFixed(2)}%</td>
        <td>${runItem.completed_lots.toLocaleString()}</td>
        <td>${(runItem.wall_clock_sec || runItem.runtime_sec).toFixed(1)}s</td>
      `;
      tbody.prepend(row);
    }
  }

  function updatePolicyDesc() {
    const sel = document.getElementById("demo-policy-select");
    const descEn = document.getElementById("demo-policy-desc-en");
    const descZh = document.getElementById("demo-policy-desc-zh");
    if (!sel) return;
    const val = sel.value;
    const desc = POLICY_DESCRIPTIONS[val] || POLICY_DESCRIPTIONS.fifo;
    if (descEn) descEn.textContent = desc.en;
    if (descZh) descZh.textContent = desc.zh;
  }

  function runSimulation() {
    const policySelect = document.getElementById("demo-policy-select");
    const seedInput = document.getElementById("demo-seed");
    const policy = policySelect ? policySelect.value : "fifo";
    const seed = seedInput ? parseInt(seedInput.value, 10) || 42 : 42;

    const w = initWorker();
    if (!w) return;

    if (workerIsInitialized) {
      setState("running");
    } else {
      setState("loading-pyodide");
    }
    w.postMessage({ type: "run", policy, seed });
  }

  window.addEventListener("DOMContentLoaded", () => {
    const runBtn = document.getElementById("demo-run-btn");
    const policySelect = document.getElementById("demo-policy-select");

    if (runBtn) {
      runBtn.addEventListener("click", runSimulation);
    }

    if (policySelect) {
      policySelect.addEventListener("change", updatePolicyDesc);
      updatePolicyDesc();
    }
  });
})();
