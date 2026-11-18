#!/usr/bin/env node
/**
 * scripts/sync_catalog_stats.js
 * Synchronizes catalog.json statistics with index.html, layout-editor.html, and catalog views.
 */

const fs = require("fs");
const path = require("path");

const rootDir = path.resolve(__dirname, "..");
const catalogPath = path.join(rootDir, "catalog.json");
const indexPath = path.join(rootDir, "index.html");

function syncStats() {
  console.log("Reading catalog.json...");
  const rawCatalog = fs.readFileSync(catalogPath, "utf-8");
  const catalog = JSON.parse(rawCatalog);

  const tools = Array.isArray(catalog) ? catalog : catalog.tools || [];
  const totalTools = tools.length;

  let fabCount = 0;
  let osatCount = 0;
  const tiers = {
    L1: 0,
    L2: 0,
    L3: 0,
    draft: 0,
  };

  tools.forEach((t) => {
    const isOsat =
      (t.category && t.category.startsWith("osat_")) ||
      t.domain === "osat" ||
      t.domain_id === "osat";
    if (isOsat) {
      osatCount++;
    } else {
      fabCount++;
    }

    const lvl = (t.conformance_level || "draft").toLowerCase();
    if (lvl === "l1") tiers.L1++;
    else if (lvl === "l2") tiers.L2++;
    else if (lvl === "l3") tiers.L3++;
    else tiers.draft++;
  });

  const l1Pct = Math.round((tiers.L1 / totalTools) * 100);
  const draftPct = 100 - l1Pct;

  console.log(`Total Tools: ${totalTools} (Fab: ${fabCount}, OSAT: ${osatCount})`);
  console.log(`Tiers: L1=${tiers.L1} (${l1Pct}%), Draft=${tiers.draft} (${draftPct}%)`);

  // Update index.html
  let indexHtml = fs.readFileSync(indexPath, "utf-8");

  // Replace L1 verified stat
  indexHtml = indexHtml.replace(
    /id="funnel-l1-stat"[\s\S]*?>[\d]+%\s*·\s*[\d]+\s*tools<\/span>/,
    `id="funnel-l1-stat" class="font-mono font-semibold text-emerald-600 dark:text-emerald-400">${l1Pct}% · ${tiers.L1} tools</span>`
  );
  indexHtml = indexHtml.replace(
    /id="funnel-l1-bar"[\s\S]*?style="width:\s*[\d]+%"/,
    `id="funnel-l1-bar" class="bg-emerald-500 h-1.5 rounded-full" style="width: ${l1Pct}%"`
  );

  // Replace Draft stat
  indexHtml = indexHtml.replace(
    /id="funnel-draft-stat"[\s\S]*?>[\d]+%\s*·\s*[\d]+\s*tools<\/span>/,
    `id="funnel-draft-stat" class="font-mono font-semibold text-amber-600 dark:text-amber-400">${draftPct}% · ${tiers.draft} tools</span>`
  );
  indexHtml = indexHtml.replace(
    /id="funnel-draft-bar"[\s\S]*?style="width:\s*[\d]+%"/,
    `id="funnel-draft-bar" class="bg-amber-500 h-1.5 rounded-full" style="width: ${draftPct}%"`
  );

  fs.writeFileSync(indexPath, indexHtml, "utf-8");
  console.log("Successfully synchronized index.html catalog funnel stats!");
}

syncStats();
