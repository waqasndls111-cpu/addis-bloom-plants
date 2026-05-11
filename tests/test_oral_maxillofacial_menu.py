from __future__ import annotations

import pytest

from src.config import (
    get_base_url,
    get_oral_maxillofacial_parent_page,
    get_oral_maxillofacial_submenu_pages,
    get_related_oral_maxillofacial_links,
    get_service_menu_pages,
)


@pytest.fixture(scope="session")
def driver():
    from src.driver_factory import create_chrome_driver

    browser = create_chrome_driver()
    yield browser
    browser.quit()


def test_services_menu_has_oral_maxillofacial_branch():
    labels = [page.label for page in get_service_menu_pages()]
    assert labels == [
        "Dental Implants",
        "Teeth in a Day (All-On-X)",
        "Bone Grafting",
        "Oral & Maxillofacial Surgeries",
        "Facial Birth Deformities",
        "Anesthesia Options",
    ]

    oral_parent = get_oral_maxillofacial_parent_page()
    assert oral_parent.label == "Oral & Maxillofacial Surgeries"
    assert oral_parent.path == "/oral-and-maxillofacial/"


def test_oral_maxillofacial_header_submenu_pages_are_complete():
    pages = get_oral_maxillofacial_submenu_pages()
    assert [(page.label, page.path) for page in pages] == [
        ("Teeth Extractions", "/teeth-extractions/"),
        ("Wisdom Teeth Removal", "/wisdom-teeth-removal/"),
        ("Impacted Canines", "/impacted-canines/"),
        ("Orthognathic Jaw Surgery", "/orthognathic-jaw-surgery/"),
    ]


def test_related_oral_maxillofacial_footer_links_are_recorded():
    labels = [page.label for page in get_related_oral_maxillofacial_links()]
    assert labels == [
        "Frenectomy",
        "TMJ Disorders & Surgery",
        "Facial Trauma",
        "Oral Pathology",
        "MOHS Reconstruction",
        "Anesthesia Options",
    ]


@pytest.mark.live
def test_oral_maxillofacial_header_submenu_links(driver):
    from src.menu_navigator import ServicesMenuNavigator

    base_url = get_base_url()
    parent_page = get_oral_maxillofacial_parent_page()
    pages = get_oral_maxillofacial_submenu_pages()

    navigator = ServicesMenuNavigator(driver, base_url)
    results = navigator.validate_nested_header_submenu_pages(parent_page, pages)

    failures = [result for result in results if not result.passed]
    assert not failures, "Failed pages: " + ", ".join(result.label for result in failures)
