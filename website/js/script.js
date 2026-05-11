'use strict';

const qs = (selector, scope = document) => scope.querySelector(selector);
const qsa = (selector, scope = document) => Array.from(scope.querySelectorAll(selector));

const header = qs('.site-header');
const mobileToggle = qs('.mobile-toggle');
const navMenu = qs('#primary-menu');
const backToTop = qs('.back-to-top');

let lastScrollY = window.scrollY;
let galleryTimer = null;

function initHeader() {
  if (!header) return;

  window.addEventListener('scroll', () => {
    const current = window.scrollY;
    header.classList.toggle('scrolled', current > 20);

    if (current > 560 && current > lastScrollY + 12 && !document.body.classList.contains('menu-open')) {
      header.classList.add('is-hidden');
    } else if (current < lastScrollY - 12) {
      header.classList.remove('is-hidden');
    }

    if (current < 80) header.classList.remove('is-hidden');
    lastScrollY = current;
  }, { passive: true });
}

function initMobileMenu() {
  if (!mobileToggle || !navMenu) return;

  const closeMenu = () => {
    mobileToggle.setAttribute('aria-expanded', 'false');
    navMenu.classList.remove('open');
    document.body.classList.remove('menu-open');
    qsa('.has-dropdown.open', navMenu).forEach(item => item.classList.remove('open'));
    qsa('.submenu-toggle', navMenu).forEach(button => {
      button.textContent = '+';
      button.setAttribute('aria-expanded', 'false');
    });
  };

  mobileToggle.addEventListener('click', () => {
    const isOpen = mobileToggle.getAttribute('aria-expanded') === 'true';
    mobileToggle.setAttribute('aria-expanded', String(!isOpen));
    navMenu.classList.toggle('open', !isOpen);
    document.body.classList.toggle('menu-open', !isOpen);
  });

  qsa('.submenu-toggle', navMenu).forEach(button => {
    button.addEventListener('click', event => {
      event.preventDefault();
      const parent = button.closest('.has-dropdown');
      if (!parent) return;
      const isOpen = parent.classList.toggle('open');
      button.textContent = isOpen ? '−' : '+';
      button.setAttribute('aria-expanded', String(isOpen));
    });
  });

  qsa('a', navMenu).forEach(link => {
    link.addEventListener('click', () => {
      if (window.matchMedia('(max-width: 980px)').matches) closeMenu();
    });
  });

  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') closeMenu();
  });

  document.addEventListener('click', event => {
    const clickedInside = navMenu.contains(event.target) || mobileToggle.contains(event.target);
    if (!clickedInside && navMenu.classList.contains('open')) closeMenu();
  });
}

function initRevealAnimations() {
  const elements = qsa('.reveal');
  if (!elements.length) return;

  if (!('IntersectionObserver' in window)) {
    elements.forEach(element => element.classList.add('in-view'));
    return;
  }

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.16, rootMargin: '0px 0px -50px 0px' });

  elements.forEach(element => observer.observe(element));
}

function initServiceImageChanger() {
  const image = qs('#service-sticky-image');
  const triggers = qsa('.image-trigger');
  if (!image || !triggers.length) return;

  const setActive = target => {
    const nextSrc = target.dataset.image;
    if (!nextSrc || image.getAttribute('src') === nextSrc) return;

    triggers.forEach(trigger => trigger.classList.toggle('is-active', trigger === target));
    image.classList.add('fade-out');

    window.setTimeout(() => {
      image.src = nextSrc;
      image.classList.remove('fade-out');
    }, 160);
  };

  triggers[0].classList.add('is-active');

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) setActive(entry.target);
      });
    }, { threshold: 0.5, rootMargin: '-24% 0px -34% 0px' });

    triggers.forEach(trigger => observer.observe(trigger));
  }

  triggers.forEach(trigger => {
    trigger.addEventListener('mouseenter', () => setActive(trigger));
    trigger.addEventListener('focusin', () => setActive(trigger));
  });
}

function animateCounter(element) {
  const target = Number(element.dataset.target || 0);
  const duration = 1600;
  const start = performance.now();

  function frame(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    const value = Math.floor(target * eased);
    element.textContent = value.toLocaleString();

    if (progress < 1) requestAnimationFrame(frame);
    else element.textContent = target.toLocaleString();
  }

  requestAnimationFrame(frame);
}

function initCounters() {
  const counters = qsa('.counter');
  if (!counters.length) return;

  if (!('IntersectionObserver' in window)) {
    counters.forEach(counter => animateCounter(counter));
    return;
  }

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !entry.target.dataset.counted) {
        entry.target.dataset.counted = 'true';
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.55 });

  counters.forEach(counter => observer.observe(counter));
}

function initAccordion() {
  const items = qsa('.accordion-item');
  if (!items.length) return;

  items.forEach(item => {
    const button = qs('button', item);
    if (!button) return;

    button.addEventListener('click', () => {
      const wasActive = item.classList.contains('active');
      items.forEach(other => {
        other.classList.remove('active');
        const otherButton = qs('button', other);
        if (otherButton) otherButton.setAttribute('aria-expanded', 'false');
      });

      item.classList.toggle('active', !wasActive);
      button.setAttribute('aria-expanded', String(!wasActive));
    });
  });
}

function initGallerySlider() {
  const slider = qs('[data-slider]');
  if (!slider) return;

  const slides = qsa('.slide', slider);
  const prev = qs('.prev', slider);
  const next = qs('.next', slider);
  if (!slides.length) return;

  let index = slides.findIndex(slide => slide.classList.contains('active'));
  if (index < 0) index = 0;

  const show = nextIndex => {
    slides[index].classList.remove('active');
    index = (nextIndex + slides.length) % slides.length;
    slides[index].classList.add('active');
  };

  const resetTimer = () => {
    if (galleryTimer) clearInterval(galleryTimer);
    galleryTimer = setInterval(() => show(index + 1), 4400);
  };

  prev?.addEventListener('click', () => {
    show(index - 1);
    resetTimer();
  });

  next?.addEventListener('click', () => {
    show(index + 1);
    resetTimer();
  });

  slider.addEventListener('mouseenter', () => galleryTimer && clearInterval(galleryTimer));
  slider.addEventListener('mouseleave', resetTimer);
  slider.addEventListener('focusin', () => galleryTimer && clearInterval(galleryTimer));
  slider.addEventListener('focusout', resetTimer);

  resetTimer();
}

function initCallbackForm() {
  const form = qs('#callback-form');
  if (!form) return;

  const status = qs('.form-status', form);

  form.addEventListener('submit', event => {
    event.preventDefault();
    const requiredFields = qsa('[required]', form);
    let valid = true;

    requiredFields.forEach(field => {
      const fieldValid = field.checkValidity() && field.value.trim().length > 0;
      field.classList.toggle('invalid', !fieldValid);
      if (!fieldValid) valid = false;
    });

    const phone = form.elements.phone;
    if (phone && phone.value.trim()) {
      const digits = phone.value.replace(/\D/g, '');
      const phoneValid = digits.length >= 7;
      phone.classList.toggle('invalid', !phoneValid);
      if (!phoneValid) valid = false;
    }

    if (!valid) {
      if (status) status.textContent = 'Please enter a valid email and phone number.';
      return;
    }

    const formData = new FormData(form);
    const firstName = String(formData.get('firstName') || '').trim() || 'there';
    if (status) status.textContent = `Thanks, ${firstName}. This demo form is ready to connect to your CRM or email service.`;
    form.reset();
  });

  qsa('input', form).forEach(input => {
    input.addEventListener('input', () => input.classList.remove('invalid'));
  });
}

function initBackToTop() {
  if (!backToTop) return;

  window.addEventListener('scroll', () => {
    backToTop.classList.toggle('visible', window.scrollY > 800);
  }, { passive: true });

  backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

function initLogoTrack() {
  const track = qs('.logo-track');
  if (!track) return;

  const trackWidth = track.scrollWidth;
  const viewportWidth = window.innerWidth;

  if (trackWidth < viewportWidth * 1.8) {
    track.innerHTML += track.innerHTML;
  }
}

function init() {
  initHeader();
  initMobileMenu();
  initRevealAnimations();
  initServiceImageChanger();
  initCounters();
  initAccordion();
  initGallerySlider();
  initCallbackForm();
  initBackToTop();
  initLogoTrack();
}

document.addEventListener('DOMContentLoaded', init);
