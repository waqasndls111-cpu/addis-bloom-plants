# Sinus Lift HTML findings

## Stable values extracted from the HTML

The Sinus Lift page uses WordPress page class `page-id-4188`, Elementor page class `elementor-page-4188`, and canonical path `/sinus-lift/`.

Stable selectors should prefer:

- `link[rel="canonical"]` with href `https://statenislandoralsurgery.us/sinus-lift/`
- `main#content h1` containing `Support Dental Implants With A Sinus Lift In Staten Island, NY`
- `main#content h2` containing `Sinus Lift`
- FAQ heading text:
  - `How Is A Sinus Lift Performed?`
  - `How Can A Sinus Lift Help Me?`
  - `What Can I Expect From A Sinus Lift?`
- YouTube URL `https://youtu.be/B3sq-jgLDew` or video ID `B3sq-jgLDew`
- Overlay image `https://statenislandoralsurgery.us/wp-content/uploads/maxresdefault-4.jpg`

## Dynamic values to avoid

The SmartMenus IDs beginning with `sm-177845...` are dynamic and should not be used for durable tests. Elementor `data-id` values are more stable than SmartMenus IDs, but content text and href paths are still better.
