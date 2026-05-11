# Staten Island Oral Surgery - Services Menu Automation

This project contains the Selenium setup and structured page data for navigating and validating Services menu branches plus the Patient Center menu branch on `statenislandoralsurgery.us`.

It now includes the previously completed **Bone Grafting** branch plus the supplied **Oral & Maxillofacial Surgeries**, **Facial Birth Deformities**, and **Patient Center** branches, with detailed page data extracted from the outer HTML you provided for:

- Oral & Maxillofacial Surgeries
- Teeth Extractions
- Wisdom Teeth Removal
- Impacted Canines
- Orthognathic Jaw Surgery
- Facial Birth Deformities
- Cleft Lip & Palate Surgery
- Hemifacial Microsomia
- Treacher Collins Syndrome
- Pierre Robin Sequence
- Neonatal Distraction
- Patient Center
- Patient Forms
- Patient Testimonials
- Media

## Included Services menu pages

| Label | URL path | Status in project |
|---|---:|---|
| Dental Implants | `/dental-implants/` | Services submenu link |
| Teeth in a Day (All-On-X) | `/teeth-in-a-day-all-on-x/` | Services submenu link |
| Bone Grafting | `/bone-grafting/` | Services submenu parent |
| Oral & Maxillofacial Surgeries | `/oral-and-maxillofacial/` | Services submenu parent with detailed page data added |
| Facial Birth Deformities | `/facial-birth-deformities/` | Services submenu parent with detailed page data added |
| Anesthesia Options | `/anesthesia-options/` | Services submenu link |

## Bone Grafting branch

| Label | URL path | Status in project |
|---|---:|---|
| Bone Grafting FAQs | `/bone-grafting-faqs/` | Header hover submenu page |
| Ridge Augmentation | `/ridge-augmentation/` | Header hover submenu page with detailed page data added |
| Sinus Lift | `/sinus-lift/` | Header hover submenu page with detailed page data added |
| Platelet Rich Fibrin (PRF) | `/platelet-rich-fibrin-prf/` | Header hover submenu page with detailed page data added |
| BMP Infuse Bone Graft | `/bmp-infuse-bone-graft/` | Footer/body related link only |

## Oral & Maxillofacial branch

| Label | URL path | Status in project |
|---|---:|---|
| Oral & Maxillofacial Surgeries | `/oral-and-maxillofacial/` | Parent page with detailed page data added |
| Teeth Extractions | `/teeth-extractions/` | Header hover submenu page with detailed page data added |
| Wisdom Teeth Removal | `/wisdom-teeth-removal/` | Header hover submenu page with detailed page data added |
| Impacted Canines | `/impacted-canines/` | Header hover submenu page with detailed page data added |
| Orthognathic Jaw Surgery | `/orthognathic-jaw-surgery/` | Header hover submenu page with detailed page data added |

Additional Oral & Maxillofacial footer links recorded in project data:

| Label | URL path |
|---|---:|
| Frenectomy | `/frenectomy/` |
| TMJ Disorders & Surgery | `/tmj-disorders-surgery/` |
| Facial Trauma | `/facial-trauma/` |
| Oral Pathology | `/oral-pathology/` |
| MOHS Reconstruction | `/mohs-reconstruction/` |
| Anesthesia Options | `/anesthesia-options/` |


## Patient Center branch

| Label | URL path | Status in project |
|---|---:|---|
| Patient Center | `/patient-center/` | Top-level menu parent with detailed page data added |
| First Visit | `/first-visit/` | Patient Center submenu link |
| Patient Forms | `/patient-forms/` | Patient Center submenu page with detailed page data added |
| Surgical Instructions | `/surgical-instructions/` | Patient Center submenu link |
| Insurance & Financing | `/insurance-and-financing/` | Patient Center submenu link |
| Patient Testimonials | `/testimonials/` | Patient Center submenu page with detailed page data added |
| Wisdom Tooth Consent | `/our-services/oral-and-maxillofacial/wisdom-teeth-removal/#consent` | Patient Center submenu custom anchor link |
| Pay Your Bill | `/pay-your-bill/` | Patient Center submenu link |
| Media | `/media/` | Patient Center submenu page with detailed page data added |

## Detailed page data added

Structured data is stored in:

```text
data/bone_grafting_pages.json
data/ridge_augmentation_page.json
data/ridge_augmentation_faqs.csv
data/sinus_lift_page.json
data/sinus_lift_faqs.csv
data/platelet_rich_fibrin_prf_page.json
data/platelet_rich_fibrin_prf_faqs.csv
data/oral_and_maxillofacial_page.json
data/teeth_extractions_page.json
data/teeth_extractions_faqs.csv
data/wisdom_teeth_removal_page.json
data/wisdom_teeth_removal_faqs.csv
data/impacted_canines_page.json
data/impacted_canines_faqs.csv
data/orthognathic_jaw_surgery_page.json
data/orthognathic_jaw_surgery_faqs.csv
data/facial_birth_deformities_page.json
data/cleft_lip_palate_surgery_page.json
data/cleft_lip_palate_surgery_faqs.csv
data/hemifacial_microsomia_page.json
data/hemifacial_microsomia_faqs.csv
data/treacher_collins_syndrome_page.json
data/treacher_collins_syndrome_faqs.csv
data/pierre_robin_sequence_page.json
data/pierre_robin_sequence_faqs.csv
data/neonatal_distraction_page.json
data/neonatal_distraction_faqs.csv
data/patient_forms_links.csv
data/patient_forms_page.json
data/patient_center_page.json
data/patient_testimonials_page.json
data/patient_testimonials_items.csv
data/media_page.json
data/media_videos.csv
data/media_magazines.csv
data/media_news_items.csv
```

It includes, where present in the supplied HTML:

- WordPress page IDs
- titles and canonical URLs
- SEO meta descriptions
- Open Graph image URLs and alt text
- published and modified timestamps
- H1 and hero H2 text
- hero intro copy
- phone CTA text and callback CTA links
- YouTube video URL and overlay image for Ridge Augmentation, Sinus Lift, Wisdom Teeth Removal, Orthognathic Jaw Surgery, Cleft Lip & Palate Surgery, and Pierre Robin Sequence
- primary/secondary image URLs, dimensions, and alt text
- Lottie animation URL for Teeth Extractions, Orthognathic Jaw Surgery, Cleft Lip & Palate Surgery, Hemifacial Microsomia, Treacher Collins Syndrome, Pierre Robin Sequence, and Neonatal Distraction
- body content sections
- FAQ questions and answers
- current-menu classes found in the header
- footer/service related links found on the pages
- Patient Testimonials review cards, reviewer names, and Google/Yelp outbound links
- Media page video cards, magazine PDF links, news item, and commercial section

Readable summaries are included in:

```text
docs/HTML_FINDINGS.md
docs/RIDGE_AUGMENTATION_FINDINGS.md
docs/RIDGE_AUGMENTATION_HTML_FINDINGS.md
docs/SINUS_LIFT_FINDINGS.md
docs/SINUS_LIFT_HTML_FINDINGS.md
docs/PLATELET_RICH_FIBRIN_FINDINGS.md
docs/PLATELET_RICH_FIBRIN_HTML_FINDINGS.md
docs/ORAL_MAXILLOFACIAL_FINDINGS.md
docs/ORAL_MAXILLOFACIAL_HTML_FINDINGS.md
docs/TEETH_EXTRACTIONS_FINDINGS.md
docs/TEETH_EXTRACTIONS_HTML_FINDINGS.md
docs/WISDOM_TEETH_REMOVAL_FINDINGS.md
docs/WISDOM_TEETH_REMOVAL_HTML_FINDINGS.md
docs/IMPACTED_CANINES_FINDINGS.md
docs/IMPACTED_CANINES_HTML_FINDINGS.md
docs/ORTHOGNATHIC_JAW_SURGERY_FINDINGS.md
docs/ORTHOGNATHIC_JAW_SURGERY_HTML_FINDINGS.md
docs/FACIAL_BIRTH_DEFORMITIES_FINDINGS.md
docs/FACIAL_BIRTH_DEFORMITIES_HTML_FINDINGS.md
docs/CLEFT_LIP_PALATE_SURGERY_FINDINGS.md
docs/CLEFT_LIP_PALATE_SURGERY_HTML_FINDINGS.md
docs/HEMIFACIAL_MICROSOMIA_FINDINGS.md
docs/HEMIFACIAL_MICROSOMIA_HTML_FINDINGS.md
docs/TREACHER_COLLINS_SYNDROME_FINDINGS.md
docs/TREACHER_COLLINS_SYNDROME_HTML_FINDINGS.md
docs/PIERRE_ROBIN_SEQUENCE_FINDINGS.md
docs/PIERRE_ROBIN_SEQUENCE_HTML_FINDINGS.md
docs/NEONATAL_DISTRACTION_FINDINGS.md
docs/NEONATAL_DISTRACTION_HTML_FINDINGS.md
docs/PATIENT_FORMS_HTML_FINDINGS.md
docs/PATIENT_FORMS_FINDINGS.md
docs/PATIENT_CENTER_HTML_FINDINGS.md
docs/PATIENT_CENTER_FINDINGS.md
docs/PATIENT_TESTIMONIALS_HTML_FINDINGS.md
docs/PATIENT_TESTIMONIALS_FINDINGS.md
docs/MEDIA_HTML_FINDINGS.md
docs/MEDIA_FINDINGS.md
```

Short main-content snippets are included in:

```text
source_html_snippets/ridge_augmentation_main_content.html
source_html_snippets/sinus_lift_main_content.html
source_html_snippets/platelet_rich_fibrin_prf_main_content.html
source_html_snippets/oral_and_maxillofacial_main_content.html
source_html_snippets/teeth_extractions_main_content.html
source_html_snippets/wisdom_teeth_removal_main_content.html
source_html_snippets/impacted_canines_main_content.html
source_html_snippets/orthognathic_jaw_surgery_main_content.html
source_html_snippets/facial_birth_deformities_main_content.html
source_html_snippets/cleft_lip_palate_surgery_main_content.html
source_html_snippets/hemifacial_microsomia_main_content.html
source_html_snippets/treacher_collins_syndrome_main_content.html
source_html_snippets/pierre_robin_sequence_main_content.html
source_html_snippets/neonatal_distraction_main_content.html
source_html_snippets/patient_forms_main_content.html
source_html_snippets/patient_center_main_content.html
source_html_snippets/patient_testimonials_main_content.html
source_html_snippets/media_main_content.html
```

Screenshot references are included in:

```text
reference/bone_grafting_hover_menu.png
reference/oral_maxillofacial_hover_menu.png
reference/facial_birth_deformities_hover_menu.png
reference/patient_center_hover_menu.png
```

## Why these locators are used

The page generates dynamic SmartMenus IDs such as `sm-177846...`. Those IDs change between sessions, so the automation does **not** rely on them.

Instead, the project uses stable values:

- link text, such as `Oral & Maxillofacial Surgeries` and `Teeth Extractions`
- href path, such as `/oral-and-maxillofacial/` and `/teeth-extractions/`
- the visible desktop header nav only
- exclusion of Elementor sticky spacer duplicate nav
- page H1/H2 text, FAQ question text, canonical link, video overlay data, and durable image URLs

## Install

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Selenium 4 can usually manage the browser driver automatically. Chrome is the default browser in this project.

## Run the navigation scripts

Bone Grafting only:

```bash
python -m src.run_bone_grafting_menu
```

All currently tracked Services menu branches:

```bash
python -m src.run_services_menu
```


Patient Center menu:

```bash
python -m src.run_patient_center_menu
```

The Services menu script will:

1. open the parent page,
2. hover `Services`,
3. hover the branch parent, such as `Bone Grafting`, `Oral & Maxillofacial Surgeries`, or `Facial Birth Deformities`,
4. click each tracked inner submenu item,
5. confirm the browser lands on the expected URL path,
6. print the page title and H1.

## Run a structured page data report

```bash
python -m src.run_page_data_report
```

This prints the extracted title, canonical URL, H1, H2, and FAQ data that came from the provided outer HTML.

## Run pytest validation

Data-only checks can be run without opening a browser:

```bash
pytest -q -m "not live"
```

Full browser validation can be run when Chrome/network access is available:

```bash
pytest -q
```

The tests include:

- hover navigation validation for visible Bone Grafting submenu pages
- hover navigation validation for visible Oral & Maxillofacial submenu pages
- hover navigation validation for visible Facial Birth Deformities submenu pages
- hover navigation validation for visible Patient Center submenu pages
- project-data completeness validation for Ridge Augmentation, Sinus Lift, Platelet Rich Fibrin (PRF), Oral & Maxillofacial Surgeries, Teeth Extractions, Wisdom Teeth Removal, Impacted Canines, Orthognathic Jaw Surgery, Facial Birth Deformities, Cleft Lip & Palate Surgery, Hemifacial Microsomia, Treacher Collins Syndrome, Pierre Robin Sequence, and Neonatal Distraction
- live page content validation for titles, H1s, H2s, canonical links, video/image data, CTA headings, and FAQ question labels

## Headless mode

By default, the scripts run with a visible browser because hover menus are easier to debug visually. To run headless:

```bash
HEADLESS=1 python -m src.run_services_menu
HEADLESS=1 python -m src.run_patient_center_menu
HEADLESS=1 pytest -q
```

## Project structure

```text
staten_island_bone_grafting_project/
  README.md
  requirements.txt
  data/
    bone_grafting_pages.json
    menu_structure.csv
    ridge_augmentation_page.json
    ridge_augmentation_faqs.csv
    sinus_lift_page.json
    sinus_lift_faqs.csv
    platelet_rich_fibrin_prf_page.json
    platelet_rich_fibrin_prf_faqs.csv
    oral_and_maxillofacial_page.json
    teeth_extractions_page.json
    teeth_extractions_faqs.csv
    wisdom_teeth_removal_page.json
    wisdom_teeth_removal_faqs.csv
    impacted_canines_page.json
    impacted_canines_faqs.csv
    orthognathic_jaw_surgery_page.json
    orthognathic_jaw_surgery_faqs.csv
    facial_birth_deformities_page.json
    cleft_lip_palate_surgery_page.json
    cleft_lip_palate_surgery_faqs.csv
    hemifacial_microsomia_page.json
    hemifacial_microsomia_faqs.csv
    treacher_collins_syndrome_page.json
    treacher_collins_syndrome_faqs.csv
    pierre_robin_sequence_page.json
    pierre_robin_sequence_faqs.csv
    neonatal_distraction_page.json
    neonatal_distraction_faqs.csv
  docs/
    *_FINDINGS.md
    *_HTML_FINDINGS.md
    UPDATE_SUMMARY.md
  source_html_snippets/
    ridge_augmentation_main_content.html
    sinus_lift_main_content.html
    platelet_rich_fibrin_prf_main_content.html
    oral_and_maxillofacial_main_content.html
    teeth_extractions_main_content.html
    wisdom_teeth_removal_main_content.html
    impacted_canines_main_content.html
    orthognathic_jaw_surgery_main_content.html
    facial_birth_deformities_main_content.html
    cleft_lip_palate_surgery_main_content.html
    hemifacial_microsomia_main_content.html
    treacher_collins_syndrome_main_content.html
    pierre_robin_sequence_main_content.html
    neonatal_distraction_main_content.html
  reference/
    bone_grafting_hover_menu.png
    oral_maxillofacial_hover_menu.png
  src/
    __init__.py
    config.py
    driver_factory.py
    selectors.py
    menu_navigator.py
    run_bone_grafting_menu.py
    run_services_menu.py
    run_page_data_report.py
    page_validator.py
  tests/
    test_bone_grafting_menu.py
    test_ridge_augmentation_page.py
    test_sinus_lift_page.py
    test_platelet_rich_fibrin_page.py
    test_oral_maxillofacial_menu.py
    test_oral_and_maxillofacial_page.py
    test_teeth_extractions_page.py
    test_wisdom_teeth_removal_page.py
    test_impacted_canines_page.py
    test_orthognathic_jaw_surgery_page.py
    test_facial_birth_deformities_menu.py
    test_facial_birth_deformities_page.py
    test_cleft_lip_palate_surgery_page.py
    test_hemifacial_microsomia_page.py
    test_treacher_collins_syndrome_page.py
    test_pierre_robin_sequence_page.py
    test_neonatal_distraction_page.py
  pytest.ini
```


## Facial Birth Deformities branch update

This package now includes the first supplied Facial Birth Deformities pages:

| Label | URL path | Status in project |
|---|---:|---|
| Facial Birth Deformities | `/facial-birth-deformities/` | Parent page with detailed page data added |
| Cleft Lip & Palate Surgery | `/cleft-lip-palate-surgery/` | Header hover submenu page with detailed page data added |
| Hemifacial Microsomia | `/hemifacial-microsomia/` | Header hover submenu page with detailed page data added |
| Treacher Collins Syndrome | `/treacher-collins-syndrome/` | Header hover submenu page with detailed page data added |
| Pierre Robin Sequence | `/pierre-robin-sequence/` | Header hover submenu page with detailed page data added |
| Neonatal Distraction | `/neonatal-distraction/` | Header hover submenu page with detailed page data added |

New structured data files:

```text
data/facial_birth_deformities_page.json
data/cleft_lip_palate_surgery_page.json
data/hemifacial_microsomia_page.json
data/hemifacial_microsomia_faqs.csv
data/treacher_collins_syndrome_page.json
data/treacher_collins_syndrome_faqs.csv
data/pierre_robin_sequence_page.json
data/pierre_robin_sequence_faqs.csv
data/neonatal_distraction_page.json
data/neonatal_distraction_faqs.csv
data/patient_forms_links.csv
data/patient_forms_page.json
data/patient_center_page.json
data/patient_testimonials_page.json
data/patient_testimonials_items.csv
data/media_page.json
data/media_videos.csv
data/media_magazines.csv
data/media_news_items.csv
data/cleft_lip_palate_surgery_faqs.csv
```

New docs and snippets:

```text
docs/FACIAL_BIRTH_DEFORMITIES_FINDINGS.md
docs/FACIAL_BIRTH_DEFORMITIES_HTML_FINDINGS.md
docs/CLEFT_LIP_PALATE_SURGERY_FINDINGS.md
docs/CLEFT_LIP_PALATE_SURGERY_HTML_FINDINGS.md
docs/HEMIFACIAL_MICROSOMIA_FINDINGS.md
docs/HEMIFACIAL_MICROSOMIA_HTML_FINDINGS.md
docs/TREACHER_COLLINS_SYNDROME_FINDINGS.md
docs/TREACHER_COLLINS_SYNDROME_HTML_FINDINGS.md
docs/PIERRE_ROBIN_SEQUENCE_FINDINGS.md
docs/PIERRE_ROBIN_SEQUENCE_HTML_FINDINGS.md
docs/NEONATAL_DISTRACTION_FINDINGS.md
docs/NEONATAL_DISTRACTION_HTML_FINDINGS.md
docs/PATIENT_FORMS_HTML_FINDINGS.md
docs/PATIENT_FORMS_FINDINGS.md
docs/PATIENT_CENTER_HTML_FINDINGS.md
docs/PATIENT_CENTER_FINDINGS.md
docs/PATIENT_TESTIMONIALS_HTML_FINDINGS.md
docs/PATIENT_TESTIMONIALS_FINDINGS.md
docs/MEDIA_HTML_FINDINGS.md
docs/MEDIA_FINDINGS.md
source_html_snippets/facial_birth_deformities_main_content.html
source_html_snippets/cleft_lip_palate_surgery_main_content.html
source_html_snippets/hemifacial_microsomia_main_content.html
source_html_snippets/treacher_collins_syndrome_main_content.html
source_html_snippets/pierre_robin_sequence_main_content.html
source_html_snippets/neonatal_distraction_main_content.html
source_html_snippets/patient_forms_main_content.html
source_html_snippets/patient_center_main_content.html
source_html_snippets/patient_testimonials_main_content.html
source_html_snippets/media_main_content.html
```

Data-only tests now also cover the Facial Birth Deformities parent page, Cleft Lip & Palate Surgery, Hemifacial Microsomia, Treacher Collins Syndrome, Pierre Robin Sequence, Neonatal Distraction, Patient Testimonials, Media, their CSV exports, and the nested Facial Birth Deformities and Patient Center menu links.


## Latest update

The supplied Pierre Robin Sequence outer HTML and Neonatal Distraction outer HTML have been extracted into structured page JSON, FAQ CSV files, findings docs, source snippets, config getters, and pytest checks.


## Patient Testimonials and Media update

- Added Patient Testimonials (`/testimonials/`) detailed archive data from the supplied outer HTML.
- Added Media (`/media/`) detailed page data from the supplied outer HTML.
- Added CSV exports for testimonial cards, Media videos, magazine PDF links, and news items.
- Added page-specific docs, snippets, and pytest data checks.
