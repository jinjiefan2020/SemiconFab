import json

with open('data/osat-catalog-inlined.json', 'r', encoding='utf-8') as f:
    osat_raw = f.read().strip()

html_content = f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"
    />
    <title>OSAT Packaging & Testing 3D Digital Twin | SemiconFab</title>
    <meta
      name="description"
      content="Interactive 3D Digital Twin for Post-Fab Semiconductor Assembly & Test (OSAT) Facility. 86 production equipment models across 11 packaging & testing process bays: Dicing, Die Attach, Wire Bonding, Flip Chip, Molding, Singulation, Bumping/RDL, Prober, ATE, Handler, and Inspection."
    />
    <link rel="icon" type="image/svg+xml" href="favicon.svg" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap"
      rel="stylesheet"
    />
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="css/semicon-theme.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="js/translations.js"></script>
    <script src="js/i18n.js"></script>
    <style>
      :root {{
        --header-height: 48px;
        --flow-height: 38px;
      }}
      body {{
        margin: 0;
        padding: 0;
        overflow: hidden;
        font-family: "Manrope", system-ui, sans-serif;
        background-color: var(--bg);
        color: var(--ink);
      }}
      .font-mono {{
        font-family: "IBM Plex Mono", monospace;
      }}
      #three-canvas {{
        width: 100%;
        height: 100%;
        display: block;
        touch-action: none;
      }}
      /* Custom Scrollbars */
      ::-webkit-scrollbar {{
        width: 5px;
        height: 5px;
      }}
      ::-webkit-scrollbar-track {{
        background: transparent;
      }}
      ::-webkit-scrollbar-thumb {{
        background: var(--line);
        border-radius: 3px;
      }}
      ::-webkit-scrollbar-thumb:hover {{
        background: var(--ink-3);
      }}
      .badge-inferred {{
        background-color: var(--amber-bg);
        color: var(--amber);
        border: 1px solid var(--amber);
      }}
      .badge-vendor_confirmed {{
        background-color: #ecfdf5;
        color: #059669;
        border: 1px solid #10b981;
      }}
      .chevron-step.active {{
        background-color: var(--accent);
        color: #ffffff;
        border-color: var(--accent);
        box-shadow: 0 0 12px rgba(14, 110, 107, 0.35);
      }}
      .cat-pill.active {{
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
      }}
      .cat-dot {{
        box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.15);
      }}
      .cat-pill.active .cat-dot {{
        box-shadow: 0 0 0 1.5px rgba(255, 255, 255, 0.6);
      }}
    </style>
  </head>
  <body class="flex flex-col h-screen select-none">
    <!-- Inline Standalone OSAT Catalog Dataset (86 Equipment Models) -->
    <script id="osat-catalog-data" type="application/json">{osat_raw}</script>

    <!-- TOP GLOBAL NAVIGATION BAR -->
    <header class="h-[var(--header-height)] bg-[var(--surface)] border-b border-[var(--line)] px-3 flex items-center justify-between shrink-0 z-30 shadow-sm">
      <div class="flex items-center gap-3">
        <a href="index.html" class="flex items-center gap-2 group decoration-none">
          <svg class="w-6 h-6 text-[var(--accent)]" viewBox="0 0 50 50" fill="none">
            <circle cx="25" cy="25" r="21" stroke="currentColor" stroke-width="2.8"/>
            <line x1="12" y1="18" x2="38" y2="18" stroke="currentColor" stroke-width="1.4"/>
            <line x1="9" y1="25" x2="41" y2="25" stroke="currentColor" stroke-width="1.4"/>
            <line x1="12" y1="32" x2="38" y2="32" stroke="currentColor" stroke-width="1.4"/>
            <rect x="23" y="21" width="8" height="8" rx="1.5" fill="var(--accent)"/>
          </svg>
          <div class="flex flex-col">
            <div class="flex items-center gap-1.5 leading-none">
              <span class="text-sm font-bold tracking-tight text-[var(--ink)]">SemiconFab<span class="text-[var(--accent)]">.org</span></span>
              <span class="px-1.5 py-0.5 text-[9px] font-mono font-semibold rounded bg-[var(--surface-2)] text-[var(--ink-2)]">v1.6.0</span>
            </div>
            <span class="text-[10px] text-[var(--ink-3)] font-medium leading-tight mt-0.5" id="header-subtitle">OSAT Packaging & Test Facility · From Wafer to Shipment</span>
          </div>
        </a>

        <!-- Link to Front-End Fab Twin -->
        <a
          href="twin.html"
          id="btn-link-fab-twin"
          class="hidden sm:flex items-center gap-1.5 px-2.5 py-1 text-xs font-semibold rounded-md border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] hover:text-[var(--accent)] transition ml-2"
          title="Switch to 300mm Front-End Fab Cleanroom Twin"
        >
          <i data-lucide="cpu" class="w-3.5 h-3.5 text-[var(--accent)]"></i>
          <span id="link-fab-text">300mm Fab Twin →</span>
        </a>
      </div>

      <!-- Center: Camera Presets & View Modes -->
      <div class="flex items-center gap-1 bg-[var(--surface-2)] p-0.5 rounded-lg border border-[var(--line)]">
        <button
          onclick="setCameraPreset('iso')"
          class="cam-btn px-2 py-1 text-xs font-medium rounded-md text-[var(--ink-2)] hover:bg-[var(--surface)] hover:text-[var(--ink)] transition flex items-center gap-1"
          title="Global Overview"
        >
          <i data-lucide="globe" class="w-3.5 h-3.5"></i>
          <span class="hidden md:inline" id="cam-iso-text">Overview</span>
        </button>
        <button
          onclick="setCameraPreset('top')"
          class="cam-btn px-2 py-1 text-xs font-medium rounded-md text-[var(--ink-2)] hover:bg-[var(--surface)] hover:text-[var(--ink)] transition flex items-center gap-1"
          title="Top Down Floor Plan"
        >
          <i data-lucide="arrow-down-to-line" class="w-3.5 h-3.5"></i>
          <span class="hidden md:inline" id="cam-top-text">Top</span>
        </button>
        <button
          onclick="setCameraPreset('assembly')"
          class="cam-btn px-2 py-1 text-xs font-medium rounded-md text-[var(--ink-2)] hover:bg-[var(--surface)] hover:text-[var(--ink)] transition flex items-center gap-1"
          title="Focus Assembly Hall (ISO 7-8)"
        >
          <i data-lucide="box" class="w-3.5 h-3.5 text-amber-600"></i>
          <span class="hidden md:inline" id="cam-asm-text">Assembly Hall</span>
        </button>
        <button
          onclick="setCameraPreset('test')"
          class="cam-btn px-2 py-1 text-xs font-medium rounded-md text-[var(--ink-2)] hover:bg-[var(--surface)] hover:text-[var(--ink)] transition flex items-center gap-1"
          title="Focus Final Test Hall (DC Class)"
        >
          <i data-lucide="activity" class="w-3.5 h-3.5 text-sky-600"></i>
          <span class="hidden md:inline" id="cam-test-text">Test Hall</span>
        </button>
        <div class="h-3.5 w-px bg-[var(--line)] mx-0.5"></div>
        <button
          id="btn-tour-toggle"
          onclick="toggleProcessTour()"
          class="px-2 py-1 text-xs font-medium rounded-md bg-emerald-600 text-white hover:bg-emerald-700 transition flex items-center gap-1 shadow-sm"
          title="Automatic Process Tour Walkthrough"
        >
          <i data-lucide="play" class="w-3 h-3 fill-current"></i>
          <span id="tour-btn-text">Tour</span>
        </button>
      </div>

      <!-- Right: Toggles (Roof, Theme, Language) -->
      <div class="flex items-center gap-2">
        <button
          onclick="toggleRoof()"
          id="btn-toggle-roof"
          class="p-1.5 rounded-md border border-[var(--line)] bg-[var(--surface)] text-[var(--ink-2)] hover:text-[var(--ink)] transition"
          title="Toggle Roof Infrastructure"
        >
          <i data-lucide="home" class="w-4 h-4"></i>
        </button>
        <button
          onclick="toggleTheme()"
          id="btn-toggle-theme"
          class="px-2 py-1 rounded-md border border-[var(--line)] bg-[var(--surface)] text-xs font-semibold text-[var(--ink)] hover:bg-[var(--surface-2)] transition flex items-center gap-1.5"
          title="Toggle Day/Dark Theme"
        >
          <span id="theme-icon">☀️</span>
          <span id="theme-label" class="hidden sm:inline">Day</span>
        </button>
        <button
          onclick="toggleLanguage()"
          id="btn-toggle-lang"
          class="px-2.5 py-1 rounded-md border border-[var(--line)] bg-[var(--surface)] text-xs font-semibold text-[var(--ink)] hover:bg-[var(--surface-2)] transition font-mono"
        >
          En/中文
        </button>
      </div>
    </header>

    <!-- FLOATING PROCESS FLOW STEP NAVIGATOR (FROM WAFER TO SHIPMENT) -->
    <div class="h-[var(--flow-height)] bg-[var(--surface)] border-b border-[var(--line)] px-2 flex items-center justify-between shrink-0 z-20 overflow-x-auto text-xs font-medium">
      <div class="flex items-center gap-1 shrink-0">
        <span class="text-[10px] font-bold text-[var(--ink-3)] uppercase tracking-wider px-2 font-mono" id="label-flow">Flow:</span>
        <button onclick="focusBay('osat_dicing')" class="chevron-step px-2 py-0.5 rounded text-[11px] border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition flex items-center gap-1.5 shrink-0" data-bay="osat_dicing">
          <span class="w-1.5 h-1.5 rounded-full shrink-0" style="background-color: #0284c7;"></span>
          <span class="step-name">1. Dicing</span>
        </button>
        <span class="text-[var(--ink-3)] text-[10px]">→</span>
        <button onclick="focusBay('osat_die_attach')" class="chevron-step px-2 py-0.5 rounded text-[11px] border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition flex items-center gap-1.5 shrink-0" data-bay="osat_die_attach">
          <span class="w-1.5 h-1.5 rounded-full shrink-0" style="background-color: #059669;"></span>
          <span class="step-name">2. Die Attach</span>
        </button>
        <span class="text-[var(--ink-3)] text-[10px]">→</span>
        <button onclick="focusBay('osat_wire_bonding')" class="chevron-step px-2 py-0.5 rounded text-[11px] border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition flex items-center gap-1.5 shrink-0" data-bay="osat_wire_bonding">
          <span class="w-1.5 h-1.5 rounded-full shrink-0" style="background-color: #d97706;"></span>
          <span class="step-name">3. Wire Bond</span>
        </button>
        <span class="text-[var(--ink-3)] text-[10px]">→</span>
        <button onclick="focusBay('osat_flip_chip')" class="chevron-step px-2 py-0.5 rounded text-[11px] border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition flex items-center gap-1.5 shrink-0" data-bay="osat_flip_chip">
          <span class="w-1.5 h-1.5 rounded-full shrink-0" style="background-color: #2563eb;"></span>
          <span class="step-name">4. Flip Chip</span>
        </button>
        <span class="text-[var(--ink-3)] text-[10px]">→</span>
        <button onclick="focusBay('osat_molding')" class="chevron-step px-2 py-0.5 rounded text-[11px] border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition flex items-center gap-1.5 shrink-0" data-bay="osat_molding">
          <span class="w-1.5 h-1.5 rounded-full shrink-0" style="background-color: #7c3aed;"></span>
          <span class="step-name">5. Molding</span>
        </button>
        <span class="text-[var(--ink-3)] text-[10px]">→</span>
        <button onclick="focusBay('osat_singulation')" class="chevron-step px-2 py-0.5 rounded text-[11px] border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition flex items-center gap-1.5 shrink-0" data-bay="osat_singulation">
          <span class="w-1.5 h-1.5 rounded-full shrink-0" style="background-color: #0891b2;"></span>
          <span class="step-name">6. Singulation</span>
        </button>
        <span class="text-[var(--ink-3)] text-[10px]">→</span>
        <button onclick="focusBay('osat_bumping_rdl')" class="chevron-step px-2 py-0.5 rounded text-[11px] border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition flex items-center gap-1.5 shrink-0" data-bay="osat_bumping_rdl">
          <span class="w-1.5 h-1.5 rounded-full shrink-0" style="background-color: #4f46e5;"></span>
          <span class="step-name">7. Bumping/RDL</span>
        </button>
        <span class="text-[var(--ink-3)] text-[10px] font-bold">│</span>
        <button onclick="focusBay('osat_prober')" class="chevron-step px-2 py-0.5 rounded text-[11px] border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition flex items-center gap-1.5 shrink-0" data-bay="osat_prober">
          <span class="w-1.5 h-1.5 rounded-full shrink-0" style="background-color: #0d9488;"></span>
          <span class="step-name">8. Wafer Prober</span>
        </button>
        <span class="text-[var(--ink-3)] text-[10px]">→</span>
        <button onclick="focusBay('osat_ate')" class="chevron-step px-2 py-0.5 rounded text-[11px] border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition flex items-center gap-1.5 shrink-0" data-bay="osat_ate">
          <span class="w-1.5 h-1.5 rounded-full shrink-0" style="background-color: #e11d48;"></span>
          <span class="step-name">9. ATE Test</span>
        </button>
        <span class="text-[var(--ink-3)] text-[10px]">→</span>
        <button onclick="focusBay('osat_test_handler')" class="chevron-step px-2 py-0.5 rounded text-[11px] border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition flex items-center gap-1.5 shrink-0" data-bay="osat_test_handler">
          <span class="w-1.5 h-1.5 rounded-full shrink-0" style="background-color: #16a34a;"></span>
          <span class="step-name">10. Test Handler</span>
        </button>
        <span class="text-[var(--ink-3)] text-[10px]">→</span>
        <button onclick="focusBay('osat_inspection')" class="chevron-step px-2 py-0.5 rounded text-[11px] border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition flex items-center gap-1.5 shrink-0" data-bay="osat_inspection">
          <span class="w-1.5 h-1.5 rounded-full shrink-0" style="background-color: #64748b;"></span>
          <span class="step-name">11. AOI Inspection</span>
        </button>
      </div>

      <div class="hidden lg:flex items-center gap-2 text-[10px] text-[var(--ink-3)] font-mono shrink-0 pl-2">
        <span class="inline-block w-2 h-2 rounded-full bg-emerald-500"></span>
        <span id="stat-summary-tag">86 Tools · 23 Tier-1 Vendors · 11 Bays</span>
      </div>
    </div>

    <!-- MAIN INTERACTIVE WORKSPACE -->
    <div class="relative flex-1 w-full overflow-hidden flex">
      <!-- LEFT EQUIPMENT DIRECTORY DRAWER -->
      <aside
        id="equipment-sidebar"
        class="w-72 md:w-80 h-full bg-[var(--surface)] border-r border-[var(--line)] flex flex-col z-10 transition-transform duration-300 shadow-lg shrink-0"
      >
        <!-- Sidebar Search Header -->
        <div class="p-3 border-b border-[var(--line)] flex flex-col gap-2 bg-[var(--surface-2)]">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-[var(--ink)] flex items-center gap-1.5">
              <i data-lucide="package" class="w-3.5 h-3.5 text-[var(--accent)]"></i>
              <span id="sidebar-title">OSAT Equipment Directory</span>
            </span>
            <div class="flex items-center gap-1.5">
              <span id="sidebar-count-badge" class="px-1.5 py-0.5 text-[10px] font-mono font-bold rounded bg-[var(--surface)] text-[var(--accent)] border border-[var(--line)]">86</span>
              <a href="catalog-demo.html?domain=osat" target="_blank" id="sidebar-catalog-link" class="px-1.5 py-0.5 text-[10px] font-medium rounded bg-[var(--surface)] hover:text-[var(--accent)] text-[var(--ink-2)] border border-[var(--line)] transition flex items-center gap-0.5" title="Open in Equipment Catalog">
                <span>名录</span><i data-lucide="external-link" class="w-2.5 h-2.5"></i>
              </a>
            </div>
          </div>
          <div class="relative">
            <i data-lucide="search" class="w-3.5 h-3.5 absolute left-2.5 top-2.5 text-[var(--ink-3)]"></i>
            <input
              type="text"
              id="sidebar-search"
              placeholder="Search vendor, model, process..."
              class="w-full pl-8 pr-7 py-1.5 text-xs bg-[var(--surface)] border border-[var(--line)] rounded-md text-[var(--ink)] placeholder-[var(--ink-3)] focus:outline-none focus:border-[var(--accent)] transition"
              oninput="handleSearch(this.value)"
            />
            <button
              id="search-clear-btn"
              onclick="clearSearch()"
              class="hidden absolute right-2 top-2 text-[var(--ink-3)] hover:text-[var(--ink)]"
            >
              <i data-lucide="x" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>

        <!-- Equipment Cards List -->
        <div id="equipment-list-container" class="flex-1 overflow-y-auto p-2 space-y-1.5">
          <!-- Dynamically populated -->
        </div>
      </aside>

      <!-- 3D VIEWPORT CANVAS -->
      <main class="relative flex-1 h-full w-full bg-slate-900">
        <canvas id="three-canvas"></canvas>

        <!-- FLOATING OVERLAY NOTICES -->
        <div class="absolute top-3 left-3 pointer-events-none flex flex-col gap-1.5 z-10">
          <div class="px-2.5 py-1 rounded bg-[var(--surface)]/90 backdrop-blur-md border border-[var(--line)] text-xs font-semibold shadow-sm text-[var(--ink)] flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            <span id="overlay-zone-title">OSAT Dual-Zone Facility (108m × 51m)</span>
          </div>
          <div id="overlay-zone-sub" class="px-2 py-0.5 rounded bg-[var(--surface-2)]/85 backdrop-blur-md border border-[var(--line)] text-[10px] font-mono text-[var(--ink-2)] shadow-sm">
            West: ISO 7-8 Assembly · East: Final Test Hall
          </div>
          <div id="overlay-logistics-status" class="px-2 py-0.5 rounded bg-[var(--surface-2)]/85 backdrop-blur-md border border-[var(--line)] text-[10px] font-mono text-[var(--ink-2)] shadow-sm flex items-center gap-1.5 pointer-events-auto cursor-pointer hover:border-[var(--accent)] transition" onclick="toggleLogistics()" title="Toggle Logistics Simulation">
            <span class="w-1.5 h-1.5 rounded-full bg-sky-500 animate-pulse"></span>
            <span id="logistics-status-text">Logistics: 6 Active (4 AMR · 2 Trolleys)</span>
          </div>
        </div>

        <!-- BOTTOM CATEGORY PILLS BAR -->
        <div class="absolute bottom-3 left-1/2 -translate-x-1/2 max-w-[95%] overflow-x-auto flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-[var(--surface)]/95 backdrop-blur-md border border-[var(--line)] shadow-lg z-10">
          <button onclick="filterCategory('ALL')" class="cat-pill active px-2.5 py-1 rounded-full text-xs font-semibold border border-[var(--accent)] bg-[var(--accent)] text-white transition shrink-0 flex items-center gap-1.5 shadow-sm" data-cat="ALL">
            <span class="cat-dot w-2.5 h-2.5 rounded-full shrink-0" style="background-color: #ffffff;"></span>
            <span class="cat-label">All (86)</span>
          </button>
          <button onclick="filterCategory('osat_dicing')" class="cat-pill px-2.5 py-1 rounded-full text-xs font-semibold border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition shrink-0 flex items-center gap-1.5" data-cat="osat_dicing">
            <span class="cat-dot w-2.5 h-2.5 rounded-full shrink-0 shadow-xs" style="background-color: #0284c7;"></span>
            <span class="cat-label">Dicing (15)</span>
          </button>
          <button onclick="filterCategory('osat_die_attach')" class="cat-pill px-2.5 py-1 rounded-full text-xs font-semibold border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition shrink-0 flex items-center gap-1.5" data-cat="osat_die_attach">
            <span class="cat-dot w-2.5 h-2.5 rounded-full shrink-0 shadow-xs" style="background-color: #059669;"></span>
            <span class="cat-label">Die Attach (4)</span>
          </button>
          <button onclick="filterCategory('osat_wire_bonding')" class="cat-pill px-2.5 py-1 rounded-full text-xs font-semibold border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition shrink-0 flex items-center gap-1.5" data-cat="osat_wire_bonding">
            <span class="cat-dot w-2.5 h-2.5 rounded-full shrink-0 shadow-xs" style="background-color: #d97706;"></span>
            <span class="cat-label">Wire Bond (5)</span>
          </button>
          <button onclick="filterCategory('osat_flip_chip')" class="cat-pill px-2.5 py-1 rounded-full text-xs font-semibold border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition shrink-0 flex items-center gap-1.5" data-cat="osat_flip_chip">
            <span class="cat-dot w-2.5 h-2.5 rounded-full shrink-0 shadow-xs" style="background-color: #2563eb;"></span>
            <span class="cat-label">Flip Chip (12)</span>
          </button>
          <button onclick="filterCategory('osat_molding')" class="cat-pill px-2.5 py-1 rounded-full text-xs font-semibold border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition shrink-0 flex items-center gap-1.5" data-cat="osat_molding">
            <span class="cat-dot w-2.5 h-2.5 rounded-full shrink-0 shadow-xs" style="background-color: #7c3aed;"></span>
            <span class="cat-label">Molding (1)</span>
          </button>
          <button onclick="filterCategory('osat_singulation')" class="cat-pill px-2.5 py-1 rounded-full text-xs font-semibold border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition shrink-0 flex items-center gap-1.5" data-cat="osat_singulation">
            <span class="cat-dot w-2.5 h-2.5 rounded-full shrink-0 shadow-xs" style="background-color: #0891b2;"></span>
            <span class="cat-label">Singulation (1)</span>
          </button>
          <button onclick="filterCategory('osat_bumping_rdl')" class="cat-pill px-2.5 py-1 rounded-full text-xs font-semibold border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition shrink-0 flex items-center gap-1.5" data-cat="osat_bumping_rdl">
            <span class="cat-dot w-2.5 h-2.5 rounded-full shrink-0 shadow-xs" style="background-color: #4f46e5;"></span>
            <span class="cat-label">Bumping/RDL (3)</span>
          </button>
          <button onclick="filterCategory('osat_prober')" class="cat-pill px-2.5 py-1 rounded-full text-xs font-semibold border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition shrink-0 flex items-center gap-1.5" data-cat="osat_prober">
            <span class="cat-dot w-2.5 h-2.5 rounded-full shrink-0 shadow-xs" style="background-color: #0d9488;"></span>
            <span class="cat-label">Prober (8)</span>
          </button>
          <button onclick="filterCategory('osat_ate')" class="cat-pill px-2.5 py-1 rounded-full text-xs font-semibold border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition shrink-0 flex items-center gap-1.5" data-cat="osat_ate">
            <span class="cat-dot w-2.5 h-2.5 rounded-full shrink-0 shadow-xs" style="background-color: #e11d48;"></span>
            <span class="cat-label">ATE (13)</span>
          </button>
          <button onclick="filterCategory('osat_test_handler')" class="cat-pill px-2.5 py-1 rounded-full text-xs font-semibold border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition shrink-0 flex items-center gap-1.5" data-cat="osat_test_handler">
            <span class="cat-dot w-2.5 h-2.5 rounded-full shrink-0 shadow-xs" style="background-color: #16a34a;"></span>
            <span class="cat-label">Handler (9)</span>
          </button>
          <button onclick="filterCategory('osat_inspection')" class="cat-pill px-2.5 py-1 rounded-full text-xs font-semibold border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition shrink-0 flex items-center gap-1.5" data-cat="osat_inspection">
            <span class="cat-dot w-2.5 h-2.5 rounded-full shrink-0 shadow-xs" style="background-color: #64748b;"></span>
            <span class="cat-label">Inspection (15)</span>
          </button>
        </div>
      </main>

      <!-- RIGHT INSPECTOR DRAWER (SEMI E72 METRICS & HONESTY DISCLOSURE) -->
      <aside
        id="inspector-panel"
        class="absolute right-0 top-0 w-80 md:w-96 h-full bg-[var(--surface)] border-l border-[var(--line)] z-20 transition-transform duration-300 translate-x-full shadow-2xl flex flex-col overflow-hidden"
      >
        <!-- Inspector Header -->
        <div class="p-3 border-b border-[var(--line)] flex items-center justify-between bg-[var(--surface-2)]">
          <div class="flex items-center gap-2 overflow-hidden">
            <span id="inspect-category-badge" class="px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider bg-[var(--accent)] text-white shrink-0">OSAT Dicing</span>
            <span id="inspect-vendor" class="text-xs font-bold text-[var(--ink-2)] truncate">DISCO</span>
          </div>
          <button onclick="closeInspector()" class="p-1 rounded hover:bg-[var(--line)] text-[var(--ink-3)] hover:text-[var(--ink)]">
            <i data-lucide="x" class="w-4 h-4"></i>
          </button>
        </div>

        <!-- Inspector Scrollable Body -->
        <div class="flex-1 overflow-y-auto p-3.5 space-y-3 text-xs">
          <!-- Model Header -->
          <div>
            <h2 id="inspect-model" class="text-base font-extrabold text-[var(--ink)] leading-snug">DFD6361</h2>
            <div class="flex items-center gap-2 mt-0.5">
              <span id="inspect-tier-badge" class="px-1.5 py-0.5 text-[9px] font-mono font-bold rounded badge-inferred">● Inferred</span>
              <span id="inspect-wafer-size" class="text-[10px] text-[var(--ink-2)] font-mono">300mm</span>
            </div>
          </div>

          <!-- Amber Honesty Banner (For Draft Shells) -->
          <div id="inspect-honesty-banner" class="p-2.5 rounded-md border border-[var(--amber)] bg-[var(--amber-bg)] flex items-start gap-2 text-[11px] text-[var(--ink)]">
            <i data-lucide="alert-triangle" class="w-4 h-4 text-[var(--amber)] shrink-0 mt-0.5"></i>
            <div>
              <div class="font-bold text-[var(--amber)]" id="inspect-honesty-title">Dimensions pending verification</div>
              <div class="text-[10px] text-[var(--ink-2)] mt-0.5 leading-relaxed" id="inspect-honesty-desc">
                3D scene geometry is a procedural category placeholder shell without physical CAD measurements.
              </div>
            </div>
          </div>

          <!-- TOWA Gap Row Notice (Hidden by default) -->
          <div id="inspect-towa-notice" class="hidden p-2.5 rounded-md border border-sky-400 bg-sky-50 text-sky-900 text-[11px]">
            <div class="font-bold" id="inspect-towa-title">【Gap Row Documentation】</div>
            <div class="text-[10px] mt-0.5 leading-relaxed" id="inspect-towa-desc">
              TOWA discloses technical specifications only, withholding explicit model names. TOWA commands ~2/3 global market share in semiconductor molding (multi-plunger transfer & compression molding).
            </div>
          </div>

          <!-- 1-Click Contribution CTA -->
          <a
            id="inspect-cta-contribute"
            href="/add-equipment.html"
            target="_blank"
            class="flex items-center justify-between px-3 py-2 rounded-md bg-[var(--accent)] hover:opacity-90 text-white font-semibold text-xs shadow-sm transition"
          >
            <span id="inspect-cta-text">+ Contribute Verified Equipment Specs</span>
            <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
          </a>

          <!-- Physical Dimensions Card -->
          <div class="p-2.5 rounded-md border border-[var(--line)] bg-[var(--surface-2)] space-y-1.5">
            <div class="text-[10px] font-mono uppercase font-bold text-[var(--ink-3)] flex items-center justify-between">
              <span id="inspect-envelope-label">Physical Envelope (SEMI E72)</span>
              <span id="inspect-dim-status" class="text-[9px] text-[var(--amber)] font-bold">Nominal</span>
            </div>
            <div class="grid grid-cols-2 gap-2 text-xs font-mono">
              <div>
                <span id="inspect-dim-label" class="text-[9px] text-[var(--ink-3)] block">Dimensions (W×D×H):</span>
                <span id="inspect-dimensions" class="font-bold text-[var(--ink)]">2.20 × 2.60 × 3.20 m</span>
              </div>
              <div>
                <span id="inspect-weight-label" class="text-[9px] text-[var(--ink-3)] block">Gross Weight:</span>
                <span id="inspect-weight" class="font-bold text-[var(--ink)]">Pending</span>
              </div>
            </div>
          </div>

          <!-- Process Capabilities & Specifications -->
          <div class="p-2.5 rounded-md border border-[var(--line)] bg-[var(--surface-2)] space-y-1.5">
            <div id="inspect-specs-label" class="text-[10px] font-mono uppercase font-bold text-[var(--ink-3)]">Key Technical Specs</div>
            <p id="inspect-specs" class="text-xs text-[var(--ink)] leading-relaxed font-sans">
              Cut speed 0.1-600mm/s; dual spindle 1.2kW.
            </p>
          </div>

          <!-- Notes & Provenance Citation -->
          <div class="p-2.5 rounded-md border border-[var(--line)] bg-[var(--surface-2)] space-y-1">
            <div id="inspect-prov-label" class="text-[10px] font-mono uppercase font-bold text-[var(--ink-3)]">Data Provenance</div>
            <p id="inspect-notes" class="text-[11px] text-[var(--ink-2)] leading-normal italic">
              Specification sheet republishing OEM data.
            </p>
            <div class="pt-1">
              <a
                id="inspect-source-link"
                href="#"
                target="_blank"
                class="text-[11px] text-[var(--accent)] hover:underline flex items-center gap-1 font-mono truncate"
              >
                <i data-lucide="link" class="w-3 h-3 shrink-0"></i>
                <span id="inspect-source-url" class="truncate">Verified Public Citation</span>
              </a>
            </div>
          </div>
        </div>
      </aside>
    </div>

    <!-- MAIN JAVASCRIPT ENGINE -->
    <script>
      // ==========================================
      // 1. DATA & CATEGORY TAXONOMY
      // ==========================================
      let catalogRecords = [];
      let selectedTool = null;
      let activeFilter = "ALL";
      const initialUrlParams = new URLSearchParams(window.location.search);
      const urlLang = initialUrlParams.get("lang");
      if (urlLang) {{
        currentLang = urlLang.startsWith("zh") ? "zh-CN" : "en";
      }} else {{
        currentLang = localStorage.getItem("semiconfab_lang") || (typeof currentLang !== "undefined" ? currentLang : "en");
      }}
      let currentTheme = localStorage.getItem("semicon_theme") || "light";

      // 11 OSAT Process Bays layout geometry (Centered at 0, 0, 0: x in [-54, 54], z in [-25.5, 25.5])
      const OSAT_BAYS = {{
        osat_dicing: {{
          nameEn: "Wafer Dicing & Sawing Bay",
          nameZh: "晶圆精密划片切片区",
          xRange: [-51, -42],
          zRange: [-23, 23],
          color: 0x0284c7,
          hex: "#0284c7",
          hall: "assembly",
          stage: 1
        }},
        osat_die_attach: {{
          nameEn: "Die Attach & Pick-and-Place Bay",
          nameZh: "芯片贴装与固晶工位区",
          xRange: [-40, -33],
          zRange: [-23, 23],
          color: 0x059669,
          hex: "#059669",
          hall: "assembly",
          stage: 2
        }},
        osat_wire_bonding: {{
          nameEn: "Wire Bonding & Interconnect Bay",
          nameZh: "金铝线键合焊接工位区",
          xRange: [-31, -23],
          zRange: [-23, 23],
          color: 0xd97706,
          hex: "#d97706",
          hall: "assembly",
          stage: 3
        }},
        osat_flip_chip: {{
          nameEn: "Flip Chip & Advanced Bonding Bay",
          nameZh: "倒装倒贴高密度热压焊接区",
          xRange: [-21, -11],
          zRange: [-23, 23],
          color: 0x2563eb,
          hex: "#2563eb",
          hall: "assembly",
          stage: 4
        }},
        osat_molding: {{
          nameEn: "Compression & Transfer Molding Bay",
          nameZh: "注塑包封与传递模塑区",
          xRange: [-9, -2],
          zRange: [-23, 23],
          color: 0x7c3aed,
          hex: "#7c3aed",
          hall: "assembly",
          stage: 5
        }},
        osat_singulation: {{
          nameEn: "Package Singulation & Trim Bay",
          nameZh: "封装切筋打弯与切断分离区",
          xRange: [0, 6],
          zRange: [-23, 23],
          color: 0x0891b2,
          hex: "#0891b2",
          hall: "assembly",
          stage: 6
        }},
        osat_bumping_rdl: {{
          nameEn: "Wafer Bumping & RDL Bay",
          nameZh: "晶圆级微凸点与重布线区",
          xRange: [-51, -33],
          zRange: [7, 23],
          color: 0x4f46e5,
          hex: "#4f46e5",
          hall: "assembly",
          stage: 7
        }},
        osat_prober: {{
          nameEn: "Wafer Prober & CP Test Bay",
          nameZh: "晶圆探针电测工位区",
          xRange: [10, 18],
          zRange: [-23, 23],
          color: 0x0d9488,
          hex: "#0d9488",
          hall: "test",
          stage: 8
        }},
        osat_ate: {{
          nameEn: "High-Speed ATE Final Test Bay",
          nameZh: "集成电路 ATE 高速测试机群",
          xRange: [20, 30],
          zRange: [-23, 23],
          color: 0xe11d48,
          hex: "#e11d48",
          hall: "test",
          stage: 9
        }},
        osat_test_handler: {{
          nameEn: "Pick-and-Place & Gravity Test Handlers",
          nameZh: "三温测试分选与编带包装机群",
          xRange: [32, 40],
          zRange: [-23, 23],
          color: 0x16a34a,
          hex: "#16a34a",
          hall: "test",
          stage: 10
        }},
        osat_inspection: {{
          nameEn: "Final 3D AOI & X-Ray Inspection Bay",
          nameZh: "出厂成品外观光学量测与质检区",
          xRange: [42, 51],
          zRange: [-23, 23],
          color: 0x64748b,
          hex: "#64748b",
          hall: "test",
          stage: 11
        }}
      }};

      // ==========================================
      // 2. THREE.JS SCENE, CAMERA & LIGHTING
      // ==========================================
      let scene, camera, renderer, controls;
      let osatBuildingGroup, osatRoofGroup, equipmentGroup;
      let interactiveMeshes = [];
      let highlightBox = null;
      let showRoof = false;
      let isTourRunning = false;
      let tourTimer = null;
      let tourStep = 0;

      function initThree() {{
        const container = document.getElementById("three-canvas");
        const width = container.clientWidth;
        const height = container.clientHeight;

        scene = new THREE.Scene();
        updateSceneBackground();

        camera = new THREE.PerspectiveCamera(45, width / height, 0.5, 400);
        camera.position.set(0, 48, 62);

        renderer = new THREE.WebGLRenderer({{
          canvas: container,
          antialias: true,
          powerPreference: "high-performance"
        }});
        renderer.setSize(width, height);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.shadowMap.enabled = true;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;

        controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.06;
        controls.maxPolarAngle = Math.PI / 2 - 0.03;
        controls.minDistance = 4;
        controls.maxDistance = 200;
        controls.target.set(0, 1.5, 0);

        setupLighting();
        buildBuildingStructure();
        buildRoofLayer();
        buildLogisticsSystem();

        window.addEventListener("resize", onWindowResize);
        container.addEventListener("pointerdown", onPointerDown);

        animate();
      }}

      function updateSceneBackground() {{
        const isDark = document.documentElement.classList.contains("dark");
        const bgCol = isDark ? 0x12161a : 0xf2f1ec;
        scene.background = new THREE.Color(bgCol);
        scene.fog = new THREE.FogExp2(bgCol, 0.005);
      }}

      function setupLighting() {{
        const ambient = new THREE.AmbientLight(0xffffff, 0.72);
        scene.add(ambient);

        const dirLight = new THREE.DirectionalLight(0xffffff, 0.75);
        dirLight.position.set(40, 80, 50);
        dirLight.castShadow = true;
        dirLight.shadow.mapSize.width = 2048;
        dirLight.shadow.mapSize.height = 2048;
        dirLight.shadow.camera.near = 10;
        dirLight.shadow.camera.far = 200;
        dirLight.shadow.camera.left = -60;
        dirLight.shadow.camera.right = 60;
        dirLight.shadow.camera.top = 40;
        dirLight.shadow.camera.bottom = -40;
        scene.add(dirLight);

        // Fill light
        const fillLight = new THREE.DirectionalLight(0xbae6fd, 0.3);
        fillLight.position.set(-40, 50, -30);
        scene.add(fillLight);
      }}

      function buildBuildingStructure() {{
        osatBuildingGroup = new THREE.Group();
        osatBuildingGroup.name = "osatBuilding";

        const bWidth = 108; // -54 to 54
        const bDepth = 51;  // -25.5 to 25.5
        const bHeight = 5.2;

        // 1. Concrete Slab (y: 0 to -0.35m)
        const slabGeo = new THREE.BoxGeometry(bWidth, 0.35, bDepth);
        const slabMat = new THREE.MeshStandardMaterial({{
          color: 0x334155,
          roughness: 0.85,
          metalness: 0.1
        }});
        const slab = new THREE.Mesh(slabGeo, slabMat);
        slab.position.set(0, -0.175, 0);
        slab.receiveShadow = true;
        osatBuildingGroup.add(slab);

        // 2. West Assembly Floor (ISO 7-8: x from -54 to 8)
        const asmWidth = 8 - (-54); // 62m
        const asmFloorGeo = new THREE.PlaneGeometry(asmWidth - 0.2, bDepth - 0.2);
        const asmFloorMat = new THREE.MeshStandardMaterial({{
          color: 0xe2e8f0, // Clean light slate epoxy
          roughness: 0.42,
          metalness: 0.12
        }});
        const asmFloor = new THREE.Mesh(asmFloorGeo, asmFloorMat);
        asmFloor.rotation.x = -Math.PI / 2;
        asmFloor.position.set(-54 + asmWidth / 2, 0.015, 0);
        asmFloor.receiveShadow = true;
        osatBuildingGroup.add(asmFloor);

        // 3. East Final Test Floor (Data Center: x from 8 to 54)
        const testWidth = 54 - 8; // 46m
        const testFloorGeo = new THREE.PlaneGeometry(testWidth - 0.2, bDepth - 0.2);
        const testFloorMat = new THREE.MeshStandardMaterial({{
          color: 0x1e293b, // High-contrast slate raised tiles
          roughness: 0.55,
          metalness: 0.2
        }});
        const testFloor = new THREE.Mesh(testFloorGeo, testFloorMat);
        testFloor.rotation.x = -Math.PI / 2;
        testFloor.position.set(8 + testWidth / 2, 0.015, 0);
        testFloor.receiveShadow = true;
        osatBuildingGroup.add(testFloor);

        // 4. Central Divider Line (x = 8)
        const divGeo = new THREE.BoxGeometry(0.35, 0.04, bDepth);
        const divMat = new THREE.MeshBasicMaterial({{ color: 0x0284c7 }});
        const divLine = new THREE.Mesh(divGeo, divMat);
        divLine.position.set(8, 0.02, 0);
        osatBuildingGroup.add(divLine);

        // 5. Central AGV & Logistics Corridor with Process Chevrons
        const corrGeo = new THREE.PlaneGeometry(bWidth - 4, 4.0);
        const corrMat = new THREE.MeshStandardMaterial({{
          color: 0x475569,
          roughness: 0.6,
          metalness: 0.2
        }});
        const corridor = new THREE.Mesh(corrGeo, corrMat);
        corridor.rotation.x = -Math.PI / 2;
        corridor.position.set(0, 0.02, 0);
        osatBuildingGroup.add(corridor);

        // 10 Glowing Process Flow Chevrons (West to East)
        for (let i = 0; i < 10; i++) {{
          const cx = -45 + i * 10;
          const chevron = createFlowChevron();
          chevron.position.set(cx, 0.035, 0);
          osatBuildingGroup.add(chevron);
        }}

        // 6. Perimeter Walls with Ribbon Windows
        const wallMat = new THREE.MeshStandardMaterial({{ color: 0x334155, roughness: 0.7, metalness: 0.25 }});
        const glassMat = new THREE.MeshPhysicalMaterial({{
          color: 0xbae6fd,
          transparent: true,
          opacity: 0.35,
          roughness: 0.1,
          transmission: 0.7
        }});

        // Plinths & Friezes
        const plinthN = new THREE.Mesh(new THREE.BoxGeometry(bWidth, 1.0, 0.3), wallMat);
        plinthN.position.set(0, 0.5, -25.5);
        const plinthS = new THREE.Mesh(new THREE.BoxGeometry(bWidth, 1.0, 0.3), wallMat);
        plinthS.position.set(0, 0.5, 25.5);
        const glassN = new THREE.Mesh(new THREE.BoxGeometry(bWidth - 0.4, 2.4, 0.1), glassMat);
        glassN.position.set(0, 2.2, -25.5);
        const glassS = new THREE.Mesh(new THREE.BoxGeometry(bWidth - 0.4, 2.4, 0.1), glassMat);
        glassS.position.set(0, 2.2, 25.5);
        const friezeN = new THREE.Mesh(new THREE.BoxGeometry(bWidth, 1.8, 0.3), wallMat);
        friezeN.position.set(0, 4.3, -25.5);
        const friezeS = new THREE.Mesh(new THREE.BoxGeometry(bWidth, 1.8, 0.3), wallMat);
        friezeS.position.set(0, 4.3, 25.5);
        osatBuildingGroup.add(plinthN, plinthS, glassN, glassS, friezeN, friezeS);

        // West Wall & Entrance Portal
        const wallW1 = new THREE.Mesh(new THREE.BoxGeometry(0.3, bHeight, 20), wallMat);
        wallW1.position.set(-54, bHeight / 2, -15.5);
        const wallW2 = new THREE.Mesh(new THREE.BoxGeometry(0.3, bHeight, 20), wallMat);
        wallW2.position.set(-54, bHeight / 2, 15.5);
        const portalTop = new THREE.Mesh(new THREE.BoxGeometry(0.6, 1.4, 11), wallMat);
        portalTop.position.set(-54, 4.5, 0);
        osatBuildingGroup.add(wallW1, wallW2, portalTop);

        // East Wall & Shutter Doors
        const wallE1 = new THREE.Mesh(new THREE.BoxGeometry(0.3, bHeight, 18), wallMat);
        wallE1.position.set(54, bHeight / 2, -16.5);
        const wallE2 = new THREE.Mesh(new THREE.BoxGeometry(0.3, bHeight, 18), wallMat);
        wallE2.position.set(54, bHeight / 2, 16.5);
        osatBuildingGroup.add(wallE1, wallE2);

        [-5.0, 5.0].forEach((zDoor) => {{
          const shutterGeo = new THREE.PlaneGeometry(5.6, 3.6);
          const shutterMat = new THREE.MeshStandardMaterial({{ color: 0x475569, metalness: 0.8, roughness: 0.3 }});
          const shutter = new THREE.Mesh(shutterGeo, shutterMat);
          shutter.rotation.y = Math.PI / 2;
          shutter.position.set(54.05, 1.8, zDoor);
          osatBuildingGroup.add(shutter);
        }});

        // 7. Structural Columns Grid (14m spacing)
        const colGeo = new THREE.BoxGeometry(0.45, bHeight, 0.45);
        const colMat = new THREE.MeshStandardMaterial({{ color: 0x64748b, roughness: 0.4, metalness: 0.4 }});
        for (let x = -42; x <= 45; x += 14) {{
          for (let z = -18; z <= 18; z += 18) {{
            const col = new THREE.Mesh(colGeo, colMat);
            col.position.set(x, bHeight / 2, z);
            osatBuildingGroup.add(col);
          }}
        }}

        // 8. Overhead HVAC Ducts (Assembly Hall)
        [-12, 12].forEach((zDuct) => {{
          const ductGeo = new THREE.CylinderGeometry(0.35, 0.35, 58, 16);
          const ductMat = new THREE.MeshStandardMaterial({{ color: 0xcfd8dc, metalness: 0.75, roughness: 0.25 }});
          const duct = new THREE.Mesh(ductGeo, ductMat);
          duct.rotation.z = Math.PI / 2;
          duct.position.set(-24, 4.5, zDuct);
          osatBuildingGroup.add(duct);
        }});

        // 9. Testing Hall Overhead Power Busways (East)
        [-8, 8].forEach((zBus) => {{
          const busGeo = new THREE.BoxGeometry(42, 0.22, 0.22);
          const busMat = new THREE.MeshStandardMaterial({{ color: 0x0284c7, metalness: 0.4, roughness: 0.3 }});
          const bus = new THREE.Mesh(busGeo, busMat);
          bus.position.set(31, 4.5, zBus);
          osatBuildingGroup.add(bus);
        }});

        // 10. Precision CRAC Units (Testing Hall Perimeter)
        const cracMat = new THREE.MeshStandardMaterial({{ color: 0x1e293b, metalness: 0.5, roughness: 0.4 }});
        const cracLedMat = new THREE.MeshBasicMaterial({{ color: 0x0284c7 }});
        [-24.2, 24.2].forEach((zWall) => {{
          for (let cx = 14; cx <= 46; cx += 11) {{
            const crac = new THREE.Mesh(new THREE.BoxGeometry(2.4, 2.8, 1.2), cracMat);
            crac.position.set(cx, 1.4, zWall);
            const led = new THREE.Mesh(new THREE.BoxGeometry(2.0, 0.08, 0.05), cracLedMat);
            led.position.set(cx, 2.6, zWall + (zWall > 0 ? -0.61 : 0.61));
            osatBuildingGroup.add(crac, led);
          }}
        }});

        scene.add(osatBuildingGroup);
      }}

      function createFlowChevron() {{
        const group = new THREE.Group();
        const shape = new THREE.Shape();
        shape.moveTo(-1.2, -0.4);
        shape.lineTo(0.4, -0.4);
        shape.lineTo(1.2, 0.0);
        shape.lineTo(0.4, 0.4);
        shape.lineTo(-1.2, 0.4);
        shape.lineTo(-0.4, 0.0);
        shape.closePath();

        const geo = new THREE.ShapeGeometry(shape);
        const mat = new THREE.MeshBasicMaterial({{
          color: 0x38bdf8,
          side: THREE.DoubleSide
        }});
        const mesh = new THREE.Mesh(geo, mat);
        mesh.rotation.x = -Math.PI / 2;
        group.add(mesh);
        return group;
      }}

      function buildRoofLayer() {{
        osatRoofGroup = new THREE.Group();
        osatRoofGroup.name = "osatRoof";
        osatRoofGroup.visible = showRoof;

        const bWidth = 108;
        const bDepth = 51;
        const bHeight = 5.2;

        const slabGeo = new THREE.BoxGeometry(bWidth, 0.25, bDepth);
        const slabMat = new THREE.MeshStandardMaterial({{ color: 0xcfd4dc, roughness: 0.65, metalness: 0.2 }});
        const slab = new THREE.Mesh(slabGeo, slabMat);
        slab.position.set(0, bHeight + 0.125, 0);
        osatRoofGroup.add(slab);

        // Rooftop Chillers
        for (let i = 0; i < 4; i++) {{
          const chillerGeo = new THREE.BoxGeometry(4.2, 2.2, 3.2);
          const chillerMat = new THREE.MeshStandardMaterial({{ color: 0x64748b, metalness: 0.6, roughness: 0.3 }});
          const chiller = new THREE.Mesh(chillerGeo, chillerMat);
          chiller.position.set(-30 + i * 20, bHeight + 1.35, 12);
          osatRoofGroup.add(chiller);
        }}

        scene.add(osatRoofGroup);
      }}

      function toggleRoof() {{
        showRoof = !showRoof;
        if (osatRoofGroup) osatRoofGroup.visible = showRoof;
        const btn = document.getElementById("btn-toggle-roof");
        if (btn) {{
          btn.className = `p-1.5 rounded-md border transition ${{
            showRoof
              ? "bg-[var(--accent)] text-white border-[var(--accent)]"
              : "border-[var(--line)] bg-[var(--surface)] text-[var(--ink-2)]"
          }}`;
        }}
      }}

      // ==========================================
      // 2.8. LOGISTICS FLEET & SIMULATION (AGV / AMR & MANUAL TROLLEYS)
      // ==========================================
      let logisticsGroup = null;
      let logisticsFleet = [];
      let showLogistics = true;

      const L_STRAIGHT = 84.0;
      const R_LOOP = 1.15;
      const L_TURN = Math.PI * R_LOOP;
      const L_TOTAL = L_STRAIGHT * 2 + L_TURN * 2; // 175.2257m

      function getLoopPose(s) {{
        const normS = ((s % L_TOTAL) + L_TOTAL) % L_TOTAL;
        if (normS < L_STRAIGHT) {{
          return {{ x: -42.0 + normS, z: 1.15, yaw: 0.0 }};
        }} else if (normS < L_STRAIGHT + L_TURN) {{
          const t = (normS - L_STRAIGHT) / L_TURN;
          const theta = Math.PI / 2.0 - t * Math.PI;
          return {{
            x: 42.0 + R_LOOP * Math.cos(theta),
            z: R_LOOP * Math.sin(theta),
            yaw: -t * Math.PI
          }};
        }} else if (normS < L_STRAIGHT * 2.0 + L_TURN) {{
          const s2 = normS - (L_STRAIGHT + L_TURN);
          return {{ x: 42.0 - s2, z: -1.15, yaw: -Math.PI }};
        }} else {{
          const t = (normS - L_STRAIGHT * 2.0 - L_TURN) / L_TURN;
          const theta = -Math.PI / 2.0 - t * Math.PI;
          return {{
            x: -42.0 + R_LOOP * Math.cos(theta),
            z: R_LOOP * Math.sin(theta),
            yaw: -Math.PI - t * Math.PI
          }};
        }}
      }}

      function createAmrMesh(cargoType) {{
        const group = new THREE.Group();
        group.name = "AMR_Vehicle";

        // 1. Chassis Base (Dark rubber bumper)
        const skirtGeo = new THREE.BoxGeometry(1.15, 0.08, 0.7);
        const skirtMat = new THREE.MeshStandardMaterial({{ color: 0x0f172a, roughness: 0.8 }});
        const skirt = new THREE.Mesh(skirtGeo, skirtMat);
        skirt.position.y = 0.04;
        group.add(skirt);

        // 2. Main Body Enclosure (Cleanroom White PBR)
        const bodyGeo = new THREE.BoxGeometry(1.08, 0.26, 0.64);
        const bodyMat = new THREE.MeshStandardMaterial({{
          color: 0xf8fafc,
          metalness: 0.3,
          roughness: 0.35
        }});
        const body = new THREE.Mesh(bodyGeo, bodyMat);
        body.position.y = 0.21;
        body.castShadow = true;
        group.add(body);

        // Accent stripe along side
        const stripeGeo = new THREE.BoxGeometry(1.1, 0.04, 0.66);
        const stripeMat = new THREE.MeshBasicMaterial({{ color: 0x0284c7 }});
        const stripe = new THREE.Mesh(stripeGeo, stripeMat);
        stripe.position.y = 0.25;
        group.add(stripe);

        // 3. LIDAR Safety Scanner Pucks
        const lidarGeo = new THREE.CylinderGeometry(0.045, 0.045, 0.06, 12);
        const lidarMat = new THREE.MeshStandardMaterial({{ color: 0x0f172a, roughness: 0.4 }});
        const lidar1 = new THREE.Mesh(lidarGeo, lidarMat);
        lidar1.position.set(0.5, 0.12, 0.26);
        const lidar2 = new THREE.Mesh(lidarGeo, lidarMat);
        lidar2.position.set(-0.5, 0.12, -0.26);
        group.add(lidar1, lidar2);

        // 4. Status Light Beacon (Mast at rear)
        const mastGeo = new THREE.CylinderGeometry(0.012, 0.012, 0.45, 8);
        const mastMat = new THREE.MeshStandardMaterial({{ color: 0x64748b, metalness: 0.8 }});
        const mast = new THREE.Mesh(mastGeo, mastMat);
        mast.position.set(-0.44, 0.52, 0.22);

        const beaconGeo = new THREE.CylinderGeometry(0.035, 0.035, 0.1, 10);
        const beaconMat = new THREE.MeshBasicMaterial({{ color: 0x10b981 }});
        const beacon = new THREE.Mesh(beaconGeo, beaconMat);
        beacon.position.set(-0.44, 0.78, 0.22);
        group.add(mast, beacon);
        group.userData.beacon = beacon;

        // 5. Cargo on Top Deck
        if (cargoType === "foup") {{
          // 300mm Wafer FOUP Carrier
          const foupGeo = new THREE.BoxGeometry(0.48, 0.42, 0.44);
          const foupMat = new THREE.MeshStandardMaterial({{
            color: 0x0284c7,
            metalness: 0.5,
            roughness: 0.3
          }});
          const foup = new THREE.Mesh(foupGeo, foupMat);
          foup.position.set(0.05, 0.55, 0);
          foup.castShadow = true;

          const doorGeo = new THREE.BoxGeometry(0.02, 0.36, 0.36);
          const doorMat = new THREE.MeshStandardMaterial({{ color: 0x0f172a, roughness: 0.7 }});
          const door = new THREE.Mesh(doorGeo, doorMat);
          door.position.set(0.29, 0.55, 0);

          const handleGeo = new THREE.BoxGeometry(0.18, 0.05, 0.04);
          const handleMat = new THREE.MeshStandardMaterial({{ color: 0x38bdf8, metalness: 0.8 }});
          const handle = new THREE.Mesh(handleGeo, handleMat);
          handle.position.set(0.05, 0.78, 0);
          group.add(foup, door, handle);
        }} else if (cargoType === "magazine") {{
          // Metal Leadframe Magazine Carrier (PCB / Strip cassettes)
          const magRackGeo = new THREE.BoxGeometry(0.55, 0.45, 0.38);
          const magRackMat = new THREE.MeshStandardMaterial({{
            color: 0xd97706,
            metalness: 0.8,
            roughness: 0.35
          }});
          const magRack = new THREE.Mesh(magRackGeo, magRackMat);
          magRack.position.set(0.05, 0.57, 0);
          magRack.castShadow = true;
          group.add(magRack);
        }} else if (cargoType === "tray") {{
          // Stack of ESD JEDEC IC Trays
          const trayStackGeo = new THREE.BoxGeometry(0.52, 0.32, 0.36);
          const trayStackMat = new THREE.MeshStandardMaterial({{
            color: 0x1e293b,
            roughness: 0.9
          }});
          const trayStack = new THREE.Mesh(trayStackGeo, trayStackMat);
          trayStack.position.set(0.05, 0.5, 0);
          trayStack.castShadow = true;

          const strapGeo = new THREE.BoxGeometry(0.53, 0.33, 0.04);
          const strapMat = new THREE.MeshBasicMaterial({{ color: 0xe11d48 }});
          const strap1 = new THREE.Mesh(strapGeo, strapMat);
          strap1.position.set(0.05, 0.5, -0.1);
          const strap2 = new THREE.Mesh(strapGeo, strapMat);
          strap2.position.set(0.05, 0.5, 0.1);
          group.add(trayStack, strap1, strap2);
        }} else {{
          // Tape & Reel Spool Rack
          const spoolGeo = new THREE.CylinderGeometry(0.18, 0.18, 0.04, 16);
          const spoolMat = new THREE.MeshStandardMaterial({{ color: 0x38bdf8, metalness: 0.4 }});
          const spool1 = new THREE.Mesh(spoolGeo, spoolMat);
          spool1.rotation.z = Math.PI / 2;
          spool1.position.set(0, 0.56, -0.1);
          const spool2 = new THREE.Mesh(spoolGeo, spoolMat);
          spool2.rotation.z = Math.PI / 2;
          spool2.position.set(0, 0.56, 0.1);
          group.add(spool1, spool2);
        }}

        // 6. Blue Safety Spotlight projected ahead on floor (Real cleanroom AMR feature)
        const blueSpotGeo = new THREE.CircleGeometry(0.32, 16);
        const blueSpotMat = new THREE.MeshBasicMaterial({{
          color: 0x0284c7,
          transparent: true,
          opacity: 0.55
        }});
        const blueSpot = new THREE.Mesh(blueSpotGeo, blueSpotMat);
        blueSpot.rotation.x = -Math.PI / 2;
        blueSpot.position.set(1.5, 0.02, 0);
        group.add(blueSpot);

        return group;
      }}

      function createManualTrolleyMesh(cargoType) {{
        const group = new THREE.Group();
        group.name = "Manual_Trolley";

        // 1. Stainless Steel Double Shelf Frame
        const frameMat = new THREE.MeshStandardMaterial({{
          color: 0x94a3b8,
          metalness: 0.9,
          roughness: 0.2
        }});

        // 2 Shelves
        const shelfGeo = new THREE.BoxGeometry(0.85, 0.02, 0.52);
        const bottomShelf = new THREE.Mesh(shelfGeo, frameMat);
        bottomShelf.position.set(0, 0.18, 0);
        const topShelf = new THREE.Mesh(shelfGeo, frameMat);
        topShelf.position.set(0, 0.78, 0);
        topShelf.castShadow = true;
        group.add(bottomShelf, topShelf);

        // 4 Vertical Tubular Corner Posts
        const postGeo = new THREE.CylinderGeometry(0.014, 0.014, 0.85, 8);
        for (let dx of [-0.4, 0.4]) {{
          for (let dz of [-0.24, 0.24]) {{
            const post = new THREE.Mesh(postGeo, frameMat);
            post.position.set(dx, 0.44, dz);
            group.add(post);
          }}
        }}

        // Push Handle at rear (-X)
        const handleBarGeo = new THREE.CylinderGeometry(0.016, 0.016, 0.5, 8);
        const handleBar = new THREE.Mesh(handleBarGeo, frameMat);
        handleBar.position.set(-0.48, 0.92, 0);
        const bracketGeo = new THREE.CylinderGeometry(0.012, 0.012, 0.18, 6);
        const b1 = new THREE.Mesh(bracketGeo, frameMat);
        b1.rotation.z = Math.PI / 4;
        b1.position.set(-0.44, 0.85, -0.2);
        const b2 = new THREE.Mesh(bracketGeo, frameMat);
        b2.rotation.z = Math.PI / 4;
        b2.position.set(-0.44, 0.85, 0.2);
        group.add(handleBar, b1, b2);

        // 4 Castor Wheels
        const wheelGeo = new THREE.CylinderGeometry(0.04, 0.04, 0.03, 10);
        const wheelMat = new THREE.MeshStandardMaterial({{ color: 0x334155, roughness: 0.8 }});
        for (let dx of [-0.38, 0.38]) {{
          for (let dz of [-0.22, 0.22]) {{
            const w = new THREE.Mesh(wheelGeo, wheelMat);
            w.rotation.z = Math.PI / 2;
            w.position.set(dx, 0.06, dz);
            group.add(w);
          }}
        }}

        // Cargo on top shelf
        const boxGeo = new THREE.BoxGeometry(0.42, 0.3, 0.34);
        const boxMat = new THREE.MeshStandardMaterial({{ color: 0x0284c7, roughness: 0.4 }});
        const box = new THREE.Mesh(boxGeo, boxMat);
        box.position.set(0.05, 0.95, 0);
        box.castShadow = true;
        group.add(box);

        // 2. Cleanroom Operator (Technician in White Bunny Suit)
        const opGroup = new THREE.Group();
        const suitMat = new THREE.MeshStandardMaterial({{ color: 0xf1f5f9, roughness: 0.55 }});
        const darkVisorMat = new THREE.MeshStandardMaterial({{ color: 0x0f172a, roughness: 0.2, metalness: 0.8 }});
        const bootsMat = new THREE.MeshStandardMaterial({{ color: 0x475569, roughness: 0.7 }});

        // Legs
        const legGeo = new THREE.CylinderGeometry(0.07, 0.06, 0.65, 8);
        const legL = new THREE.Mesh(legGeo, suitMat);
        legL.position.set(0, 0.38, -0.11);
        const legR = new THREE.Mesh(legGeo, suitMat);
        legR.position.set(0, 0.38, 0.11);
        const bootL = new THREE.Mesh(new THREE.BoxGeometry(0.18, 0.08, 0.1), bootsMat);
        bootL.position.set(0.03, 0.04, -0.11);
        const bootR = new THREE.Mesh(new THREE.BoxGeometry(0.18, 0.08, 0.1), bootsMat);
        bootR.position.set(0.03, 0.04, 0.11);
        opGroup.add(legL, legR, bootL, bootR);

        // Torso
        const torsoGeo = new THREE.BoxGeometry(0.32, 0.52, 0.4);
        const torso = new THREE.Mesh(torsoGeo, suitMat);
        torso.position.set(0, 0.96, 0);
        opGroup.add(torso);

        // Head with Hood & Visor
        const headGeo = new THREE.SphereGeometry(0.14, 12, 10);
        const head = new THREE.Mesh(headGeo, suitMat);
        head.position.set(0, 1.34, 0);

        const visorGeo = new THREE.BoxGeometry(0.08, 0.06, 0.18);
        const visor = new THREE.Mesh(visorGeo, darkVisorMat);
        visor.position.set(0.1, 1.34, 0);
        opGroup.add(head, visor);

        // Arms reaching forward to push handle
        const armGeo = new THREE.CylinderGeometry(0.04, 0.035, 0.42, 8);
        const armL = new THREE.Mesh(armGeo, suitMat);
        armL.rotation.z = -Math.PI / 3;
        armL.position.set(0.18, 1.05, -0.18);
        const armR = new THREE.Mesh(armGeo, suitMat);
        armR.rotation.z = -Math.PI / 3;
        armR.position.set(0.18, 1.05, 0.18);
        opGroup.add(armL, armR);

        opGroup.position.set(-0.75, 0, 0);
        group.add(opGroup);

        return group;
      }}

      function buildLogisticsSystem() {{
        logisticsGroup = new THREE.Group();
        logisticsGroup.name = "OSAT_Logistics";

        // 1. Floor Dashed Lane Markings on Corridor
        const lineGeo = new THREE.PlaneGeometry(0.8, 0.06);
        const lineMat = new THREE.MeshBasicMaterial({{
          color: 0xfbbf24,
          transparent: true,
          opacity: 0.45
        }});

        // Lane 1 (+Z: 1.15) & Lane 2 (-Z: -1.15)
        for (let x = -40; x <= 40; x += 2.5) {{
          const m1 = new THREE.Mesh(lineGeo, lineMat);
          m1.rotation.x = -Math.PI / 2;
          m1.position.set(x, 0.026, 1.15);
          const m2 = new THREE.Mesh(lineGeo, lineMat);
          m2.rotation.x = -Math.PI / 2;
          m2.position.set(x, 0.026, -1.15);
          logisticsGroup.add(m1, m2);
        }}

        // 2. Build 6 Vehicles spaced around the loop
        const configs = [
          {{ type: "amr", cargo: "foup", name: "AMR-01 (Wafer FOUP)" }},
          {{ type: "amr", cargo: "magazine", name: "AMR-02 (Leadframe Strip)" }},
          {{ type: "trolley", cargo: "wafers", name: "Cart-01 (Manual Trolley)" }},
          {{ type: "amr", cargo: "tray", name: "AMR-03 (JEDEC IC Trays)" }},
          {{ type: "amr", cargo: "reels", name: "AMR-04 (Tape & Reel)" }},
          {{ type: "trolley", cargo: "tools", name: "Cart-02 (Maintenance Trolley)" }}
        ];

        const spacing = L_TOTAL / configs.length;

        logisticsFleet = configs.map((cfg, idx) => {{
          const mesh = cfg.type === "amr" ? createAmrMesh(cfg.cargo) : createManualTrolleyMesh(cfg.cargo);
          logisticsGroup.add(mesh);
          return {{
            cfg: cfg,
            mesh: mesh,
            s: idx * spacing,
            speed: 2.2,
            beacon: mesh.userData.beacon || null
          }};
        }});

        scene.add(logisticsGroup);
      }}

      let lastAnimTime = 0;

      function updateLogisticsSimulation(time) {{
        if (!showLogistics || logisticsFleet.length === 0) return;
        const now = time * 0.001;
        const dt = Math.min(0.08, lastAnimTime > 0 ? (now - lastAnimTime) : 0.016);
        lastAnimTime = now;

        for (let i = 0; i < logisticsFleet.length; i++) {{
          const veh = logisticsFleet[i];
          veh.s += veh.speed * dt;
          const pose = getLoopPose(veh.s);
          veh.mesh.position.set(pose.x, 0.02, pose.z);
          veh.mesh.rotation.y = -pose.yaw;

          // Pulse beacon LED
          if (veh.beacon) {{
            const pulse = 0.5 + 0.5 * Math.sin(now * 8 + i * 1.5);
            veh.beacon.material.opacity = pulse > 0.4 ? 1.0 : 0.25;
            veh.beacon.material.color.setHex(pulse > 0.5 ? 0x10b981 : 0x0284c7);
          }}
        }}
      }}

      function toggleLogistics() {{
        showLogistics = !showLogistics;
        if (logisticsGroup) logisticsGroup.visible = showLogistics;
        const pill = document.getElementById("overlay-logistics-status");
        if (pill) {{
          pill.style.opacity = showLogistics ? "1" : "0.5";
        }}
      }}

      // ==========================================
      // 3. EQUIPMENT GENERATION & POSITIONING
      // ==========================================
      function computeBaySlots(bayCfg, count) {{
        const slots = [];
        const [xMin, xMax] = bayCfg.xRange;
        const [zMin, zMax] = bayCfg.zRange;
        const w = xMax - xMin;

        // Place equipment in two rows: North aisle (z > 3.5) and South aisle (z < -3.5)
        const northSlots = [];
        const southSlots = [];
        const half = Math.ceil(count / 2);

        // North aisle: z from 5 to 21
        const nSpan = 16;
        const nStep = nSpan / Math.max(half, 1);
        for (let i = 0; i < half; i++) {{
          northSlots.push({{
            x: (xMin + xMax) / 2,
            z: 5 + (i + 0.5) * nStep,
            rotY: 0
          }});
        }}

        // South aisle: z from -5 to -21
        const sCount = count - half;
        const sStep = nSpan / Math.max(sCount, 1);
        for (let i = 0; i < sCount; i++) {{
          southSlots.push({{
            x: (xMin + xMax) / 2,
            z: -5 - (i + 0.5) * sStep,
            rotY: Math.PI
          }});
        }}

        // Interleave North and South slots
        for (let i = 0; i < count; i++) {{
          if (i % 2 === 0 && northSlots.length > 0) {{
            slots.push(northSlots.shift());
          }} else if (southSlots.length > 0) {{
            slots.push(southSlots.shift());
          }} else if (northSlots.length > 0) {{
            slots.push(northSlots.shift());
          }}
        }}

        return slots;
      }}

      function loadAndRenderEquipment() {{
        interactiveMeshes = [];
        if (equipmentGroup) scene.remove(equipmentGroup);
        equipmentGroup = new THREE.Group();
        equipmentGroup.name = "osatEquipmentGroup";

        const raw = document.getElementById("osat-catalog-data").textContent;
        catalogRecords = JSON.parse(raw);

        // Group by category
        const byCat = {{}};
        Object.keys(OSAT_BAYS).forEach((k) => (byCat[k] = []));
        catalogRecords.forEach((item) => {{
          const c = item.category;
          if (byCat[c]) byCat[c].push(item);
        }});

        // Render equipment in each bay
        Object.entries(byCat).forEach(([catKey, items]) => {{
          const bayCfg = OSAT_BAYS[catKey];
          if (!bayCfg) return;

          const slots = computeBaySlots(bayCfg, items.length);

          // Sort dimensioned tools first
          const sorted = [...items].sort((a, b) => {{
            const aHas = a.record?.physical?.width_mm?.value ? 0 : 1;
            const bHas = b.record?.physical?.width_mm?.value ? 0 : 1;
            return aHas - bHas;
          }});

          sorted.forEach((item, idx) => {{
            const slot = slots[idx] || {{ x: bayCfg.xRange[0] + 2, z: 0, rotY: 0 }};
            const mesh = createTool3DMesh(item, slot, bayCfg);
            mesh.userData = {{ item: item, bay: bayCfg, slot: slot }};
            equipmentGroup.add(mesh);
            interactiveMeshes.push(mesh);
          }});
        }});

        scene.add(equipmentGroup);
        populateSidebarList(catalogRecords);
      }}

      function createTool3DMesh(item, slot, bayCfg) {{
        const group = new THREE.Group();
        group.position.set(slot.x, 0, slot.z);
        group.rotation.y = slot.rotY || 0;

        const phys = item.record?.physical || {{}};
        const hasRealDims = Boolean(phys.width_mm?.value);

        // Footprint width, depth, height in meters
        const w = hasRealDims ? phys.width_mm.value / 1000 : 2.2;
        const d = hasRealDims ? phys.depth_mm.value / 1000 : 2.6;
        const h = hasRealDims ? phys.height_mm.value / 1000 : 2.4;

        // Heavy concrete base plinth
        const baseGeo = new THREE.BoxGeometry(w + 0.25, 0.1, d + 0.25);
        const baseMat = new THREE.MeshStandardMaterial({{ color: 0x0f172a, roughness: 0.8 }});
        const base = new THREE.Mesh(baseGeo, baseMat);
        base.position.y = 0.05;
        group.add(base);

        // Main Tool Enclosure
        const bodyGeo = new THREE.BoxGeometry(w, h, d);
        let bodyMat;
        if (hasRealDims) {{
          // Solid Opaque High-Grade PBR
          bodyMat = new THREE.MeshStandardMaterial({{
            color: 0xf1f5f9,
            metalness: 0.35,
            roughness: 0.35
          }});
        }} else {{
          // High-Quality Cleanroom Enclosure
          bodyMat = new THREE.MeshStandardMaterial({{
            color: 0xe2e8f0,
            metalness: 0.25,
            roughness: 0.4
          }});
        }}
        const body = new THREE.Mesh(bodyGeo, bodyMat);
        body.position.y = h / 2 + 0.1;
        body.castShadow = true;
        body.receiveShadow = true;
        group.add(body);

        // Distinct Category Accent Band
        const bandGeo = new THREE.BoxGeometry(w + 0.02, 0.18, d + 0.02);
        const bandMat = new THREE.MeshBasicMaterial({{ color: bayCfg.color }});
        const band = new THREE.Mesh(bandGeo, bandMat);
        band.position.y = h * 0.7;
        group.add(band);

        // Status Stack Light (Andon Tower Beacon)
        const poleGeo = new THREE.CylinderGeometry(0.02, 0.02, 0.3, 8);
        const poleMat = new THREE.MeshStandardMaterial({{ color: 0x334155, metalness: 0.8 }});
        const pole = new THREE.Mesh(poleGeo, poleMat);
        pole.position.set(w / 2 - 0.15, h + 0.25, -d / 2 + 0.15);

        const beaconGeo = new THREE.CylinderGeometry(0.045, 0.045, 0.15, 12);
        const beaconMat = new THREE.MeshBasicMaterial({{ color: 0x10b981 }});
        const beacon = new THREE.Mesh(beaconGeo, beaconMat);
        beacon.position.set(w / 2 - 0.15, h + 0.45, -d / 2 + 0.15);
        group.add(pole, beacon);

        return group;
      }}

      // ==========================================
      // 4. SELECTION, RAYCASTING & INSPECTOR
      // ==========================================
      const raycaster = new THREE.Raycaster();
      const pointer = new THREE.Vector2();

      function onPointerDown(event) {{
        const rect = renderer.domElement.getBoundingClientRect();
        pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
        pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

        raycaster.setFromCamera(pointer, camera);
        const intersects = raycaster.intersectObjects(equipmentGroup.children, true);

        if (intersects.length > 0) {{
          let topGroup = intersects[0].object;
          while (topGroup.parent && topGroup.parent !== equipmentGroup) {{
            topGroup = topGroup.parent;
          }}
          if (topGroup.userData && topGroup.userData.item) {{
            selectEquipment(topGroup.userData.item, topGroup.userData.slot, true);
          }}
        }}
      }}

      function selectEquipment(item, slot, flyCam = false) {{
        selectedTool = item;
        const isZh = currentLang.startsWith("zh");

        // Open Right Panel
        const panel = document.getElementById("inspector-panel");
        panel.classList.remove("translate-x-full");

        // Fill Header Info
        const bayCfg = OSAT_BAYS[item.category] || {{ nameEn: "OSAT Bay", nameZh: "封测工位", hex: "#0e6e6b" }};
        const catBadge = document.getElementById("inspect-category-badge");
        catBadge.textContent = isZh ? bayCfg.nameZh : bayCfg.nameEn;
        catBadge.style.backgroundColor = bayCfg.hex || "var(--accent)";
        document.getElementById("inspect-vendor").textContent = item.vendor || "";
        document.getElementById("inspect-model").textContent = item.model || "";

        // Tier badge
        const tier = item.record?.identity?.vendor?.provenance?.tier || "inferred";
        const tierBadge = document.getElementById("inspect-tier-badge");
        if (tier === "vendor_confirmed") {{
          tierBadge.className = "px-1.5 py-0.5 text-[9px] font-mono font-bold rounded badge-vendor_confirmed";
          tierBadge.textContent = isZh ? "● 厂商官方核验" : "● Vendor Confirmed";
        }} else {{
          tierBadge.className = "px-1.5 py-0.5 text-[9px] font-mono font-bold rounded badge-inferred";
          tierBadge.textContent = isZh ? "● 推断数据" : "● Inferred";
        }}

        document.getElementById("inspect-wafer-size").textContent = (item.record?.identity?.wafer_sizes_mm?.value?.[0] ? `${{item.record.identity.wafer_sizes_mm.value[0]}}mm Wafer` : (isZh ? "引线框架 / 板级" : "Strip / Panel"));

        // Honesty Banner
        const hasRealDims = Boolean(item.record?.physical?.width_mm?.value);
        const honestyBanner = document.getElementById("inspect-honesty-banner");
        const towaNotice = document.getElementById("inspect-towa-notice");

        if (item.model === "(型号未公开)" || item.is_gap_row) {{
          honestyBanner.classList.add("hidden");
          towaNotice.classList.remove("hidden");
        }} else if (hasRealDims) {{
          honestyBanner.classList.add("hidden");
          towaNotice.classList.add("hidden");
        }} else {{
          honestyBanner.classList.remove("hidden");
          towaNotice.classList.add("hidden");
        }}

        // Dimensions
        const dimStatus = document.getElementById("inspect-dim-status");
        const dimVal = document.getElementById("inspect-dimensions");
        const weightVal = document.getElementById("inspect-weight");

        if (hasRealDims) {{
          const p = item.record.physical;
          dimStatus.textContent = isZh ? "官方实测" : "Verified";
          dimStatus.className = "text-[9px] text-emerald-600 font-bold";
          dimVal.textContent = `${{(p.width_mm.value / 1000).toFixed(2)}} × ${{(p.depth_mm.value / 1000).toFixed(2)}} × ${{(p.height_mm.value / 1000).toFixed(2)}} m`;
          weightVal.textContent = p.weight_kg?.value ? `${{p.weight_kg.value}} kg` : (isZh ? "待补充" : "Pending");
        }} else {{
          dimStatus.textContent = isZh ? "概念占位" : "Nominal";
          dimStatus.className = "text-[9px] text-amber-600 font-bold";
          dimVal.textContent = "2.20 × 2.60 × 2.40 m";
          weightVal.textContent = isZh ? "待实测" : "Pending";
        }}

        // Specs
        const cap = item.record?.process_capability?.capabilities?.[0]?.detail?.value;
        document.getElementById("inspect-specs").textContent = cap || item.key_specs || (isZh ? "高精度集成电路后道封装与测试工序机台。" : "High-precision back-end semiconductor packaging and testing tool.");

        // Notes & Link
        document.getElementById("inspect-notes").textContent = item.record?.notes || item.notes || "";
        const sourceUrl = item.record?.identity?.vendor?.provenance?.source || item.source_url || "#";
        const linkEl = document.getElementById("inspect-source-link");
        const linkText = document.getElementById("inspect-source-url");
        linkEl.href = sourceUrl;
        linkText.textContent = sourceUrl;

        // CTA
        const ctaBtn = document.getElementById("inspect-cta-contribute");
        ctaBtn.href = `/add-equipment.html?vendor=${{encodeURIComponent(item.vendor)}}&model=${{encodeURIComponent(item.model)}}`;

        // Highlight Box
        if (slot) {{
          updateHighlightBox(slot, hasRealDims ? item.record.physical : null);
          if (flyCam) {{
            flyCameraTo(
              new THREE.Vector3(slot.x + 4.5, 3.8, slot.z + 5.5),
              new THREE.Vector3(slot.x, 1.2, slot.z),
              800
            );
          }}
        }}

        if (window.lucide) lucide.createIcons();
      }}

      function updateHighlightBox(slot, phys) {{
        if (highlightBox) scene.remove(highlightBox);
        const w = phys?.width_mm?.value ? phys.width_mm.value / 1000 : 2.2;
        const d = phys?.depth_mm?.value ? phys.depth_mm.value / 1000 : 2.6;
        const h = phys?.height_mm?.value ? phys.height_mm.value / 1000 : 2.4;

        const geo = new THREE.BoxGeometry(w + 0.3, h + 0.3, d + 0.3);
        const edges = new THREE.EdgesGeometry(geo);
        const mat = new THREE.LineBasicMaterial({{ color: 0xf59e0b, linewidth: 2 }});
        highlightBox = new THREE.LineSegments(edges, mat);
        highlightBox.position.set(slot.x, h / 2 + 0.1, slot.z);
        scene.add(highlightBox);
      }}

      function closeInspector() {{
        document.getElementById("inspector-panel").classList.add("translate-x-full");
        if (highlightBox) {{
          scene.remove(highlightBox);
          highlightBox = null;
        }}
      }}

      // ==========================================
      // 5. SIDEBAR & FILTERS
      // ==========================================
      function populateSidebarList(records) {{
        const container = document.getElementById("equipment-list-container");
        container.innerHTML = "";

        const query = (document.getElementById("sidebar-search")?.value || "").toLowerCase().trim();

        const filtered = records.filter((item) => {{
          const matchesCat = activeFilter === "ALL" || item.category === activeFilter;
          const matchesQuery =
            !query ||
            item.vendor.toLowerCase().includes(query) ||
            item.model.toLowerCase().includes(query) ||
            (item.category && item.category.toLowerCase().includes(query));
          return matchesCat && matchesQuery;
        }});

        document.getElementById("sidebar-count-badge").textContent = filtered.length;

        filtered.forEach((item) => {{
          const card = document.createElement("div");
          card.className =
            "p-2 rounded border border-[var(--line)] bg-[var(--surface)] hover:border-[var(--accent)] cursor-pointer transition flex items-center justify-between text-xs";
          const tier = item.record?.identity?.vendor?.provenance?.tier || "inferred";
          const hasDims = Boolean(item.record?.physical?.width_mm?.value);
          const bayCfg = OSAT_BAYS[item.category];
          const catHex = bayCfg?.hex || "#0e6e6b";

          card.innerHTML = `
            <div class="overflow-hidden flex items-center gap-2">
              <span class="w-2 h-2 rounded-full shrink-0 shadow-xs" style="background-color: ${{catHex}};" title="${{item.category}}"></span>
              <div class="overflow-hidden">
                <div class="font-bold text-[var(--ink)] truncate">${{item.vendor}} <span class="text-[var(--accent)]">${{item.model}}</span></div>
                <div class="text-[10px] text-[var(--ink-3)] font-mono truncate">${{item.category.replace("osat_", "")}} · ${{item.wafer_size || "300mm"}}</div>
              </div>
            </div>
            <div class="flex flex-col items-end gap-1 shrink-0 ml-2">
              <span class="w-1.5 h-1.5 rounded-full ${{hasDims ? "bg-emerald-500" : "bg-amber-500"}}"></span>
              <span class="text-[9px] font-mono text-[var(--ink-3)]">${{hasDims ? "CAD" : "Draft"}}</span>
            </div>
          `;

          card.onclick = () => {{
            const mesh = interactiveMeshes.find((m) => m.userData.item.record_id === item.record_id);
            if (mesh) {{
              selectEquipment(item, mesh.userData.slot, true);
            }}
          }};

          container.appendChild(card);
        }});
      }}

      function handleSearch(val) {{
        const clearBtn = document.getElementById("search-clear-btn");
        if (clearBtn) clearBtn.classList.toggle("hidden", !val);
        populateSidebarList(catalogRecords);
      }}

      function clearSearch() {{
        const input = document.getElementById("sidebar-search");
        if (input) input.value = "";
        handleSearch("");
      }}

      function filterCategory(cat) {{
        activeFilter = cat;
        document.querySelectorAll(".cat-pill").forEach((btn) => {{
          const btnCat = btn.getAttribute("data-cat");
          const isAct = btnCat === cat;
          const bayCfg = OSAT_BAYS[btnCat];
          const dot = btn.querySelector(".cat-dot");

          if (isAct) {{
            btn.classList.add("active");
            if (btnCat === "ALL") {{
              btn.className = "cat-pill active px-2.5 py-1 rounded-full text-xs font-semibold border transition shrink-0 flex items-center gap-1.5 shadow-sm";
              btn.style.backgroundColor = "var(--accent)";
              btn.style.borderColor = "var(--accent)";
              btn.style.color = "#ffffff";
              if (dot) dot.style.backgroundColor = "#ffffff";
            }} else if (bayCfg) {{
              btn.className = "cat-pill active px-2.5 py-1 rounded-full text-xs font-semibold border transition shrink-0 flex items-center gap-1.5 shadow-sm";
              btn.style.backgroundColor = bayCfg.hex;
              btn.style.borderColor = bayCfg.hex;
              btn.style.color = "#ffffff";
              if (dot) dot.style.backgroundColor = "#ffffff";
            }}
          }} else {{
            btn.classList.remove("active");
            btn.className = "cat-pill px-2.5 py-1 rounded-full text-xs font-semibold border border-[var(--line)] bg-[var(--surface-2)] text-[var(--ink-2)] hover:border-[var(--accent)] transition shrink-0 flex items-center gap-1.5";
            btn.style.backgroundColor = "";
            btn.style.borderColor = "";
            btn.style.color = "";
            if (dot) {{
              dot.style.backgroundColor = btnCat === "ALL" ? "var(--accent)" : (bayCfg ? bayCfg.hex : "var(--accent)");
            }}
          }}
        }});

        populateSidebarList(catalogRecords);

        // Highlight/show relevant meshes
        interactiveMeshes.forEach((mesh) => {{
          const item = mesh.userData.item;
          mesh.visible = cat === "ALL" || item.category === cat;
        }});

        if (cat !== "ALL" && OSAT_BAYS[cat]) {{
          focusBay(cat);
        }}
      }}

      function focusBay(catKey) {{
        const bay = OSAT_BAYS[catKey];
        if (!bay) return;

        // Highlight active step button in floating flow bar
        document.querySelectorAll(".chevron-step").forEach((b) => {{
          b.classList.remove("active");
          b.style.backgroundColor = "";
          b.style.borderColor = "";
          b.style.color = "";
        }});
        const btn = Array.from(document.querySelectorAll(".chevron-step")).find((b) =>
          b.getAttribute("data-bay") === catKey || b.getAttribute("onclick")?.includes(catKey)
        );
        if (btn) {{
          btn.classList.add("active");
          btn.style.backgroundColor = bay.hex;
          btn.style.borderColor = bay.hex;
          btn.style.color = "#ffffff";
        }}

        const cx = (bay.xRange[0] + bay.xRange[1]) / 2;
        flyCameraTo(
          new THREE.Vector3(cx, 18, 28),
          new THREE.Vector3(cx, 1.5, 0),
          1000
        );
      }}

      // ==========================================
      // 6. CAMERA PRESETS & PROCESS TOUR
      // ==========================================
      let activeCamAnimId = 0;

      function flyCameraTo(endPos, endTarget, duration = 1000, onComplete = null) {{
        const animId = ++activeCamAnimId;
        const startPos = camera.position.clone();
        const startTarget = controls.target.clone();
        const startTime = performance.now();

        function step(time) {{
          if (animId !== activeCamAnimId) return;
          const elapsed = time - startTime;
          const progress = Math.min(elapsed / duration, 1);
          const ease = 0.5 - Math.cos(progress * Math.PI) / 2;

          camera.position.lerpVectors(startPos, endPos, ease);
          controls.target.lerpVectors(startTarget, endTarget, ease);
          controls.update();

          if (progress < 1) {{
            requestAnimationFrame(step);
          }} else {{
            if (typeof onComplete === "function") onComplete();
          }}
        }}
        requestAnimationFrame(step);
      }}

      function setCameraPreset(type) {{
        stopProcessTour();
        closeInspector();

        if (type === "iso") {{
          flyCameraTo(new THREE.Vector3(0, 48, 62), new THREE.Vector3(0, 1.5, 0));
        }} else if (type === "top") {{
          flyCameraTo(new THREE.Vector3(0, 85, 0.1), new THREE.Vector3(0, 0, 0));
        }} else if (type === "assembly") {{
          flyCameraTo(new THREE.Vector3(-24, 28, 38), new THREE.Vector3(-24, 1.5, 0));
        }} else if (type === "test") {{
          flyCameraTo(new THREE.Vector3(30, 28, 38), new THREE.Vector3(30, 1.5, 0));
        }}
      }}

      const TOUR_STAGES = [
        "osat_dicing",
        "osat_die_attach",
        "osat_wire_bonding",
        "osat_flip_chip",
        "osat_molding",
        "osat_singulation",
        "osat_bumping_rdl",
        "osat_prober",
        "osat_ate",
        "osat_test_handler",
        "osat_inspection"
      ];

      function toggleProcessTour() {{
        if (isTourRunning) {{
          stopProcessTour();
        }} else {{
          startProcessTour();
        }}
      }}

      function startProcessTour() {{
        isTourRunning = true;
        tourStep = 0;
        updateTourBtnUI(true);
        runTourStep();
      }}

      function stopProcessTour() {{
        isTourRunning = false;
        if (tourTimer) clearTimeout(tourTimer);
        tourTimer = null;
        updateTourBtnUI(false);
      }}

      function updateTourBtnUI(running) {{
        const btn = document.getElementById("btn-tour-toggle");
        const text = document.getElementById("tour-btn-text");
        if (!btn || !text) return;
        if (running) {{
          btn.className = "px-2 py-1 text-xs font-medium rounded-md bg-rose-600 text-white hover:bg-rose-700 transition flex items-center gap-1 shadow-sm animate-pulse";
          text.textContent = "Stop";
        }} else {{
          btn.className = "px-2 py-1 text-xs font-medium rounded-md bg-emerald-600 text-white hover:bg-emerald-700 transition flex items-center gap-1 shadow-sm";
          text.textContent = "Tour";
        }}
      }}

      function runTourStep() {{
        if (!isTourRunning) return;
        const catKey = TOUR_STAGES[tourStep % TOUR_STAGES.length];
        focusBay(catKey);

        tourTimer = setTimeout(() => {{
          if (!isTourRunning) return;
          tourStep++;
          runTourStep();
        }}, 4500);
      }}

      // ==========================================
      // 7. THEME & LOCALIZATION ENGINE
      // ==========================================
      function toggleTheme() {{
        currentTheme = currentTheme === "light" ? "dark" : "light";
        document.documentElement.setAttribute("data-theme", currentTheme);
        document.documentElement.className = currentTheme;
        localStorage.setItem("semicon_theme", currentTheme);
        updateThemeUI();
        updateSceneBackground();
      }}

      function updateThemeUI() {{
        const icon = document.getElementById("theme-icon");
        const label = document.getElementById("theme-label");
        const isDark = currentTheme === "dark";
        if (icon) icon.textContent = isDark ? "🌙" : "☀️";
        if (label) label.textContent = isDark ? "Dark" : "Day";
      }}

      function toggleLanguage() {{
        currentLang = currentLang.startsWith("zh") ? "en" : "zh-CN";
        localStorage.setItem("semiconfab_lang", currentLang);
        localStorage.setItem("semicon_lang", currentLang.startsWith("zh") ? "zh" : "en");
        if (typeof setLanguage === "function") {{
          try {{ setLanguage(currentLang); }} catch (e) {{}}
        }}
        updateLanguageUI();
        if (selectedTool) {{
          selectEquipment(selectedTool, null, false);
        }}
        populateSidebarList(catalogRecords);
      }}

      window.onSemiconLanguageChange = function(lang) {{
        currentLang = lang;
        updateLanguageUI();
        if (selectedTool) {{
          selectEquipment(selectedTool, null, false);
        }}
        populateSidebarList(catalogRecords);
      }};

      const FLOW_STEPS = {{
        osat_dicing: {{ en: "1. Dicing", zh: "1. 晶圆划片" }},
        osat_die_attach: {{ en: "2. Die Attach", zh: "2. 芯片贴装" }},
        osat_wire_bonding: {{ en: "3. Wire Bond", zh: "3. 引线键合" }},
        osat_flip_chip: {{ en: "4. Flip Chip", zh: "4. 倒装焊接" }},
        osat_molding: {{ en: "5. Molding", zh: "5. 模塑封装" }},
        osat_singulation: {{ en: "6. Singulation", zh: "6. 冲切分离" }},
        osat_bumping_rdl: {{ en: "7. Bumping/RDL", zh: "7. 凸块与RDL" }},
        osat_prober: {{ en: "8. Wafer Prober", zh: "8. 晶圆探针" }},
        osat_ate: {{ en: "9. ATE Test", zh: "9. ATE 测试" }},
        osat_test_handler: {{ en: "10. Test Handler", zh: "10. 终测分选" }},
        osat_inspection: {{ en: "11. AOI Inspection", zh: "11. 出厂检测" }}
      }};

      const CAT_PILL_LABELS = {{
        ALL: {{ en: "All (86)", zh: "全部 (86)" }},
        osat_dicing: {{ en: "Dicing (15)", zh: "划片 (15)" }},
        osat_die_attach: {{ en: "Die Attach (4)", zh: "贴片 (4)" }},
        osat_wire_bonding: {{ en: "Wire Bond (5)", zh: "键合 (5)" }},
        osat_flip_chip: {{ en: "Flip Chip (12)", zh: "倒装 (12)" }},
        osat_molding: {{ en: "Molding (1)", zh: "塑封 (1)" }},
        osat_singulation: {{ en: "Singulation (1)", zh: "冲切 (1)" }},
        osat_bumping_rdl: {{ en: "Bumping/RDL (3)", zh: "凸块 (3)" }},
        osat_prober: {{ en: "Prober (8)", zh: "探针 (8)" }},
        osat_ate: {{ en: "ATE (13)", zh: "ATE 测试 (13)" }},
        osat_test_handler: {{ en: "Handler (9)", zh: "分选 (9)" }},
        osat_inspection: {{ en: "Inspection (15)", zh: "检测 (15)" }}
      }};

      function updateLanguageUI() {{
        const isZh = currentLang.startsWith("zh");
        document.title = isZh ? "OSAT 后道封测数字孪生工厂 | SemiconFab" : "OSAT Packaging & Testing 3D Digital Twin | SemiconFab";
        const btnToggleLang = document.getElementById("btn-toggle-lang");
        if (btnToggleLang) btnToggleLang.textContent = isZh ? "中/En" : "En/中文";

        const headerSubtitle = document.getElementById("header-subtitle");
        if (headerSubtitle) {{
          headerSubtitle.textContent = isZh
            ? "OSAT 后道封测数字孪生工厂 · 从硅片到芯片出货"
            : "OSAT Packaging & Test Facility · From Wafer to Shipment";
        }}

        const linkFab = document.getElementById("link-fab-text");
        if (linkFab) linkFab.textContent = isZh ? "前道 300mm 晶圆孪生 →" : "300mm Fab Twin →";

        const camIso = document.getElementById("cam-iso-text");
        if (camIso) camIso.textContent = isZh ? "全局视角" : "Overview";
        const camTop = document.getElementById("cam-top-text");
        if (camTop) camTop.textContent = isZh ? "俯视布局" : "Top";
        const camAsm = document.getElementById("cam-asm-text");
        if (camAsm) camAsm.textContent = isZh ? "封测装配区" : "Assembly Hall";
        const camTest = document.getElementById("cam-test-text");
        if (camTest) camTest.textContent = isZh ? "终测大厅" : "Test Hall";

        const tourBtn = document.getElementById("tour-btn-text");
        if (tourBtn && !isTourRunning) tourBtn.textContent = isZh ? "漫游" : "Tour";

        const themeLabel = document.getElementById("theme-label");
        if (themeLabel) {{
          const isDark = currentTheme === "dark";
          themeLabel.textContent = isDark ? (isZh ? "暗色" : "Dark") : (isZh ? "亮色" : "Day");
        }}

        // Floating Process Flow Step Bar
        const labelFlow = document.getElementById("label-flow");
        if (labelFlow) labelFlow.textContent = isZh ? "工序流向:" : "Flow:";

        document.querySelectorAll(".chevron-step").forEach((btn) => {{
          const bay = btn.getAttribute("data-bay");
          const stepSpan = btn.querySelector(".step-name");
          if (stepSpan && bay && FLOW_STEPS[bay]) {{
            stepSpan.textContent = isZh ? FLOW_STEPS[bay].zh : FLOW_STEPS[bay].en;
          }}
        }});

        const statSummary = document.getElementById("stat-summary-tag");
        if (statSummary) {{
          statSummary.textContent = isZh
            ? "86 台设备 · 23 家主流设备厂商 · 11 大工艺区"
            : "86 Tools · 23 Tier-1 Vendors · 11 Bays";
        }}

        // Left sidebar
        const sidebarTitle = document.getElementById("sidebar-title");
        if (sidebarTitle) sidebarTitle.textContent = isZh ? "封测设备全量目录" : "OSAT Equipment Directory";

        const sidebarCatLink = document.getElementById("sidebar-catalog-link");
        if (sidebarCatLink) {{
          sidebarCatLink.innerHTML = "<span>" + (isZh ? "名录" : "Catalog") + '</span><i data-lucide="external-link" class="w-2.5 h-2.5"></i>';
        }}

        const searchInput = document.getElementById("sidebar-search");
        if (searchInput) {{
          searchInput.placeholder = isZh ? "搜索厂商、型号、工艺分类..." : "Search vendor, model, process...";
        }}

        // Overlay titles
        const overlayZoneTitle = document.getElementById("overlay-zone-title");
        if (overlayZoneTitle) {{
          overlayZoneTitle.textContent = isZh ? "OSAT 双大厅独立厂房 (108m × 51m)" : "OSAT Dual-Zone Facility (108m × 51m)";
        }}
        const overlayZoneSub = document.getElementById("overlay-zone-sub");
        if (overlayZoneSub) {{
          overlayZoneSub.textContent = isZh
            ? "西区: ISO 7-8 封装装配车间 · 东区: 终测与探针大厅"
            : "West: ISO 7-8 Assembly · East: Final Test Hall";
        }}
        const logisticsText = document.getElementById("logistics-status-text");
        if (logisticsText) {{
          logisticsText.textContent = isZh
            ? "自动化物流: 6 台运行中 (4台 AMR · 2台 人工推车)"
            : "Logistics: 6 Active (4 AMR · 2 Trolleys)";
        }}

        // Category pills
        document.querySelectorAll(".cat-pill").forEach((pill) => {{
          const cat = pill.getAttribute("data-cat");
          const labelSpan = pill.querySelector(".cat-label");
          if (labelSpan && cat && CAT_PILL_LABELS[cat]) {{
            labelSpan.textContent = isZh ? CAT_PILL_LABELS[cat].zh : CAT_PILL_LABELS[cat].en;
          }} else if (cat && CAT_PILL_LABELS[cat]) {{
            pill.textContent = isZh ? CAT_PILL_LABELS[cat].zh : CAT_PILL_LABELS[cat].en;
          }}
        }});

        // Inspector Drawer Labels & Notices
        const honestyTitle = document.getElementById("inspect-honesty-title");
        if (honestyTitle) honestyTitle.textContent = isZh ? "尺寸待实测" : "Dimensions pending verification";

        const honestyDesc = document.getElementById("inspect-honesty-desc");
        if (honestyDesc) {{
          honestyDesc.textContent = isZh
            ? "当前 3D 几何为工艺分类概念占位包络，尚未录入官方实测 CAD 外形尺寸。"
            : "3D scene geometry is a procedural category placeholder shell without physical CAD measurements.";
        }}

        const towaTitle = document.getElementById("inspect-towa-title");
        if (towaTitle) towaTitle.textContent = isZh ? "【缺口行说明】" : "【Gap Row Documentation】";

        const towaDesc = document.getElementById("inspect-towa-desc");
        if (towaDesc) {{
          towaDesc.textContent = isZh
            ? "TOWA 官网只公开技术说明、不公开型号命名——型号无法核实，本行即缺口标注。TOWA 约占全球芯片塑封设备 2/3 份额，涵盖多柱塞传递模塑与流动压缩模塑(FCM)。"
            : "TOWA discloses technical specifications only, withholding explicit model names. TOWA commands ~2/3 global market share in semiconductor molding (multi-plunger transfer & compression molding).";
        }}

        const ctaText = document.getElementById("inspect-cta-text");
        if (ctaText) ctaText.textContent = isZh ? "+ 提交经核验的设备参数" : "+ Contribute Verified Equipment Specs";

        const envelopeLabel = document.getElementById("inspect-envelope-label");
        if (envelopeLabel) envelopeLabel.textContent = isZh ? "物理外形包络 (SEMI E72)" : "Physical Envelope (SEMI E72)";

        const dimLabel = document.getElementById("inspect-dim-label");
        if (dimLabel) dimLabel.textContent = isZh ? "几何尺寸 (长×宽×高):" : "Dimensions (W×D×H):";

        const weightLabel = document.getElementById("inspect-weight-label");
        if (weightLabel) weightLabel.textContent = isZh ? "设备整备毛重:" : "Gross Weight:";

        const specsLabel = document.getElementById("inspect-specs-label");
        if (specsLabel) specsLabel.textContent = isZh ? "核心关键技术规格" : "Key Technical Specs";

        const provLabel = document.getElementById("inspect-prov-label");
        if (provLabel) provLabel.textContent = isZh ? "数据来源与存证" : "Data Provenance";
      }}

      function onWindowResize() {{
        const container = document.getElementById("three-canvas");
        const width = container.clientWidth;
        const height = container.clientHeight;
        camera.aspect = width / height;
        camera.updateProjectionMatrix();
        renderer.setSize(width, height);
      }}

      function animate(time) {{
        requestAnimationFrame(animate);
        controls.update();
        if (typeof updateLogisticsSimulation === "function") {{
          updateLogisticsSimulation(time || performance.now());
        }}
        renderer.render(scene, camera);
      }}

      // ==========================================
      // 8. INITIALIZATION
      // ==========================================
      window.addEventListener("DOMContentLoaded", () => {{
        document.documentElement.setAttribute("data-theme", currentTheme);
        document.documentElement.className = currentTheme;
        updateThemeUI();
        updateLanguageUI();

        initThree();
        loadAndRenderEquipment();

        // Handle URL parameters
        const urlP = new URLSearchParams(window.location.search);
        const modelParam = urlP.get("model") || urlP.get("tool");
        if (modelParam) {{
          const found = catalogRecords.find((x) =>
            x.model?.toLowerCase() === modelParam.toLowerCase() ||
            x.record_id === modelParam
          );
          if (found) {{
            const mesh = interactiveMeshes.find((m) => m.userData.item.record_id === found.record_id);
            if (mesh) {{
              selectEquipment(found, mesh.userData.slot, false);
              const s = mesh.userData.slot;
              camera.position.set(s.x + 4.5, 3.8, s.z + 5.5);
              controls.target.set(s.x, 1.2, s.z);
              controls.update();
            }}
          }}
        }}

        if (window.lucide) lucide.createIcons();
      }});
    </script>
  </body>
</html>
'''

with open('twin-osat.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated twin-osat.html successfully! File size: {len(html_content)} bytes")
