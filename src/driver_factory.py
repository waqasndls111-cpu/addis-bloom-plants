from __future__ import annotations

import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def create_chrome_driver() -> webdriver.Chrome:
    """Create a Chrome driver with a desktop viewport so hover menus are available."""
    options = ChromeOptions()
    options.add_argument("--window-size=1440,900")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    if os.getenv("HEADLESS", "0") in {"1", "true", "TRUE", "yes", "YES"}:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(45)
    return driver
