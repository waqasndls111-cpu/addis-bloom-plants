from __future__ import annotations

from .config import get_base_url, get_header_submenu_pages, get_parent_page, get_related_bone_grafting_links
from .driver_factory import create_chrome_driver
from .menu_navigator import BoneGraftingMenuNavigator


def main() -> int:
    base_url = get_base_url()
    parent_page = get_parent_page()
    header_pages = get_header_submenu_pages()
    related_pages = get_related_bone_grafting_links()

    print("Target site:", base_url)
    print("Parent page:", parent_page.label, parent_page.path)
    print("Header submenu pages:")
    for page in header_pages:
        print(f"  - {page.label}: {page.path}")

    if related_pages:
        print("Related Bone Grafting links included in project data:")
        for page in related_pages:
            print(f"  - {page.label}: {page.path} ({page.source})")

    driver = create_chrome_driver()
    try:
        navigator = BoneGraftingMenuNavigator(driver, base_url)
        results = navigator.validate_header_submenu_pages(parent_page.path, header_pages)

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
