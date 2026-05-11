from __future__ import annotations

import csv
from pathlib import Path

import pytest

from src.config import ROOT_DIR, get_base_url, get_treacher_collins_syndrome_details


def test_treacher_collins_syndrome_extracted_data_is_complete():
    details = get_treacher_collins_syndrome_details()

    assert details["path"] == "/treacher-collins-syndrome/"
    assert details["page_id"] == 4276
    assert details["title"] == "Treacher Collins Syndrome | Staten Island Oral Surgery"
    assert details["canonical"] == "https://statenislandoralsurgery.us/treacher-collins-syndrome/"
    assert details["main_h1"] == "Treacher Collins Syndrome Treatment & Surgery In Staten Island, NY"
    assert details["hero_h2"] == "Treacher Collins Syndrome"
    assert details["primary_image"]["alt"] == "Baby in white sweater laying on white bedsheets"
    assert details["secondary_image"]["alt"] == "Woman holding up baby feet while baby is sleeping"
    assert details["decorative_animation"]["url"].endswith("Different-age-and-gender-groups-line-2.aep_.json")
    assert [item["question"] for item in details["faq_items"]] == [
        "How Can A Treacher Collins Syndrome Treatment Help?",
        "What Can I Expect From Surgery To Correct Treacher Collins Syndrome?",
    ]
    assert details["cta"]["button_path"] == "/callback-request/"


def test_treacher_collins_syndrome_faq_csv_matches_json():
    details = get_treacher_collins_syndrome_details()
    csv_path = Path(ROOT_DIR) / "data" / "treacher_collins_syndrome_faqs.csv"
    with csv_path.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert [row["question"] for row in rows] == [item["question"] for item in details["faq_items"]]
    assert all(row["answer"].strip() for row in rows)


@pytest.mark.live
def test_treacher_collins_syndrome_page_matches_extracted_html_data():
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_treacher_collins_syndrome_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
