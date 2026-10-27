<!-- SemiconFab.org — Source-available 300mm Wafer Fab Digital Twin Platform -->

# SemiconFab

SemiconFab is a source-available 300mm logic semiconductor wafer fabrication digital twin and equipment catalog platform combining first-principles cleanroom visualization, discrete-event scheduling benchmarks, and crowdsourced equipment taxonomy.

> **License Notice**: This project is released under the **PolyForm Noncommercial License 1.0.0** (source-available). Commercial use requires a separate license — contact info@semiconfab.org.

---

## Architecture Map

```
┌────────────────────────────────────────────────────────────────────────┐
│                        SemiconFab Platform                             │
├────────────────────────────────┬───────────────────────────────────────┤
│ 1. 3D Digital Twin             │ Cleanroom ballroom, subfab MEP loops, │
│    (/twin, twin.html)          │ SEMI E10 stack lights, AMHS monorail  │
├────────────────────────────────┼───────────────────────────────────────┤
│ 2. Equipment Catalog           │ 167 normalized OEM equipment records, │
│    (/catalog-demo.html,        │ 5 data provenance tiers, 13 process   │
│     catalog.json, schema.json) │ categories, Schema v1.0 standard     │
├────────────────────────────────┼───────────────────────────────────────┤
│ 3. MIMAC-2026 Benchmark        │ 18 tool groups, 217 machines, 3 logic │
│    (/benchmark, benchmark.html,│ products (A/B/C), Gym API (FabEnv),   │
│     benchmark/simulator/)      │ SimPy discrete-event simulation engine │
├────────────────────────────────┼───────────────────────────────────────┤
│ 4. Submission & Verification   │ Crowdsourced equipment prefill form,  │
│    (/add-equipment,            │ client-side Schema v1.0 validation,   │
│     /verification)             │ cryptographic provenance audit trail  │
├────────────────────────────────┼───────────────────────────────────────┤
│ 5. Pure Static Hosting         │ Cloudflare Pages global static edge,  │
│    (wrangler.toml)             │ zero serverless runtime, zero DB      │
└────────────────────────────────┴───────────────────────────────────────┘
```

- **Fab Data Layer (`/fab-data-layer`, `fab-data-layer.html`)**: 5-layer fab data flow architecture and shop-floor signal propagation teaching model.
- **Fab Operations (`/fab-operations`, `fab-operations.html`)**: Unified map of semiconductor fab operational domains, available modules, and planned topics.
- **MES & Dispatch (`/fab-mes`, `fab-mes.html`)**: Interactive teaching explainer on how MES routes, queues, dispatches, executes, tracks, and holds wafer lots.

> **Cleanroom Digital Twin Sandbox Scope**:  
> 本洁净室为 SemiconFab 概念验证与全谱系设备编目孪生沙盒，集成了前道与后道代表性设备，但机台数量显著少于实际先进制程Fab。_(This cleanroom serves as a SemiconFab proof-of-concept and full-spectrum equipment catalog digital twin sandbox, integrating representative front-end and back-end equipment, with machine counts significantly lower than an actual high-volume advanced node semiconductor fab.)_

---

## Local Development in 3 Steps

1. **Clone the repository and install formatter/linter tools**:

   ```bash
   git clone https://github.com/jinjiefan2020/SemiconFab.git
   cd SemiconFab
   npm install
   ```

2. **Set up Python environment (optional, for benchmark & validator CLI)**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install jsonschema simpy numpy
   ```

3. **Serve locally**:
   ```bash
   npx serve .
   # or
   python3 -m http.server 8000
   ```
   Open `http://localhost:8000/` or `http://localhost:8000/twin` in any modern web browser.

---

## Directory Map

| Path                   | Contents                                                                                   |
| :--------------------- | :----------------------------------------------------------------------------------------- |
| `benchmark/`           | MIMAC-2026 benchmark specifications and machine-readable route definitions (`routes.json`) |
| `benchmark/simulator/` | Standalone MIMAC-2026 SimPy discrete-event simulation benchmark suite and Gymnasium API    |
| `data/`                | Master equipment databases (`semiconductor_equipment_database.json`, `.csv`)               |
| `diagrams/`            | Standalone SVG architectural diagrams and benchmark illustrations                          |
| `downloads/`           | Offline simulator package distribution archives (`mimac2026-simulator.zip`)                |
| `js/`                  | Client-side internationalization dictionaries (`translations.js`, `i18n.js`)               |
| `output/`              | Schema v1.0 migration audit trail and reports (`migration_report.md`, `README.md`)         |
| `scripts/`             | Data synthesis and event trace generation utilities (`generate_twin_events.py`)            |
| `tools/`               | Catalog build pipeline (`build_catalog.py`) and migration tools (`migrate.py`)             |
| `tools/validator/`     | Python CLI and validation package (`schemavalidator`) for Schema v1.0                      |
| `twin/`                | Operational trace event logs (`events-t1-fifo.jsonl`) consumed by the 3D twin              |

---

## Contributing & Code Style

Contributions to equipment taxonomy records, verification benchmarks, and documentation are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and the equipment submission runbook in [SUBMISSION.md](SUBMISSION.md) before submitting pull requests.

Code formatting is enforced via Prettier (`npm run format`) and linted with ESLint (`npm run lint`).

---

## License

This project is source-available software licensed under the [PolyForm Noncommercial License 1.0.0](LICENSE).

Commercial use requires a separate license — contact info@semiconfab.org.
