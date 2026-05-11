from __future__ import annotations

import csv
from pathlib import Path

import pytest

from src.config import ROOT_DIR, get_base_url, get_hemifacial_microsomia_details


def test_hemifacial_microsomia_extracted_data_is_complete():
    details = get_hemifacial_microsomia_details()

    assert details["path"] == "/hemifacial-microsomia/"
    assert details["page_id"] == 4270
    assert details["title"] == "Hemifacial Microsomia | Staten Island Oral Surgery"
    assert details["canonical"] == "https://statenislandoralsurgery.us/hemifacial-microsomia/"
    assert details["main_h1"] == "Treatment Of Hemifacial Microsomia In Staten Island NY"
    assert details["hero_h2"] == "Hemifacial Microsomia"
    assert details["primary_image"]["alt"] == "Person holding baby feet in the shape of a heart"
    assert details["secondary_image"]["alt"] == "Baby hand in pink sweater"
    assert details["decorative_animation"]["url"].endswith("Different-age-and-gender-groups-line-2.aep_.json")
    assert [item["question"] for item in details["faq_items"]] == [
        "How Can A Hemifacial Microsomia Treatment Help?",
        "What Can I Expect From Surgery To Correct Hemifacial Microsomia?",
    ]
    assert details["cta"]["button_path"] == "/callback-request/"


def test_hemifacial_microsomia_faq_csv_matches_json():
    details = get_hemifacial_microsomia_details()
    csv_path = Path(ROOT_DIR) / "data" / "hemifacial_microsomia_faqs.csv"
    with csv_path.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert [row["question"] for row in rows] == [item["question"] for item in details["faq_items"]]
    assert all(row["answer"].strip() for row in rows)


@pytest.mark.live
def test_hemifacial_microsomia_page_matches_extracted_html_data():
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_hemifacial_microsomia_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
