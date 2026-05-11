# Platelet Rich Fibrin (PRF) HTML findings

## Stable values extracted from the HTML

The PRF page uses WordPress page class `page-id-6397`, Elementor page class `elementor-page-6397`, and canonical path `/platelet-rich-fibrin-prf/`.

Stable selectors should prefer:

- `link[rel="canonical"]` with href `https://statenislandoralsurgery.us/platelet-rich-fibrin-prf/`
- `main#content h1` containing `Platelet Rich Fibrin (PRF) Staten Island, NY`
- `main#content h2` containing `Platelet Rich Fibrin (PRF)`
- FAQ heading text:
  - `What can PRF be used for?`
  - `Why should I want PRF for my oral surgery procedure?`
- Hero image URL `https://statenislandoralsurgery.us/wp-content/uploads/close-up-doctor-checking-smiley-patient.jpg`
- Secondary image alt text `Person holding a vile of blood`

## Dynamic values to avoid

The SmartMenus IDs beginning with `sm-177845...` are dynamic and should not be used for durable tests. The sticky header duplicates the navigation markup, so tests should use the real desktop nav and exclude `.elementor-sticky__spacer`.
