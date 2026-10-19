import re

FILE_PATH = "catalog-demo.html"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

target = '''              ${
                notesVal
                  ? `
                <div style="margin-top: 8px;">
                  <span class="field-label" style="display:block; margin-bottom:4px;">${t.fields.notes}:</span>
                  <div class="specs-text" style="color:#94a3b8; font-size:0.75rem;">${escapeHtml(notesVal)}</div>
                </div>
              `
                  : ""
              }
            </div>'''

replacement = '''              ${
                notesVal
                  ? `
                <div style="margin-top: 8px;">
                  <span class="field-label" style="display:block; margin-bottom:4px;">${t.fields.notes}:</span>
                  <div class="specs-text" style="color:#94a3b8; font-size:0.75rem;">${escapeHtml(notesVal)}</div>
                </div>
              `
                  : ""
              }

              <!-- Price Details Section in Drawer (1.6.0) -->
              <div style="margin-top: 14px; padding-top: 10px; border-top: 1px solid #334155; display: flex; flex-direction: column; gap: 6px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <span class="field-label" style="font-weight: 700; color: #38bdf8;">${currentLang === "zh" ? "设备价格估算与依据" : "Estimated Price & Valuation Basis"}:</span>
                  <a href="compare.html?compare=${item.record_id}" style="font-size: 0.75rem; color: #60a5fa; text-decoration: underline;">
                    ${currentLang === "zh" ? "对比此机台 →" : "Compare this tool →"}
                  </a>
                </div>
                ${est && est.basis !== "unknown" && est.low_usd ? `
                  <div style="font-size: 0.875rem; font-weight: 800; color: #fff;">
                    ${formatPriceUSD(est.low_usd)} – ${formatPriceUSD(est.high_usd)} USD
                    <span class="basis-pill basis-${est.basis || 'category_estimate'}" style="margin-left: 6px;">● ${est.basis === 'reported' ? t.basisReported : (est.basis === 'observed_listing' ? t.basisObserved : t.basisEstimate)}</span>
                    <span class="cond-pill">${est.condition === 'used' ? t.condUsed : (est.condition === 'refurbished' ? t.condRefurbished : t.condNew)}</span>
                  </div>
                  ${est.note ? `<div style="font-size: 0.75rem; color: #94a3b8; line-height: 1.4;">${escapeHtml(est.note)}</div>` : ''}
                  ${est.source_url ? `<div><a href="${escapeHtml(est.source_url)}" target="_blank" rel="noopener noreferrer" style="font-size: 0.75rem; color: #38bdf8; text-decoration: underline;">🔗 ${currentLang === 'zh' ? '公开来源出处 / 报道' : 'Public Source Citation'}</a></div>` : ''}
                ` : `<div style="color: #64748b; font-size: 0.75rem;">${t.fields.notAvailable}</div>`}
              </div>
            </div>'''

if target in content:
    content = content.replace(target, replacement, 1)
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully added price details to catalog-demo.html drawer!")
else:
    print("Target block not found in catalog-demo.html")
