from __future__ import annotations

import csv
from pathlib import Path

import pytest

from src.config import ROOT_DIR, get_base_url, get_cleft_lip_palate_surgery_details


def test_cleft_lip_palate_surgery_extracted_data_is_complete():
    details = get_cleft_lip_palate_surgery_details()

    assert details["path"] == "/cleft-lip-palate-surgery/"
    assert details["page_id"] == 4235
    assert details["title"] == "Cleft Lip & Palate Surgery | Staten Island Oral Surgery"
    assert details["canonical"] == "https://statenislandoralsurgery.us/cleft-lip-palate-surgery/"
    assert details["main_h1"] == "Staten Island, NY Cleft Palate & Cleft Lip Repair"
    assert details["hero_h2"] == "Cleft Lip & Palate Surgery"
    assert details["primary_image"]["alt"] == "Baby with cleft palate in NY"
    assert details["secondary_image"]["alt"] == "Baby with cleft lip and cleft palate laying down"
    assert len(details["gallery_images"]) == 21
    assert details["gallery_images"][0]["url"].endswith("/4-5.jpg")
    assert [video["url"].rsplit("=", 1)[-1] for video in details["videos"]] == [
        "kfD-g8M4JBU",
        "hKt6mYy3YrQ",
        "iLOHJO0Fb6Y",
    ]
    assert details["decorative_animation"]["url"].endswith("Different-age-and-gender-groups-line-2.aep_.json")
    assert [item["question"] for item in details["faq_items"]] == [
        "What Is A Cleft Palate?",
        "Are Cleft Lip & Palate Common?",
        "How Is A Cleft Lip Corrected?",
        "How Is A Cleft Palate Corrected?",
        "How Are Cleft Lip & Palate Managed?",
        "What Can The Patient Expect After Cleft Lip & Palate Surgery?",
    ]
    assert details["cta"]["button_path"] == "/callback-request/"


def test_cleft_lip_palate_surgery_faq_csv_matches_json():
    details = get_cleft_lip_palate_surgery_details()
    csv_path = Path(ROOT_DIR) / "data" / "cleft_lip_palate_surgery_faqs.csv"
    with csv_path.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert [row["question"] for row in rows] == [item["question"] for item in details["faq_items"]]
    assert all(row["answer"].strip() for row in rows)


@pytest.mark.live
def test_cleft_lip_palate_surgery_page_matches_extracted_html_data():
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_cleft_lip_palate_surgery_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
