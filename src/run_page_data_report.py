from __future__ import annotations

from .config import get_page_details


def main() -> int:
    details = get_page_details()
    for key, page in details.items():
        print(f"\n{page['label']} ({key})")
        print(f"  path:      {page['path']}")
        print(f"  page id:   {page.get('page_id', '')}")
        print(f"  title:     {page.get('title', '')}")
        print(f"  canonical: {page.get('canonical', '')}")
        print(f"  h1:        {page.get('main_h1', '')}")
        print(f"  h2:        {page.get('hero_h2', '')}")
        if page.get('faq_items'):
            print("  FAQs:")
            for item in page['faq_items']:
                print(f"    - {item['question']}")
        elif page.get('faq_questions'):
            print("  FAQs:")
            for question in page['faq_questions']:
                print(f"    - {question}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
