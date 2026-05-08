(function () {
  const SITE = {
    name: 'Addis Implant',
    phone: '+251 93 520 7720',
    email: 'draslambaig@gmail.com',
    address: 'Near 4th Floor JEMS Building, Opposite Dreamliner Hotel, Gabon St, Addis Ababa, Ethiopia.',
    nav: [
      { key: 'home', label: 'Home', href: 'index.html' },
      { key: 'about', label: 'About', href: 'about.html' },
      { key: 'services', label: 'Services', href: 'services.html' },
      { key: 'implants', label: 'Implants', href: 'dental-implants.html' },
      { key: 'all-on-4', label: 'All-on-4', href: 'all-on-4.html' },
      { key: 'process', label: 'Process', href: 'process.html' },
      { key: 'results', label: 'Results', href: 'results.html' },
      { key: 'faq', label: 'FAQ', href: 'faq.html' },
      { key: 'contact', label: 'Contact', href: 'contact.html' }
    ],
    footerLinks: [
      { label: 'Insurance & Financing', href: 'insurance.html' },
      { label: 'First Visit', href: 'first-visit.html' },
      { label: 'Post-Op Care', href: 'post-op-care.html' },
      { label: 'Disclaimer', href: 'disclaimer.html' }
    ]
  };

  const body = document.body;
  const pageKey = body?.dataset?.page || '';

  function renderHeader() {
    return `
      <div class="site-shell sticky top-0 z-50">
        <div class="mx-auto flex max-w-7xl items-center justify-between gap-4 px-4 py-4 sm:px-6 lg:px-8">
          <a href="index.html" class="group flex items-center gap-3">
            <div class="grid h-12 w-12 place-items-center rounded-2xl bg-gradient-to-br from-[#002d5b] to-[#0f2745] text-white shadow-lg">
              <span class="font-bold">AI</span>
            </div>
            <div>
              <div class="text-sm font-extrabold uppercase tracking-[0.24em] text-[#002d5b]">${SITE.name}</div>
              <div class="text-xs text-slate-500">Implant clinic in Addis Ababa</div>
            </div>
          </a>

          <button class="inline-flex items-center justify-center rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-bold text-slate-800 shadow-sm lg:hidden" data-menu-button aria-expanded="false" aria-controls="primary-nav">
            Menu
          </button>

          <nav id="primary-nav" class="hidden lg:flex lg:items-center lg:gap-2" data-menu>
            ${SITE.nav.map(item => `
              <a class="nav-link rounded-full px-4 py-2 text-sm font-semibold text-slate-700 hover:bg-[#002d5b]/5 hover:text-[#002d5b]" data-nav-link data-nav-key="${item.key}" href="${item.href}">
                ${item.label}
              </a>
            `).join('')}
          </nav>

          <a href="contact.html" class="gold-button hidden rounded-full px-5 py-3 text-sm font-bold text-white transition lg:inline-flex">
            Request Appointment
          </a>
        </div>
        <div class="hidden border-t border-slate-200 bg-white lg:hidden" data-mobile-panel>
          <div class="mx-auto grid max-w-7xl gap-1 px-4 py-3 sm:px-6 lg:px-8">
            ${SITE.nav.map(item => `
              <a class="nav-link rounded-2xl px-4 py-3 text-sm font-semibold text-slate-700 hover:bg-[#002d5b]/5 hover:text-[#002d5b]" data-nav-link data-nav-key="${item.key}" href="${item.href}">
                ${item.label}
              </a>
            `).join('')}
            <a href="contact.html" class="gold-button mt-2 rounded-2xl px-4 py-3 text-center text-sm font-bold text-white">
              Request Appointment
            </a>
          </div>
        </div>
      </div>
    `;
  }

  function renderFooter() {
    return `
      <div class="bg-slate-950 text-slate-100">
        <div class="mx-auto grid max-w-7xl gap-10 px-4 py-16 sm:px-6 lg:grid-cols-[1.3fr_0.8fr_0.8fr] lg:px-8">
          <div>
            <div class="display-font text-4xl font-bold text-white">${SITE.name}</div>
            <p class="mt-4 max-w-xl text-sm leading-7 text-slate-300">
              High-end implant dentistry, bone regeneration, and full-arch smile restoration for patients in Addis Ababa and across Ethiopia.
            </p>
            <div class="mt-6 space-y-2 text-sm text-slate-300">
              <div><span class="font-semibold text-white">Phone:</span> <a href="tel:${SITE.phone.replace(/\s+/g, '')}" class="hover:text-white">${SITE.phone}</a></div>
              <div><span class="font-semibold text-white">Email:</span> <a href="mailto:${SITE.email}" class="hover:text-white">${SITE.email}</a></div>
              <div><span class="font-semibold text-white">Address:</span> ${SITE.address}</div>
            </div>
          </div>

          <div>
            <h3 class="text-lg font-bold text-white">Quick Links</h3>
            <ul class="mt-4 space-y-3 text-sm text-slate-300">
              ${SITE.nav.map(item => `<li><a class="hover:text-white" href="${item.href}">${item.label}</a></li>`).join('')}
            </ul>
          </div>

          <div>
            <h3 class="text-lg font-bold text-white">Patient Resources</h3>
            <ul class="mt-4 space-y-3 text-sm text-slate-300">
              ${SITE.footerLinks.map(item => `<li><a class="hover:text-white" href="${item.href}">${item.label}</a></li>`).join('')}
            </ul>
            <a href="contact.html" class="gold-button mt-6 inline-flex rounded-full px-5 py-3 text-sm font-bold text-white">
              Request Appointment
            </a>
          </div>
        </div>
        <div class="border-t border-white/10">
          <div class="mx-auto flex max-w-7xl flex-col gap-2 px-4 py-5 text-xs text-slate-400 sm:px-6 lg:flex-row lg:items-center lg:justify-between lg:px-8">
            <div>&copy; <span data-year></span> ${SITE.name}. All rights reserved.</div>
            <div class="footer-fineprint">Addis Ababa implant dentistry website template.</div>
          </div>
        </div>
      </div>
    `;
  }

  function normalizePath(path) {
    const clean = path.split('?')[0].split('#')[0].replace(/^\.\//, '');
    if (!clean || clean === '/' || clean === 'index.html') return 'home';
    return clean.replace(/\/$/, '');
  }

  function setActiveNav() {
    const current = pageKey || normalizePath(location.pathname);
    document.querySelectorAll('[data-nav-link]').forEach(link => {
      const key = link.getAttribute('data-nav-key');
      const href = link.getAttribute('href') || '';
      const normalizedHref = normalizePath(href);
      const isActive = key === current || normalizedHref === current;
      link.dataset.active = isActive ? 'true' : 'false';
      if (isActive) {
        link.classList.add('text-[#002d5b]');
      }
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

  function initCarousel() {
    const root = document.querySelector('[data-carousel]');
    if (!root) return;
    const slides = Array.from(root.querySelectorAll('[data-slide]'));
    const prev = root.querySelector('[data-carousel-prev]');
    const next = root.querySelector('[data-carousel-next]');
    let current = slides.findIndex(slide => slide.dataset.active === 'true');
    if (current < 0) current = 0;

    function show(index) {
      slides.forEach((slide, idx) => {
        const active = idx === index;
        slide.dataset.active = active ? 'true' : 'false';
        slide.classList.toggle('opacity-100', active);
        slide.classList.toggle('pointer-events-auto', active);
        slide.classList.toggle('opacity-0', !active);
        slide.classList.toggle('pointer-events-none', !active);
      });
      current = index;
    }

    function advance(step) {
      const nextIndex = (current + step + slides.length) % slides.length;
      show(nextIndex);
    }

    if (prev) prev.addEventListener('click', () => advance(-1));
    if (next) next.addEventListener('click', () => advance(1));
    show(current);
    window.setInterval(() => advance(1), 6500);
  }

  function initCompareSliders() {
    document.querySelectorAll('[data-compare-slider]').forEach(slider => {
      const input = slider.querySelector('[data-compare-input]');
      if (!input) return;
      const update = value => slider.style.setProperty('--position', `${value}%`);
      update(input.value || 50);
      input.addEventListener('input', event => update(event.target.value));
    });
  }

  function initFaq() {
    document.querySelectorAll('[data-accordion-button]').forEach(button => {
      const panelId = button.getAttribute('aria-controls');
      const panel = panelId ? document.getElementById(panelId) : null;
      if (!panel) return;
      button.addEventListener('click', () => {
        const isOpen = panel.dataset.open === 'true';
        panel.dataset.open = String(!isOpen);
        button.setAttribute('aria-expanded', String(!isOpen));
      });
    });
  }

  function initReveal() {
    const items = document.querySelectorAll('.reveal');
    if (!('IntersectionObserver' in window) || !items.length) {
      items.forEach(item => item.classList.add('is-visible'));
      return;
    }
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.16 });
    items.forEach(item => observer.observe(item));
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
    initCarousel();
    initCompareSliders();
    initFaq();
    initReveal();
  }

  document.addEventListener('DOMContentLoaded', mount);
})();
