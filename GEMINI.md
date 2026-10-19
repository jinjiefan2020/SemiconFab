# SemiconFab.org 核心设计规范与记忆规则 (Design System & Memory)

本文档是 SemiconFab.org 全站统一 UI/UX 与色调设计规范的持久化记忆规则。在进行任何页面开发、样式修改或组件重构时，必须严格遵守以下规范。

---

## 1. 核心色调与视觉设计规范 (对齐 `fab-cost.html`)

| 设计元素 | 亮色模式（默认） | 洁净室暗色模式（可选） | 视觉特征与设计意图 |
| :--- | :--- | :--- | :--- |
| **页面底色 (Base)** | `#f2f1ec`（温润纸质微暖灰） | `#12161a`（深炭黑深空基底） | 取代生冷的冷白灰与旧深色 `#090d16`，营造顶级研究期刊（Nature / FT 风格）质感 |
| **主卡片面板 (Surface)** | `#ffffff`（纯白卡片） | `#1a2026`（炭青微光面板） | 从暖纸底色中自然浮现，配备 `0 1px 2px / 0 8px 24px` 立体层次微阴影 |
| **次级面板/表头 (Surface-2)** | `#e9e7df`（暖石浅色层） | `#232b33`（次级炭黑） | 用于表格 `thead`、过滤标签底、输入框及价格底板 |
| **主要文字 (Ink)** | `#1c2126`（深炭黑墨水色） | `#e8eaec`（温和高亮米白） | 比生硬纯黑 `#000` 更雅致，对比度高达 13.2:1（WCAG AAA 级合规） |
| **次要文字 (Ink-2)** | `#4c5560`（冷炭灰说明文字） | `#aeb7bf`（中阶次级灰） | 辅助描述、度量单位与字段标签 |
| **微弱文字 (Ink-3)** | `#7a838d`（浅石灰说明） | `#7e8891`（低阶辅助灰） | 版权脚注、占位提示、不活跃图标 |
| **品牌主强调色 (Accent)** | `#0e6e6b`（雅致深青松绿 / Teal） | `#3fbdb8`（薄荷荧光青） | 导航激活项、价格高亮、主按钮与芯片 Accent（悬停：`#0a5451` / `#7fd8d3`） |
| **警告与草稿 (Amber)** | `#b45309` / 底 `#fdf3e3` | `#e8a04c` / 底 `#2c2417` | 缺失字段警告、未验证标签与试验线指示条、日间模式太阳图标 |
| **错误与警示红 (Red)** | `#a83226` / 底 `#fdf2f2` | `#e0786a` / 底 `#2c1a18` | 验证失败指标、极高风险提示 |
| **分割边线 (Line)** | `#d8d4c8`（暖石极细线） | `#333c45`（炭黑分割线） | 柔和微界线，杜绝刺眼黑线 |
| **排版字体 (Typography)** | `Manrope` + `IBM Plex Mono` | `Manrope` + `IBM Plex Mono` | 全局统一为现代工程西文字体与等宽代码/数字字体 |

---

## 2. 全局 CSS 变量声明标准 (`css/semicon-theme.css`)

```css
:root, html.light, [data-theme="light"] {
  color-scheme: light dark;
  --bg: #f2f1ec;
  --surface: #ffffff;
  --surface-2: #e9e7df;
  --ink: #1c2126;
  --ink-2: #4c5560;
  --ink-3: #7a838d;
  --line: #d8d4c8;
  --accent: #0e6e6b;
  --accent-ink: #0a5451;
  --amber: #b45309;
  --amber-bg: #fdf3e3;
  --red: #a83226;
  --red-bg: #fdf2f2;
  --chart-grid: #ddd9cc;
  --shadow: 0 1px 2px rgba(28, 33, 38, 0.06), 0 8px 24px rgba(28, 33, 38, 0.06);
}

html.dark, [data-theme="dark"] {
  --bg: #12161a;
  --surface: #1a2026;
  --surface-2: #232b33;
  --ink: #e8eaec;
  --ink-2: #aeb7bf;
  --ink-3: #7e8891;
  --line: #333c45;
  --accent: #3fbdb8;
  --accent-ink: #7fd8d3;
  --amber: #e8a04c;
  --amber-bg: #2c2417;
  --red: #e0786a;
  --red-bg: #2c1a18;
  --chart-grid: #2c343d;
  --shadow: 0 1px 2px rgba(0, 0, 0, 0.3), 0 8px 24px rgba(0, 0, 0, 0.25);
}
```

---

## 3. 页面顶部导航规范 (Header Navigation)

1. **左侧品牌区**：
   - 包含 300mm 晶圆图章（金色芯片微光 `fill="var(--accent)"`）。
   - 品牌字样 `SemiconFab<span style="color:var(--accent)">.org</span>`。
   - `v1.6` 胶囊徽章（背景 `var(--surface-2)`，文字 `var(--ink-2)`）。
   - **禁止添加多余的“首页”链接**：品牌 Logo 自身即直达首页交互，顶部导航菜单内不得包含“首页”。
2. **中心导航菜单**：
   - 保持专业与克制，**不得出现“提交您的设备”**（该入口仅在全量设备库或特定工具页面提供）。
   - 导航项字号为 13px，字重 600，默认颜色 `var(--ink-2)`，悬停背景 `var(--surface-2)`，激活项高亮为 `var(--accent)`（700 字重）。
3. **右侧操作控制区**：
   - 明暗主题切换按钮（采用 `.site-nav-btn` 样式，边框 `var(--line)`，背景 `var(--surface)`）：
     - 亮色模式显示太阳图标（`var(--amber)`）与文字 `亮色 / Day`。
     - 暗色模式显示月亮图标（`var(--accent)`）与文字 `暗色 / Dark`。
   - 多语言切换按钮：
     - 在全站统一导航控制器（`js/site-nav.js`，包含 Equipment、Economics、Standards 下拉菜单所属的所有页面）中，右上角语言切换按钮统一为 `En/中文`（文本为 `"En/中文"`，杜绝多余地球图标）。
     - 支持中英双语快速即时切换，并同步向子页面派发 `window.onSemiconLanguageChange(lang)`。
   - 行动按钮（如“Launch 3D Twin”）：背景 `var(--accent)`，白字，微光高亮。

---

## 4. 依赖引入规范

每个 HTML 页面在 `<head>` 中必须引入：
```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
  href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap"
  rel="stylesheet"
/>
<link rel="stylesheet" href="css/semicon-theme.css" />
```
并在 `<body>` 末尾加载统一多语言与站点控制器脚本。

---

## 5. 版本发布与 Git 推送规范 (Release Management)

- **发布版本**：`1.6.0`（`v1.6.0`）。
- **发布核心内容**：设备横向对比矩阵（`compare.html`）、晶圆厂全厂总造价 Capex 测算器（`fab-capex.html`）、全量 167 台机台价格与置信度数据库（`data/price_estimates.json`）、厂务成本拆解报告（`fab-cost.html`）与统一设计系统规范（`css/semicon-theme.css`、`js/site-nav.js`）。


