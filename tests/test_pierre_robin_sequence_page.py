from __future__ import annotations

import csv
from pathlib import Path

import pytest

from src.config import ROOT_DIR, get_base_url, get_pierre_robin_sequence_details


def test_pierre_robin_sequence_extracted_data_is_complete():
    details = get_pierre_robin_sequence_details()

    assert details["path"] == "/pierre-robin-sequence/"
    assert details["page_id"] == 4282
    assert details["title"] == "Pierre Robin Sequence | Staten Island Oral Surgery"
    assert details["canonical"] == "https://statenislandoralsurgery.us/pierre-robin-sequence/"
    assert details["main_h1"] == "Treatment Of Pierre Robin Sequence In Staten Island NY & Pierre Robin Cleft Palate"
    assert details["hero_h2"] == "Pierre Robin Sequence"
    assert details["primary_image"]["alt"] == "Person holding a baby's hand wearing a hospital bracelet"
    assert details["secondary_image"]["alt"] == "Baby feet wrapped in blue blanket with hearts"
    assert [video["url"] for video in details["videos"]] == [
        "https://www.youtube.com/watch?v=JiIvvBAKSYM",
        "https://www.youtube.com/watch?v=6gIYV3wo2w4",
    ]
    assert [item["question"] for item in details["faq_items"]] == [
        "How Can The Surgeons at Staten Island Oral & Maxillofacial Surgery Help My Child’s Pierre Robin Syndrome?",
        "What Can I Expect After Surgery To Correct Pierre Robin Syndrome?",
    ]
    assert details["cta"]["button_path"] == "/callback-request/"


def test_pierre_robin_sequence_faq_csv_matches_json():
    details = get_pierre_robin_sequence_details()
    csv_path = Path(ROOT_DIR) / "data" / "pierre_robin_sequence_faqs.csv"
    with csv_path.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert [row["question"] for row in rows] == [item["question"] for item in details["faq_items"]]
    assert all(row["answer"].strip() for row in rows)


@pytest.mark.live
def test_pierre_robin_sequence_page_matches_extracted_html_data():
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_pierre_robin_sequence_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
