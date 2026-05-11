# Complete Website Package

This ZIP contains one combined project for the Staten Island Oral Surgery website work.

## Static website folder

The `website/` folder contains a complete navigable static HTML/CSS/JS website with the header menu, nested hover/click submenus, Patient Center menu, Contact menu, and footer links.

Pages generated from supplied outer HTML structured data:

- `cleft-lip-palate-surgery.html` — Cleft Lip & Palate Surgery (/cleft-lip-palate-surgery/)
- `facial-birth-deformities.html` — Facial Birth Deformities (/facial-birth-deformities/)
- `hemifacial-microsomia.html` — Hemifacial Microsomia (/hemifacial-microsomia/)
- `impacted-canines.html` — Impacted Canines (/impacted-canines/)
- `media.html` — Media (/media/)
- `neonatal-distraction.html` — Neonatal Distraction (/neonatal-distraction/)
- `oral-and-maxillofacial.html` — Oral & Maxillofacial Surgeries (/oral-and-maxillofacial/)
- `orthognathic-jaw-surgery.html` — Orthognathic Jaw Surgery (/orthognathic-jaw-surgery/)
- `patient-center.html` — Patient Center (/patient-center/)
- `patient-forms.html` — Patient Forms (/patient-forms/)
- `testimonials.html` — Patient Testimonials (/testimonials/)
- `pierre-robin-sequence.html` — Pierre Robin Sequence (/pierre-robin-sequence/)
- `platelet-rich-fibrin-prf.html` — Platelet Rich Fibrin (PRF) (/platelet-rich-fibrin-prf/)
- `ridge-augmentation.html` — Ridge Augmentation (/ridge-augmentation/)
- `sinus-lift.html` — Sinus Lift (/sinus-lift/)
- `teeth-extractions.html` — Teeth Extractions (/teeth-extractions/)
- `treacher-collins-syndrome.html` — Treacher Collins Syndrome (/treacher-collins-syndrome/)
- `wisdom-teeth-removal.html` — Wisdom Teeth Removal (/wisdom-teeth-removal/)

Additional starter pages are included so menu/footer links resolve inside the same project file. These starter pages should be replaced with final approved content if their outer HTML is supplied later.

## Data and tests

The root `data/`, `docs/`, `source_html_snippets/`, `src/`, and `tests/` folders preserve the extracted page data, findings, snippets, Selenium helpers, and pytest checks from the supplied outer HTML.

Key files:

- `data/menu_structure.csv` — full combined header/footer menu inventory.
- `data/full_site_menu_structure.csv` — same full-site menu inventory for clarity.
- `data/site_pages_manifest.csv` — every static HTML page included in `website/`.
- `website/index.html` — static site entry point.

