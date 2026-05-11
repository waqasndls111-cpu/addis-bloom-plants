from __future__ import annotations

import pytest

from src.config import get_ridge_augmentation_details


def test_ridge_augmentation_extracted_data_is_complete():
    details = get_ridge_augmentation_details()

    assert details["path"] == "/ridge-augmentation/"
    assert details["page_id"] == 4180
    assert details["title"] == "Ridge Augmentation | Staten Island Oral Surgery"
    assert details["main_h1"] == "Ridge Augmentation Surgery In Staten Island, NY"
    assert details["hero_h2"] == "Ridge Augmentation"
    assert details["hero_video"]["url"] == "https://www.youtube.com/watch?v=oEZAOWL4HJQ"
    assert details["primary_image"]["alt"] == "Older man smiling after ridge augmentation"
    assert [item["question"] for item in details["faq_items"]] == [
        "How Is a Ridge Augmentation Surgery Performed?",
        "What Can Ridge Augmentation Do For Dental Implants?",
        "Am I a Good Candidate For Ridge Augmentation?",
    ]


@pytest.mark.live
def test_ridge_augmentation_page_matches_extracted_html_data():
    # Selenium is imported inside the live browser test so the data-only test above
    # can still run before dependencies are installed.
    from src.config import get_base_url
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_page_content(get_ridge_augmentation_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
