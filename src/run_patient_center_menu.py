from __future__ import annotations

from .config import get_base_url, get_patient_center_parent_page, get_patient_center_submenu_pages
from .driver_factory import create_chrome_driver
from .menu_navigator import ServicesMenuNavigator


def main() -> int:
    base_url = get_base_url()
    parent_page = get_patient_center_parent_page()
    pages = get_patient_center_submenu_pages()

    print("Target site:", base_url)
    print("Parent page:", parent_page.label, parent_page.path)
    print("Patient Center submenu pages:")
    for page in pages:
        suffix = f" ({page.source})" if page.source else ""
        print(f"  - {page.label}: {page.path}{suffix}")

    driver = create_chrome_driver()
    try:
        navigator = ServicesMenuNavigator(driver, base_url)
        results = navigator.validate_top_level_submenu_pages(parent_page, pages)

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
