from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
from typing import Any


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT_DIR / "data" / "bone_grafting_pages.json"
RIDGE_AUGMENTATION_FILE = ROOT_DIR / "data" / "ridge_augmentation_page.json"
SINUS_LIFT_FILE = ROOT_DIR / "data" / "sinus_lift_page.json"
PLATELET_RICH_FIBRIN_FILE = ROOT_DIR / "data" / "platelet_rich_fibrin_prf_page.json"
ORAL_MAXILLOFACIAL_FILE = ROOT_DIR / "data" / "oral_and_maxillofacial_page.json"
TEETH_EXTRACTIONS_FILE = ROOT_DIR / "data" / "teeth_extractions_page.json"
WISDOM_TEETH_REMOVAL_FILE = ROOT_DIR / "data" / "wisdom_teeth_removal_page.json"
IMPACTED_CANINES_FILE = ROOT_DIR / "data" / "impacted_canines_page.json"
ORTHOGNATHIC_JAW_SURGERY_FILE = ROOT_DIR / "data" / "orthognathic_jaw_surgery_page.json"
FACIAL_BIRTH_DEFORMITIES_FILE = ROOT_DIR / "data" / "facial_birth_deformities_page.json"
CLEFT_LIP_PALATE_SURGERY_FILE = ROOT_DIR / "data" / "cleft_lip_palate_surgery_page.json"
HEMIFACIAL_MICROSOMIA_FILE = ROOT_DIR / "data" / "hemifacial_microsomia_page.json"
TREACHER_COLLINS_SYNDROME_FILE = ROOT_DIR / "data" / "treacher_collins_syndrome_page.json"
PIERRE_ROBIN_SEQUENCE_FILE = ROOT_DIR / "data" / "pierre_robin_sequence_page.json"
NEONATAL_DISTRACTION_FILE = ROOT_DIR / "data" / "neonatal_distraction_page.json"
PATIENT_CENTER_FILE = ROOT_DIR / "data" / "patient_center_page.json"
PATIENT_FORMS_FILE = ROOT_DIR / "data" / "patient_forms_page.json"
PATIENT_TESTIMONIALS_FILE = ROOT_DIR / "data" / "patient_testimonials_page.json"
MEDIA_FILE = ROOT_DIR / "data" / "media_page.json"


@dataclass(frozen=True)
class PageLink:
    label: str
    path: str
    source: str = ""

    @property
    def expected_path(self) -> str:
        # Normalize only the URL path for navigation assertions. Custom menu
        # items can include anchors or query strings, such as #consent.
        path = self.path.split("#", 1)[0].split("?", 1)[0]
        return path if path.endswith("/") else f"{path}/"


def load_project_data() -> dict[str, Any]:
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_page_file(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def _page_links(key: str) -> list[PageLink]:
    return [PageLink(**item) for item in load_project_data().get(key, [])]


def get_base_url() -> str:
    return load_project_data()["base_url"].rstrip("/")


def get_parent_page() -> PageLink:
    data = load_project_data()["parent_page"]
    return PageLink(**data)


def get_header_submenu_pages() -> list[PageLink]:
    return _page_links("header_submenu_pages")


def get_related_bone_grafting_links() -> list[PageLink]:
    return _page_links("related_bone_grafting_links")


def get_service_menu_pages() -> list[PageLink]:
    return _page_links("service_menu_pages")


def get_oral_maxillofacial_parent_page() -> PageLink:
    data = load_project_data()["oral_maxillofacial_parent_page"]
    return PageLink(**data)


def get_oral_maxillofacial_submenu_pages() -> list[PageLink]:
    return _page_links("oral_maxillofacial_header_submenu_pages")


def get_related_oral_maxillofacial_links() -> list[PageLink]:
    return _page_links("related_oral_maxillofacial_links")


def get_facial_birth_deformities_parent_page() -> PageLink:
    data = load_project_data()["facial_birth_deformities_parent_page"]
    return PageLink(**data)


def get_facial_birth_deformities_submenu_pages() -> list[PageLink]:
    return _page_links("facial_birth_deformities_header_submenu_pages")


def get_patient_center_parent_page() -> PageLink:
    data = load_project_data()["patient_center_parent_page"]
    return PageLink(**data)


def get_patient_center_submenu_pages() -> list[PageLink]:
    return _page_links("patient_center_header_submenu_pages")


def get_patient_center_card_pages() -> list[PageLink]:
    return _page_links("patient_center_card_pages")


def get_page_details(page_key: str | None = None) -> dict[str, Any]:
    """Return structured page details extracted from the provided outer HTML."""
    details = load_project_data().get("page_details", {})
    if page_key is None:
        return details
    return details[page_key]


def get_ridge_augmentation_details() -> dict[str, Any]:
    return load_page_file(RIDGE_AUGMENTATION_FILE)


def get_sinus_lift_details() -> dict[str, Any]:
    return load_page_file(SINUS_LIFT_FILE)


def get_platelet_rich_fibrin_details() -> dict[str, Any]:
    return load_page_file(PLATELET_RICH_FIBRIN_FILE)


def get_oral_and_maxillofacial_details() -> dict[str, Any]:
    return load_page_file(ORAL_MAXILLOFACIAL_FILE)


def get_teeth_extractions_details() -> dict[str, Any]:
    return load_page_file(TEETH_EXTRACTIONS_FILE)


def get_wisdom_teeth_removal_details() -> dict[str, Any]:
    return load_page_file(WISDOM_TEETH_REMOVAL_FILE)


def get_impacted_canines_details() -> dict[str, Any]:
    return load_page_file(IMPACTED_CANINES_FILE)


def get_orthognathic_jaw_surgery_details() -> dict[str, Any]:
    return load_page_file(ORTHOGNATHIC_JAW_SURGERY_FILE)


def get_facial_birth_deformities_details() -> dict[str, Any]:
    return load_page_file(FACIAL_BIRTH_DEFORMITIES_FILE)


def get_cleft_lip_palate_surgery_details() -> dict[str, Any]:
    return load_page_file(CLEFT_LIP_PALATE_SURGERY_FILE)


def get_hemifacial_microsomia_details() -> dict[str, Any]:
    return load_page_file(HEMIFACIAL_MICROSOMIA_FILE)


def get_treacher_collins_syndrome_details() -> dict[str, Any]:
    return load_page_file(TREACHER_COLLINS_SYNDROME_FILE)


def get_pierre_robin_sequence_details() -> dict[str, Any]:
    return load_page_file(PIERRE_ROBIN_SEQUENCE_FILE)


def get_neonatal_distraction_details() -> dict[str, Any]:
    return load_page_file(NEONATAL_DISTRACTION_FILE)


def get_patient_center_details() -> dict[str, Any]:
    return load_page_file(PATIENT_CENTER_FILE)


def get_patient_forms_details() -> dict[str, Any]:
    return load_page_file(PATIENT_FORMS_FILE)


def get_patient_testimonials_details() -> dict[str, Any]:
    return load_page_file(PATIENT_TESTIMONIALS_FILE)


def get_media_details() -> dict[str, Any]:
    return load_page_file(MEDIA_FILE)

