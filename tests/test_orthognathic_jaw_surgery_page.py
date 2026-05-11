from __future__ import annotations

import csv
from pathlib import Path

import pytest

from src.config import ROOT_DIR, get_orthognathic_jaw_surgery_details


def test_orthognathic_jaw_surgery_extracted_data_is_complete():
    details = get_orthognathic_jaw_surgery_details()

    assert details["path"] == "/orthognathic-jaw-surgery/"
    assert details["page_id"] == 4329
    assert details["title"] == "Orthognathic Jaw Surgery | Staten Island Oral Surgery"
    assert details["canonical"] == "https://statenislandoralsurgery.us/orthognathic-jaw-surgery/"
    assert details["main_h1"] == "Staten Island Orthognathic Jaw Surgery For Misaligned Teeth & Jaw"
    assert details["hero_h2"] == "Orthognathic Jaw Surgery"
    assert details["primary_image"]["alt"] == "Woman smiling with braces"
    assert details["secondary_image"]["alt"] == "Skull showing teeth with braces"
    assert details["videos"][0]["url"].endswith("JiIvvBAKSYM")
    assert details["videos"][1]["url"].endswith("6gIYV3wo2w4")
    assert details["decorative_animation"]["url"].endswith("02-Prosthesis.json")
    assert [item["question"] for item in details["faq_items"]] == [
        "What Are The Symptoms Of Misaligned Jaws?",
        "Who is a Candidate for Orthognathic Surgery?",
        "How Is Orthognathic Surgery Performed?",
        "Can I See How Beforehand What I Can Expect to Look Like After Jaw Surgery?",
    ]
    assert details["cta"]["button_path"] == "/callback-request/"


def test_orthognathic_jaw_surgery_faq_csv_matches_json():
    details = get_orthognathic_jaw_surgery_details()
    csv_path = Path(ROOT_DIR) / "data" / "orthognathic_jaw_surgery_faqs.csv"
    with csv_path.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert [row["question"] for row in rows] == [item["question"] for item in details["faq_items"]]
    assert all(row["answer"].strip() for row in rows)


@pytest.mark.live
def test_orthognathic_jaw_surgery_page_matches_extracted_html_data():
    from src.config import get_base_url
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_orthognathic_jaw_surgery_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
