from __future__ import annotations

from .config import (
    get_base_url,
    get_facial_birth_deformities_parent_page,
    get_facial_birth_deformities_submenu_pages,
    get_header_submenu_pages,
    get_oral_maxillofacial_parent_page,
    get_oral_maxillofacial_submenu_pages,
    get_parent_page,
    get_related_bone_grafting_links,
    get_related_oral_maxillofacial_links,
    get_service_menu_pages,
)
from .driver_factory import create_chrome_driver
from .menu_navigator import ServicesMenuNavigator


def print_links(title: str, pages) -> None:
    print(title)
    for page in pages:
        suffix = f" ({page.source})" if page.source else ""
        print(f"  - {page.label}: {page.path}{suffix}")


def main() -> int:
    base_url = get_base_url()
    bone_parent = get_parent_page()
    bone_pages = get_header_submenu_pages()
    oral_parent = get_oral_maxillofacial_parent_page()
    oral_pages = get_oral_maxillofacial_submenu_pages()
    facial_parent = get_facial_birth_deformities_parent_page()
    facial_pages = get_facial_birth_deformities_submenu_pages()

    print("Target site:", base_url)
    print_links("Services menu pages:", get_service_menu_pages())
    print_links("Bone Grafting submenu pages:", bone_pages)
    print_links("Oral & Maxillofacial submenu pages:", oral_pages)
    print_links("Facial Birth Deformities submenu pages:", facial_pages)

    related_bone = get_related_bone_grafting_links()
    if related_bone:
        print_links("Related Bone Grafting links included in project data:", related_bone)

    related_oral = get_related_oral_maxillofacial_links()
    if related_oral:
        print_links("Related Oral & Maxillofacial footer links included in project data:", related_oral)

    driver = create_chrome_driver()
    try:
        navigator = ServicesMenuNavigator(driver, base_url)
        results = []
        results.extend(navigator.validate_header_submenu_pages(bone_parent.path, bone_pages))
        results.extend(navigator.validate_nested_header_submenu_pages(oral_parent, oral_pages))
        results.extend(navigator.validate_nested_header_submenu_pages(facial_parent, facial_pages))

        print("\nResults:")
        all_passed = True
        for result in results:
            status = "PASS" if result.passed else "FAIL"
            all_passed = all_passed and result.passed
            print(f"[{status}] {result.label}")
            print(f"  expected path: {result.expected_path}")
            print(f"  current url:    {result.current_url}")
            print(f"  title:          {result.title}")
            print(f"  h1:             {result.h1}")

        return 0 if all_passed else 1
    finally:
        driver.quit()


if __name__ == "__main__":
    raise SystemExit(main())
