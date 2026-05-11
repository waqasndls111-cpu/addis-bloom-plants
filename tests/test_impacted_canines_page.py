from __future__ import annotations

import csv
from pathlib import Path

import pytest

from src.config import ROOT_DIR, get_impacted_canines_details


def test_impacted_canines_extracted_data_is_complete():
    details = get_impacted_canines_details()

    assert details["path"] == "/impacted-canines/"
    assert details["page_id"] == 4317
    assert details["title"] == "Impacted Canines | Staten Island Oral Surgery"
    assert details["canonical"] == "https://statenislandoralsurgery.us/impacted-canines/"
    assert details["main_h1"] == "Early Detection & Treatment Of Impacted Canine Teeth In Staten Island"
    assert details["hero_h2"] == "Impacted Canines"
    assert details["primary_image"]["alt"] == "Little girl with front teeth starting to grow in"
    assert details["secondary_image"]["alt"] == "Little boy smiling with head resting on arms"
    assert [item["question"] for item in details["faq_items"]] == [
        "What Are Cuspid Teeth?",
        "What Kind Of Problems Can Impacted Canine Teeth Cause?",
        "Why Is Early Detection Of Impacted Canine Teeth Important?",
        "How Are Impacted Canine Teeth Treated?",
        "What Happens If The Canine Tooth Will Not Erupt When Proper Space Is Available?",
        "What Can I Expect From Surgery To Expose And Bracket An Impacted Tooth?",
        "How Long Is Recovery After Impacted Canine Teeth Are Exposed And Bracketed?",
    ]
    assert details["cta"]["button_path"] == "/callback-request/"


def test_impacted_canines_faq_csv_matches_json():
    details = get_impacted_canines_details()
    csv_path = Path(ROOT_DIR) / "data" / "impacted_canines_faqs.csv"
    with csv_path.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert [row["question"] for row in rows] == [item["question"] for item in details["faq_items"]]
    assert all(row["answer"].strip() for row in rows)


@pytest.mark.live
def test_impacted_canines_page_matches_extracted_html_data():
    from src.config import get_base_url
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_impacted_canines_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
