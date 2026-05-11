from __future__ import annotations

import csv
from pathlib import Path

import pytest

from src.config import ROOT_DIR, get_base_url, get_media_details


def test_media_extracted_data_is_complete():
    details = get_media_details()

    assert details["path"] == "/media/"
    assert details["page_id"] == 4419
    assert details["title"] == "Media | Staten Island Oral Surgery"
    assert details["canonical"] == "https://statenislandoralsurgery.us/media/"
    assert details["main_h1"] == "Staten Island Oral & Maxillofacial Surgery Media & Videos"
    assert details["hero_h2"] == "Media & Videos"
    assert details["primary_image"]["url"].endswith("/SIOMS-7-1.jpg")
    assert len(details["videos"]) == 10
    assert details["videos"][0]["video_id"] == "ytfZbOiSK88"
    assert details["commercial"]["video_id"] == "taQ83Lz21ns"
    assert [item["label"] for item in details["magazines"]] == [
        "Read The Russian Copy",
        "Read The Spanish Copy",
    ]
    assert details["news_items"][0]["button_label"] == "Read The Full Story"


def test_media_videos_csv_matches_json():
    details = get_media_details()
    csv_path = Path(ROOT_DIR) / "data" / "media_videos.csv"
    with csv_path.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert [row["video_id"] for row in rows] == [item["video_id"] for item in details["videos"]]


@pytest.mark.live
def test_media_page_matches_extracted_html_data():
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_media_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
