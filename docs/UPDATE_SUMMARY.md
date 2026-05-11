# Update Summary

This project file has been updated with the supplied outer HTML details for the Oral & Maxillofacial branch of the Services menu.

## Previously added Bone Grafting pages

- Ridge Augmentation (`/ridge-augmentation/`)
- Sinus Lift (`/sinus-lift/`)
- Platelet Rich Fibrin (PRF) (`/platelet-rich-fibrin-prf/`)

## Newly added Oral & Maxillofacial pages

- Oral & Maxillofacial Surgeries (`/oral-and-maxillofacial/`)
- Teeth Extractions (`/teeth-extractions/`)
- Wisdom Teeth Removal (`/wisdom-teeth-removal/`)
- Impacted Canines (`/impacted-canines/`)
- Orthognathic Jaw Surgery (`/orthognathic-jaw-surgery/`)

## Menu update

The Services menu data now includes:

- Dental Implants
- Teeth in a Day (All-On-X)
- Bone Grafting and its submenu pages
- Oral & Maxillofacial Surgeries and its submenu pages: Teeth Extractions, Wisdom Teeth Removal, Impacted Canines, Orthognathic Jaw Surgery
- Facial Birth Deformities and its submenu pages
- Anesthesia Options

## Added/updated files

- structured JSON data for the four Oral & Maxillofacial pages now supplied
- CSV export for Teeth Extractions, Wisdom Teeth Removal, Impacted Canines, and Orthognathic Jaw Surgery FAQs
- expanded `data/menu_structure.csv`
- screenshot reference for the Oral & Maxillofacial hover menu
- page-specific findings documents
- main-content HTML snippets for the Oral & Maxillofacial pages now supplied, including Orthognathic Jaw Surgery
- Selenium menu helper methods for generic Services submenus
- pytest checks for the new menu branch and extracted page data

Data-only tests were run locally after the update using `pytest -q -m "not live"`.


## Facial Birth Deformities update

- Added Facial Birth Deformities parent page data.
- Added Cleft Lip & Palate Surgery page data and FAQ CSV.
- Added Facial Birth Deformities submenu coverage for all five nested header links.


## Hemifacial Microsomia and Treacher Collins Syndrome update

- Added Hemifacial Microsomia page data and FAQ CSV.
- Added Treacher Collins Syndrome page data and FAQ CSV.
- Updated Facial Birth Deformities submenu sources for the two newly supplied inner pages.
- Added page-specific pytest data checks, live validation hooks, findings docs, and main-content HTML snippets.

## Pierre Robin Sequence and Neonatal Distraction update

- Added Pierre Robin Sequence page data and FAQ CSV from the supplied outer HTML.
- Added Neonatal Distraction page data and FAQ CSV from the supplied outer HTML.
- Updated Facial Birth Deformities submenu sources for both pages.
- Added page-specific pytest data checks, live validation hooks, findings docs, and main-content HTML snippets.
- Data-only tests pass with `pytest -q -m "not live"`.



## Patient Center update

- Added the top-level Patient Center menu item.
- Added all Patient Center submenu pages shown in the screenshot/header HTML: First Visit, Patient Forms, Surgical Instructions, Insurance & Financing, Patient Testimonials, Wisdom Tooth Consent, Pay Your Bill, and Media.
- Added detailed page data for Patient Center and Patient Forms from the supplied outer HTML.
- Added Patient Forms form/document links CSV, page-specific pytest checks, live validation hooks, findings docs, and main-content HTML snippets.


## Patient Testimonials and Media update

- Added detailed Patient Testimonials archive data from the supplied outer HTML.
- Added visible testimonial cards and reviewer names to JSON and CSV.
- Added detailed Media & Videos page data from the supplied outer HTML.
- Added Media video cards, magazine PDF links, news item, and commercial section to JSON and CSV.
- Updated Patient Center submenu sources for Patient Testimonials and Media.
- Added page-specific pytest data checks, live validation hooks, findings docs, and main-content HTML snippets.
