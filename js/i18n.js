// ==========================================
// SemiconFab.org — 9-Language Internationalization (i18n) Engine
// ==========================================

const SUPPORTED_LANGUAGES = [
  { code: "en", name: "English", label: "English" },
  { code: "zh-CN", name: "简体中文", label: "简体中文" },
  { code: "zh-TW", name: "繁體中文", label: "繁體中文" },
  { code: "ja", name: "日本語", label: "日本語" },
  { code: "ko", name: "한국어", label: "한국어" },
  { code: "de", name: "Deutsch", label: "Deutsch" },
  { code: "fr", name: "Français", label: "Français" },
  { code: "it", name: "Italiano", label: "Italiano" },
  { code: "es", name: "Español", label: "Español" },
];

let currentLang = "en";

function detectInitialLanguage() {
  // 1. Explicit URL search param: ?lang=...
  const urlParams = new URLSearchParams(window.location.search);
  let langParam = urlParams.get("lang");
  if (langParam === "zh") langParam = "zh-CN";
  if (langParam && I18N_DICTIONARY[langParam]) {
    return langParam;
  }

  // 2. User saved preference in LocalStorage
  const saved = localStorage.getItem("semiconfab_lang");
  if (saved && I18N_DICTIONARY[saved]) {
    return saved;
  }

  // 3. Auto-detect browser language if available
  const browserLang = (
    navigator.language ||
    navigator.userLanguage ||
    ""
  ).toLowerCase();
  if (browserLang.startsWith("zh")) {
    return "zh-CN";
  }

  // 4. Default to English as the primary canonical language for semiconductor engineering
  return "en";
}

function t(key) {
  const dict = I18N_DICTIONARY[currentLang] || I18N_DICTIONARY["en"];
  return dict[key] || I18N_DICTIONARY["en"][key] || key;
}

function toggleLanguage() {
  const targetLang = currentLang === "zh-CN" ? "en" : "zh-CN";
  setLanguage(targetLang);
}

function setLanguage(langCode) {
  if (langCode === "zh") langCode = "zh-CN";
  if (!I18N_DICTIONARY[langCode]) langCode = "en";
  currentLang = langCode;
  localStorage.setItem("semiconfab_lang", langCode);
  localStorage.setItem("semicon_lang", langCode.startsWith("zh") ? "zh" : langCode);
  document.documentElement.lang = langCode;
  document.documentElement.setAttribute("data-lang", langCode.startsWith("zh") ? "zh" : langCode);

  // 1. Update textContent for elements with data-i18n
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.getAttribute("data-i18n");
    const translated = t(key);
    if (translated && translated !== key) {
      el.textContent = translated;
    }
  });

  // 1.1 Update innerHTML for elements with data-i18n-html
  document.querySelectorAll("[data-i18n-html]").forEach((el) => {
    const key = el.getAttribute("data-i18n-html");
    const translated = t(key);
    if (translated && translated !== key) {
      el.innerHTML = translated;
    }
  });

  // 1.2 Update data-lbl for responsive mobile table cells
  document.querySelectorAll("[data-i18n-lbl]").forEach((el) => {
    const key = el.getAttribute("data-i18n-lbl");
    const translated = t(key);
    if (translated && translated !== key) {
      el.setAttribute("data-lbl", translated);
    }
  });

  // 1.3 Update aria-label for accessibility & chart SVGs
  document.querySelectorAll("[data-i18n-aria-label]").forEach((el) => {
    const key = el.getAttribute("data-i18n-aria-label");
    const translated = t(key);
    if (translated && translated !== key) {
      el.setAttribute("aria-label", translated);
    }
  });

  // 2. Update placeholders for inputs
  document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
    const key = el.getAttribute("data-i18n-placeholder");
    el.placeholder = t(key);
  });

  // 3. Update titles
  document.querySelectorAll("[data-i18n-title]").forEach((el) => {
    const key = el.getAttribute("data-i18n-title");
    el.title = t(key);
  });

  // 4. Update language picker UI state
  updateLangPickerUI();

  // 4.1 Update theme-label bilingual text
  const themeLabel = document.getElementById("theme-label");
  if (themeLabel) {
    const isDark = document.documentElement.classList.contains("dark") || document.documentElement.getAttribute("data-theme") === "dark";
    const isZh = langCode.startsWith("zh");
    themeLabel.textContent = isZh ? (isDark ? "暗色" : "亮色") : (isDark ? "Dark" : "Day");
  }

  // 5. Update language dropdown active state
  setupLangDropdown();

  // 5.1 Update FinFET, GAA, DRAM & NAND links based on language
  // Only Simplified Chinese ('zh-CN') links to Chinese version, all other languages link to English version
  const finfetTarget =
    langCode === "zh-CN" ? "finfet.html?lang=zh" : "finfet.html?lang=en";
  const gaaTarget =
    langCode === "zh-CN" ? "gaa.html?lang=zh" : "gaa.html?lang=en";
  const dramTarget =
    langCode === "zh-CN" ? "dram.html?lang=zh" : "dram.html?lang=en";
  const nandTarget =
    langCode === "zh-CN" ? "nand.html?lang=zh" : "nand.html?lang=en";
  const hbmTarget =
    langCode === "zh-CN" ? "hbm.html?lang=zh" : "hbm.html?lang=en";
  document.querySelectorAll('a[href*="finfet.html"]').forEach((a) => {
    a.href = finfetTarget;
  });
  document.querySelectorAll('a[href*="gaa.html"]').forEach((a) => {
    a.href = gaaTarget;
  });
  document.querySelectorAll('a[href*="dram.html"]').forEach((a) => {
    a.href = dramTarget;
  });
  document.querySelectorAll('a[href*="nand.html"]').forEach((a) => {
    a.href = nandTarget;
  });
  document.querySelectorAll('a[href*="hbm.html"]').forEach((a) => {
    a.href = hbmTarget;
  });

  // 6. Dispatch global event for custom components (like Three.js or Dynamic Dropdowns)
  window.dispatchEvent(
    new CustomEvent("semiconfab:langChanged", { detail: { lang: langCode } }),
  );
}

function updateLangPickerUI() {
  const currentObj =
    SUPPORTED_LANGUAGES.find((l) => l.code === currentLang) ||
    SUPPORTED_LANGUAGES[0];
  const labelEl = document.getElementById("current-lang-label");
  if (labelEl) {
    labelEl.innerHTML = `<span class="font-medium">${currentObj.name}</span>`;
  }
  const flagEl = document.getElementById("current-lang-flag");
  if (flagEl) {
    flagEl.remove();
  }
  const codeEl = document.getElementById("current-lang-code");
  if (codeEl) {
    codeEl.textContent =
      currentLang === "zh-CN"
        ? "中文"
        : currentLang === "zh-TW"
          ? "繁中"
          : currentObj.code.toUpperCase();
  }
}

function initI18n() {
  currentLang = detectInitialLanguage();
  setLanguage(currentLang);
  setupLangDropdown();
}

function setupLangDropdown() {
  const container = document.getElementById("lang-selector-menu");
  if (!container) return;

  container.innerHTML = SUPPORTED_LANGUAGES.map(
    (l) => `
    <button onclick="setLanguage('${l.code}'); toggleLangDropdown(false);" 
            class="w-full text-left px-3 py-2 text-xs hover:bg-slate-100 flex items-center justify-between rounded-lg transition ${l.code === currentLang ? "font-bold text-slate-900 bg-slate-50" : "text-slate-600"}">
      <span class="flex items-center gap-2"><span class="font-mono text-[9.5px] uppercase px-1 py-0.2 rounded bg-slate-100 text-slate-500 font-bold">${l.code}</span> <span>${l.name}</span></span>
      ${l.code === currentLang ? '<span class="text-emerald-600 text-xs">✓</span>' : ""}
    </button>
  `,
  ).join("");
}

function toggleLangDropdown(forceState) {
  const dropdown = document.getElementById("lang-dropdown-panel");
  if (!dropdown) return;
  if (typeof forceState === "boolean") {
    if (forceState) dropdown.classList.remove("hidden");
    else dropdown.classList.add("hidden");
  } else {
    dropdown.classList.toggle("hidden");
  }
}

// Global click outside to close dropdown
document.addEventListener("click", (e) => {
  const btn = document.getElementById("lang-picker-btn");
  const panel = document.getElementById("lang-dropdown-panel");
  if (btn && panel && !btn.contains(e.target) && !panel.contains(e.target)) {
    panel.classList.add("hidden");
  }
});
