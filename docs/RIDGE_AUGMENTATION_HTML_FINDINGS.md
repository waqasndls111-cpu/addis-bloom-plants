# Ridge Augmentation HTML findings

Source URL:

```text
https://statenislandoralsurgery.us/ridge-augmentation/
```

This file captures the important data extracted from the Ridge Augmentation outer HTML supplied by the user.

## SEO and page identity

```text
WordPress page id: 4180
Body class: page-id-4180
Elementor page class: elementor-4180
Title: Ridge Augmentation | Staten Island Oral Surgery
Canonical: https://statenislandoralsurgery.us/ridge-augmentation/
Meta description: Our team of oral and maxillofacial surgeons specialize in ridge augmentation in Staten Island, NY. Get in touch with our skilled doctors today!
Published time: 2023-05-15T20:56:31+00:00
Modified time: 2026-04-20T14:21:13+00:00
Twitter read time: 3 minutes
```

## Navigation state

The active desktop header path is:

```text
Services > Bone Grafting > Ridge Augmentation
```

Visible nested Bone Grafting submenu items in the provided HTML:

```text
Bone Grafting FAQs -> /bone-grafting-faqs/
Ridge Augmentation -> /ridge-augmentation/
Sinus Lift -> /sinus-lift/
Platelet Rich Fibrin (PRF) -> /platelet-rich-fibrin-prf/
```

The active Ridge Augmentation nav item has these useful classes:

```text
current-menu-item
page_item
page-item-4180
current_page_item
elementor-item-active
```

## Hero section

```text
H1: Ridge Augmentation Surgery In Staten Island, NY
H2: Ridge Augmentation
Intro: A ridge augmentation can help shape and contour your gum and jawline to what it was before any teeth were removed or any alveoli were damaged. After a successful ridge augmentation, you will have enough healthy bone to support future dental implants.
Phone CTA: +1 (718) 226-1251
Phone href: tel:+17182261251
```

Hero video data:

```text
Video widget element id: d60be26
YouTube URL: https://www.youtube.com/watch?v=oEZAOWL4HJQ
Overlay image: https://statenislandoralsurgery.us/wp-content/uploads/hqdefault-1.jpg
Play aria-label: Play Video
```

## Images and media

Open Graph and main content image:

```text
URL: https://statenislandoralsurgery.us/wp-content/uploads/Staten-Island-Oral-and-Maxillofacial-Surgery-42.jpg
Alt: Older man smiling after ridge augmentation
Width: 1200
Height: 1200
```

Lottie animation:

```text
Path: https://statenislandoralsurgery.us/wp-content/uploads/11_1.json
Renderer: svg
Loop: true
Play speed: 0.5
```

## Body section

```text
Heading: What is Ridge Augmentation?
```

Body copy summary:

```text
Ridge augmentation surgery is commonly performed after tooth extraction to help reconstruct your natural gum and jawline. It can shape the jaw to treat bone loss associated with tooth extraction or other dental conditions. The page explains alveolar ridges, alveoli, and why enough healthy bone is needed to support dental implants.
```

Internal body link:

```text
dental implants -> /dental-implants/
```

## FAQ accordion headings

```text
How Is a Ridge Augmentation Surgery Performed?
What Can Ridge Augmentation Do For Dental Implants?
Am I a Good Candidate For Ridge Augmentation?
```

## Closing CTA

```text
Heading: How Can I Find Out More About Ridge Augmentation?
Phone href: tel:+17182261251
Phone text: +1 (718-226-1251)
Button: Request a Callback
Button path: /callback-request/
```

## Footer Bone Grafting links present on this page

```text
Bone Grafting -> /bone-grafting/
Bone Grafting FAQs -> /bone-grafting-faqs/
Ridge Augmentation -> /ridge-augmentation/
Sinus Lift -> /sinus-lift/
BMP Infuse® Bone Graft -> /bmp-infuse-bone-graft/
```

## Stable locator recommendations for Selenium

Avoid generated SmartMenus IDs such as:

```text
sm-17784585880032534-7
sm-17784585880074558-7
```

Use stable XPath patterns instead:

```text
//header//nav[contains(@class,'elementor-nav-menu--main') and not(ancestor::*[contains(@class,'elementor-sticky__spacer')])]
//a[normalize-space()='Services']
//a[normalize-space()='Bone Grafting' and contains(@href,'/bone-grafting/')]
//a[normalize-space()='Ridge Augmentation' and contains(@href,'/ridge-augmentation/')]
//main//h1[normalize-space()='Ridge Augmentation Surgery In Staten Island, NY']
//main//h2[normalize-space()='Ridge Augmentation']
//main//h4[contains(@class,'jet-toggle__label-text')]
```
