from __future__ import annotations

import pytest

from src.config import (
    get_base_url,
    get_facial_birth_deformities_parent_page,
    get_facial_birth_deformities_submenu_pages,
)


def test_facial_birth_deformities_header_submenu_pages_are_complete():
    parent = get_facial_birth_deformities_parent_page()
    assert parent.label == "Facial Birth Deformities"
    assert parent.path == "/facial-birth-deformities/"

    pages = get_facial_birth_deformities_submenu_pages()
    assert [(page.label, page.path) for page in pages] == [
        ("Cleft Lip & Palate Surgery", "/cleft-lip-palate-surgery/"),
        ("Hemifacial Microsomia", "/hemifacial-microsomia/"),
        ("Treacher Collins Syndrome", "/treacher-collins-syndrome/"),
        ("Pierre Robin Sequence", "/pierre-robin-sequence/"),
        ("Neonatal Distraction", "/neonatal-distraction/"),
    ]


@pytest.mark.live
def test_facial_birth_deformities_header_submenu_links():
    from src.driver_factory import create_chrome_driver
    from src.menu_navigator import ServicesMenuNavigator

    driver = create_chrome_driver()
    try:
        navigator = ServicesMenuNavigator(driver, get_base_url())
        results = navigator.validate_nested_header_submenu_pages(
            get_facial_birth_deformities_parent_page(),
            get_facial_birth_deformities_submenu_pages(),
        )
        failures = [result for result in results if not result.passed]
        assert not failures, "Failed pages: " + ", ".join(result.label for result in failures)
    finally:
        driver.quit()
