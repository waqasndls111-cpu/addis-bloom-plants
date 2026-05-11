from __future__ import annotations

import csv
from pathlib import Path

import pytest

from src.config import ROOT_DIR, get_base_url, get_neonatal_distraction_details


def test_neonatal_distraction_extracted_data_is_complete():
    details = get_neonatal_distraction_details()

    assert details["path"] == "/neonatal-distraction/"
    assert details["page_id"] == 4288
    assert details["title"] == "Neonatal Distraction | Staten Island Oral Surgery"
    assert details["canonical"] == "https://statenislandoralsurgery.us/neonatal-distraction/"
    assert details["main_h1"] == "Neonatal Distraction In Staten Island For Underdeveloped Jaw"
    assert details["hero_h2"] == "Neonatal Distraction"
    assert details["primary_image"]["alt"] == "Baby feet laying in basket"
    assert details["secondary_image"]["alt"] == "Woman holding a baby's head"
    assert details["decorative_animation"]["url"].endswith("Different-age-and-gender-groups-line-2.aep_.json")
    assert [item["question"] for item in details["faq_items"]] == [
        "How Can Neonatal Distraction Help My Child?",
        "What Can I Expect From Neonatal Distraction?",
    ]
    assert details["cta"]["button_path"] == "/callback-request/"


def test_neonatal_distraction_faq_csv_matches_json():
    details = get_neonatal_distraction_details()
    csv_path = Path(ROOT_DIR) / "data" / "neonatal_distraction_faqs.csv"
    with csv_path.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert [row["question"] for row in rows] == [item["question"] for item in details["faq_items"]]
    assert all(row["answer"].strip() for row in rows)


@pytest.mark.live
def test_neonatal_distraction_page_matches_extracted_html_data():
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_neonatal_distraction_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
