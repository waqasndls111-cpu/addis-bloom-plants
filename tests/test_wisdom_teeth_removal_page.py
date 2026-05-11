from __future__ import annotations

import csv
from pathlib import Path

import pytest

from src.config import ROOT_DIR, get_wisdom_teeth_removal_details


def test_wisdom_teeth_removal_extracted_data_is_complete():
    details = get_wisdom_teeth_removal_details()

    assert details["path"] == "/wisdom-teeth-removal/"
    assert details["page_id"] == 4304
    assert details["title"] == "Wisdom Teeth Removal in Staten Island, NY"
    assert details["canonical"] == "https://statenislandoralsurgery.us/wisdom-teeth-removal/"
    assert details["main_h1"] == "Wisdom Teeth Removal in Staten Island, NY"
    assert details["hero_h2"] == "Get Your Wisdom Teeth Removed"
    assert details["primary_image"]["alt"] == "Xray showing impacted wisdom tooth in staten island"
    assert details["secondary_image"]["alt"] == "Man holding jaw in pain from impacted wisdom tooth"
    assert details["hero_video"]["url"].endswith("AAw7zA7L2NE")
    assert [item["question"] for item in details["faq_items"]] == [
        "How Do I Know If My Wisdom Teeth Should be Removed?",
        "What Should I Expect from Wisdom Teeth Surgery?",
        "How Long Is Recovery From Wisdom Teeth Surgery?",
    ]
    assert details["cta"]["button_path"] == "/callback-request/"


def test_wisdom_teeth_removal_faq_csv_matches_json():
    details = get_wisdom_teeth_removal_details()
    csv_path = Path(ROOT_DIR) / "data" / "wisdom_teeth_removal_faqs.csv"
    with csv_path.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert [row["question"] for row in rows] == [item["question"] for item in details["faq_items"]]
    assert all(row["answer"].strip() for row in rows)


@pytest.mark.live
def test_wisdom_teeth_removal_page_matches_extracted_html_data():
    from src.config import get_base_url
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_wisdom_teeth_removal_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
