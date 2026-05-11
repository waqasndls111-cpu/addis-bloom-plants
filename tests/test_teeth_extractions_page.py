from __future__ import annotations

import csv
from pathlib import Path

import pytest

from src.config import ROOT_DIR, get_teeth_extractions_details


def test_teeth_extractions_extracted_data_is_complete():
    details = get_teeth_extractions_details()

    assert details["path"] == "/teeth-extractions/"
    assert details["page_id"] == 4294
    assert details["title"] == "Teeth Extractions | Staten Island Oral Surgery"
    assert details["canonical"] == "https://statenislandoralsurgery.us/teeth-extractions/"
    assert details["main_h1"] == "Remove Teeth In Staten Island, NY"
    assert details["hero_h2"] == "Teeth Extractions"
    assert details["primary_image"]["alt"] == "Dentist holding tooth after extraction"
    assert details["secondary_image"]["alt"] == "Dentist tools extracting a tooth from person's mouth"
    assert [item["question"] for item in details["faq_items"]] == [
        "How Are Teeth Extracted?",
        "What Tooth Replacement Options Are There After Tooth Extractions?",
        "Dental Implant Surgery",
        "Teeth In A Day",
    ]
    assert details["cta"]["button_path"] == "/callback-request/"


def test_teeth_extractions_faq_csv_matches_json():
    details = get_teeth_extractions_details()
    csv_path = Path(ROOT_DIR) / "data" / "teeth_extractions_faqs.csv"
    with csv_path.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert [row["question"] for row in rows] == [item["question"] for item in details["faq_items"]]
    assert all(row["answer"].strip() for row in rows)


@pytest.mark.live
def test_teeth_extractions_page_matches_extracted_html_data():
    from src.config import get_base_url
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_teeth_extractions_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
