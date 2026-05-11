from __future__ import annotations

import pytest

from src.config import get_oral_and_maxillofacial_details


def test_oral_and_maxillofacial_extracted_data_is_complete():
    details = get_oral_and_maxillofacial_details()

    assert details["path"] == "/oral-and-maxillofacial/"
    assert details["page_id"] == 4045
    assert details["title"] == "Oral & Maxillofacial Surgeries | Staten Island Oral Surgery"
    assert details["canonical"] == "https://statenislandoralsurgery.us/oral-and-maxillofacial/"
    assert details["main_h1"] == "Staten Island Oral & Maxillofacial"
    assert details["hero_h2"] == "Oral & Maxillofacial"
    assert details["primary_image"]["alt"] == "Patient sitting in chair while dentists look over their records"
    assert details["secondary_image"]["url"].endswith("Staten-Island-Oral-and-Maxillofacial-Surgery-3.jpg")
    assert [link["label"] for link in details["content_sections"][0]["links"]] == [
        "Teeth Extractions",
        "Impacted Canines",
        "Wisdom Teeth Removal",
        "Orthognathic Jaw Surgery",
    ]


@pytest.mark.live
def test_oral_and_maxillofacial_page_matches_extracted_html_data():
    from src.config import get_base_url
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_oral_and_maxillofacial_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
