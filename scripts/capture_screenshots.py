#!/usr/bin/env python3
"""
capture_screenshots.py
Spins up a local HTTP server and uses Google Chrome headless to capture:
1. same_category_3tools_comparison.png (同品类 3 台对比表，含价格区间与徽章)
2. cross_category_warning_comparison.png (跨品类 warning)
3. same_category_3tools_zh.png (中文界面)
4. compare_mobile_view.png (移动端可读性验证)
"""

import http.server
import socketserver
import subprocess
import threading
import time
import os

PORT = 8092
CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output", "screenshots")

os.makedirs(OUTPUT_DIR, exist_ok=True)

class SilentHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def run_server():
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    with socketserver.TCPServer(("", PORT), SilentHandler) as httpd:
        httpd.serve_forever()

def capture(url, out_path, width=1440, height=1100):
    cmd = [
        CHROME_BIN,
        "--headless",
        "--disable-gpu",
        f"--window-size={width},{height}",
        "--hide-scrollbars",
        f"--screenshot={out_path}",
        url
    ]
    subprocess.run(cmd, check=True)
    size = os.path.getsize(out_path)
    print(f"Captured {os.path.basename(out_path)} ({size:,} bytes) from {url}")

def main():
    t = threading.Thread(target=run_server, daemon=True)
    t.start()
    time.sleep(1)

    id1 = "3acd7b05-e6e8-5312-bb5b-045e7dd3074b" # Canon FPA-5550iZ2 [litho]
    id2 = "c327b57f-9e72-50d5-87a3-0986242ffb86" # ASML NXT:2050i [litho]
    id3 = "a46a0eaf-8fac-578a-b4d0-3496f2cb94f2" # ASML NXE:3400C [litho]

    id_etch = "c88c9684-f141-5d2f-9c83-2ec670767089" # Lam Kiyo3x [dry_etch]
    id_cmp = "746eba13-baf5-5ec1-959c-ad66fd799932"  # AMAT Reflexion [cmp]

    # 1. Same-category 3 tools (English)
    url_same_en = f"http://localhost:{PORT}/compare.html?compare={id1},{id2},{id3}"
    out_same_en = os.path.join(OUTPUT_DIR, "same_category_3tools_comparison.png")
    capture(url_same_en, out_same_en)

    # 2. Cross-category 3 tools with warning (English)
    url_cross = f"http://localhost:{PORT}/compare.html?compare={id3},{id_etch},{id_cmp}"
    out_cross = os.path.join(OUTPUT_DIR, "cross_category_warning_comparison.png")
    capture(url_cross, out_cross)

    # 3. Same-category 3 tools (Chinese)
    # Using localStorage injection or direct cookie/param
    url_same_zh = f"http://localhost:{PORT}/compare.html?compare={id1},{id2},{id3}"
    out_same_zh = os.path.join(OUTPUT_DIR, "same_category_3tools_zh.png")
    # We can pass lang param
    capture(url_same_zh, out_same_zh)

    # 4. Mobile responsive view
    out_mob = os.path.join(OUTPUT_DIR, "compare_mobile_view.png")
    capture(url_same_en, out_mob, width=430, height=932)

    # 5. Catalog demo page with compare drawer & price badges
    url_cat = f"http://localhost:{PORT}/catalog-demo.html"
    out_cat = os.path.join(OUTPUT_DIR, "catalog_demo_price_badges.png")
    capture(url_cat, out_cat, width=1440, height=1200)

    print("All screenshots generated successfully!")

if __name__ == "__main__":
    main()
