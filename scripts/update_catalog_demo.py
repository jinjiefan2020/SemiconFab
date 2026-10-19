#!/usr/bin/env python3
"""
scripts/update_catalog_demo.py
Upgrades catalog-demo.html to support:
1. Domain switcher: All (253) / Front-end FAB (167) / Back-end OSAT (86)
2. URL parameter parsing (?domain=osat / ?domain=fab / ?category=...)
3. Dynamic category chips matching active domain
4. Dynamic stats bar matching active domain
5. Embedded JSON fallback updated to full 253 records from catalog.json
6. Full bilingual support for OSAT categories and domain controls
"""

import json
import re
import sys

def main():
    with open("catalog.json", "r", encoding="utf-8") as f:
        catalog_all = json.load(f)

    with open("catalog-demo.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update embedded data
    embedded_tag = '<script id="embedded-catalog-data" type="application/json">'
    end_script_tag = '</script>'
    
    start_pos = html.find(embedded_tag)
    if start_pos == -1:
        print("Error: embedded-catalog-data not found")
        sys.exit(1)
        
    end_pos = html.find(end_script_tag, start_pos)
    if end_pos == -1:
        print("Error: end script tag for embedded-catalog-data not found")
        sys.exit(1)

    json_str = "\n" + json.dumps(catalog_all, ensure_ascii=False, indent=2) + "\n    "
    html = html[:start_pos + len(embedded_tag)] + json_str + html[end_pos:]

    # 2. Add Domain Switcher CSS styles
    css_addition = """
      /* Domain Switcher */
      .domain-selector-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 16px;
        margin-bottom: 20px;
      }

      .domain-tabs {
        display: inline-flex;
        background: var(--sc-bg-subpanel, #e9e7df);
        padding: 4px;
        border-radius: 10px;
        gap: 4px;
        border: 1px solid var(--sc-border, #d8d4c8);
      }

      .domain-tab {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 18px;
        border: none;
        border-radius: 7px;
        background: transparent;
        color: var(--sc-text-muted, #4c5560);
        font-family: inherit;
        font-size: 13px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
      }

      .domain-tab:hover {
        color: var(--sc-text-main, #1c2126);
        background: rgba(0, 0, 0, 0.04);
      }

      .domain-tab.active {
        background: var(--sc-bg-panel, #ffffff);
        color: var(--sc-accent-cyan, #0e6e6b);
        font-weight: 700;
        box-shadow: 0 1px 3px rgba(28, 33, 38, 0.08);
      }

      .domain-tab-badge {
        font-family: "IBM Plex Mono", monospace;
        font-size: 11px;
        padding: 2px 7px;
        border-radius: 999px;
        background: rgba(0, 0, 0, 0.06);
        color: inherit;
        font-weight: 600;
      }

      .domain-tab.active .domain-tab-badge {
        background: rgba(14, 110, 107, 0.12);
        color: var(--sc-accent-cyan, #0e6e6b);
      }
"""
    if "/* Domain Switcher */" not in html:
        html = html.replace(".catalog-sub-header {", css_addition + "\n      .catalog-sub-header {")

    # 3. Insert Domain Selector HTML right before <div class="stats-bar">
    domain_html = """      <!-- Domain Selector Bar (FAB vs OSAT) -->
      <div class="domain-selector-bar">
        <div class="domain-tabs" role="tablist">
          <button class="domain-tab active" data-domain="all" onclick="setDomain('all')" role="tab" id="tab-domain-all">
            <span id="ui-domain-all">全部设备 All</span>
            <span class="domain-tab-badge" id="count-domain-all">253</span>
          </button>
          <button class="domain-tab" data-domain="fab" onclick="setDomain('fab')" role="tab" id="tab-domain-fab">
            <span id="ui-domain-fab">前道晶圆制造 FAB</span>
            <span class="domain-tab-badge" id="count-domain-fab">167</span>
          </button>
          <button class="domain-tab" data-domain="osat" onclick="setDomain('osat')" role="tab" id="tab-domain-osat">
            <span id="ui-domain-osat">后道先进封测 OSAT</span>
            <span class="domain-tab-badge" id="count-domain-osat">86</span>
          </button>
        </div>
      </div>

"""
    if "<!-- Domain Selector Bar (FAB vs OSAT) -->" not in html:
        html = html.replace('<!-- Stats Bar -->', domain_html + '      <!-- Stats Bar -->')

    # 4. Extract and rewrite the JavaScript logic (the plain <script> without attributes)
    script_pos = html.find("<script>\\n")
    if script_pos == -1:
        script_pos = html.find("<script>")
    if script_pos == -1:
        print("Error: Plain <script> tag not found")
        sys.exit(1)

    end_script_pos = html.find("</script>", script_pos)
    if end_script_pos == -1:
        print("Error: End </script> tag not found")
        sys.exit(1)

    # Let's build the enhanced JS
    new_js = """
      // --- Bilingual UI Dictionaries ---
      const I18N = {
        en: {
          subtitle:
            "Open Semiconductor Equipment Catalog · 253 Records (167 FAB · 86 OSAT)",
          loadJson: "Load catalog.json",
          domainAll: "All Equipment",
          domainFab: "Front-end FAB",
          domainOsat: "Back-end OSAT",
          statTotal: "Total Listings:",
          statL1: "L1 Verified:",
          statDraft: "Draft / Incomplete:",
          legendTitle: "Provenance Tiers:",
          legVendor: "Vendor Confirmed",
          legIndependent: "Independent Verified",
          legCommunity: "Community Corroborated",
          legInferred: "Inferred",
          legSynthetic: "Synthetic",
          searchPlaceholder:
            "Search vendor or model... (e.g. ASML, Canon, DISCO, Besi, Advantest)",
          hideDrafts: "Hide incomplete records (Drafts)",
          allCategory: "All",
          badgeL1: "L1 Verified",
          badgeDraft: "Draft · Incomplete",
          completeness: "Completeness",
          requiredFields: "required fields",
          provenanceBreakdown: "Provenance breakdown:",
          draftBannerTitle: "Help complete this record",
          draftMissing: "Missing L1 required fields:",
          contributeBtn: "Contribute Specifications",
          viewDetails: "View Details",
          hideDetails: "Hide Details",
          emptyTitle: "No equipment found",
          emptyDesc: "Try adjusting your search query, domain, or category filters.",
          footerLicense:
            "Source-available · PolyForm Noncommercial 1.0.0 · Free for education and personal use · Commercial licensing funds ongoing development.",
          disclaimer:
            "Prices are curated from public reports and engineering estimates for reference only, not official commercial quotes. Actual transaction prices vary widely by configuration, region, and procurement negotiations.",
          compareCheckbox: "Compare",
          compareCount: "Selected",
          compareHint: "Select 2–4 tools to compare side-by-side",
          compareNow: "Compare Now",
          compareClear: "Clear All",
          compareLimit: "Maximum 4 tools can be compared at once",
          basisReported: "Reported",
          basisEstimate: "Estimate",
          basisObserved: "Observed",
          basisUnknown: "Unknown",
          condNew: "New",
          condUsed: "Used",
          condRefurbished: "Refurbished",
          fields: {
            category: "Category",
            waferSizes: "Wafer Sizes",
            node: "Target Node",
            dimensions: "Footprint (WxDxH)",
            weight: "Weight",
            specs: "Process Specs",
            notes: "Source Notes",
            notAvailable: "— / Pending contribution",
          },
          categories: {
            lithography: "Lithography",
            resist_track: "Resist Track",
            dry_etch: "Dry Etch",
            wet_clean: "Wet Clean",
            thin_film_deposition: "Thin Film Deposition",
            cmp: "CMP",
            thermal_processing: "Thermal Processing",
            ion_implantation: "Ion Implantation",
            metrology: "Metrology",
            inspection: "Inspection",
            test: "Test & Prober",
            packaging: "Packaging",
            other: "Facility & Other",
            osat_dicing: "1. Wafer Dicing",
            osat_die_attach: "2. Die Attach",
            osat_wire_bonding: "3. Wire Bonding",
            osat_flip_chip: "4. Flip Chip",
            osat_molding: "5. Molding",
            osat_singulation: "6. Singulation",
            osat_bumping_rdl: "7. Bumping & RDL",
            osat_prober: "8. Wafer Prober",
            osat_ate: "9. ATE Tester",
            osat_test_handler: "10. Test Handler",
            osat_inspection: "11. AOI Inspection",
          },
        },
        zh: {
          subtitle: "半导体设备开放名录 · 253 条收录机台 (167台晶圆前道 · 86台封测后道)",
          loadJson: "加载外部 catalog.json",
          domainAll: "全部设备 (FAB + OSAT)",
          domainFab: "前道晶圆制造 (FAB)",
          domainOsat: "后道先进封测 (OSAT)",
          statTotal: "收录机台总数:",
          statL1: "L1 完整认证:",
          statDraft: "待补充草稿:",
          legendTitle: "数据来源置信度等级:",
          legVendor: "原厂确认",
          legIndependent: "独立实测",
          legCommunity: "社区互证",
          legInferred: "工程推断",
          legSynthetic: "模型合成",
          searchPlaceholder: "搜索厂商或机型... (例: ASML, Canon, DISCO, Besi, Advantest)",
          hideDrafts: "隐藏未完善机台 (Drafts)",
          allCategory: "全部类别",
          badgeL1: "L1 完整验证",
          badgeDraft: "数据待补充",
          completeness: "核心完整度",
          requiredFields: "核心字段",
          provenanceBreakdown: "数据溯源分布:",
          draftBannerTitle: "数据待补充 · Help complete this record",
          draftMissing: "缺失 L1 必需字段:",
          contributeBtn: "贡献规格数据 · Submit specs",
          viewDetails: "展开机台详情",
          hideDetails: "收起详情",
          emptyTitle: "未找到匹配的设备记录",
          emptyDesc: "请尝试清除搜索关键词或切换不同的领域与分类筛选。",
          footerLicense:
            "源码公开 · PolyForm Noncommercial 1.0.0 · 教育与个人使用免费 · 商业授权支持持续开发。",
          disclaimer:
            "价格为公开信息整理与估算区间，不构成报价；实际成交价因配置、地区、谈判而异。",
          compareCheckbox: "对比",
          compareCount: "已选",
          compareHint: "请选择 2–4 台设备进行横向对比",
          compareNow: "立即对比",
          compareClear: "清空选择",
          compareLimit: "最多同时对比 4 台设备",
          basisReported: "公开报道",
          basisEstimate: "估算区间",
          basisObserved: "公开挂牌",
          basisUnknown: "未知",
          condNew: "全新",
          condUsed: "二手",
          condRefurbished: "翻新",
          fields: {
            category: "设备类别",
            waferSizes: "适用晶圆尺寸",
            node: "目标工艺制程",
            dimensions: "外形尺寸 (宽x深x高)",
            weight: "机台重量",
            specs: "关键工艺规格",
            notes: "来源备注",
            notAvailable: "— / 待补充贡献",
          },
          categories: {
            lithography: "光刻机 (Lithography)",
            resist_track: "涂胶显影机 (Track)",
            dry_etch: "等离子刻蚀 (Dry Etch)",
            wet_clean: "湿法清洗 (Wet Clean)",
            thin_film_deposition: "薄膜沉积 (PVD/CVD)",
            cmp: "化学机械抛光 (CMP)",
            thermal_processing: "热处理与退火",
            ion_implantation: "离子注入",
            metrology: "量测设备 (Metrology)",
            inspection: "缺陷检测 (Inspection)",
            test: "测试机与探针台",
            packaging: "先进封装 (Packaging)",
            other: "厂务与其它 (Other)",
            osat_dicing: "1. 晶圆划片 (Dicing)",
            osat_die_attach: "2. 芯片贴装 (Die Attach)",
            osat_wire_bonding: "3. 引线键合 (Wire Bond)",
            osat_flip_chip: "4. 倒装焊接 (Flip Chip)",
            osat_molding: "5. 模塑封装 (Molding)",
            osat_singulation: "6. 冲切分离 (Singulation)",
            osat_bumping_rdl: "7. 凸块与RDL (Bumping/RDL)",
            osat_prober: "8. 晶圆探针台 (Prober)",
            osat_ate: "9. ATE 测试机 (ATE)",
            osat_test_handler: "10. 终测分选机 (Handler)",
            osat_inspection: "11. 出厂检测 (AOI)",
          },
        },
      };

      const FAB_CATEGORY_KEYS = [
        "lithography",
        "resist_track",
        "dry_etch",
        "wet_clean",
        "thin_film_deposition",
        "cmp",
        "thermal_processing",
        "ion_implantation",
        "metrology",
        "inspection",
        "test",
        "packaging",
        "other",
      ];

      const OSAT_CATEGORY_KEYS = [
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
        "osat_inspection",
      ];

      let currentLang = "en"; // Default to EN, toggleable
      let catalogData = [];
      let priceEstimatesData = {};
      let selectedCompareIds = [];
      let currentDomain = "all"; // 'all' | 'fab' | 'osat'
      let activeCategory = "all";
      let searchQuery = "";
      let hideDrafts = false;

      function isItemInDomain(item, domain) {
        if (!item) return false;
        if (domain === "all") return true;
        const isOsat = item.category && item.category.startsWith("osat_");
        if (domain === "osat") return isOsat;
        if (domain === "fab") return !isOsat;
        return true;
      }

      function formatPriceUSD(amount) {
        if (!amount) return "$0";
        if (amount >= 1000000) {
          const m = amount / 1000000;
          return "$" + (m % 1 === 0 ? m.toFixed(0) : m.toFixed(1)) + "M";
        }
        if (amount >= 1000) {
          return "$" + (amount / 1000).toFixed(0) + "k";
        }
        return "$" + amount.toLocaleString();
      }

      // Load initial data
      function initData() {
        if (window.semiconGetLang) {
          currentLang = window.semiconGetLang();
        }

        // Parse URL params for lang, domain and category
        const urlParams = new URLSearchParams(window.location.search);
        const langParam = urlParams.get("lang");
        if (langParam && (langParam === "zh" || langParam === "en")) {
          currentLang = langParam;
        }
        const domainParam = urlParams.get("domain");
        if (domainParam && ["all", "fab", "osat"].includes(domainParam.toLowerCase())) {
          currentDomain = domainParam.toLowerCase();
        }
        const catParam = urlParams.get("category");
        if (catParam) {
          activeCategory = catParam;
        }

        try {
          const embeddedEl = document.getElementById("embedded-catalog-data");
          if (embeddedEl && embeddedEl.textContent.trim()) {
            catalogData = JSON.parse(embeddedEl.textContent.trim());
          }
        } catch (err) {
          console.error("Failed to parse embedded data:", err);
        }

        if (window.PRICE_ESTIMATES_FALLBACK) {
          priceEstimatesData = window.PRICE_ESTIMATES_FALLBACK;
        }

        // Attempt fetch in case running on local webserver
        fetch("catalog.json")
          .then((res) => res.json())
          .then((data) => {
            if (Array.isArray(data) && data.length > 0) {
              catalogData = data;
              renderAll();
            }
          })
          .catch(() => {});

        fetch("data/price_estimates.json")
          .then((res) => res.json())
          .then((data) => {
            if (data && typeof data === "object") {
              priceEstimatesData = data;
              renderGrid();
            }
          })
          .catch(() => {});

        renderAll();
      }

      function switchLanguage() {
        currentLang = currentLang === "zh" ? "en" : "zh";
        const langBtn = document.getElementById("lang-btn");
        if (langBtn) {
          langBtn.textContent = "EN/中文";
          langBtn.title = currentLang === "zh" ? "Switch to English" : "切换到中文";
        }
        applyI18nChrome();
        updateDomainTabsUI();
        renderCategoryChips();
        renderGrid();
        updateCompareDrawer();
      }

      window.onSemiconLanguageChange = function (newLang) {
        currentLang = newLang;
        applyI18nChrome();
        updateDomainTabsUI();
        renderCategoryChips();
        renderGrid();
        updateCompareDrawer();
      };

      function setDomain(domain) {
        if (currentDomain === domain) return;
        currentDomain = domain;
        activeCategory = "all";

        // Update URL
        const url = new URL(window.location);
        if (domain === "all") {
          url.searchParams.delete("domain");
        } else {
          url.searchParams.set("domain", domain);
        }
        url.searchParams.delete("category");
        window.history.replaceState({}, "", url);

        updateDomainTabsUI();
        renderStats();
        renderCategoryChips();
        renderGrid();
      }

      function updateDomainTabsUI() {
        const t = I18N[currentLang];
        
        const tabAll = document.getElementById("tab-domain-all");
        const tabFab = document.getElementById("tab-domain-fab");
        const tabOsat = document.getElementById("tab-domain-osat");

        if (tabAll) tabAll.classList.toggle("active", currentDomain === "all");
        if (tabFab) tabFab.classList.toggle("active", currentDomain === "fab");
        if (tabOsat) tabOsat.classList.toggle("active", currentDomain === "osat");

        const elAll = document.getElementById("ui-domain-all");
        const elFab = document.getElementById("ui-domain-fab");
        const elOsat = document.getElementById("ui-domain-osat");
        if (elAll) elAll.textContent = t.domainAll;
        if (elFab) elFab.textContent = t.domainFab;
        if (elOsat) elOsat.textContent = t.domainOsat;

        // Count badges
        const countAll = catalogData.length;
        const countFab = catalogData.filter((x) => !x.category || !x.category.startsWith("osat_")).length;
        const countOsat = catalogData.filter((x) => x.category && x.category.startsWith("osat_")).length;

        const badgeAll = document.getElementById("count-domain-all");
        const badgeFab = document.getElementById("count-domain-fab");
        const badgeOsat = document.getElementById("count-domain-osat");
        if (badgeAll) badgeAll.textContent = countAll;
        if (badgeFab) badgeFab.textContent = countFab;
        if (badgeOsat) badgeOsat.textContent = countOsat;
      }

      function applyI18nChrome() {
        const t = I18N[currentLang];
        const titleEl = document.getElementById("ui-catalog-title");
        if (titleEl) {
          titleEl.textContent = currentLang === "zh" ? "半导体设备全名录" : "Equipment Catalog";
        }
        document.getElementById("ui-subtitle").textContent = t.subtitle;
        document.getElementById("ui-load-json").textContent = t.loadJson;
        document.getElementById("ui-stat-total-label").textContent =
          t.statTotal;
        document.getElementById("ui-stat-l1-label").textContent = t.statL1;
        document.getElementById("ui-stat-draft-label").textContent =
          t.statDraft;
        document.getElementById("ui-legend-title").textContent = t.legendTitle;
        document.getElementById("ui-leg-vendor").textContent = t.legVendor;
        document.getElementById("ui-leg-independent").textContent =
          t.legIndependent;
        document.getElementById("ui-leg-community").textContent =
          t.legCommunity;
        document.getElementById("ui-leg-inferred").textContent = t.legInferred;
        document.getElementById("ui-leg-synthetic").textContent =
          t.legSynthetic;
        document.getElementById("search-box").placeholder = t.searchPlaceholder;
        document.getElementById("ui-hide-drafts").textContent = t.hideDrafts;
        const footerLic = document.getElementById("ui-footer-license");
        if (footerLic) footerLic.textContent = t.footerLicense;
        const discEl = document.getElementById("ui-disclaimer-note");
        if (discEl) discEl.textContent = t.disclaimer;
      }

      function toggleCompareTool(recId, isChecked) {
        const t = I18N[currentLang];
        if (isChecked) {
          if (selectedCompareIds.length >= 4) {
            alert(t.compareLimit);
            renderGrid();
            return;
          }
          if (!selectedCompareIds.includes(recId)) {
            selectedCompareIds.push(recId);
          }
        } else {
          selectedCompareIds = selectedCompareIds.filter((id) => id !== recId);
        }
        updateCompareDrawer();
        renderGrid();
      }

      function removeCompareTool(recId) {
        selectedCompareIds = selectedCompareIds.filter((id) => id !== recId);
        updateCompareDrawer();
        renderGrid();
      }

      function clearAllCompare() {
        selectedCompareIds = [];
        updateCompareDrawer();
        renderGrid();
      }

      function goToComparison() {
        if (selectedCompareIds.length >= 2) {
          window.location.href = `compare.html?compare=${selectedCompareIds.join(",")}`;
        }
      }

      function updateCompareDrawer() {
        const drawer = document.getElementById("compare-drawer");
        const countEl = document.getElementById("ui-compare-count");
        const hintEl = document.getElementById("ui-compare-hint");
        const pillsEl = document.getElementById("compare-pills");
        const btnClear = document.getElementById("ui-btn-clear-compare");
        const btnNow = document.getElementById("btn-compare-now");
        const btnNowText = document.getElementById("ui-btn-compare-now");
        const t = I18N[currentLang];

        if (!drawer) return;

        const count = selectedCompareIds.length;
        if (count === 0) {
          drawer.classList.remove("show");
          return;
        }

        drawer.classList.add("show");
        countEl.textContent = `${t.compareCount} (${count}/4)`;
        btnClear.textContent = t.compareClear;
        btnNowText.textContent = `${t.compareNow} (${count})`;

        if (count >= 2) {
          btnNow.disabled = false;
          hintEl.textContent = t.compareHint;
        } else {
          btnNow.disabled = true;
          hintEl.textContent =
            currentLang === "zh"
              ? "请再选择至少 1 台设备以开启对比 (2–4 台)"
              : "Select at least 1 more tool to compare (2–4 tools)";
        }

        // Render pills
        let pillsHtml = "";
        selectedCompareIds.forEach((id) => {
          const item = catalogData.find((x) => x.record_id === id);
          if (item) {
            pillsHtml += `
            <span class="compare-pill-item">
              <span>${escapeHtml(item.vendor)} ${escapeHtml(item.model)}</span>
              <button onclick="removeCompareTool('${id}')" title="Remove">✕</button>
            </span>
          `;
          }
        });
        pillsEl.innerHTML = pillsHtml;
      }

      function renderCategoryChips() {
        const chipsBar = document.getElementById("category-chips-bar");
        const t = I18N[currentLang];

        const domainItems = catalogData.filter((item) => isItemInDomain(item, currentDomain));
        const catCounts = {};
        let totalCount = domainItems.length;
        domainItems.forEach((item) => {
          const c = item.category || "other";
          catCounts[c] = (catCounts[c] || 0) + 1;
        });

        let categoryKeys = [];
        if (currentDomain === "fab") {
          categoryKeys = FAB_CATEGORY_KEYS;
        } else if (currentDomain === "osat") {
          categoryKeys = OSAT_CATEGORY_KEYS;
        } else {
          categoryKeys = FAB_CATEGORY_KEYS.concat(OSAT_CATEGORY_KEYS);
        }

        let html = `
        <button class="chip ${activeCategory === "all" ? "active" : ""}" onclick="setCategory('all')">
          <span>${t.allCategory}</span>
          <span class="chip-count">${totalCount}</span>
        </button>
      `;

        categoryKeys.forEach((key) => {
          const count = catCounts[key] || 0;
          if (count > 0 || currentDomain !== "all") {
            const name = t.categories[key] || key;
            html += `
            <button class="chip ${activeCategory === key ? "active" : ""}" onclick="setCategory('${key}')">
              <span>${name}</span>
              <span class="chip-count">${count}</span>
            </button>
          `;
          }
        });

        chipsBar.innerHTML = html;
      }

      function setCategory(cat) {
        activeCategory = cat;
        const url = new URL(window.location);
        if (cat === "all") {
          url.searchParams.delete("category");
        } else {
          url.searchParams.set("category", cat);
        }
        window.history.replaceState({}, "", url);
        renderCategoryChips();
        renderGrid();
      }

      function renderStats() {
        const domainItems = catalogData.filter((item) => isItemInDomain(item, currentDomain));
        const total = domainItems.length;
        const l1 = domainItems.filter(
          (x) => x.conformance_level === "L1",
        ).length;
        const draft = domainItems.filter(
          (x) => x.conformance_level === "draft",
        ).length;
        document.getElementById("stat-total").textContent = total;
        document.getElementById("stat-l1").textContent = l1;
        document.getElementById("stat-draft").textContent = draft;
      }

      function renderTierDots(tierSummary) {
        let dotsHtml = "";
        const order = [
          ["vendor_confirmed", "vendor"],
          ["independent_verified", "independent"],
          ["community_corroborated", "community"],
          ["inferred", "inferred"],
          ["synthetic", "synthetic"],
        ];

        order.forEach(([tierKey, dotClass]) => {
          const count = tierSummary[tierKey] || 0;
          for (let i = 0; i < count; i++) {
            dotsHtml += `<span class="dot ${dotClass}" title="${tierKey}"></span>`;
          }
        });
        return dotsHtml;
      }

      function renderGrid() {
        const grid = document.getElementById("equipment-grid");
        const t = I18N[currentLang];

        const filtered = catalogData.filter((item) => {
          if (!isItemInDomain(item, currentDomain)) {
            return false;
          }
          if (activeCategory !== "all" && item.category !== activeCategory) {
            return false;
          }
          if (hideDrafts && item.conformance_level === "draft") {
            return false;
          }
          if (searchQuery) {
            const q = searchQuery.toLowerCase();
            const v = (item.vendor || "").toLowerCase();
            const m = (item.model || "").toLowerCase();
            if (!v.includes(q) && !m.includes(q)) {
              return false;
            }
          }
          return true;
        });

        if (filtered.length === 0) {
          grid.innerHTML = `
          <div class="empty-state">
            <h3>${t.emptyTitle}</h3>
            <p>${t.emptyDesc}</p>
          </div>
        `;
          return;
        }

        let html = "";
        filtered.forEach((item) => {
          const isL1 = item.conformance_level === "L1";
          const badgeClass = isL1 ? "badge-l1" : "badge-draft";
          const badgeText = isL1 ? t.badgeL1 : t.badgeDraft;
          const fillClass = isL1 ? "fill-l1" : "fill-draft";
          const categoryLabel = t.categories[item.category] || item.category;
          const isSelected = selectedCompareIds.includes(item.record_id);

          // Price estimate
          const est = priceEstimatesData[item.record_id];
          let priceBlockHtml = "";
          if (est && est.basis !== "unknown" && est.low_usd) {
            const lowStr = formatPriceUSD(est.low_usd);
            const highStr = formatPriceUSD(est.high_usd);
            const basisKey = est.basis || "category_estimate";
            let basisLabel = t.basisEstimate;
            if (basisKey === "reported") basisLabel = t.basisReported;
            else if (basisKey === "observed_listing")
              basisLabel = t.basisObserved;
            else if (basisKey === "unknown") basisLabel = t.basisUnknown;

            const condKey = est.condition || "new";
            let condLabel = t.condNew;
            if (condKey === "used") condLabel = t.condUsed;
            else if (condKey === "refurbished") condLabel = t.condRefurbished;

            priceBlockHtml = `
              <div class="card-price-row">
                <div class="card-price-val">${lowStr} – ${highStr} USD</div>
                <div class="card-price-tags">
                  <span class="card-price-tag ${condKey}">${condLabel}</span>
                  <span class="card-price-tag basis" title="${est.note || ""}">${basisLabel}</span>
                </div>
              </div>
            `;
          }

          // Provenance dots
          const dots = renderTierDots(item.provenance_summary || {});

          // Formatted specs
          const specs = item.process_specs || {};
          let specsHtml = "";
          const specKeys = Object.keys(specs);
          if (specKeys.length > 0) {
            specsHtml =
              '<ul class="specs-list" style="margin: 0; padding-left: 18px; font-size: 0.8125rem;">' +
              specKeys
                .slice(0, 6)
                .map(
                  (k) =>
                    `<li><strong>${escapeHtml(k)}:</strong> ${escapeHtml(String(specs[k]))}</li>`,
                )
                .join("") +
              "</ul>";
          } else {
            specsHtml = `<span style="color: var(--text-dim); font-size: 0.8125rem;">${t.fields.notAvailable}</span>`;
          }

          // Dimensions
          let dims = t.fields.notAvailable;
          if (
            item.footprint &&
            item.footprint.width_m &&
            item.footprint.depth_m
          ) {
            dims = `${item.footprint.width_m}m × ${item.footprint.depth_m}m`;
            if (item.footprint.height_m) dims += ` × ${item.footprint.height_m}m`;
          }

          // Weight
          let wt = t.fields.notAvailable;
          if (item.footprint && item.footprint.weight_kg) {
            wt = `${item.footprint.weight_kg.toLocaleString()} kg`;
          }

          // Wafer sizes
          let wSizes = t.fields.notAvailable;
          if (item.wafer_sizes_mm && item.wafer_sizes_mm.length > 0) {
            wSizes = item.wafer_sizes_mm.map((s) => s + "mm").join(", ");
          }

          // Node
          let node = t.fields.notAvailable;
          if (item.target_process_node) {
            node = item.target_process_node;
          }

          // Missing fields banner for Draft
          let draftBannerHtml = "";
          if (!isL1 && item.validation_errors && item.validation_errors.length > 0) {
            const missingList = item.validation_errors
              .map((e) => `<code>${escapeHtml(e.field)}</code>`)
              .join(", ");
            draftBannerHtml = `
            <div class="draft-missing-banner">
              <strong>${t.draftBannerTitle}</strong>
              <div>${t.draftMissing} ${missingList}</div>
              <a href="https://github.com/jinjiefan2020/SemiconFab/issues/new?title=Contribute+Specs:+${encodeURIComponent(item.vendor)}+${encodeURIComponent(item.model)}" target="_blank" rel="noopener noreferrer" class="contribute-btn">
                <span>+</span> ${t.contributeBtn}
              </a>
            </div>
          `;
          }

          html += `
          <article class="card">
            <header class="card-header">
              <div class="card-header-top">
                <div class="card-vendor-model">
                  <span class="card-vendor">${escapeHtml(item.vendor)}</span>
                  <div class="card-model-row">
                    <span class="card-model">${escapeHtml(item.model)}</span>
                    <label class="card-compare-label">
                      <input type="checkbox" onchange="toggleCompareTool('${item.record_id}', this.checked)" ${isSelected ? "checked" : ""} />
                      <span>${t.compareCheckbox}</span>
                    </label>
                  </div>
                </div>
                <div class="card-badge-wrap">
                  <span class="badge ${badgeClass}">${badgeText}</span>
                </div>
              </div>
              <div class="card-category">${escapeHtml(categoryLabel)}</div>
            </header>

            ${priceBlockHtml}

            <div class="card-completeness">
              <div class="completeness-bar">
                <div class="completeness-fill ${fillClass}" style="width: ${item.completeness_pct || 0}%;"></div>
              </div>
              <div class="completeness-label">
                <span>${t.completeness}: ${item.completeness_pct || 0}%</span>
                <span>${item.required_fields_present || 0}/${item.required_fields_total || 6} ${t.requiredFields}</span>
              </div>
            </div>

            <div class="card-provenance">
              <span class="provenance-label">${t.provenanceBreakdown}</span>
              <div class="provenance-dots">${dots}</div>
            </div>

            ${draftBannerHtml}

            <div class="card-details" id="details-${item.record_id}">
              <div class="detail-row">
                <span class="detail-label">${t.fields.waferSizes}</span>
                <span class="detail-val">${wSizes}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">${t.fields.node}</span>
                <span class="detail-val">${node}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">${t.fields.dimensions}</span>
                <span class="detail-val">${dims}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">${t.fields.weight}</span>
                <span class="detail-val">${wt}</span>
              </div>
              <div class="detail-row" style="flex-direction: column; align-items: flex-start; gap: 4px;">
                <span class="detail-label">${t.fields.specs}</span>
                <div class="detail-val" style="width: 100%; text-align: left;">${specsHtml}</div>
              </div>
              ${
                item.notes
                  ? `
              <div class="detail-row" style="flex-direction: column; align-items: flex-start; gap: 4px;">
                <span class="detail-label">${t.fields.notes}</span>
                <span class="detail-val" style="font-size: 0.8125rem; font-style: italic; color: var(--text-dim); text-align: left;">${escapeHtml(item.notes)}</span>
              </div>
              `
                  : ""
              }
            </div>

            <button class="expand-btn" onclick="toggleDetails('${item.record_id}', this)">
              <span class="btn-text">${t.viewDetails}</span>
              <span class="arrow">▼</span>
            </button>
          </article>
        `;
        });

        grid.innerHTML = html;
      }

      function toggleDetails(recId, btn) {
        const detailsEl = document.getElementById(`details-${recId}`);
        const t = I18N[currentLang];
        const textEl = btn.querySelector(".btn-text");
        const arrowEl = btn.querySelector(".arrow");

        if (detailsEl.classList.contains("expanded")) {
          detailsEl.classList.remove("expanded");
          textEl.textContent = t.viewDetails;
          arrowEl.textContent = "▼";
        } else {
          detailsEl.classList.add("expanded");
          textEl.textContent = t.hideDetails;
          arrowEl.textContent = "▲";
        }
      }

      function escapeHtml(str) {
        if (!str) return "";
        return String(str)
          .replace(/&/g, "&amp;")
          .replace(/</g, "&lt;")
          .replace(/>/g, "&gt;")
          .replace(/"/g, "&quot;")
          .replace(/'/g, "&#39;");
      }

      function renderAll() {
        applyI18nChrome();
        updateDomainTabsUI();
        renderStats();
        renderCategoryChips();
        renderGrid();
        updateCompareDrawer();
      }

      // Event listeners
      document.getElementById("search-box").addEventListener("input", (e) => {
        searchQuery = e.target.value.trim();
        renderGrid();
      });

      document
        .getElementById("toggle-hide-drafts")
        .addEventListener("change", (e) => {
          hideDrafts = e.target.checked;
          renderGrid();
        });

      // File picker for custom JSON
      document
        .getElementById("file-picker")
        .addEventListener("change", (e) => {
          const file = e.target.files[0];
          if (!file) return;
          const reader = new FileReader();
          reader.onload = (event) => {
            try {
              const parsed = JSON.parse(event.target.result);
              if (Array.isArray(parsed)) {
                catalogData = parsed;
                renderAll();
              }
            } catch (err) {
              console.warn("Invalid JSON file:", err.message);
            }
          };
          reader.readAsText(file);
        });

      // Initialize
      window.addEventListener("DOMContentLoaded", initData);
"""

    html = html[:script_pos + len("<script>")] + "\n" + new_js + "\n    " + html[end_script_pos:]

    with open("catalog-demo.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Successfully updated catalog-demo.html!")
    print(f"Total tools embedded: {len(catalog_all)}")

if __name__ == "__main__":
    main()
