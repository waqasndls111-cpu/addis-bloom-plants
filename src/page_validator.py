from __future__ import annotations

from urllib.parse import urljoin, urlparse, parse_qs

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .selectors import xpath_literal


class PageContentValidator:
    """Small helper for validating page-level content extracted from supplied HTML."""

    def __init__(self, driver: WebDriver, base_url: str, timeout: int = 20) -> None:
        self.driver = driver
        self.base_url = base_url.rstrip("/") + "/"
        self.wait = WebDriverWait(driver, timeout)

    def open_path(self, path: str) -> None:
        self.driver.get(urljoin(self.base_url, path.lstrip("/")))
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def visible_text_exists(self, text: str) -> bool:
        locator = (By.XPATH, f"//*[normalize-space()={xpath_literal(text)}]")
        self.wait.until(EC.visibility_of_element_located(locator))
        return True

    def text_exists_in_dom(self, text: str) -> bool:
        locator = (By.XPATH, f"//*[normalize-space()={xpath_literal(text)}]")
        self.wait.until(EC.presence_of_element_located(locator))
        return True

    def element_exists_by_xpath(self, xpath: str) -> bool:
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return True

    @staticmethod
    def _value(details: dict, simple_key: str, nested_path: tuple[str, ...]) -> str:
        if simple_key in details:
            return str(details[simple_key])
        value = details
        for key in nested_path:
            value = value[key]
        return str(value)

    @staticmethod
    def _faqs(details: dict) -> list[dict]:
        return list(details.get("faq_items") or details.get("faqs") or [])

    @staticmethod
    def _youtube_id(url: str) -> str:
        parsed = urlparse(url)
        if parsed.netloc.endswith("youtu.be"):
            return parsed.path.strip("/")
        if "youtube" in parsed.netloc:
            query_id = parse_qs(parsed.query).get("v", [""])[0]
            if query_id:
                return query_id
            parts = [part for part in parsed.path.split("/") if part]
            if parts:
                return parts[-1]
        return url.rsplit("/", 1)[-1].split("?", 1)[0]

    @staticmethod
    def _cta_heading(details: dict) -> str | None:
        if "cta" in details:
            return details["cta"].get("heading")
        for section in details.get("content_sections", []):
            heading = section.get("heading", "")
            if heading.startswith("How Can I Find Out More"):
                return heading
        return None

    def _validate_canonical(self, details: dict, errors: list[str]) -> None:
        canonical = details.get("canonical")
        if not canonical:
            return
        try:
            element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "link[rel='canonical']")))
            if element.get_attribute("href") != canonical:
                errors.append(f"Canonical mismatch: expected {canonical!r}, got {element.get_attribute('href')!r}")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"Missing canonical link: {canonical!r}; {exc}")

    def _validate_video_or_image(self, details: dict, errors: list[str]) -> None:
        video = details.get("hero_video") or details.get("hero", {}).get("video", {})
        if video:
            video_url = video.get("url") or video.get("youtube_url", "")
            video_id = self._youtube_id(video_url)
            overlay_image = video.get("overlay_image", "")
            try:
                video_xpath = (
                    f"//main//*[contains(@data-settings,{xpath_literal(video_id)})"
                    f" or contains(@data-lazy-load,{xpath_literal(video_id)})"
                    f" or contains(@src,{xpath_literal(video_id)})"
                    f" or contains(@data-bg,{xpath_literal(overlay_image)})"
                    f" or contains(@style,{xpath_literal(overlay_image)})]"
                )
                self.element_exists_by_xpath(video_xpath)
            except Exception as exc:  # noqa: BLE001
                errors.append(f"Missing video data for {video_id!r}; {exc}")
            return

        image = details.get("hero_image") or details.get("primary_image") or {}
        image_url = image.get("url", "")
        if not image_url:
            return
        try:
            image_xpath = (
                f"//main//img[contains(@src,{xpath_literal(image_url)}) "
                f"or contains(@data-lazy-src,{xpath_literal(image_url)}) "
                f"or contains(@srcset,{xpath_literal(image_url)}) "
                f"or contains(@data-lazy-srcset,{xpath_literal(image_url)})]"
            )
            self.element_exists_by_xpath(image_xpath)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"Missing page image: {image_url!r}; {exc}")

    def validate_page_content(self, details: dict) -> list[str]:
        """Return validation errors. Empty list means the live page matched extracted HTML data."""
        errors: list[str] = []
        self.open_path(details["path"])

        expected_title = self._value(details, "title", ("seo", "title"))
        if self.driver.title.strip() != expected_title:
            errors.append(f"Title mismatch: expected {expected_title!r}, got {self.driver.title!r}")

        for text in [
            self._value(details, "main_h1", ("hero", "h1")),
            self._value(details, "hero_h2", ("hero", "h2")),
        ]:
            try:
                self.visible_text_exists(text)
            except Exception as exc:  # noqa: BLE001
                errors.append(f"Missing visible text: {text!r}; {exc}")

        for section in details.get("content_sections", []):
            heading = section.get("heading")
            if not heading:
                continue
            try:
                self.text_exists_in_dom(heading)
            except Exception as exc:  # noqa: BLE001
                errors.append(f"Missing content heading: {heading!r}; {exc}")

        for faq in self._faqs(details):
            try:
                self.text_exists_in_dom(faq["question"])
            except Exception as exc:  # noqa: BLE001
                errors.append(f"Missing FAQ heading: {faq['question']!r}; {exc}")

        self._validate_video_or_image(details, errors)
        self._validate_canonical(details, errors)

        cta_heading = self._cta_heading(details)
        if cta_heading:
            try:
                self.text_exists_in_dom(cta_heading)
            except Exception as exc:  # noqa: BLE001
                errors.append(f"Missing CTA heading: {cta_heading!r}; {exc}")

        return errors

    def validate_ridge_augmentation_page(self, details: dict) -> list[str]:
        return self.validate_page_content(details)

    def validate_sinus_lift_page(self, details: dict) -> list[str]:
        return self.validate_page_content(details)

    def validate_platelet_rich_fibrin_page(self, details: dict) -> list[str]:
        return self.validate_page_content(details)
