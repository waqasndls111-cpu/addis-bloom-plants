from __future__ import annotations

import csv
from pathlib import Path

import pytest

from src.config import ROOT_DIR, get_base_url, get_patient_testimonials_details


def test_patient_testimonials_extracted_data_is_complete():
    details = get_patient_testimonials_details()

    assert details["path"] == "/testimonials/"
    assert details["archive_template_id"] == 3976
    assert details["title"] == "Testimonials | Staten Island Oral Surgery"
    assert details["canonical"] == "https://statenislandoralsurgery.us/testimonials/"
    assert details["main_h1"] == "Staten Island Oral Surgery Reviews"
    assert details["hero_h2"] == "Patient Testimonials"
    assert details["videos"][0]["video_id"] == "dTUQ0U8VVCo"
    assert [item["name"] for item in details["testimonials"]] == [
        "Roseann Cacaci",
        "Judith Catarella",
        "Gloria Morales",
        "Anna Accarino",
    ]


def test_patient_testimonials_items_csv_matches_json():
    details = get_patient_testimonials_details()
    csv_path = Path(ROOT_DIR) / "data" / "patient_testimonials_items.csv"
    with csv_path.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert [row["name"] for row in rows] == [item["name"] for item in details["testimonials"]]


@pytest.mark.live
def test_patient_testimonials_page_matches_extracted_html_data():
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_patient_testimonials_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
