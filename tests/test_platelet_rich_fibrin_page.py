from __future__ import annotations

import pytest

from src.config import get_platelet_rich_fibrin_details


def test_platelet_rich_fibrin_extracted_data_is_complete():
    details = get_platelet_rich_fibrin_details()

    assert details["path"] == "/platelet-rich-fibrin-prf/"
    assert details["page_id"] == 6397
    assert details["title"] == "Platelet Rich Fibrin (PRF) Treatment in Staten Island, NY"
    assert details["main_h1"] == "Platelet Rich Fibrin (PRF) Staten Island, NY"
    assert details["hero_h2"] == "Platelet Rich Fibrin (PRF)"
    assert details["primary_image"]["alt"] == "Platelet Rich Fibrin (PRF)"
    assert details["secondary_image"]["alt"] == "Person holding a vile of blood"
    assert [item["question"] for item in details["faq_items"]] == [
        "What can PRF be used for?",
        "Why should I want PRF for my oral surgery procedure?",
    ]


@pytest.mark.live
def test_platelet_rich_fibrin_page_matches_extracted_html_data():
    from src.config import get_base_url
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_platelet_rich_fibrin_page(get_platelet_rich_fibrin_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
