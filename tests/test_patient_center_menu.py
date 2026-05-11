from __future__ import annotations

import pytest

from src.config import (
    get_base_url,
    get_patient_center_card_pages,
    get_patient_center_parent_page,
    get_patient_center_submenu_pages,
)


def test_patient_center_header_submenu_pages_are_complete():
    parent = get_patient_center_parent_page()
    assert parent.label == "Patient Center"
    assert parent.path == "/patient-center/"

    pages = get_patient_center_submenu_pages()
    assert [(page.label, page.path) for page in pages] == [
        ("First Visit", "/first-visit/"),
        ("Patient Forms", "/patient-forms/"),
        ("Surgical Instructions", "/surgical-instructions/"),
        ("Insurance & Financing", "/insurance-and-financing/"),
        ("Patient Testimonials", "/testimonials/"),
        ("Wisdom Tooth Consent", "/our-services/oral-and-maxillofacial/wisdom-teeth-removal/#consent"),
        ("Pay Your Bill", "/pay-your-bill/"),
        ("Media", "/media/"),
    ]


def test_patient_center_card_pages_are_recorded():
    cards = get_patient_center_card_pages()
    assert [(page.label, page.path) for page in cards] == [
        ("First Visit", "/first-visit/"),
        ("Patient Forms", "/patient-forms/"),
        ("Surgical Instructions", "/surgical-instructions/"),
        ("Insurance & Financing", "/insurance-and-financing/"),
        ("Patient Testimonials", "/testimonials/"),
        ("Wisdom Tooth Consent", "/wisdom-teeth-removal/#consent"),
        ("Pay Your Bill", "/pay-your-bill/"),
        ("Media", "/media/"),
    ]


@pytest.mark.live
def test_patient_center_header_submenu_links():
    from src.driver_factory import create_chrome_driver
    from src.menu_navigator import ServicesMenuNavigator

    driver = create_chrome_driver()
    try:
        navigator = ServicesMenuNavigator(driver, get_base_url())
        results = navigator.validate_top_level_submenu_pages(
            get_patient_center_parent_page(),
            get_patient_center_submenu_pages(),
        )
        failures = [result for result in results if not result.passed]
        assert not failures, "Failed pages: " + ", ".join(result.label for result in failures)
    finally:
        driver.quit()
