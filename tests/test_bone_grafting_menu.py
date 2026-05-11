from __future__ import annotations

import pytest
from src.config import get_base_url, get_header_submenu_pages, get_page_details, get_parent_page


@pytest.fixture(scope="session")
def driver():
    from src.driver_factory import create_chrome_driver

    browser = create_chrome_driver()
    yield browser
    browser.quit()


@pytest.mark.live
def test_bone_grafting_header_submenu_links(driver):
    from src.menu_navigator import BoneGraftingMenuNavigator

    base_url = get_base_url()
    parent_page = get_parent_page()
    pages = get_header_submenu_pages()

    navigator = BoneGraftingMenuNavigator(driver, base_url)
    results = navigator.validate_header_submenu_pages(parent_page.path, pages)

    failures = [result for result in results if not result.passed]
    assert not failures, "Failed pages: " + ", ".join(result.label for result in failures)


def test_project_has_all_visible_bone_grafting_submenu_pages():
    labels = [page.label for page in get_header_submenu_pages()]
    assert labels == [
        "Bone Grafting FAQs",
        "Ridge Augmentation",
        "Sinus Lift",
        "Platelet Rich Fibrin (PRF)",
    ]


def test_ridge_augmentation_project_data_is_complete():
    ridge = get_page_details("ridge_augmentation")

    assert ridge["page_id"] == 4180
    assert ridge["path"] == "/ridge-augmentation/"
    assert ridge["title"] == "Ridge Augmentation | Staten Island Oral Surgery"
    assert ridge["canonical"] == "https://statenislandoralsurgery.us/ridge-augmentation/"
    assert ridge["main_h1"] == "Ridge Augmentation Surgery In Staten Island, NY"
    assert ridge["hero_h2"] == "Ridge Augmentation"
    assert ridge["hero_video"]["url"] == "https://www.youtube.com/watch?v=oEZAOWL4HJQ"
    assert ridge["primary_image"]["alt"] == "Older man smiling after ridge augmentation"
    assert [item["question"] for item in ridge["faq_items"]] == [
        "How Is a Ridge Augmentation Surgery Performed?",
        "What Can Ridge Augmentation Do For Dental Implants?",
        "Am I a Good Candidate For Ridge Augmentation?",
    ]


@pytest.mark.live
def test_ridge_augmentation_live_page_content(driver):
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait

    from src.menu_navigator import BoneGraftingMenuNavigator
    from src.selectors import canonical_link, content_heading_by_text, faq_question_by_text, main_heading_by_text, video_play_button

    ridge = get_page_details("ridge_augmentation")
    navigator = BoneGraftingMenuNavigator(driver, get_base_url())
    navigator.open_path(ridge["path"])
    wait = WebDriverWait(driver, 20)

    wait.until(EC.visibility_of_element_located(main_heading_by_text(ridge["main_h1"])))
    wait.until(EC.visibility_of_element_located(content_heading_by_text("What is Ridge Augmentation?")))
    wait.until(EC.presence_of_element_located(video_play_button()))

    canonical = wait.until(EC.presence_of_element_located(canonical_link()))
    assert canonical.get_attribute("href") == ridge["canonical"]

    for item in ridge["faq_items"]:
        wait.until(EC.visibility_of_element_located(faq_question_by_text(item["question"])))


def test_sinus_lift_project_data_is_complete():
    sinus = get_page_details("sinus_lift")

    assert sinus["page_id"] == 4188
    assert sinus["path"] == "/sinus-lift/"
    assert sinus["title"] == "Sinus Lift | Staten Island Oral Surgery"
    assert sinus["canonical"] == "https://statenislandoralsurgery.us/sinus-lift/"
    assert sinus["main_h1"] == "Support Dental Implants With A Sinus Lift In Staten Island, NY"
    assert sinus["hero_video"]["url"] == "https://youtu.be/B3sq-jgLDew"
    assert [item["question"] for item in sinus["faq_items"]] == [
        "How Is A Sinus Lift Performed?",
        "How Can A Sinus Lift Help Me?",
        "What Can I Expect From A Sinus Lift?",
    ]


def test_platelet_rich_fibrin_project_data_is_complete():
    prf = get_page_details("platelet_rich_fibrin_prf")

    assert prf["page_id"] == 6397
    assert prf["path"] == "/platelet-rich-fibrin-prf/"
    assert prf["title"] == "Platelet Rich Fibrin (PRF) Treatment in Staten Island, NY"
    assert prf["canonical"] == "https://statenislandoralsurgery.us/platelet-rich-fibrin-prf/"
    assert prf["main_h1"] == "Platelet Rich Fibrin (PRF) Staten Island, NY"
    assert prf["primary_image"]["url"].endswith("close-up-doctor-checking-smiley-patient.jpg")
    assert [item["question"] for item in prf["faq_items"]] == [
        "What can PRF be used for?",
        "Why should I want PRF for my oral surgery procedure?",
    ]
