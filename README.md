# Staten Island Oral Surgery Complete Website Project

This is the single combined project file with the full website menu and all pages currently available from the supplied HTML/data.

## What is included

- `website/` — complete static HTML/CSS/JS website with all main header menus, nested dropdowns, Patient Center submenu pages, Contact menu pages, and footer links.
- `data/` — structured JSON/CSV extracted from the outer HTML you provided.
- `docs/` — page findings, HTML findings, update summaries, and this complete package note.
- `source_html_snippets/` — main-content HTML snippets extracted for the supplied pages.
- `src/` and `tests/` — Selenium helpers and pytest checks for data and live page validation.

## Pages generated from supplied outer HTML

- Cleft Lip & Palate Surgery — `website/cleft-lip-palate-surgery.html`
- Facial Birth Deformities — `website/facial-birth-deformities.html`
- Hemifacial Microsomia — `website/hemifacial-microsomia.html`
- Impacted Canines — `website/impacted-canines.html`
- Media — `website/media.html`
- Neonatal Distraction — `website/neonatal-distraction.html`
- Oral & Maxillofacial Surgeries — `website/oral-and-maxillofacial.html`
- Orthognathic Jaw Surgery — `website/orthognathic-jaw-surgery.html`
- Patient Center — `website/patient-center.html`
- Patient Forms — `website/patient-forms.html`
- Patient Testimonials — `website/testimonials.html`
- Pierre Robin Sequence — `website/pierre-robin-sequence.html`
- Platelet Rich Fibrin (PRF) — `website/platelet-rich-fibrin-prf.html`
- Ridge Augmentation — `website/ridge-augmentation.html`
- Sinus Lift — `website/sinus-lift.html`
- Teeth Extractions — `website/teeth-extractions.html`
- Treacher Collins Syndrome — `website/treacher-collins-syndrome.html`
- Wisdom Teeth Removal — `website/wisdom-teeth-removal.html`

## Full menu coverage

The project now includes the full visible website menu structure in one place:

- Our Center
  - About Our Office
  - Our Doctors
  - David C. Hoffman, D.D.S., F.A.C.S.
  - Lydia J. Lam, D.D.S.
  - Jessica Li, D.D.S
  - Monika Patel, D.D.S
  - Latest Technology
- Services
  - Dental Implants
  - Teeth in a Day (All-On-X)
  - Bone Grafting and its inner pages
  - Oral & Maxillofacial Surgeries and its inner pages
  - Facial Birth Deformities and its inner pages
  - Anesthesia Options
- Patient Center
  - First Visit
  - Patient Forms
  - Surgical Instructions
  - Insurance & Financing
  - Patient Testimonials
  - Wisdom Tooth Consent
  - Pay Your Bill
  - Media
- Contact Us
  - Callback Request
  - Referring Doctors
  - Find Our Office

The full menu inventory is saved at `data/menu_structure.csv` and `data/full_site_menu_structure.csv`.

## Run the static website

Open `website/index.html` in a browser, or use VS Code Live Server from the `website/` folder.

## Run data tests

From the project root:

```bash
pip install -r requirements.txt
pytest -q -m "not live"
```

