from __future__ import annotations

from dataclasses import dataclass
from time import sleep
from urllib.parse import urljoin, urlparse

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .config import PageLink
from .selectors import (
    BONE_GRAFTING_PARENT_LINK,
    PATIENT_CENTER_LINK,
    SERVICES_LINK,
    nav_link_by_text_and_path,
)


@dataclass(frozen=True)
class PageResult:
    label: str
    expected_path: str
    current_url: str
    title: str
    h1: str
    passed: bool


class BoneGraftingMenuNavigator:
    """Navigation helper for nested pages under the Services menu."""

    def __init__(self, driver: WebDriver, base_url: str, timeout: int = 20) -> None:
        self.driver = driver
        self.base_url = base_url.rstrip("/") + "/"
        self.wait = WebDriverWait(driver, timeout)

    def open_path(self, path: str) -> None:
        self.driver.get(urljoin(self.base_url, path.lstrip("/")))
        self.wait_for_page_ready()

    def wait_for_page_ready(self) -> None:
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def hover_services_then_bone_grafting(self) -> None:
        services = self.wait_for_visible(SERVICES_LINK)
        self.move_to(services)

        bone_grafting = self.wait_for_visible(BONE_GRAFTING_PARENT_LINK)
        self.move_to(bone_grafting)

    def hover_services_then_parent(self, parent_page: PageLink) -> None:
        services = self.wait_for_visible(SERVICES_LINK)
        self.move_to(services)

        parent_locator = nav_link_by_text_and_path(parent_page.label, parent_page.path)
        parent = self.wait_for_visible(parent_locator)
        self.move_to(parent)

    def hover_patient_center(self) -> None:
        patient_center = self.wait_for_visible(PATIENT_CENTER_LINK)
        self.move_to(patient_center)

    def hover_top_level_parent(self, parent_page: PageLink) -> None:
        parent_locator = nav_link_by_text_and_path(parent_page.label, parent_page.path)
        parent = self.wait_for_visible(parent_locator)
        self.move_to(parent)

    def click_header_submenu_page(self, page: PageLink) -> PageResult:
        self.hover_services_then_bone_grafting()
        return self._click_visible_submenu_item(page)

    def click_nested_submenu_page(self, parent_page: PageLink, page: PageLink) -> PageResult:
        self.hover_services_then_parent(parent_page)
        return self._click_visible_submenu_item(page)

    def click_top_level_submenu_page(self, parent_page: PageLink, page: PageLink) -> PageResult:
        self.hover_top_level_parent(parent_page)
        return self._click_visible_submenu_item(page)

    def click_patient_center_submenu_page(self, page: PageLink) -> PageResult:
        self.hover_patient_center()
        return self._click_visible_submenu_item(page)

    def _click_visible_submenu_item(self, page: PageLink) -> PageResult:
        submenu_locator = nav_link_by_text_and_path(page.label, page.path)
        submenu_item = self.wait_for_clickable(submenu_locator)
        self.move_to(submenu_item)
        submenu_item.click()

        self.wait.until(lambda d: page.expected_path in urlparse(d.current_url).path)
        self.wait_for_page_ready()

        current_url = self.driver.current_url
        title = self.driver.title.strip()
        h1 = self.get_first_h1()
        passed = self.current_path_matches(page.expected_path)

        return PageResult(
            label=page.label,
            expected_path=page.expected_path,
            current_url=current_url,
            title=title,
            h1=h1,
            passed=passed,
        )

    def validate_header_submenu_pages(self, parent_path: str, pages: list[PageLink]) -> list[PageResult]:
        results: list[PageResult] = []
        for page in pages:
            self.open_path(parent_path)
            result = self.click_header_submenu_page(page)
            results.append(result)
        return results

    def validate_nested_header_submenu_pages(self, parent_page: PageLink, pages: list[PageLink]) -> list[PageResult]:
        results: list[PageResult] = []
        for page in pages:
            self.open_path(parent_page.path)
            result = self.click_nested_submenu_page(parent_page, page)
            results.append(result)
        return results

    def validate_top_level_submenu_pages(self, parent_page: PageLink, pages: list[PageLink]) -> list[PageResult]:
        results: list[PageResult] = []
        for page in pages:
            self.open_path(parent_page.path)
            result = self.click_top_level_submenu_page(parent_page, page)
            results.append(result)
        return results

    def wait_for_visible(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def move_to(self, element: WebElement) -> None:
        ActionChains(self.driver).move_to_element(element).pause(0.25).perform()
        sleep(0.1)

    def current_path_matches(self, expected_path: str) -> bool:
        actual_path = urlparse(self.driver.current_url).path
        normalized_actual = actual_path if actual_path.endswith("/") else f"{actual_path}/"
        normalized_expected = expected_path if expected_path.endswith("/") else f"{expected_path}/"
        return normalized_actual == normalized_expected

    def get_first_h1(self) -> str:
        try:
            h1 = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
            return h1.text.strip()
        except TimeoutException:
            return ""


ServicesMenuNavigator = BoneGraftingMenuNavigator
