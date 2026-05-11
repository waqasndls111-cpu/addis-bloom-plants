from __future__ import annotations

import pytest

from src.config import get_base_url, get_patient_center_details


def test_patient_center_extracted_data_is_complete():
    details = get_patient_center_details()

    assert details["path"] == "/patient-center/"
    assert details["page_id"] == 4401
    assert details["title"] == "Patient Center | Staten Island Oral Surgery"
    assert details["canonical"] == "https://statenislandoralsurgery.us/patient-center/"
    assert details["main_h1"] == "Patient Center"
    assert details["hero_h2"] == "Patient Center"
    assert details["primary_image"]["url"].endswith("/SIOMS-5-1.jpg")
    assert [page["label"] for page in details["child_pages"]] == [
        "First Visit",
        "Patient Forms",
        "Surgical Instructions",
        "Insurance & Financing",
        "Patient Testimonials",
        "Wisdom Tooth Consent",
        "Pay Your Bill",
        "Media",
    ]


@pytest.mark.live
def test_patient_center_page_matches_extracted_html_data():
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_patient_center_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
