#!/usr/bin/env python3
"""
update_catalog_demo.py
Safely upgrades catalog-demo.html with Workstream B comparison controls,
price estimate badges, and disclaimer.
"""

import re
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "catalog-demo.html")

with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add CSS before </style>
css_block = '''
      /* Equipment Comparison UI (1.6.0) */
      .card.selected-for-compare {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.4), 0 8px 24px rgba(0, 0, 0, 0.3) !important;
      }

      .compare-card-toggle {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #1e293b;
        border: 1px solid #334155;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 0.75rem;
        color: #94a3b8;
        cursor: pointer;
        user-select: none;
        transition: all 0.2s;
      }
      .compare-card-toggle:hover {
        background: #334155;
        color: #fff;
      }
      .compare-card-toggle input[type="checkbox"] {
        cursor: pointer;
        accent-color: #3b82f6;
      }
      .compare-card-toggle.checked {
        background: rgba(59, 130, 246, 0.15);
        border-color: rgba(59, 130, 246, 0.4);
        color: #60a5fa;
      }

      /* Card Price Block */
      .card-price-row {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(51, 65, 85, 0.6);
        border-radius: 8px;
        padding: 8px 12px;
        margin: 10px 0 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 6px;
      }

      .card-price-val {
        font-size: 0.9375rem;
        font-weight: 800;
        color: #38bdf8;
        letter-spacing: -0.01em;
      }

      .card-price-tags {
        display: flex;
        align-items: center;
        gap: 6px;
      }

      .basis-pill {
        font-size: 0.6875rem;
        font-weight: 700;
        padding: 2px 6px;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 0.03em;
        display: inline-flex;
        align-items: center;
        gap: 3px;
      }
      .basis-pill.basis-reported {
        background: rgba(168, 85, 247, 0.15);
        color: #c084fc;
        border: 1px solid rgba(168, 85, 247, 0.3);
      }
      .basis-pill.basis-category_estimate {
        background: rgba(59, 130, 246, 0.15);
        color: #60a5fa;
        border: 1px solid rgba(59, 130, 246, 0.3);
      }
      .basis-pill.basis-observed_listing {
        background: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.3);
      }
      .basis-pill.basis-unknown {
        background: rgba(100, 116, 139, 0.2);
        color: #94a3b8;
        border: 1px solid rgba(100, 116, 139, 0.3);
      }

      .cond-pill {
        font-size: 0.6875rem;
        font-weight: 600;
        padding: 1px 5px;
        border-radius: 3px;
        background: #1e293b;
        color: #94a3b8;
        border: 1px solid #334155;
      }

      /* Floating Bottom Compare Drawer */
      .compare-drawer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(15, 23, 42, 0.95);
        backdrop-filter: blur(12px);
        border-top: 1px solid rgba(59, 130, 246, 0.4);
        padding: 12px 24px;
        z-index: 100;
        box-shadow: 0 -8px 24px rgba(0, 0, 0, 0.5);
        transform: translateY(110%);
        transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      }
      .compare-drawer.show {
        transform: translateY(0);
      }

      .compare-drawer-content {
        max-width: 1400px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 16px;
      }

      .compare-drawer-info {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 12px;
      }

      .compare-drawer-count {
        font-weight: 700;
        font-size: 0.9375rem;
        color: #fff;
        background: rgba(59, 130, 246, 0.2);
        border: 1px solid rgba(59, 130, 246, 0.4);
        padding: 4px 10px;
        border-radius: 6px;
      }

      .compare-drawer-hint {
        font-size: 0.8125rem;
        color: #94a3b8;
      }

      .compare-pills {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
      }

      .compare-pill-item {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 4px;
        padding: 3px 8px;
        font-size: 0.75rem;
        color: #e2e8f0;
        display: inline-flex;
        align-items: center;
        gap: 6px;
      }
      .compare-pill-item button {
        background: none;
        border: none;
        color: #94a3b8;
        cursor: pointer;
        font-size: 0.875rem;
        line-height: 1;
      }
      .compare-pill-item button:hover {
        color: #f43f5e;
      }

      .compare-drawer-actions {
        display: flex;
        align-items: center;
        gap: 12px;
      }

      .btn-clear-compare {
        background: none;
        border: 1px solid #334155;
        color: #94a3b8;
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 0.8125rem;
        cursor: pointer;
        transition: all 0.2s;
      }
      .btn-clear-compare:hover {
        color: #fff;
        background: #1e293b;
      }

      .btn-compare-now {
        background: #2563eb;
        border: none;
        color: #fff;
        padding: 8px 18px;
        border-radius: 6px;
        font-size: 0.875rem;
        font-weight: 700;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        transition: all 0.2s;
        text-decoration: none;
      }
      .btn-compare-now:hover:not(:disabled) {
        background: #1d4ed8;
      }
      .btn-compare-now:disabled {
        opacity: 0.5;
        cursor: not-allowed;
      }

      .disclaimer-note {
        margin-top: 14px;
        font-size: 0.75rem;
        color: #64748b;
        line-height: 1.5;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
        padding: 10px 14px;
        background: rgba(15, 23, 42, 0.5);
        border: 1px solid rgba(51, 65, 85, 0.5);
        border-radius: 6px;
      }
'''

if "/* Equipment Comparison UI (1.6.0) */" not in content:
    content = content.replace("    </style>", css_block + "\n    </style>", 1)

# 2. Add disclaimer note in footer and add compare-drawer
disclaimer_html = '''        <p
          id="ui-disclaimer-note"
          class="disclaimer-note"
        >
          Prices are curated from public reports and engineering estimates for reference only, not official commercial quotes. Actual transaction prices vary widely by configuration, region, and procurement negotiations.
        </p>'''

drawer_html = '''      <!-- Floating Bottom Compare Drawer (1.6.0) -->
      <div id="compare-drawer" class="compare-drawer">
        <div class="compare-drawer-content">
          <div class="compare-drawer-info">
            <span class="compare-drawer-count" id="ui-compare-count">Selected (0/4)</span>
            <span class="compare-drawer-hint" id="ui-compare-hint">Select 2–4 tools to compare</span>
            <div class="compare-pills" id="compare-pills"></div>
          </div>
          <div class="compare-drawer-actions">
            <button class="btn-clear-compare" onclick="clearAllCompare()" id="ui-btn-clear-compare">Clear All</button>
            <button class="btn-compare-now" id="btn-compare-now" onclick="goToComparison()" disabled>
              <span id="ui-btn-compare-now">Compare Now (0)</span> &rarr;
            </button>
          </div>
        </div>
      </div>'''

if 'id="ui-disclaimer-note"' not in content:
    content = content.replace('      </footer>', disclaimer_html + '\n      </footer>\n' + drawer_html, 1)

# 3. Add script tag for price fallback before main script
fallback_script = '<script src="js/price-estimates-fallback.js"></script>\n    <script>'
if 'src="js/price-estimates-fallback.js"' not in content:
    content = content.replace('    <script>\n      // --- Bilingual UI Dictionaries ---', fallback_script + '\n      // --- Bilingual UI Dictionaries ---', 1)

# 4. Update JS logic
# Replace the script section with updated functions
old_script_start = '// --- Bilingual UI Dictionaries ---'
old_script_end = 'window.addEventListener("DOMContentLoaded", initData);'

new_script = '''// --- Bilingual UI Dictionaries ---
      const I18N = {
        en: {
          subtitle:
            "Open Semiconductor Equipment Catalog · 167 Migrated Records",
          loadJson: "Load catalog.json",
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
            "Search vendor or model... (e.g. ASML, Canon, Kiyo)",
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
          emptyDesc: "Try adjusting your search query or category filters.",
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
            test: "Test",
            packaging: "Packaging",
            other: "Other",
          },
        },
        zh: {
          subtitle: "半导体设备开放目录 · 167 条迁移数据",
          loadJson: "加载外部 catalog.json",
          statTotal: "收录机台总数:",
          statL1: "L1 完整认证:",
          statDraft: "待补充草稿:",
          legendTitle: "数据来源置信度等级:",
          legVendor: "原厂确认",
          legIndependent: "独立实测",
          legCommunity: "社区互证",
          legInferred: "工程推断",
          legSynthetic: "模型合成",
          searchPlaceholder: "搜索厂商或机型... (例: ASML, Canon, Kiyo)",
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
          emptyDesc: "请尝试清除搜索关键词或切换不同的类别筛选。",
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
          },
        },
      };

      let currentLang = "en"; // Default to EN, toggleable
      let catalogData = [];
      let priceEstimatesData = {};
      let selectedCompareIds = [];
      let activeCategory = "all";
      let searchQuery = "";
      let hideDrafts = false;

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
        document.getElementById("lang-btn").textContent = "EN/中文";
        document.getElementById("lang-btn").title =
          currentLang === "zh" ? "Switch to English" : "切换到中文";
        applyI18nChrome();
        renderCategoryChips();
        renderGrid();
        updateCompareDrawer();
      }

      function applyI18nChrome() {
        const t = I18N[currentLang];
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
          hintEl.textContent = currentLang === "zh" 
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

        const catCounts = {};
        let totalCount = catalogData.length;
        catalogData.forEach((item) => {
          const c = item.category || "other";
          catCounts[c] = (catCounts[c] || 0) + 1;
        });

        const categoryKeys = [
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

        let html = `
        <button class="chip ${activeCategory === "all" ? "active" : ""}" onclick="setCategory('all')">
          <span>${t.allCategory}</span>
          <span class="chip-count">${totalCount}</span>
        </button>
      `;

        categoryKeys.forEach((key) => {
          const count = catCounts[key] || 0;
          const name = t.categories[key] || key;
          html += `
          <button class="chip ${activeCategory === key ? "active" : ""}" onclick="setCategory('${key}')">
            <span>${name}</span>
            <span class="chip-count">${count}</span>
          </button>
        `;
        });

        chipsBar.innerHTML = html;
      }

      function setCategory(cat) {
        activeCategory = cat;
        renderCategoryChips();
        renderGrid();
      }

      function renderStats() {
        const total = catalogData.length;
        const l1 = catalogData.filter(
          (x) => x.conformance_level === "L1",
        ).length;
        const draft = catalogData.filter(
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
            else if (basisKey === "observed_listing") basisLabel = t.basisObserved;
            else if (basisKey === "unknown") basisLabel = t.basisUnknown;

            const condKey = est.condition || "new";
            let condLabel = t.condNew;
            if (condKey === "used") condLabel = t.condUsed;
            else if (condKey === "refurbished") condLabel = t.condRefurbished;

            priceBlockHtml = `
              <div class="card-price-row">
                <div class="card-price-val">${lowStr} – ${highStr} USD</div>
                <div class="card-price-tags">
                  <span class="basis-pill basis-${basisKey}">● ${basisLabel}</span>
                  <span class="cond-pill">${condLabel}</span>
                </div>
              </div>
            `;
          }

          // Missing fields text
          let missingFieldsText = "";
          if (!isL1 && item.missing_fields && item.missing_fields.length > 0) {
            missingFieldsText = item.missing_fields
              .map((f) => {
                if (f.includes("width_mm")) return "width_mm (宽)";
                if (f.includes("depth_mm")) return "depth_mm (深)";
                if (f.includes("height_mm")) return "height_mm (高)";
                if (f.includes("wafer_sizes"))
                  return "wafer_sizes_mm (晶圆尺寸)";
                return f;
              })
              .join(", ");
          }

          // Draft CTA Banner
          let draftBannerHtml = "";
          if (!isL1) {
            draftBannerHtml = `
            <div class="draft-banner">
              <div class="draft-banner-title">
                <span>⚠️</span>
                <span>${t.draftBannerTitle}</span>
              </div>
              <div class="draft-missing-text">
                ${t.draftMissing} <strong>${missingFieldsText}</strong>
              </div>
              <a class="btn-contribute" href="${item.prefill_url}" target="_blank">
                ${t.contributeBtn} &rarr;
              </a>
            </div>
          `;
          }

          // Details drawer content
          const rec = item.record || {};
          const ident = rec.identity || {};
          const phys = rec.physical || {};
          const proc = rec.process_capability || {};

          let waferSizesVal = t.fields.notAvailable;
          let waferSizesTier = "";
          if (ident.wafer_sizes_mm && ident.wafer_sizes_mm.value) {
            waferSizesVal = ident.wafer_sizes_mm.value.join(", ") + " mm";
            waferSizesTier = ident.wafer_sizes_mm.provenance
              ? ident.wafer_sizes_mm.provenance.tier
              : "";
          }

          let nodeVal = t.fields.notAvailable;
          let nodeTier = "";
          if (ident.node_applicability && ident.node_applicability.value) {
            nodeVal = ident.node_applicability.value;
            nodeTier = ident.node_applicability.provenance
              ? ident.node_applicability.provenance.tier
              : "";
          }

          let dimVal = t.fields.notAvailable;
          let dimTier = "";
          if (phys.width_mm && phys.depth_mm && phys.height_mm) {
            dimVal = `${phys.width_mm.value} × ${phys.depth_mm.value} × ${phys.height_mm.value} mm`;
            dimTier = phys.width_mm.provenance
              ? phys.width_mm.provenance.tier
              : "";
          }

          let weightVal = t.fields.notAvailable;
          let weightTier = "";
          if (phys.weight_kg && phys.weight_kg.value) {
            weightVal = `${phys.weight_kg.value} kg`;
            weightTier = phys.weight_kg.provenance
              ? phys.weight_kg.provenance.tier
              : "";
          }

          let specsVal = "";
          if (proc.capabilities && proc.capabilities.length > 0) {
            specsVal = proc.capabilities[0].detail
              ? proc.capabilities[0].detail.value
              : "";
          }

          let notesVal = rec.notes || "";

          html += `
          <div class="card ${isSelected ? "selected-for-compare" : ""}" id="card-${item.record_id}">
            <div class="card-header">
              <span class="card-category-tag">${categoryLabel}</span>
              <div style="display:flex; align-items:center; gap:8px;">
                <span class="badge ${badgeClass}">${badgeText}</span>
                <label class="compare-card-toggle ${isSelected ? "checked" : ""}" onclick="event.stopPropagation()">
                  <input type="checkbox" onchange="toggleCompareTool('${item.record_id}', this.checked)" ${isSelected ? "checked" : ""}>
                  <span>${t.compareCheckbox}</span>
                </label>
              </div>
            </div>

            <div class="equipment-title">
              <div class="vendor-name">${escapeHtml(item.vendor)}</div>
              <div class="model-name">${escapeHtml(item.model)}</div>
            </div>

            ${priceBlockHtml}

            <div class="completeness-section">
              <div class="completeness-header">
                <span>${t.completeness}: <strong>${item.completeness_pct}%</strong></span>
                <span>${Math.round((item.completeness_pct * 8) / 100)}/8 ${t.requiredFields}</span>
              </div>
              <div class="progress-bar-bg">
                <div class="progress-bar-fill ${fillClass}" style="width: ${item.completeness_pct}%;"></div>
              </div>
            </div>

            <div class="tier-dots-wrap">
              <span>${t.provenanceBreakdown}</span>
              <div class="dots-group">
                ${renderTierDots(item.tier_summary || {})}
              </div>
            </div>

            ${draftBannerHtml}

            <button class="details-toggle-btn" onclick="toggleDetails('${item.record_id}')">
              <span id="btn-text-${item.record_id}">▶ ${t.viewDetails}</span>
            </button>

            <div class="details-drawer" id="drawer-${item.record_id}">
              <div class="field-row">
                <span class="field-label">${t.fields.waferSizes}</span>
                <span class="field-val-wrap">
                  <span class="field-val ${waferSizesVal === t.fields.notAvailable ? "field-empty" : ""}">${escapeHtml(waferSizesVal)}</span>
                  ${waferSizesTier ? `<span class="tier-pill ${waferSizesTier}">${waferSizesTier}</span>` : ""}
                </span>
              </div>

              <div class="field-row">
                <span class="field-label">${t.fields.node}</span>
                <span class="field-val-wrap">
                  <span class="field-val ${nodeVal === t.fields.notAvailable ? "field-empty" : ""}">${escapeHtml(nodeVal)}</span>
                  ${nodeTier ? `<span class="tier-pill ${nodeTier}">${nodeTier}</span>` : ""}
                </span>
              </div>

              <div class="field-row">
                <span class="field-label">${t.fields.dimensions}</span>
                <span class="field-val-wrap">
                  <span class="field-val ${dimVal === t.fields.notAvailable ? "field-empty" : ""}">${escapeHtml(dimVal)}</span>
                  ${dimTier ? `<span class="tier-pill ${dimTier}">${dimTier}</span>` : ""}
                </span>
              </div>

              <div class="field-row">
                <span class="field-label">${t.fields.weight}</span>
                <span class="field-val-wrap">
                  <span class="field-val ${weightVal === t.fields.notAvailable ? "field-empty" : ""}">${escapeHtml(weightVal)}</span>
                  ${weightTier ? `<span class="tier-pill ${weightTier}">${weightTier}</span>` : ""}
                </span>
              </div>

              ${
                specsVal
                  ? `
                <div style="margin-top: 10px;">
                  <span class="field-label" style="display:block; margin-bottom:4px;">${t.fields.specs}:</span>
                  <div class="specs-text">${escapeHtml(specsVal)}</div>
                </div>
              `
                  : ""
              }

              ${
                notesVal
                  ? `
                <div style="margin-top: 8px;">
                  <span class="field-label" style="display:block; margin-bottom:4px;">${t.fields.notes}:</span>
                  <div class="specs-text" style="color:#94a3b8; font-size:0.75rem;">${escapeHtml(notesVal)}</div>
                </div>
              `
                  : ""
              }
            </div>

          </div>
        `;
        });

        grid.innerHTML = html;
      }

      function toggleDetails(recId) {
        const drawer = document.getElementById(`drawer-${recId}`);
        const btnText = document.getElementById(`btn-text-${recId}`);
        const t = I18N[currentLang];
        if (drawer.classList.contains("open")) {
          drawer.classList.remove("open");
          btnText.textContent = `▶ ${t.viewDetails}`;
        } else {
          drawer.classList.add("open");
          btnText.textContent = `▼ ${t.hideDetails}`;
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
        renderStats();
        renderCategoryChips();
        renderGrid();
        updateCompareDrawer();
      }

      // Event Listeners
      document
        .getElementById("lang-btn")
        .addEventListener("click", switchLanguage);

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

      document.getElementById("file-picker").addEventListener("change", (e) => {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (event) => {
          try {
            const parsed = JSON.parse(event.target.result);
            if (Array.isArray(parsed)) {
              catalogData = parsed;
              renderAll();
            } else {
              console.warn("Uploaded JSON must be an array of catalog items.");
            }
          } catch (err) {
            console.warn("Invalid JSON file:", err.message);
          }
        };
        reader.readAsText(file);
      });

      // Initialize
      window.addEventListener("DOMContentLoaded", initData);'''

# Replace the script block
pattern = re.compile(r'// --- Bilingual UI Dictionaries ---.*?window\.addEventListener\("DOMContentLoaded", initData\);', re.DOTALL)
if pattern.search(content):
    content = pattern.sub(new_script, content)
else:
    print("Warning: regex pattern did not match script block directly")

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("catalog-demo.html updated successfully!")
