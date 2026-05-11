from __future__ import annotations

import csv
from pathlib import Path

import pytest

from src.config import ROOT_DIR, get_base_url, get_patient_forms_details


def test_patient_forms_extracted_data_is_complete():
    details = get_patient_forms_details()

    assert details["path"] == "/patient-forms/"
    assert details["page_id"] == 3940
    assert details["title"] == "Patient Forms | Staten Island Oral Surgery"
    assert details["canonical"] == "https://statenislandoralsurgery.us/patient-forms/"
    assert details["main_h1"] == "Staten Island Oral & Maxillofacial Surgery Patient Forms"
    assert details["hero_h2"] == "Patient Forms"
    assert details["primary_image"]["alt"] == "Person holding pen filling out paperwork"
    assert details["secondary_image"]["alt"] == "Woman smiling into dentist mirror"
    assert [link["label"] for link in details["form_links"]] == [
        "Staten Island Online Registration",
        "Printable Registration",
        "Privacy Policy",
        "Receipt of Privacy Policy",
        "Photo Release Authorization",
        "Site Disclaimer",
    ]


def test_patient_forms_links_csv_matches_json():
    details = get_patient_forms_details()
    csv_path = Path(ROOT_DIR) / "data" / "patient_forms_links.csv"
    with csv_path.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert [row["label"] for row in rows] == [link["label"] for link in details["form_links"]]
    assert all(row["url"].strip() for row in rows)


@pytest.mark.live
def test_patient_forms_page_matches_extracted_html_data():
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_patient_forms_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
