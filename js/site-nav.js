/**
 * SemiconFab.org - Unified Site Navigation & Responsive Mobile Controller
 * Offline Compatible · Zero External Network Dependencies · Pure Vanilla JS
 * Architecture: Global Dual-Theme (Light/Dark) Engine + Multilingual Controller
 * Version: 1.9.0
 */

(function () {
  "use strict";

  const NAV_I18N = {
    en: {
      brandSub: "300mm Fab Digital Twin",
      navTwins: "3D Twins",
      navEquipment: "Equipment",
      navCost: "Cost",
      navLearn: "Learn",
      navResearch: "Research",
      langBtn: "EN / 中文",
      themeLight: "Light",
      themeDark: "Dark",
      themeTitle: "Switch Light / Dark Theme",
      navGuide: "Guide",
      navGuideTitle: "User Guide · Platform Walkthrough",
      // Dropdown & Drawer items
      twinFab: "300mm Fab Twin",
      twinFabDesc: "Class 1 Cleanroom & Subfab Twin (121 Tools)",
      twinMega: "3nm Mega Fab Concept (3,000 Tools)",
      twinMegaDesc: "Conceptual Layout Model · 50k WSPM Dual-Phase Fab",
      twinOsat: "OSAT Packaging & Test Twin",
      twinOsatDesc: "Dual-Hall Packaging & ATE Test Facility (86 Tools)",
      layoutEditor: "2D Layout Editor",
      layoutEditorDesc: "Architectural Cleanroom Bay Design",

      catalog: "Equipment Catalog",
      catalogDesc: "253 OEM Models · 167 FAB + 86 OSAT",
      compare: "Compare Tools",
      compareDesc: "Side-by-side specs & price estimates",
      addEquip: "Add Equipment",
      addEquipDesc: "JSON Schema Generator",
      dataStandard: "Data Standard",
      dataStandardDesc: "Open JSON Schema v1.0",
      verification: "Verification",
      verificationDesc: "Provenance policy",

      fabCost: "Construction Cost Report",
      fabCostDesc: "Top-down research report",
      fabCapex: "Capex Estimator",
      fabCapexDesc: "Bottom-up interactive estimator",

      deviceLibrary: "3D Device Library",
      finfet: "FinFET",
      finfetDesc: "Tri-Gate RMG Architecture (14nm/7nm)",
      gaafet: "GAAFET",
      gaafetDesc: "Nanosheet Transistor Flow (3nm/2nm)",
      dram: "DRAM",
      dramDesc: "Buried Wordline & Capacitor (1T1C)",
      nand: "3D NAND",
      nandDesc: "Charge Trap & Replacement Gate",
      hbm: "HBM",
      hbmDesc: "3D TSV Stacking & Packaging",
      dataLayer: "Fab Data Layer",
      dataLayerDesc: "How fab data flows, layer by layer",
      fabMes: "MES & Dispatch",
      fabMesDesc: "How MES routes and dispatches lots",
      fabOperations: "Fab Operations",
      fabOperationsDesc: "Map of fab operations topics",

      benchmark: "MIMAC-2026 Benchmark",
      benchmarkDesc: "Fab scheduling benchmark",
      vision: "Vision",
      visionDesc: "Open initiative manifesto",

      // Footer
      footerTagline:
        "Open-access digital twin and equipment engineering repository for 300mm semiconductor fabs.",
      footerLicense:
        "Source-available under PolyForm Noncommercial 1.0.0. Free for education, academic research, and personal use.",
      footerQuickLinks: "Navigation",
      footerModels: "3D Models",
      footerLegal: "Project Info",
      footerRights: "SemiconFab.org Initiative · Community Maintained",
    },
    zh: {
      brandSub: "300mm晶圆厂数字孪生",
      navTwins: "数字孪生",
      navEquipment: "设备",
      navCost: "成本",
      navLearn: "学习",
      navResearch: "研究",
      langBtn: "EN / 中文",
      themeLight: "亮色",
      themeDark: "暗色",
      themeTitle: "切换明暗主题 (亮色 / 暗色)",
      navGuide: "Guide",
      navGuideTitle: "使用指南 · 平台全景操作手册",
      // Dropdown & Drawer items
      twinFab: "300mm洁净室孪生",
      twinFabDesc: "ISO 1级洁净室与次层动力系统 (121台)",
      twinMega: "3nm 概念超级晶圆厂 (3,000机台)",
      twinMegaDesc: "概念布局推演示意模型 (Conceptual Layout Model)",
      twinOsat: "封测厂数字孪生",
      twinOsatDesc: "双大厅后道封装与高密度 ATE 终测厂房 (86台)",
      layoutEditor: "2D厂房布局编辑器",
      layoutEditorDesc: "洁净室工艺区空间规划",

      catalog: "设备名录",
      catalogDesc: "253款机台 · 167前道 + 86封测",
      compare: "机台对比",
      compareDesc: "多机台参数与价格横向对比",
      addEquip: "新增设备录入",
      addEquipDesc: "标准 JSON Schema 生成器",
      dataStandard: "数据交换标准",
      dataStandardDesc: "半导体设备 Schema v1.0",
      verification: "验证",
      verificationDesc: "来源可信度政策",

      fabCost: "建设成本报告",
      fabCostDesc: "自顶向下研究报告",
      fabCapex: "总投资测算器",
      fabCapexDesc: "自底向上交互式测算器",

      deviceLibrary: "3D器件库",
      finfet: "FinFET",
      finfetDesc: "三维鳍式场效应晶体管 (14nm/7nm)",
      gaafet: "GAAFET",
      gaafetDesc: "全环绕栅极纳米片全流程 (3nm/2nm)",
      dram: "DRAM",
      dramDesc: "埋入式字线与高深宽比电容 (1T1C)",
      nand: "3D NAND",
      nandDesc: "电荷俘获与替代栅极堆叠",
      hbm: "HBM",
      hbmDesc: "3D TSV 硅通孔微凸块先进封装",
      dataLayer: "晶圆厂数据层",
      dataLayerDesc: "数据如何一层层流动",
      fabMes: "MES 与派工",
      fabMesDesc: "MES 如何建路由与派工",
      fabOperations: "晶圆厂运营",
      fabOperationsDesc: "Fab 运营话题地图",

      benchmark: "MIMAC-2026 调度基准",
      benchmarkDesc: "晶圆厂调度基准",
      vision: "愿景",
      visionDesc: "倡议宣言",

      // Footer
      footerTagline:
        "面向 300mm 晶圆制造的开放数字孪生、设备工程学与总造价建模平台。",
      footerLicense:
        "源码遵循 PolyForm Noncommercial 1.0.0 协议公开发布，教育、科研与个人使用完全免费。",
      footerQuickLinks: "核心导航",
      footerModels: "3D数字化模型",
      footerLegal: "项目信息",
      footerRights: "SemiconFab.org 倡议组织 · 社区协同维护",
    },
  };

  // 1. Language Handling
  function getLang() {
    const params = new URLSearchParams(window.location.search);
    const langParam = params.get("lang");
    if (langParam === "zh" || langParam === "zh-CN" || langParam === "zh-TW")
      return "zh";
    if (langParam === "en") return "en";
    const saved = localStorage.getItem("semicon_lang");
    if (saved === "zh" || saved === "en") return saved;
    return navigator.language && navigator.language.startsWith("zh")
      ? "zh"
      : "en";
  }

  function setLang(lang) {
    localStorage.setItem("semicon_lang", lang);
    const url = new URL(window.location.href);
    url.searchParams.set("lang", lang);
    window.location.href = url.toString();
  }

  // 2. Theme Handling (Light Mode Default + Dark Mode Option)
  function getTheme() {
    const params = new URLSearchParams(window.location.search);
    const themeParam = params.get("theme");
    if (themeParam === "dark" || themeParam === "light") {
      localStorage.setItem("semicon_theme", themeParam);
      return themeParam;
    }
    const saved = localStorage.getItem("semicon_theme");
    if (saved === "dark" || saved === "light") return saved;
    return "light"; // Default to light mode per user preference
  }

  function applyTheme(theme) {
    localStorage.setItem("semicon_theme", theme);
    const html = document.documentElement;
    if (theme === "dark") {
      html.classList.add("dark");
      html.classList.remove("light");
      html.setAttribute("data-theme", "dark");
    } else {
      html.classList.add("light");
      html.classList.remove("dark");
      html.setAttribute("data-theme", "light");
    }

    const lang = getLang();
    const t = NAV_I18N[lang] || NAV_I18N.en;
    document.querySelectorAll(".sc-btn-theme-toggle").forEach(function (btn) {
      const icon = btn.querySelector(".sc-theme-icon");
      const label = btn.querySelector(".sc-theme-label");
      if (icon) icon.textContent = theme === "dark" ? "🌙" : "☀️";
      if (label)
        label.textContent = theme === "dark" ? t.themeDark : t.themeLight;
    });

    if (typeof window.onSemiconThemeChange === "function") {
      try {
        window.onSemiconThemeChange(theme);
      } catch (e) {
        console.warn("Theme change callback error:", e);
      }
    }
  }

  function toggleTheme() {
    const current = getTheme();
    const next = current === "dark" ? "light" : "dark";
    applyTheme(next);
  }

  // Apply theme immediately to prevent any flash of dark mode
  applyTheme(getTheme());

  function getCurrentPath() {
    let pathname = window.location.pathname;
    if (pathname.endsWith("/") && pathname.length > 1) {
      pathname = pathname.slice(0, -1);
    }
    let segment = pathname.substring(pathname.lastIndexOf("/") + 1);
    if (!segment || segment === "index.html") return "index";
    if (segment.endsWith(".html")) segment = segment.slice(0, -5);
    return segment;
  }

  function renderNavbar(lang, theme) {
    const t = NAV_I18N[lang];
    const cur = getCurrentPath();

    const isTwinActive = [
      "twin",
      "twin-mega",
      "twin-osat",
      "layout-editor",
    ].includes(cur);
    const isEquipActive = [
      "catalog-demo",
      "compare",
      "add-equipment",
      "data-standard",
      "verification",
    ].includes(cur);
    const isCostActive = ["fab-cost", "fab-capex"].includes(cur);
    const isLearnActive = [
      "finfet",
      "gaa",
      "dram",
      "nand",
      "hbm",
      "fab-data-layer",
      "fab-mes",
      "fab-operations",
    ].includes(cur);
    const isResearchActive = ["benchmark", "vision"].includes(cur);

    return `
      <header class="sc-header" role="banner">
        <div class="sc-header-inner">
          <!-- Logo & Brand -->
          <a href="/" class="sc-brand">
            <div class="sc-brand-icon">
              <svg width="20" height="20" viewBox="0 0 48 48" fill="none">
                <path d="M24 4C13.2 4 4.4 12.6 4 23.3C3.6 34.3 12.3 43.4 23.3 43.98C23.6 44 23.8 43.6 23.8 43.3C23.8 42.2 24.2 41.6 24.9 41.6C25.6 41.6 26 42.2 26 43.3C26 43.6 26.2 44 26.5 43.98C37.5 43.4 46.2 34.3 45.8 23.3C45.4 12.6 36.6 4 25.8 4H24Z" stroke="currentColor" stroke-width="2.8" stroke-linejoin="round"/>
                <line x1="12" y1="18" x2="38" y2="18" stroke="currentColor" stroke-width="1.4"/>
                <line x1="9" y1="25" x2="41" y2="25" stroke="currentColor" stroke-width="1.4"/>
                <line x1="12" y1="32" x2="38" y2="32" stroke="currentColor" stroke-width="1.4"/>
                <line x1="18" y1="12" x2="18" y2="38" stroke="currentColor" stroke-width="1.4"/>
                <line x1="25" y1="9" x2="25" y2="39" stroke="currentColor" stroke-width="1.4"/>
                <line x1="32" y1="12" x2="32" y2="38" stroke="currentColor" stroke-width="1.4"/>
                <rect x="26.2" y="19.2" width="4.6" height="4.6" rx="0.8" fill="var(--sc-accent-cyan, #0e6e6b)"/>
              </svg>
            </div>
            <div class="sc-brand-title">
              <span>SemiconFab<span class="sc-brand-tld">.org</span></span>
              <span class="sc-brand-tag">v1.9</span>
            </div>
          </a>

          <!-- Desktop Navigation: 5 Categories -->
          <nav class="sc-desktop-nav" aria-label="Main Navigation">
            <!-- 1. 3D Twins Dropdown -->
            <div class="sc-nav-item">
              <button type="button" class="sc-nav-link ${isTwinActive ? "active" : ""}">
                <span>${t.navTwins}</span>
                <svg class="sc-nav-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="sc-dropdown-panel">
                <a href="/twin" class="sc-dropdown-item ${cur === "twin" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.twinFab}</span>
                  <span class="sc-dropdown-desc">${t.twinFabDesc}</span>
                </a>
                <a href="/twin-mega" class="sc-dropdown-item ${cur === "twin-mega" ? "active" : ""}">
                  <span class="sc-dropdown-title" style="color:var(--sc-accent-cyan); font-weight:700;">${t.twinMega}</span>
                  <span class="sc-dropdown-desc">${t.twinMegaDesc}</span>
                </a>
                <a href="/twin-osat" class="sc-dropdown-item ${cur === "twin-osat" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.twinOsat}</span>
                  <span class="sc-dropdown-desc">${t.twinOsatDesc}</span>
                </a>
                <a href="/layout-editor" class="sc-dropdown-item ${cur === "layout-editor" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.layoutEditor}</span>
                  <span class="sc-dropdown-desc">${t.layoutEditorDesc}</span>
                </a>
              </div>
            </div>

            <!-- 2. Equipment Dropdown -->
            <div class="sc-nav-item">
              <button type="button" class="sc-nav-link ${isEquipActive ? "active" : ""}">
                <span>${t.navEquipment}</span>
                <svg class="sc-nav-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="sc-dropdown-panel">
                <a href="/catalog-demo" class="sc-dropdown-item ${cur === "catalog-demo" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.catalog}</span>
                  <span class="sc-dropdown-desc">${t.catalogDesc}</span>
                </a>
                <a href="/compare" class="sc-dropdown-item ${cur === "compare" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.compare}</span>
                  <span class="sc-dropdown-desc">${t.compareDesc}</span>
                </a>
                <a href="/add-equipment" class="sc-dropdown-item ${cur === "add-equipment" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.addEquip}</span>
                  <span class="sc-dropdown-desc">${t.addEquipDesc}</span>
                </a>
                <a href="/data-standard" class="sc-dropdown-item ${cur === "data-standard" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.dataStandard}</span>
                  <span class="sc-dropdown-desc">${t.dataStandardDesc}</span>
                </a>
                <a href="/verification" class="sc-dropdown-item ${cur === "verification" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.verification}</span>
                  <span class="sc-dropdown-desc">${t.verificationDesc}</span>
                </a>
              </div>
            </div>

            <!-- 3. Cost Dropdown -->
            <div class="sc-nav-item">
              <button type="button" class="sc-nav-link ${isCostActive ? "active" : ""}">
                <span>${t.navCost}</span>
                <svg class="sc-nav-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="sc-dropdown-panel">
                <a href="/fab-cost" class="sc-dropdown-item ${cur === "fab-cost" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.fabCost}</span>
                  <span class="sc-dropdown-desc">${t.fabCostDesc}</span>
                </a>
                <a href="/fab-capex" class="sc-dropdown-item ${cur === "fab-capex" ? "active" : ""}">
                  <span class="sc-dropdown-title" style="color:var(--sc-accent-cyan)">${t.fabCapex}</span>
                  <span class="sc-dropdown-desc">${t.fabCapexDesc}</span>
                </a>
              </div>
            </div>

            <!-- 4. Learn Dropdown -->
            <div class="sc-nav-item">
              <button type="button" class="sc-nav-link ${isLearnActive ? "active" : ""}">
                <span>${t.navLearn}</span>
                <svg class="sc-nav-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="sc-dropdown-panel">
                <div class="sc-dropdown-header" style="padding: 6px 12px; font-size: 11px; font-weight: 700; color: var(--sc-text-dim); text-transform: uppercase; letter-spacing: 0.05em;">
                  ${t.deviceLibrary}
                </div>
                <a href="/finfet" class="sc-dropdown-item ${cur === "finfet" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.finfet}</span>
                  <span class="sc-dropdown-desc">${t.finfetDesc}</span>
                </a>
                <a href="/gaa" class="sc-dropdown-item ${cur === "gaa" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.gaafet}</span>
                  <span class="sc-dropdown-desc">${t.gaafetDesc}</span>
                </a>
                <a href="/dram" class="sc-dropdown-item ${cur === "dram" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.dram}</span>
                  <span class="sc-dropdown-desc">${t.dramDesc}</span>
                </a>
                <a href="/nand" class="sc-dropdown-item ${cur === "nand" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.nand}</span>
                  <span class="sc-dropdown-desc">${t.nandDesc}</span>
                </a>
                <a href="/hbm" class="sc-dropdown-item ${cur === "hbm" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.hbm}</span>
                  <span class="sc-dropdown-desc">${t.hbmDesc}</span>
                </a>
                <a href="/fab-data-layer" class="sc-dropdown-item ${cur === "fab-data-layer" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.dataLayer}</span>
                  <span class="sc-dropdown-desc">${t.dataLayerDesc}</span>
                </a>
                <a href="/fab-mes" class="sc-dropdown-item ${cur === "fab-mes" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.fabMes}</span>
                  <span class="sc-dropdown-desc">${t.fabMesDesc}</span>
                </a>
                <a href="/fab-operations" class="sc-dropdown-item ${cur === "fab-operations" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.fabOperations}</span>
                  <span class="sc-dropdown-desc">${t.fabOperationsDesc}</span>
                </a>
              </div>
            </div>

            <!-- 5. Research Dropdown -->
            <div class="sc-nav-item">
              <button type="button" class="sc-nav-link ${isResearchActive ? "active" : ""}">
                <span>${t.navResearch}</span>
                <svg class="sc-nav-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="sc-dropdown-panel">
                <a href="/benchmark" class="sc-dropdown-item ${cur === "benchmark" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.benchmark}</span>
                  <span class="sc-dropdown-desc">${t.benchmarkDesc}</span>
                </a>
                <a href="/vision" class="sc-dropdown-item ${cur === "vision" ? "active" : ""}">
                  <span class="sc-dropdown-title">${t.vision}</span>
                  <span class="sc-dropdown-desc">${t.visionDesc}</span>
                </a>
              </div>
            </div>
          </nav>

          <!-- Right Action Controls -->
          <div class="sc-header-actions">
            <!-- Guide Button -->
            <a href="/guide" class="sc-btn-guide ${cur === "guide" ? "active" : ""}" title="${t.navGuideTitle || "User Guide"}">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
                <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
              </svg>
              <span>Guide</span>
            </a>

            <!-- Theme Switcher Button -->
            <button type="button" id="sc-btn-theme-toggle" class="sc-btn-theme-toggle" title="${t.themeTitle}">
              <span class="sc-theme-icon">${theme === "dark" ? "🌙" : "☀️"}</span>
              <span class="sc-theme-label">${theme === "dark" ? t.themeDark : t.themeLight}</span>
            </button>

            <!-- Language Switcher Button -->
            <button type="button" id="sc-btn-lang-toggle" class="sc-btn-lang" title="${lang === "zh" ? "Switch to English" : "切换为中文"}">
              <span>EN / 中文</span>
            </button>

            <!-- Mobile Hamburger Button -->
            <button type="button" id="sc-btn-hamburger" class="sc-hamburger-btn" aria-label="Toggle mobile menu">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="3" y1="12" x2="21" y2="12"></line>
                <line x1="3" y1="6" x2="21" y2="6"></line>
                <line x1="3" y1="18" x2="21" y2="18"></line>
              </svg>
            </button>
          </div>
        </div>
      </header>

      <!-- Mobile Backdrop -->
      <div id="sc-mobile-backdrop" class="sc-mobile-backdrop"></div>

      <!-- Mobile Slide-Out Drawer -->
      <aside id="sc-mobile-drawer" class="sc-mobile-drawer" aria-label="Mobile Navigation">
        <!-- 1. 3D Twins -->
        <div class="sc-drawer-section">
          <div class="sc-drawer-heading">${t.navTwins}</div>
          <a href="/twin" class="sc-drawer-link ${cur === "twin" ? "active" : ""}">
            <span>${t.twinFab}</span>
            <span class="sc-drawer-badge">121</span>
          </a>
          <a href="/twin-mega" class="sc-drawer-link ${cur === "twin-mega" ? "active" : ""}">
            <span style="font-weight:700; color:var(--sc-accent-cyan)">${t.twinMega}</span>
            <span class="sc-drawer-badge" style="background-color:var(--sc-accent-cyan); color:#fff">3,000</span>
          </a>
          <a href="/twin-osat" class="sc-drawer-link ${cur === "twin-osat" ? "active" : ""}">
            <span>${t.twinOsat}</span>
            <span class="sc-drawer-badge">86</span>
          </a>
          <a href="/layout-editor" class="sc-drawer-link ${cur === "layout-editor" ? "active" : ""}">
            <span>${t.layoutEditor}</span>
          </a>
        </div>

        <!-- 2. Equipment -->
        <div class="sc-drawer-section">
          <div class="sc-drawer-heading">${t.navEquipment}</div>
          <a href="/catalog-demo" class="sc-drawer-link ${cur === "catalog-demo" ? "active" : ""}">
            <span>${t.catalog}</span>
            <span class="sc-drawer-badge">253</span>
          </a>
          <a href="/compare" class="sc-drawer-link ${cur === "compare" ? "active" : ""}">
            <span>${t.compare}</span>
          </a>
          <a href="/add-equipment" class="sc-drawer-link ${cur === "add-equipment" ? "active" : ""}">
            <span>${t.addEquip}</span>
          </a>
          <a href="/data-standard" class="sc-drawer-link ${cur === "data-standard" ? "active" : ""}">
            <span>${t.dataStandard}</span>
          </a>
          <a href="/verification" class="sc-drawer-link ${cur === "verification" ? "active" : ""}">
            <span>${t.verification}</span>
          </a>
        </div>

        <!-- 3. Cost -->
        <div class="sc-drawer-section">
          <div class="sc-drawer-heading">${t.navCost}</div>
          <a href="/fab-cost" class="sc-drawer-link ${cur === "fab-cost" ? "active" : ""}">
            <span>${t.fabCost}</span>
            <span class="sc-drawer-badge">Report</span>
          </a>
          <a href="/fab-capex" class="sc-drawer-link ${cur === "fab-capex" ? "active" : ""}">
            <span style="color:var(--sc-accent-cyan)">${t.fabCapex}</span>
            <span class="sc-drawer-badge">BOM</span>
          </a>
        </div>

        <!-- 4. Learn -->
        <div class="sc-drawer-section">
          <div class="sc-drawer-heading">${t.navLearn}</div>
          <a href="/finfet" class="sc-drawer-link ${cur === "finfet" ? "active" : ""}">
            <span>${t.finfet}</span>
          </a>
          <a href="/gaa" class="sc-drawer-link ${cur === "gaa" ? "active" : ""}">
            <span>${t.gaafet}</span>
          </a>
          <a href="/dram" class="sc-drawer-link ${cur === "dram" ? "active" : ""}">
            <span>${t.dram}</span>
          </a>
          <a href="/nand" class="sc-drawer-link ${cur === "nand" ? "active" : ""}">
            <span>${t.nand}</span>
          </a>
          <a href="/hbm" class="sc-drawer-link ${cur === "hbm" ? "active" : ""}">
            <span>${t.hbm}</span>
          </a>
          <a href="/fab-data-layer" class="sc-drawer-link ${cur === "fab-data-layer" ? "active" : ""}">
            <span>${t.dataLayer}</span>
          </a>
          <a href="/fab-mes" class="sc-drawer-link ${cur === "fab-mes" ? "active" : ""}">
            <span>${t.fabMes}</span>
          </a>
          <a href="/fab-operations" class="sc-drawer-link ${cur === "fab-operations" ? "active" : ""}">
            <span>${t.fabOperations}</span>
          </a>
        </div>

        <!-- 5. Research -->
        <div class="sc-drawer-section">
          <div class="sc-drawer-heading">${t.navResearch}</div>
          <a href="/benchmark" class="sc-drawer-link ${cur === "benchmark" ? "active" : ""}">
            <span>${t.benchmark}</span>
          </a>
          <a href="/vision" class="sc-drawer-link ${cur === "vision" ? "active" : ""}">
            <span>${t.vision}</span>
          </a>
        </div>

        <!-- 6. Guide -->
        <div class="sc-drawer-section">
          <div class="sc-drawer-heading">${lang === "zh" ? "使用指南" : "Documentation"}</div>
          <a href="/guide" class="sc-drawer-link ${cur === "guide" ? "active" : ""}">
            <span style="font-weight: 700; color: var(--sc-accent-cyan);">${lang === "zh" ? "使用指南 (Guide)" : "User Guide"}</span>
            <span class="sc-drawer-badge">v1.9</span>
          </a>
        </div>

        <!-- Mobile Drawer Action Controls -->
        <div class="sc-drawer-controls">
          <button type="button" id="sc-drawer-btn-theme-toggle" class="sc-btn-theme-toggle" style="flex: 1;" title="${t.themeTitle}">
            <span class="sc-theme-icon">${theme === "dark" ? "🌙" : "☀️"}</span>
            <span class="sc-theme-label">${theme === "dark" ? t.themeDark : t.themeLight}</span>
          </button>
          <button type="button" id="sc-drawer-btn-lang-toggle" class="sc-btn-lang" style="flex: 1;" title="${lang === "zh" ? "Switch to English" : "切换为中文"}">
            <span>EN / 中文</span>
          </button>
        </div>
      </aside>
    `;
  }

  function renderFooter(lang) {
    const t = NAV_I18N[lang];
    return `
      <footer class="sc-footer" role="contentinfo">
        <div class="sc-footer-inner">
          <div class="sc-footer-col">
            <h5>SemiconFab.org</h5>
            <p style="margin: 0 0 12px 0; max-width: 320px; line-height: 1.6;">${t.footerTagline}</p>
            <p style="margin: 0; font-size: 0.75rem; color: var(--sc-text-dim); line-height: 1.5;">${t.footerLicense}</p>
          </div>
          <div class="sc-footer-col">
            <h5>${t.footerQuickLinks}</h5>
            <ul>
              <li><a href="/guide" style="font-weight: 700; color: var(--sc-accent-cyan);">${lang === "zh" ? "使用指南 (Guide)" : "User Guide"}</a></li>
              <li><a href="/twin">${t.twinFab}</a></li>
              <li><a href="/twin-mega" style="font-weight: 700; color: var(--sc-accent-cyan);">${t.twinMega} (3,000)</a></li>
              <li><a href="/twin-osat">${t.twinOsat}</a></li>
              <li><a href="/layout-editor">${t.layoutEditor}</a></li>
              <li><a href="/catalog-demo">${t.catalog}</a></li>
              <li><a href="/compare">${t.compare}</a></li>
              <li><a href="/fab-cost">${t.fabCost}</a></li>
              <li><a href="/fab-capex">${t.fabCapex}</a></li>
            </ul>
          </div>
          <div class="sc-footer-col">
            <h5>${t.footerModels}</h5>
            <ul>
              <li><a href="/finfet">${t.finfet}</a></li>
              <li><a href="/gaa">${t.gaafet}</a></li>
              <li><a href="/dram">${t.dram}</a></li>
              <li><a href="/nand">${t.nand}</a></li>
              <li><a href="/hbm">${t.hbm}</a></li>
            </ul>
          </div>
          <div class="sc-footer-col">
            <h5>${t.footerLegal}</h5>
            <ul>
              <li><a href="/benchmark">${t.benchmark}</a></li>
              <li><a href="/vision">${t.vision}</a></li>
              <li><a href="/data-standard">${t.dataStandard}</a></li>
              <li><a href="/verification">${t.verification}</a></li>
            </ul>
          </div>
        </div>
        <div class="sc-footer-bottom">
          <div>© 2026 ${t.footerRights}</div>
          <div>PolyForm Noncommercial 1.0.0 · Source-Available · v1.9.0</div>
        </div>
      </footer>
    `;
  }

  function initSiteNav() {
    const lang = getLang();
    const theme = getTheme();
    document.documentElement.setAttribute("data-lang", lang);
    document.documentElement.setAttribute(
      "lang",
      lang === "zh" ? "zh-CN" : "en",
    );
    document.body.classList.add("sc-themed");

    // Ensure theme is applied on root
    applyTheme(theme);

    // 1. Mount or replace Header
    let mountHeader = document.getElementById("sc-header-mount");
    if (!mountHeader) {
      mountHeader = document.createElement("div");
      mountHeader.id = "sc-header-mount";
      document.body.insertBefore(mountHeader, document.body.firstChild);
    }
    mountHeader.innerHTML = renderNavbar(lang, theme);

    // 2. Mount or append Footer (if mount container present or page has #sc-footer-mount)
    const mountFooter = document.getElementById("sc-footer-mount");
    if (mountFooter) {
      mountFooter.innerHTML = renderFooter(lang);
    }

    // 3. Bind Hamburger Event
    const btnBurger = document.getElementById("sc-btn-hamburger");
    const backdrop = document.getElementById("sc-mobile-backdrop");

    function toggleDrawer(open) {
      if (open === undefined) {
        document.body.classList.toggle("sc-drawer-open");
      } else if (open) {
        document.body.classList.add("sc-drawer-open");
      } else {
        document.body.classList.remove("sc-drawer-open");
      }
    }

    if (btnBurger) {
      btnBurger.addEventListener("click", () => toggleDrawer());
    }
    if (backdrop) {
      backdrop.addEventListener("click", () => toggleDrawer(false));
    }
    if (!window._scEscapeBound) {
      window.addEventListener("keydown", (e) => {
        if (e.key === "Escape") toggleDrawer(false);
      });
      window._scEscapeBound = true;
    }

    // 4. Bind Theme Toggle Buttons (Header + Mobile Drawer)
    const btnTheme = document.getElementById("sc-btn-theme-toggle");
    const btnDrawerTheme = document.getElementById(
      "sc-drawer-btn-theme-toggle",
    );
    if (btnTheme) {
      btnTheme.addEventListener("click", toggleTheme);
    }
    if (btnDrawerTheme) {
      btnDrawerTheme.addEventListener("click", toggleTheme);
    }

    // 5. Bind Language Toggle Buttons (Header + Mobile Drawer)
    function onLangClick() {
      const currentLang =
        document.documentElement.getAttribute("data-lang") || lang;
      const nextLang = currentLang === "zh" ? "en" : "zh";
      localStorage.setItem("semicon_lang", nextLang);
      localStorage.setItem(
        "semiconfab_lang",
        nextLang === "zh" ? "zh-CN" : "en",
      );
      document.documentElement.setAttribute("data-lang", nextLang);
      document.documentElement.setAttribute(
        "lang",
        nextLang === "zh" ? "zh-CN" : "en",
      );

      const url = new URL(window.location.href);
      if (url.searchParams.has("lang")) {
        url.searchParams.set("lang", nextLang);
        window.history.replaceState({}, "", url.toString());
      }

      if (typeof window.onSemiconLanguageChange === "function") {
        try {
          window.onSemiconLanguageChange(nextLang);
        } catch (e) {
          console.warn("Language change callback error:", e);
        }
        initSiteNav();
      } else {
        setLang(nextLang);
      }
    }

    const btnLang = document.getElementById("sc-btn-lang-toggle");
    const btnDrawerLang = document.getElementById("sc-drawer-btn-lang-toggle");
    if (btnLang) {
      btnLang.addEventListener("click", onLangClick);
    }
    if (btnDrawerLang) {
      btnDrawerLang.addEventListener("click", onLangClick);
    }
  }

  // Auto-init on DOMContentLoaded or immediately if document is ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initSiteNav);
  } else {
    initSiteNav();
  }

  // Export helper to global scope
  window.SemiconSiteNav = {
    getLang: getLang,
    setLang: setLang,
    getTheme: getTheme,
    applyTheme: applyTheme,
    toggleTheme: toggleTheme,
    refresh: initSiteNav,
  };
})();
