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
