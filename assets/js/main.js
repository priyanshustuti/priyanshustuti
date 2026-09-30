(function () {
  'use strict';

  // Mobile menu
  var burger = document.querySelector('.burger');
  var nav = document.getElementById('nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open);
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a') && !e.target.closest('.has-sub > a')) {
        nav.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Services dropdown toggle (touch / keyboard)
  document.querySelectorAll('.sub-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var li = btn.parentElement;
      var open = li.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
    });
  });

  // Scroll reveal (stagger siblings)
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) {
      var sibs = el.parentElement.querySelectorAll(':scope > .reveal');
      el.style.setProperty('--d', (Array.prototype.indexOf.call(sibs, el) * 0.09) + 's');
      io.observe(el);
    });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Clients marquee: duplicate track for a seamless loop
  var track = document.querySelector('.marquee__track');
  if (track) {
    Array.prototype.slice.call(track.children).forEach(function (li) {
      var c = li.cloneNode(true);
      c.setAttribute('aria-hidden', 'true');
      c.querySelector('img').alt = '';
      track.appendChild(c);
    });
  }

  // Hero carousel
  var slides = document.querySelectorAll('.slides img');
  var dots = document.querySelectorAll('.dots button');
  if (slides.length > 1) {
    var cur = 0, timer, reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var frame = document.querySelector('.hero__frame');
    var show = function (n) {
      cur = (n + slides.length) % slides.length;
      slides.forEach(function (s, i) { s.classList.toggle('on', i === cur); s.loading = 'eager'; });
      dots.forEach(function (d, i) { d.classList.toggle('on', i === cur); d.setAttribute('aria-current', i === cur); });
    };
    var play = function () { if (!reduce) { clearInterval(timer); timer = setInterval(function () { show(cur + 1); }, 5000); } };
    var stop = function () { clearInterval(timer); };
    dots.forEach(function (d, i) { d.addEventListener('click', function () { show(i); play(); }); });
    document.querySelector('.car-btn--prev').addEventListener('click', function () { show(cur - 1); play(); });
    document.querySelector('.car-btn--next').addEventListener('click', function () { show(cur + 1); play(); });
    frame.addEventListener('mouseenter', stop);
    frame.addEventListener('mouseleave', play);
    frame.addEventListener('focusin', stop);
    frame.addEventListener('focusout', play);
    var x0 = null;
    frame.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    frame.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 40) { show(cur + (dx < 0 ? 1 : -1)); play(); }
    });
    document.addEventListener('visibilitychange', function () { if (document.hidden) { stop(); } else { play(); } });
    show(0); play();
  }

  // Enquiry form -> opens the visitor's email app (static site, no server)
  var form = document.getElementById('enquiry');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = form.querySelector('.form__note');
      if (!form.name.value.trim() || !form.phone.value.trim()) {
        note.textContent = 'Please enter your name and phone number.';
        return;
      }
      var body = 'Name: ' + form.name.value + '\nPhone: ' + form.phone.value +
        '\nEmail: ' + form.email.value + '\nService: ' + form.service.value +
        '\n\n' + form.message.value;
      window.location.href = 'mailto:corp.uniquely@gmail.com?subject=' +
        encodeURIComponent('Website enquiry – ' + form.service.value) +
        '&body=' + encodeURIComponent(body);
      note.textContent = 'Opening your email app… if nothing happens, write to corp.uniquely@gmail.com.';
    });
  }

  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();
})();
