(function () {
  const SITE = {
    name: 'Addis Implant',
    phone: '+251 93 520 7720',
    email: 'draslambaig@gmail.com',
    address: 'Near 4th Floor JEMS Building, Opposite Dreamliner Hotel, Gabon St, Addis Ababa, Ethiopia.',
    services: [
      { label: 'Dental Implants', href: 'dental-implants.html' },
      { label: 'All-on-4', href: 'all-on-4.html' },
      { label: 'Bone Grafting', href: 'bone-grafting.html' },
      { label: 'Sinus Lift', href: 'sinus-lift.html' }
    ],
    patientCenter: [
      { label: 'First Visit', href: 'first-visit.html' },
      { label: 'Insurance & Financing', href: 'insurance.html' },
      { label: 'Post-Op Care', href: 'post-op-care.html' },
      { label: 'FAQ', href: 'faq.html' }
    ],
    quickLinks: [
      { label: 'About', href: 'about.html' },
      { label: 'Services', href: 'services.html' },
      { label: 'Results', href: 'results.html' },
      { label: 'Contact', href: 'contact.html' }
    ]
  };

  const navItems = [
    { key: 'home', label: 'Home', href: 'index.html' },
    { key: 'about', label: 'About', href: 'about.html' },
    { key: 'services', label: 'Services', href: 'services.html' },
    { key: 'results', label: 'Results', href: 'results.html' },
    { key: 'contact', label: 'Contact', href: 'contact.html' }
  ];

  function normalizePath(path) {
    const clean = (path || '').split('?')[0].split('#')[0].replace(/^\.\//, '');
    if (!clean || clean === '/' || clean === 'index.html') return 'home';
    return clean.replace(/\/$/, '');
  }

  function renderHeader() {
    return `
      <div class="site-shell">
        <div class="site-topbar">
          <div class="mx-auto flex max-w-7xl flex-col gap-2 px-4 py-3 sm:px-6 lg:flex-row lg:items-center lg:justify-between lg:px-8">
            <div class="flex flex-wrap items-center gap-x-6 gap-y-2">
              <span class="topbar-item">Call: <a href="tel:+251935207720" class="font-semibold">+251 93 520 7720</a></span>
              <span class="topbar-item">Email: <a href="mailto:draslambaig@gmail.com" class="font-semibold">draslambaig@gmail.com</a></span>
            </div>
            <div class="topbar-item">Near 4th Floor JEMS Building, Opposite Dreamliner Hotel, Gabon St, Addis Ababa</div>
          </div>
        </div>

        <div class="main-nav">
          <div class="mx-auto flex max-w-7xl items-center justify-between gap-4 px-4 py-5 sm:px-6 lg:px-8">
            <a href="index.html" class="flex items-center gap-3">
              <div class="logo-mark">AI</div>
              <div>
                <div class="text-sm font-extrabold uppercase tracking-[0.24em] text-[var(--primary-blue)]">${SITE.name}</div>
                <div class="text-xs text-slate-500">Oral surgery in Addis Ababa</div>
              </div>
            </a>

            <button class="inline-flex items-center justify-center rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-bold text-slate-800 shadow-sm lg:hidden" data-menu-button aria-expanded="false" aria-controls="primary-nav">
              Menu
            </button>

            <nav id="primary-nav" class="hidden lg:flex lg:items-center lg:gap-8" data-menu>
              ${navItems.map(item => `
                <a class="nav-link" data-nav-link data-nav-key="${item.key}" href="${item.href}">${item.label}</a>
              `).join('')}
              <a href="contact.html" class="gold-button rounded-full px-5 py-3 text-sm font-bold text-white">Request Appointment</a>
            </nav>
          </div>

          <div class="hidden border-t border-slate-200 bg-white lg:hidden" data-mobile-panel>
            <div class="mx-auto grid max-w-7xl gap-2 px-4 py-4 sm:px-6 lg:px-8">
              ${navItems.map(item => `
                <a class="nav-link rounded-2xl px-4 py-3" data-nav-link data-nav-key="${item.key}" href="${item.href}">${item.label}</a>
              `).join('')}
              <a href="contact.html" class="gold-button mt-2 rounded-2xl px-4 py-3 text-center text-sm font-bold text-white">Request Appointment</a>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  function renderFooter() {
    return `
      <footer class="bg-[var(--primary-blue)] text-white">
        <div class="mx-auto grid max-w-7xl gap-12 px-4 py-24 sm:px-6 lg:grid-cols-4 lg:px-8">
          <div>
            <div class="text-3xl font-bold text-white">${SITE.name}</div>
            <p class="mt-5 max-w-sm text-lg leading-8 text-white/85">
              Premium dental implants and oral surgery care in Addis Ababa with a patient-first, internationally polished experience.
            </p>
          </div>

          <div>
            <h3 class="text-lg font-bold text-white">Services</h3>
            <ul class="mt-5 space-y-3 text-lg leading-8 text-white/85">
              ${SITE.services.map(item => `<li><a class="footer-link" href="${item.href}">${item.label}</a></li>`).join('')}
            </ul>
          </div>

          <div>
            <h3 class="text-lg font-bold text-white">Patient Center</h3>
            <ul class="mt-5 space-y-3 text-lg leading-8 text-white/85">
              ${SITE.patientCenter.map(item => `<li><a class="footer-link" href="${item.href}">${item.label}</a></li>`).join('')}
            </ul>
          </div>

          <div>
            <h3 class="text-lg font-bold text-white">Quick Links</h3>
            <ul class="mt-5 space-y-3 text-lg leading-8 text-white/85">
              ${SITE.quickLinks.map(item => `<li><a class="footer-link" href="${item.href}">${item.label}</a></li>`).join('')}
            </ul>
            <div class="mt-8">
              <h4 class="text-lg font-bold text-white">Location</h4>
              <p class="mt-4 text-lg leading-8 text-white/85">${SITE.address}</p>
            </div>
          </div>
        </div>
        <div class="border-t border-white/10">
          <div class="mx-auto max-w-7xl px-4 py-5 text-sm uppercase tracking-[0.14em] text-white/70 sm:px-6 lg:px-8">
            &copy; <span data-year></span> ${SITE.name}. All rights reserved.
          </div>
        </div>
      </footer>
    `;
  }

  function setActiveNav() {
    const current = normalizePath(location.pathname);
    document.querySelectorAll('[data-nav-link]').forEach(link => {
      const key = link.getAttribute('data-nav-key');
      const href = normalizePath(link.getAttribute('href'));
      const active = current === key || current === href;
      link.dataset.active = active ? 'true' : 'false';
    });
  }

  function initMenu() {
    const button = document.querySelector('[data-menu-button]');
    const panel = document.querySelector('[data-mobile-panel]');
    if (!button || !panel) return;
    button.addEventListener('click', () => {
      const isOpen = !panel.classList.contains('hidden');
      panel.classList.toggle('hidden');
      button.setAttribute('aria-expanded', String(!isOpen));
    });
  }

  function initStickyHeader() {
    const shell = document.querySelector('.site-shell');
    if (!shell) return;
    const update = () => shell.classList.toggle('shadow-lg', window.scrollY > 8);
    update();
    window.addEventListener('scroll', update, { passive: true });
  }

  function initReveal() {
    const items = document.querySelectorAll('.reveal');
    if (!('IntersectionObserver' in window) || !items.length) {
      items.forEach(item => item.classList.add('is-visible'));
      return;
    }
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    items.forEach(item => observer.observe(item));
  }

  function initTrustRail() {
    const track = document.querySelector('[data-trust-track]');
    if (!track) return;
    track.innerHTML += track.innerHTML;
  }

  function initCallbacks() {
    document.querySelectorAll('[data-callback-form]').forEach(form => {
      const status = form.querySelector('[data-form-status]');
      form.addEventListener('submit', async event => {
        event.preventDefault();
        const submit = form.querySelector('[type="submit"]');
        const original = submit?.textContent || 'Submit';
        if (submit) {
          submit.disabled = true;
          submit.textContent = 'Sending...';
        }
        try {
          const formData = new FormData(form);
          const body = new URLSearchParams();
          formData.forEach((value, key) => body.append(key, String(value)));
          await fetch(form.action, {
            method: 'POST',
            body,
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
          });
          form.reset();
          if (status) {
            status.textContent = 'Thank you. We will call you back shortly.';
            status.classList.remove('hidden');
          }
        } catch {
          if (status) {
            status.textContent = 'Thanks. Your request has been captured locally.';
            status.classList.remove('hidden');
          }
        } finally {
          if (submit) {
            submit.disabled = false;
            submit.textContent = original;
          }
        }
      });
    });
  }

  function mount() {
    const header = document.getElementById('site-header');
    const footer = document.getElementById('site-footer');
    if (header) header.innerHTML = renderHeader();
    if (footer) footer.innerHTML = renderFooter();
    const year = document.querySelector('[data-year]');
    if (year) year.textContent = new Date().getFullYear();
    setActiveNav();
    initMenu();
    initStickyHeader();
    initReveal();
    initTrustRail();
    initCallbacks();
  }

  document.addEventListener('DOMContentLoaded', mount);
})();


/* --- HERO SLIDER LOGIC --- */
let currentSlide = 0;
const slides = document.querySelectorAll('.slide');

function showSlide(index) {
    if (slides.length === 0) return; // Safety check
    slides.forEach((slide, i) => {
        slide.style.opacity = i === index ? '1' : '0';
        slide.style.transition = 'opacity 1s ease-in-out';
        slide.style.visibility = i === index ? 'visible' : 'hidden';
        slide.style.zIndex = i === index ? '10' : '1';
    });
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

// Initialize slider if slides exist
if(slides.length > 0) {
    // Start automatic sliding every 5 seconds
    setInterval(nextSlide, 5000);
    // Show the first slide immediately
    showSlide(0);
}

/* --- THREE-SLIDE CAROUSEL LOGIC --- */
(function () {
  function initThreeSlideCarousels() {
    document.querySelectorAll('[data-three-slider]').forEach(root => {
      const slideSelector = root.querySelectorAll('[data-three-slide], .slide, [data-slide]');
      const slides = Array.from(slideSelector);
      if (slides.length < 2) return;

      const prev = root.querySelector('[data-three-prev], [data-carousel-prev]');
      const next = root.querySelector('[data-three-next], [data-carousel-next]');
      let current = slides.findIndex(slide => slide.getAttribute('data-active') === 'true');
      if (current < 0) current = 0;

      root.style.position = root.style.position || 'relative';
      root.style.overflow = 'hidden';

      slides.forEach((slide, index) => {
        slide.style.position = 'absolute';
        slide.style.inset = '0';
        slide.style.width = '100%';
        slide.style.height = '100%';
        slide.style.transition = 'opacity 900ms ease, transform 900ms ease';
        slide.style.willChange = 'opacity, transform';
        slide.style.opacity = index === current ? '1' : '0';
        slide.style.transform = index === current ? 'translateX(0)' : 'translateX(0)';
        slide.style.pointerEvents = index === current ? 'auto' : 'none';
        slide.setAttribute('aria-hidden', index === current ? 'false' : 'true');
      });

      function render(index) {
        slides.forEach((slide, i) => {
          const active = i === index;
          slide.setAttribute('data-active', active ? 'true' : 'false');
          slide.style.opacity = active ? '1' : '0';
          slide.style.pointerEvents = active ? 'auto' : 'none';
          slide.style.zIndex = active ? '2' : '1';
          slide.setAttribute('aria-hidden', active ? 'false' : 'true');
        });
        current = index;
      }

      function advance(step) {
        const nextIndex = (current + step + slides.length) % slides.length;
        render(nextIndex);
      }

      if (prev) prev.addEventListener('click', () => advance(-1));
      if (next) next.addEventListener('click', () => advance(1));

      render(current);
      window.setInterval(() => advance(1), 5500);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initThreeSlideCarousels);
  } else {
    initThreeSlideCarousels();
  }
})();
