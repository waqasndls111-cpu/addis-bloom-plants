from __future__ import annotations

import pytest

from src.config import get_sinus_lift_details


def test_sinus_lift_extracted_data_is_complete():
    details = get_sinus_lift_details()

    assert details["path"] == "/sinus-lift/"
    assert details["page_id"] == 4188
    assert details["title"] == "Sinus Lift | Staten Island Oral Surgery"
    assert details["main_h1"] == "Support Dental Implants With A Sinus Lift In Staten Island, NY"
    assert details["hero_h2"] == "Sinus Lift"
    assert details["hero_video"]["url"] == "https://youtu.be/B3sq-jgLDew"
    assert details["primary_image"]["alt"] == "Person smiling with perfect teeth after dental procedure"
    assert [item["question"] for item in details["faq_items"]] == [
        "How Is A Sinus Lift Performed?",
        "How Can A Sinus Lift Help Me?",
        "What Can I Expect From A Sinus Lift?",
    ]


@pytest.mark.live
def test_sinus_lift_page_matches_extracted_html_data():
    from src.config import get_base_url
    from src.driver_factory import create_chrome_driver
    from src.page_validator import PageContentValidator

    driver = create_chrome_driver()
    try:
        validator = PageContentValidator(driver, get_base_url())
        errors = validator.validate_sinus_lift_page(get_sinus_lift_details())
        assert not errors, "\n".join(errors)
    finally:
        driver.quit()
