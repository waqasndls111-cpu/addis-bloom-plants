(function () {
  function normalizePath(path) {
    const clean = (path || '').split('?')[0].split('#')[0].replace(/^\.\//, '');
    if (!clean || clean === '/' || clean === 'index.html') return 'home';
    return clean.replace(/\/$/, '');
  }

  function buildSharedHeader() {
    return `
      <header class="site-shell">
        <div class="site-topbar">
          <div class="mx-auto flex max-w-7xl flex-col gap-2 px-4 py-3 sm:px-6 lg:flex-row lg:items-center lg:justify-between lg:px-8">
            <div class="flex flex-wrap items-center gap-x-6 gap-y-2">
              <span class="topbar-item">Call: <a href="tel:+251935207720" class="font-semibold">+251 93 520 7720</a></span>
              <span class="topbar-item">Email: <a href="mailto:draslambaig@gmail.com" class="font-semibold">draslambaig@gmail.com</a></span>
            </div>
            <div class="topbar-item">JEMS Building, Gabon St, Addis Ababa, Ethiopia</div>
          </div>
        </div>

        <div class="main-nav">
          <div class="mx-auto flex max-w-7xl items-center justify-between gap-4 px-4 py-5 sm:px-6 lg:px-8">
            <a href="./index.html" class="flex items-center gap-3">
              <div class="logo-mark">AI</div>
              <div>
                <div class="site-brand">ADDIS IMPLANT</div>
                <div class="site-subbrand">Oral Surgery in Addis Ababa</div>
              </div>
            </a>

            <button class="inline-flex items-center justify-center rounded-full border border-[rgba(18,29,43,0.14)] bg-white px-4 py-2 text-sm font-bold text-[var(--navy)] shadow-sm lg:hidden" data-menu-button aria-expanded="false" aria-controls="primary-nav">
              Menu
            </button>

            <nav id="primary-nav" class="hidden lg:flex lg:items-center lg:gap-8" data-menu>
              <a class="nav-link" data-nav-link data-nav-key="home" href="./index.html">Home</a>
              <a class="nav-link" data-nav-link data-nav-key="about" href="./about.html">About</a>
              <a class="nav-link" data-nav-link data-nav-key="services" href="./services.html">Services</a>
              <a class="nav-link" data-nav-link data-nav-key="results" href="./results.html">Results</a>
              <a class="nav-link" data-nav-link data-nav-key="contact" href="./contact.html">Contact</a>
              <a href="./contact.html" class="cta-button">Request Appointment</a>
            </nav>
          </div>

          <div class="hidden border-t border-[rgba(18,29,43,0.08)] bg-white lg:hidden" data-mobile-panel>
            <div class="mx-auto grid max-w-7xl gap-2 px-4 py-4 sm:px-6 lg:px-8">
              <a class="nav-link rounded-2xl px-4 py-3" data-nav-link data-nav-key="home" href="./index.html">Home</a>
              <a class="nav-link rounded-2xl px-4 py-3" data-nav-link data-nav-key="about" href="./about.html">About</a>
              <a class="nav-link rounded-2xl px-4 py-3" data-nav-link data-nav-key="services" href="./services.html">Services</a>
              <a class="nav-link rounded-2xl px-4 py-3" data-nav-link data-nav-key="results" href="./results.html">Results</a>
              <a class="nav-link rounded-2xl px-4 py-3" data-nav-link data-nav-key="contact" href="./contact.html">Contact</a>
              <a href="./contact.html" class="cta-button mt-2 rounded-2xl px-4 py-3 text-center">Request Appointment</a>
            </div>
          </div>
        </div>
      </header>
    `;
  }

  function buildSharedFooter() {
    return `
      <footer class="footer-shell">
        <div class="mx-auto max-w-7xl px-4 py-24 sm:px-6 lg:px-8">
          <div class="max-w-3xl">
            <h2 class="text-3xl text-white">Addis Implant</h2>
            <p class="mt-4 max-w-2xl text-lg leading-8 text-white/82">Premium dental implants and oral surgery care in Addis Ababa with an international medical aesthetic and a patient-first approach.</p>
          </div>

          <div class="mt-14 grid gap-12 lg:grid-cols-4">
            <div>
              <h3 class="footer-heading text-lg">Services</h3>
              <ul class="mt-5 space-y-3 text-lg leading-8">
                <li><a class="footer-link" href="./dental-implants.html">Dental Implants</a></li>
                <li><a class="footer-link" href="./all-on-4.html">All-on-4</a></li>
                <li><a class="footer-link" href="./bone-grafting.html">Bone Grafting</a></li>
                <li><a class="footer-link" href="./sinus-lift.html">Sinus Lift</a></li>
              </ul>
            </div>

            <div>
              <h3 class="footer-heading text-lg">Patient Center</h3>
              <ul class="mt-5 space-y-3 text-lg leading-8">
                <li><a class="footer-link" href="./first-visit.html">First Visit</a></li>
                <li><a class="footer-link" href="./insurance.html">Insurance & Financing</a></li>
                <li><a class="footer-link" href="./post-op-care.html">Post-Op Care</a></li>
                <li><a class="footer-link" href="./faq.html">FAQ</a></li>
              </ul>
            </div>

            <div>
              <h3 class="footer-heading text-lg">Quick Links</h3>
              <ul class="mt-5 space-y-3 text-lg leading-8">
                <li><a class="footer-link" href="./index.html">Home</a></li>
                <li><a class="footer-link" href="./about.html">About</a></li>
                <li><a class="footer-link" href="./results.html">Results</a></li>
                <li><a class="footer-link" href="./contact.html">Contact</a></li>
              </ul>
            </div>

            <div>
              <h3 class="footer-heading text-lg">Location</h3>
              <p class="mt-5 text-lg leading-8 text-white/82">Near 4th Floor JEMS Building, Opposite Dreamliner Hotel, Gabon St, Addis Ababa, Ethiopia.</p>
              <div class="mt-5 space-y-2 text-lg leading-8 text-white/82">
                <p>Phone: <a class="footer-link" href="tel:+251935207720">+251 93 520 7720</a></p>
                <p>Email: <a class="footer-link" href="mailto:draslambaig@gmail.com">draslambaig@gmail.com</a></p>
              </div>
            </div>
          </div>
        </div>

        <div class="border-t border-white/10">
          <div class="mx-auto max-w-7xl px-4 py-5 text-sm uppercase tracking-[0.14em] text-white/70 sm:px-6 lg:px-8">
            &copy; <span data-year></span> Addis Implant. All rights reserved.
          </div>
        </div>
      </footer>
    `;
  }

  function injectSharedShell() {
    const headerHost = document.querySelector('#site-header');
    if (headerHost && !headerHost.querySelector('.site-shell')) {
      headerHost.innerHTML = buildSharedHeader();
    }

    const footerHost = document.querySelector('#site-footer');
    if (footerHost && !footerHost.querySelector('.footer-shell')) {
      footerHost.innerHTML = buildSharedFooter();
    }
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

    panel.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        panel.classList.add('hidden');
        button.setAttribute('aria-expanded', 'false');
      });
    });
  }

  function initStickyHeader() {
    const shell = document.querySelector('.site-shell');
    if (!shell) return;

    const onScroll = () => {
      shell.classList.toggle('is-scrolled', window.scrollY > 8);
    };

    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  function setActiveNav() {
    const current = normalizePath(document.body?.dataset?.page || location.pathname);
    document.querySelectorAll('[data-nav-link]').forEach(link => {
      const href = normalizePath(link.getAttribute('href'));
      const key = link.getAttribute('data-nav-key');
      const active = current === href || current === key || (current === 'home' && href === 'home');
      link.dataset.active = active ? 'true' : 'false';
    });
  }

  function initSwiperHero() {
    const swiperEl = document.querySelector('.heroSwiper');
    if (!swiperEl || typeof Swiper === 'undefined') return;

    new Swiper(swiperEl, {
      loop: true,
      effect: 'fade',
      fadeEffect: { crossFade: true },
      speed: 1000,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
      },
      pagination: {
        el: swiperEl.querySelector('.swiper-pagination'),
        clickable: true,
      },
      navigation: {
        nextEl: swiperEl.querySelector('.swiper-button-next'),
        prevEl: swiperEl.querySelector('.swiper-button-prev'),
      },
      allowTouchMove: true,
    });
  }

  function initTrustRail() {
    const track = document.querySelector('[data-trust-track]');
    if (!track || track.dataset.cloned === 'true') return;
    track.innerHTML += track.innerHTML;
    track.dataset.cloned = 'true';
  }

  function initCallbackForms() {
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
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          });

          form.reset();
          if (status) {
            status.textContent = 'Thank you. We will call you back shortly.';
            status.classList.remove('hidden');
          }
        } catch (error) {
          if (status) {
            status.textContent = 'Your request could not be sent right now, but it has been prepared locally.';
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
    injectSharedShell();
    initMenu();
    initStickyHeader();
    setActiveNav();
    initSwiperHero();
    initTrustRail();
    initCallbackForms();
    const year = document.querySelector('[data-year]');
    if (year) year.textContent = new Date().getFullYear();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }
})();
