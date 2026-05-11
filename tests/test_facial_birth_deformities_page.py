from __future__ import annotations

import pytest

from src.config import get_base_url, get_facial_birth_deformities_details


def test_facial_birth_deformities_extracted_data_is_complete():
    details = get_facial_birth_deformities_details()

    assert details["path"] == "/facial-birth-deformities/"
    assert details["page_id"] == 4051
    assert details["title"] == "Facial Birth Deformities | Staten Island Oral Surgery"
    assert details["canonical"] == "https://statenislandoralsurgery.us/facial-birth-deformities/"
    assert details["main_h1"] == "Staten Island Facial Birth Deformities"
    assert details["hero_h2"] == "Facial Birth Deformities"
    assert details["primary_image"]["alt"] == "Woman holding baby with Facial Birth Deformities in Staten Island"
    assert details["secondary_image"]["alt"] == "Woman holding baby with cleft lip"
    assert [page["label"] for page in details["child_pages"]] == [
        "Cleft Lip & Palate Surgery",
        "Hemifacial Microsomia",
        "Treacher Collins Syndrome",
        "Pierre Robin Sequence",
        "Neonatal Distraction",
    ]


@pytest.mark.live
def test_facial_birth_deformities_page_matches_extracted_html_data():
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_facial_birth_deformities_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
