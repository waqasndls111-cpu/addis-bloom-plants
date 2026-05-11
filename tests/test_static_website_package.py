from __future__ import annotations

import csv
from pathlib import Path

from src.config import ROOT_DIR


def test_static_website_manifest_pages_exist():
    manifest = Path(ROOT_DIR) / "data" / "site_pages_manifest.csv"
    website = Path(ROOT_DIR) / "website"
    with manifest.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    assert len(rows) >= 45
    missing = [row["file"] for row in rows if not (website / row["file"]).exists()]
    assert not missing


def test_full_site_menu_internal_paths_have_static_pages():
    menu = Path(ROOT_DIR) / "data" / "full_site_menu_structure.csv"
    website = Path(ROOT_DIR) / "website"
    ignored_external_prefixes = ("http://", "https://", "mailto:", "tel:")
    missing = []
    with menu.open("r", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            path = row["path"]
            if path.startswith(ignored_external_prefixes):
                continue
            path = path.split("#", 1)[0].split("?", 1)[0].strip("/")
            filename = "index.html" if not path else f"{path.split('/')[-1]}.html"
            if not (website / filename).exists():
                missing.append((row["label"], filename))
    assert not missing
