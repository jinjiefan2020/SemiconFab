#!/usr/bin/env python3
"""
scripts/test_dual_themes.py
Captures side-by-side verification screenshots of Light Mode and Dark Mode across:
1. fab-capex.html (Capex estimator, Production Scale, BOM table)
2. compare.html (Equipment comparison matrix)
3. catalog-demo.html (Equipment catalog grid)
4. data-standard.html (Specification & Schema standards)
"""

import http.server
import socketserver
import subprocess
import threading
import time
import os

PORT = 8094
CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output", "screenshots", "dual_theme")
os.makedirs(OUTPUT_DIR, exist_ok=True)

class SilentHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def run_server():
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    with socketserver.TCPServer(("", PORT), SilentHandler) as httpd:
        httpd.serve_forever()

def capture(url, out_name, width=1440, height=1050):
    out_path = os.path.join(OUTPUT_DIR, out_name)
    cmd = [
        CHROME_BIN,
        "--headless",
        "--disable-gpu",
        f"--window-size={width},{height}",
        "--hide-scrollbars",
        "--virtual-time-budget=3500",
        f"--screenshot={out_path}",
        url
    ]
    subprocess.run(cmd, check=True)
    size = os.path.getsize(out_path)
    print(f"Captured {out_name} ({size:,} bytes) [size: {width}x{height}]")

def main():
    t = threading.Thread(target=run_server, daemon=True)
    t.start()
    time.sleep(1)

    id1 = "3acd7b05-e6e8-5312-bb5b-045e7dd3074b" # Canon FPA-5550iZ2 [litho]
    id2 = "c327b57f-9e72-50d5-87a3-0986242ffb86" # ASML NXT:2050i [litho]

    pages = [
        ("fab-capex.html?theme=light", "capex_light_desktop.png", 1440, 1050),
        ("fab-capex.html?theme=dark",  "capex_dark_desktop.png", 1440, 1050),
        ("fab-capex.html?theme=light", "capex_light_mobile.png", 540, 960),
        (f"compare.html?compare={id1},{id2}&theme=light", "compare_light_desktop.png", 1440, 1050),
        (f"compare.html?compare={id1},{id2}&theme=dark",  "compare_dark_desktop.png", 1440, 1050),
        ("catalog-demo.html?theme=light", "catalog_light_desktop.png", 1440, 1050),
        ("catalog-demo.html?theme=dark",  "catalog_dark_desktop.png", 1440, 1050),
        ("fab-cost.html?theme=light", "fab_cost_light_desktop.png", 1440, 1050),
        ("fab-cost.html?theme=dark",  "fab_cost_dark_desktop.png", 1440, 1050),
        ("index.html?theme=light",    "index_light_desktop.png", 1440, 1050),
        ("index.html?theme=dark",     "index_dark_desktop.png", 1440, 1050),
        ("data-standard.html?theme=light", "data_standard_light.png", 1440, 1050),
        ("data-standard.html?theme=dark",  "data_standard_dark.png", 1440, 1050),
    ]

    for rel_url, out_name, w, h in pages:
        full_url = f"http://localhost:{PORT}/{rel_url}"
        capture(full_url, out_name, width=w, height=h)

    print("All dual-theme screenshots successfully captured!")

if __name__ == "__main__":
    main()
