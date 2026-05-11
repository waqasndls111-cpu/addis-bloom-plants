from __future__ import annotations

from selenium.webdriver.common.by import By


def xpath_literal(value: str) -> str:
    """Return a safe XPath string literal for any label text."""
    if "'" not in value:
        return f"'{value}'"
    if '"' not in value:
        return f'"{value}"'
    parts = value.split("'")
    return "concat(" + ', "\'", '.join(f"'{part}'" for part in parts) + ")"


# Use only the real desktop header nav. Elementor creates duplicate nav markup for
# mobile dropdowns and sticky spacers, so we explicitly exclude the spacer copy.
DESKTOP_HEADER_NAV_XPATH = (
    "//header//nav[contains(@class,'elementor-nav-menu--main') "
    "and not(ancestor::*[contains(@class,'elementor-sticky__spacer')])]"
)

MAIN_CONTENT_XPATH = "//main[@id='content']"


def nav_link_by_text(label: str) -> tuple[str, str]:
    literal = xpath_literal(label)
    return By.XPATH, f"{DESKTOP_HEADER_NAV_XPATH}//a[normalize-space()={literal}]"


def nav_link_by_text_and_path(label: str, path: str) -> tuple[str, str]:
    literal = xpath_literal(label)
    return By.XPATH, (
        f"{DESKTOP_HEADER_NAV_XPATH}//a[normalize-space()={literal} "
        f"and contains(@href,{xpath_literal(path)})]"
    )


def nav_link_by_path(path: str) -> tuple[str, str]:
    return By.XPATH, f"{DESKTOP_HEADER_NAV_XPATH}//a[contains(@href,{xpath_literal(path)})]"


def main_heading_by_text(text: str) -> tuple[str, str]:
    return By.XPATH, f"{MAIN_CONTENT_XPATH}//h1[normalize-space()={xpath_literal(text)}]"


def content_heading_by_text(text: str) -> tuple[str, str]:
    return By.XPATH, f"{MAIN_CONTENT_XPATH}//h2[normalize-space()={xpath_literal(text)}]"


def faq_question_by_text(text: str) -> tuple[str, str]:
    return By.XPATH, (
        f"{MAIN_CONTENT_XPATH}//*[contains(concat(' ',normalize-space(@class),' '),' jet-toggle__label-text ') "
        f"and normalize-space()={xpath_literal(text)}]"
    )


def image_by_url(url: str) -> tuple[str, str]:
    literal = xpath_literal(url)
    return By.XPATH, (
        f"{MAIN_CONTENT_XPATH}//img[contains(@src,{literal}) "
        f"or contains(@data-lazy-src,{literal}) "
        f"or contains(@srcset,{literal}) "
        f"or contains(@data-lazy-srcset,{literal})]"
    )


def canonical_link() -> tuple[str, str]:
    return By.CSS_SELECTOR, "link[rel='canonical']"


def video_play_button() -> tuple[str, str]:
    return By.CSS_SELECTOR, ".elementor-custom-embed-play[aria-label='Play Video']"


SERVICES_LINK = nav_link_by_text("Services")
BONE_GRAFTING_PARENT_LINK = nav_link_by_text_and_path("Bone Grafting", "/bone-grafting/")
ORAL_MAXILLOFACIAL_PARENT_LINK = nav_link_by_text_and_path(
    "Oral & Maxillofacial Surgeries", "/oral-and-maxillofacial/"
)

PATIENT_CENTER_LINK = nav_link_by_text_and_path("Patient Center", "/patient-center/")
