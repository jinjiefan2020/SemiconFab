/**
 * SemiconFab.org - Unified Site Navigation & Responsive Mobile Controller
 * Offline Compatible · Zero External Network Dependencies · Pure Vanilla JS
 * Architecture: Global Dual-Theme (Light/Dark) Engine + Multilingual Controller
 */

(function () {
  "use strict";

  const NAV_I18N = {
    en: {
      brandSub: "300mm Fab Digital Twin",
      navTwin: "3D Twin",
      navProcesses: "Processes",
      navEquipment: "Equipment",
      navEconomics: "Economics",
      navStandards: "Standards",
      langBtn: "En/中文",
      themeLight: "Light",
      themeDark: "Dark",
      themeTitle: "Switch Light / Dark Theme",
      // Dropdown & Drawer items
      cleanroomTwin: "300mm Fab Cleanroom",
      cleanroomTwinDesc: "Class 1 Cleanroom & Subfab Twin",
      osatTwin: "OSAT Packaging & Test",
      osatTwinDesc: "Dual-Hall Back-End Packaging & ATE Test Twin",
      layoutEditor: "2D Layout Editor",
      layoutEditorDesc: "Architectural Cleanroom Bay Design",
      finfet: "FinFET (14nm/7nm)",
      finfetDesc: "Tri-Gate RMG Architecture",
      gaafet: "GAAFET (3nm/2nm)",
      gaafetDesc: "Nanosheet Transistor Flow",
      dram: "DRAM (1T1C)",
      dramDesc: "Buried Wordline & Capacitor",
      nand: "3D NAND Flash",
      nandDesc: "Charge Trap & Replacement Gate",
      hbm: "HBM3E / HBM4",
      hbmDesc: "3D TSV Stacking & Packaging",
      catalog: "Equipment Catalog",
      catalogDesc: "253 OEM Models (167 FAB · 86 OSAT)",
      compare: "Side-by-Side Comparison",
      compareDesc: "Cross-Tool Technical & Price Matrix",
      addEquip: "Add Equipment",
      addEquipDesc: "JSON Schema Generator",
      fabCapex: "Fab Capex Estimator",
      fabCapexDesc: "Total Cleanroom & Facility Capex",
      fabCost: "Facility Cost Report",
      fabCostDesc: "Parametric Infrastructure Breakdown",
      dataStandard: "Data Standard",
      dataStandardDesc: "Open JSON Schema v1.0",
      verification: "Verification Suite",
      verificationDesc: "Automated Data Integrity Tests",
      benchmark: "System Benchmarks",
      benchmarkDesc: "Hardware & WebGL Performance",
      vision: "Vision & Roadmap",
      visionDesc: "Open Science Initiative",
      // Footer
      footerTagline: "Open-access digital twin and equipment engineering repository for 300mm semiconductor fabs.",
      footerLicense: "Source-available under PolyForm Noncommercial 1.0.0. Free for education, academic research, and personal use.",
      footerQuickLinks: "Navigation",
      footerModels: "3D Models",
      footerLegal: "Project Info",
      footerRights: "SemiconFab.org Initiative · Community Maintained"
    },
    zh: {
      brandSub: "300mm晶圆厂数字孪生",
      navTwin: "3D孪生车间",
      navProcesses: "先进制程",
      navEquipment: "核心设备",
      navEconomics: "建厂与投资",
      navStandards: "规范验证",
      langBtn: "En/中文",
      themeLight: "亮色",
      themeDark: "暗色",
      themeTitle: "切换明暗主题 (亮色 / 暗色)",
      // Dropdown & Drawer items
      cleanroomTwin: "300mm洁净室数字孪生",
      cleanroomTwinDesc: "ISO 1级洁净室与次层动力系统",
      osatTwin: "封测厂数字孪生 (OSAT)",
      osatTwinDesc: "双大厅后道封装与高密度 ATE 终测厂房",
      layoutEditor: "2D厂房布局编辑器",
      layoutEditorDesc: "洁净室工艺区空间规划",
      finfet: "FinFET (14nm/7nm 晶体管)",
      finfetDesc: "三维鳍式场效应 RMG 工艺",
      gaafet: "GAAFET (3nm/2nm 纳米片)",
      gaafetDesc: "全环绕栅极纳米片全流程",
      dram: "DRAM 内存 (1T1C)",
      dramDesc: "埋入式字线与高深宽比电容",
      nand: "3D NAND 闪存",
      nandDesc: "电荷俘获与替代栅极堆叠",
      hbm: "HBM 高带宽内存",
      hbmDesc: "3D TSV 硅通孔微凸块先进封装",
      catalog: "半导体设备全名录 (253台)",
      catalogDesc: "前道晶圆制造 (167台) 与后道先进封测 (86台)",
      compare: "机台横向多维对比",
      compareDesc: "2~4台设备技术参数与成本矩阵",
      addEquip: "新增设备录入",
      addEquipDesc: "标准 JSON Schema 生成器",
      fabCapex: "晶圆厂全厂总造价测算器",
      fabCapexDesc: "数字孪生 BOM 与自顶向下总投资",
      fabCost: "厂务基建成本拆解报告",
      fabCostDesc: "超纯水、动力、特气与暖通经验模型",
      dataStandard: "数据交换标准",
      dataStandardDesc: "半导体设备 Schema v1.0",
      verification: "数据真实性校验集",
      verificationDesc: "自动化数据完整性审计",
      benchmark: "性能基准测试",
      benchmarkDesc: "硬件算力与 WebGL 渲染性能",
      vision: "倡议愿景与路线图",
      visionDesc: "半导体工程开放科学平台",
      // Footer
      footerTagline: "面向 300mm 晶圆制造的开放数字孪生、设备工程学与总造价建模平台。",
      footerLicense: "源码遵循 PolyForm Noncommercial 1.0.0 协议公开发布，教育、科研与个人使用完全免费。",
      footerQuickLinks: "核心导航",
      footerModels: "3D数字化模型",
      footerLegal: "项目信息",
      footerRights: "SemiconFab.org 倡议组织 · 社区协同维护"
    }
  };

  // 1. Language Handling
  function getLang() {
    const params = new URLSearchParams(window.location.search);
    const langParam = params.get("lang");
    if (langParam === "zh" || langParam === "zh-CN" || langParam === "zh-TW") return "zh";
    if (langParam === "en") return "en";
    const saved = localStorage.getItem("semicon_lang");
    if (saved === "zh" || saved === "en") return saved;
    return navigator.language && navigator.language.startsWith("zh") ? "zh" : "en";
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
      if (label) label.textContent = theme === "dark" ? t.themeDark : t.themeLight;
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
    const pathname = window.location.pathname;
    const filename = pathname.substring(pathname.lastIndexOf("/") + 1) || "index.html";
    return filename;
  }

  function renderNavbar(lang, theme) {
    const t = NAV_I18N[lang];
    const cur = getCurrentPath();

    const isTwinActive = ["twin.html", "twin-osat.html", "layout-editor.html"].includes(cur);
    const isProcessActive = ["finfet.html", "gaa.html", "dram.html", "nand.html", "hbm.html"].includes(cur);
    const isEquipActive = ["catalog-demo.html", "compare.html", "add-equipment.html"].includes(cur);
    const isEconActive = ["fab-capex.html", "fab-cost.html"].includes(cur);
    const isStdActive = ["data-standard.html", "verification.html", "benchmark.html", "vision.html"].includes(cur);

    return `
      <header class="sc-header" role="banner">
        <div class="sc-header-inner">
          <!-- Logo & Brand -->
          <a href="index.html" class="sc-brand">
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
              <span class="sc-brand-tag">v1.7</span>
            </div>
          </a>

          <!-- Desktop Navigation -->
          <nav class="sc-desktop-nav" aria-label="Main Navigation">
            <!-- 3D Twin Dropdown -->
            <div class="sc-nav-item">
              <button type="button" class="sc-nav-link ${isTwinActive ? 'active' : ''}">
                <span>${t.navTwin}</span>
                <svg class="sc-nav-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="sc-dropdown-panel">
                <a href="twin.html" class="sc-dropdown-item ${cur === 'twin.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title">${t.cleanroomTwin}</span>
                  <span class="sc-dropdown-desc">${t.cleanroomTwinDesc}</span>
                </a>
                <a href="twin-osat.html" class="sc-dropdown-item ${cur === 'twin-osat.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title" style="color:var(--sc-accent-cyan)">${t.osatTwin}</span>
                  <span class="sc-dropdown-desc">${t.osatTwinDesc}</span>
                </a>
                <a href="layout-editor.html" class="sc-dropdown-item ${cur === 'layout-editor.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title">${t.layoutEditor}</span>
                  <span class="sc-dropdown-desc">${t.layoutEditorDesc}</span>
                </a>
              </div>
            </div>

            <!-- Processes Dropdown -->
            <div class="sc-nav-item">
              <button type="button" class="sc-nav-link ${isProcessActive ? 'active' : ''}">
                <span>${t.navProcesses}</span>
                <svg class="sc-nav-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="sc-dropdown-panel">
                <a href="finfet.html" class="sc-dropdown-item ${cur === 'finfet.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title">${t.finfet}</span>
                  <span class="sc-dropdown-desc">${t.finfetDesc}</span>
                </a>
                <a href="gaa.html" class="sc-dropdown-item ${cur === 'gaa.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title">${t.gaafet}</span>
                  <span class="sc-dropdown-desc">${t.gaafetDesc}</span>
                </a>
                <a href="dram.html" class="sc-dropdown-item ${cur === 'dram.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title">${t.dram}</span>
                  <span class="sc-dropdown-desc">${t.dramDesc}</span>
                </a>
                <a href="nand.html" class="sc-dropdown-item ${cur === 'nand.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title">${t.nand}</span>
                  <span class="sc-dropdown-desc">${t.nandDesc}</span>
                </a>
                <a href="hbm.html" class="sc-dropdown-item ${cur === 'hbm.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title">${t.hbm}</span>
                  <span class="sc-dropdown-desc">${t.hbmDesc}</span>
                </a>
              </div>
            </div>

            <!-- Equipment Dropdown -->
            <div class="sc-nav-item">
              <button type="button" class="sc-nav-link ${isEquipActive ? 'active' : ''}">
                <span>${t.navEquipment}</span>
                <svg class="sc-nav-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="sc-dropdown-panel">
                <a href="catalog-demo.html" class="sc-dropdown-item ${cur === 'catalog-demo.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title">${t.catalog}</span>
                  <span class="sc-dropdown-desc">${t.catalogDesc}</span>
                </a>
                <a href="compare.html" class="sc-dropdown-item ${cur === 'compare.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title">${t.compare}</span>
                  <span class="sc-dropdown-desc">${t.compareDesc}</span>
                </a>
                <a href="add-equipment.html" class="sc-dropdown-item ${cur === 'add-equipment.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title">${t.addEquip}</span>
                  <span class="sc-dropdown-desc">${t.addEquipDesc}</span>
                </a>
              </div>
            </div>

            <!-- Economics Dropdown -->
            <div class="sc-nav-item">
              <button type="button" class="sc-nav-link ${isEconActive ? 'active' : ''}">
                <span>${t.navEconomics}</span>
                <svg class="sc-nav-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="sc-dropdown-panel">
                <a href="fab-capex.html" class="sc-dropdown-item ${cur === 'fab-capex.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title" style="color:var(--sc-accent-cyan)">${t.fabCapex}</span>
                  <span class="sc-dropdown-desc">${t.fabCapexDesc}</span>
                </a>
                <a href="fab-cost.html" class="sc-dropdown-item ${cur === 'fab-cost.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title">${t.fabCost}</span>
                  <span class="sc-dropdown-desc">${t.fabCostDesc}</span>
                </a>
              </div>
            </div>

            <!-- Standards Dropdown -->
            <div class="sc-nav-item">
              <button type="button" class="sc-nav-link ${isStdActive ? 'active' : ''}">
                <span>${t.navStandards}</span>
                <svg class="sc-nav-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="sc-dropdown-panel">
                <a href="data-standard.html" class="sc-dropdown-item ${cur === 'data-standard.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title">${t.dataStandard}</span>
                  <span class="sc-dropdown-desc">${t.dataStandardDesc}</span>
                </a>
                <a href="verification.html" class="sc-dropdown-item ${cur === 'verification.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title">${t.verification}</span>
                  <span class="sc-dropdown-desc">${t.verificationDesc}</span>
                </a>
                <a href="benchmark.html" class="sc-dropdown-item ${cur === 'benchmark.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title">${t.benchmark}</span>
                  <span class="sc-dropdown-desc">${t.benchmarkDesc}</span>
                </a>
                <a href="vision.html" class="sc-dropdown-item ${cur === 'vision.html' ? 'active' : ''}">
                  <span class="sc-dropdown-title">${t.vision}</span>
                  <span class="sc-dropdown-desc">${t.visionDesc}</span>
                </a>
              </div>
            </div>
          </nav>

          <!-- Right Action Controls -->
          <div class="sc-header-actions">
            <!-- Theme Switcher Button -->
            <button type="button" id="sc-btn-theme-toggle" class="sc-btn-theme-toggle" title="${t.themeTitle}">
              <span class="sc-theme-icon">${theme === 'dark' ? '🌙' : '☀️'}</span>
              <span class="sc-theme-label">${theme === 'dark' ? t.themeDark : t.themeLight}</span>
            </button>

            <!-- Language Switcher Button -->
            <button type="button" id="sc-btn-lang-toggle" class="sc-btn-lang" title="${lang === 'zh' ? 'Switch to English' : '切换为中文'}">
              <span>En/中文</span>
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
        <!-- 3D Twin & Layout -->
        <div class="sc-drawer-section">
          <div class="sc-drawer-heading">${t.navTwin}</div>
          <a href="twin.html" class="sc-drawer-link ${cur === 'twin.html' ? 'active' : ''}">
            <span>${t.cleanroomTwin}</span>
            <span class="sc-drawer-badge">Fab</span>
          </a>
          <a href="twin-osat.html" class="sc-drawer-link ${cur === 'twin-osat.html' ? 'active' : ''}">
            <span>${t.osatTwin}</span>
            <span class="sc-drawer-badge">OSAT</span>
          </a>
          <a href="layout-editor.html" class="sc-drawer-link ${cur === 'layout-editor.html' ? 'active' : ''}">
            <span>${t.layoutEditor}</span>
          </a>
        </div>

        <!-- Equipment -->
        <div class="sc-drawer-section">
          <div class="sc-drawer-heading">${t.navEquipment}</div>
          <a href="catalog-demo.html" class="sc-drawer-link ${cur === 'catalog-demo.html' ? 'active' : ''}">
            <span>${t.catalog}</span>
            <span class="sc-drawer-badge">167</span>
          </a>
          <a href="compare.html" class="sc-drawer-link ${cur === 'compare.html' ? 'active' : ''}">
            <span>${t.compare}</span>
          </a>
          <a href="add-equipment.html" class="sc-drawer-link ${cur === 'add-equipment.html' ? 'active' : ''}">
            <span>${t.addEquip}</span>
          </a>
        </div>

        <!-- Economics -->
        <div class="sc-drawer-section">
          <div class="sc-drawer-heading">${t.navEconomics}</div>
          <a href="fab-capex.html" class="sc-drawer-link ${cur === 'fab-capex.html' ? 'active' : ''}">
            <span style="color:var(--sc-accent-cyan)">${t.fabCapex}</span>
            <span class="sc-drawer-badge">BOM</span>
          </a>
          <a href="fab-cost.html" class="sc-drawer-link ${cur === 'fab-cost.html' ? 'active' : ''}">
            <span>${t.fabCost}</span>
          </a>
        </div>

        <!-- Advanced Process Architecture -->
        <div class="sc-drawer-section">
          <div class="sc-drawer-heading">${t.navProcesses}</div>
          <a href="finfet.html" class="sc-drawer-link ${cur === 'finfet.html' ? 'active' : ''}">
            <span>${t.finfet}</span>
          </a>
          <a href="gaa.html" class="sc-drawer-link ${cur === 'gaa.html' ? 'active' : ''}">
            <span>${t.gaafet}</span>
          </a>
          <a href="dram.html" class="sc-drawer-link ${cur === 'dram.html' ? 'active' : ''}">
            <span>${t.dram}</span>
          </a>
          <a href="nand.html" class="sc-drawer-link ${cur === 'nand.html' ? 'active' : ''}">
            <span>${t.nand}</span>
          </a>
          <a href="hbm.html" class="sc-drawer-link ${cur === 'hbm.html' ? 'active' : ''}">
            <span>${t.hbm}</span>
          </a>
        </div>

        <!-- Standards & Verification -->
        <div class="sc-drawer-section">
          <div class="sc-drawer-heading">${t.navStandards}</div>
          <a href="data-standard.html" class="sc-drawer-link ${cur === 'data-standard.html' ? 'active' : ''}">
            <span>${t.dataStandard}</span>
          </a>
          <a href="verification.html" class="sc-drawer-link ${cur === 'verification.html' ? 'active' : ''}">
            <span>${t.verification}</span>
          </a>
          <a href="benchmark.html" class="sc-drawer-link ${cur === 'benchmark.html' ? 'active' : ''}">
            <span>${t.benchmark}</span>
          </a>
          <a href="vision.html" class="sc-drawer-link ${cur === 'vision.html' ? 'active' : ''}">
            <span>${t.vision}</span>
          </a>
        </div>

        <!-- Mobile Drawer Action Controls -->
        <div class="sc-drawer-controls">
          <button type="button" id="sc-drawer-btn-theme-toggle" class="sc-btn-theme-toggle" style="flex: 1;" title="${t.themeTitle}">
            <span class="sc-theme-icon">${theme === 'dark' ? '🌙' : '☀️'}</span>
            <span class="sc-theme-label">${theme === 'dark' ? t.themeDark : t.themeLight}</span>
          </button>
          <button type="button" id="sc-drawer-btn-lang-toggle" class="sc-btn-lang" style="flex: 1;" title="${lang === 'zh' ? 'Switch to English' : '切换为中文'}">
            <span>En/中文</span>
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
              <li><a href="twin.html">${t.cleanroomTwin}</a></li>
              <li><a href="twin-osat.html">${t.osatTwin}</a></li>
              <li><a href="catalog-demo.html">${t.catalog}</a></li>
              <li><a href="compare.html">${t.compare}</a></li>
              <li><a href="fab-capex.html">${t.fabCapex}</a></li>
              <li><a href="fab-cost.html">${t.fabCost}</a></li>
            </ul>
          </div>
          <div class="sc-footer-col">
            <h5>${t.footerModels}</h5>
            <ul>
              <li><a href="finfet.html">${t.finfet}</a></li>
              <li><a href="gaa.html">${t.gaafet}</a></li>
              <li><a href="dram.html">${t.dram}</a></li>
              <li><a href="nand.html">${t.nand}</a></li>
              <li><a href="hbm.html">${t.hbm}</a></li>
            </ul>
          </div>
          <div class="sc-footer-col">
            <h5>${t.footerLegal}</h5>
            <ul>
              <li><a href="data-standard.html">${t.dataStandard}</a></li>
              <li><a href="verification.html">${t.verification}</a></li>
              <li><a href="benchmark.html">${t.benchmark}</a></li>
              <li><a href="vision.html">${t.vision}</a></li>
            </ul>
          </div>
        </div>
        <div class="sc-footer-bottom">
          <div>© 2026 ${t.footerRights}</div>
          <div>PolyForm Noncommercial 1.0.0 · Source-Available</div>
        </div>
      </footer>
    `;
  }

  function initSiteNav() {
    const lang = getLang();
    const theme = getTheme();
    document.documentElement.setAttribute("data-lang", lang);
    document.documentElement.setAttribute("lang", lang === "zh" ? "zh-CN" : "en");
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
    const btnDrawerTheme = document.getElementById("sc-drawer-btn-theme-toggle");
    if (btnTheme) {
      btnTheme.addEventListener("click", toggleTheme);
    }
    if (btnDrawerTheme) {
      btnDrawerTheme.addEventListener("click", toggleTheme);
    }

    // 5. Bind Language Toggle Buttons (Header + Mobile Drawer)
    function onLangClick() {
      const currentLang = document.documentElement.getAttribute("data-lang") || lang;
      const nextLang = currentLang === "zh" ? "en" : "zh";
      localStorage.setItem("semicon_lang", nextLang);
      localStorage.setItem("semiconfab_lang", nextLang === "zh" ? "zh-CN" : "en");
      document.documentElement.setAttribute("data-lang", nextLang);
      document.documentElement.setAttribute("lang", nextLang === "zh" ? "zh-CN" : "en");

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
    refresh: initSiteNav
  };
})();
