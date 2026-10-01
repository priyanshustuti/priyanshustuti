(function () {
  'use strict';
  window.__usmsReady = true;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---- Mobile menu + services dropdown ----
  var burger = $('.burger'), nav = $('#nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open);
    });
  }
  $$('.sub-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var li = btn.parentElement, open = li.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
    });
  });

  // ---- Header shadow + scroll progress ----
  var header = $('.header'), bar = $('.progress'), ticking = false;
  function onScroll() {
    var y = window.scrollY, h = document.documentElement.scrollHeight - window.innerHeight;
    if (header) header.classList.toggle('is-stuck', y > 40);
    if (bar) bar.style.transform = 'scaleX(' + (h > 0 ? Math.min(1, y / h) : 0) + ')';
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  // ---- Scroll reveal (stagger siblings) ----
  var items = $$('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) {
      var sibs = $$(':scope > .reveal', el.parentElement);
      el.style.setProperty('--d', Math.min(sibs.indexOf(el), 6) * 0.09 + 's');
      io.observe(el);
    });
  } else { items.forEach(function (el) { el.classList.add('in'); }); }

  // ---- Marquees: duplicate content for a seamless loop ----
  $$('.marquee__track').forEach(function (track) {
    $$(':scope > li', track).forEach(function (li) {
      var c = li.cloneNode(true);
      c.setAttribute('aria-hidden', 'true');
      var img = $('img', c); if (img) img.alt = '';
      track.appendChild(c);
    });
  });

  // ---- Cursor spotlight on hero ----
  var hero = $('.hero, .phero');
  if (hero && !reduce && window.matchMedia('(pointer:fine)').matches) {
    var bg = $('.hero__bg, .phero__bg', hero), raf = 0, mx = 0, my = 0;
    hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect(); mx = e.clientX - r.left; my = e.clientY - r.top;
      if (!raf) raf = requestAnimationFrame(function () { raf = 0; bg.style.setProperty('--mx', mx + 'px'); bg.style.setProperty('--my', my + 'px'); });
    });
  }

  // ---- Count-up numbers ----
  $$('[data-count]').forEach(function (el) {
    var end = +el.getAttribute('data-count'); if (reduce) return;
    el.textContent = '0';
    var o = new IntersectionObserver(function (en) {
      if (!en[0].isIntersecting) return; o.disconnect();
      var n = 0, steps = 28, iv = setInterval(function () {
        n++; el.textContent = Math.round(end * (1 - Math.pow(1 - n / steps, 3)));
        if (n >= steps) { clearInterval(iv); el.textContent = end; }
      }, 50);
    }); o.observe(el);
  });

  // ---- Hero carousel ----
  var slides = $$('.slides img'), thumbs = $$('.thumbs button');
  if (slides.length > 1) {
    var cur = 0, timer, frame = $('.hero__frame');
    var show = function (n) {
      cur = (n + slides.length) % slides.length;
      slides.forEach(function (s, i) { s.classList.toggle('on', i === cur); s.loading = 'eager'; });
      thumbs.forEach(function (d, i) { d.classList.toggle('on', i === cur); d.setAttribute('aria-current', i === cur); });
    };
    var play = function () { if (!reduce) { clearInterval(timer); timer = setInterval(function () { show(cur + 1); }, 5200); } };
    var stop = function () { clearInterval(timer); };
    thumbs.forEach(function (d, i) { d.addEventListener('click', function () { show(i); play(); }); });
    $('.car-btn--prev').addEventListener('click', function () { show(cur - 1); play(); });
    $('.car-btn--next').addEventListener('click', function () { show(cur + 1); play(); });
    frame.addEventListener('mouseenter', stop); frame.addEventListener('mouseleave', play);
    frame.addEventListener('focusin', stop); frame.addEventListener('focusout', play);
    var x0 = null;
    frame.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    frame.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 40) { show(cur + (dx < 0 ? 1 : -1)); play(); }
    });
    document.addEventListener('visibilitychange', function () { if (document.hidden) stop(); else play(); });
    show(0); play();
  }

  // ---- Expanding service panels ----
  var panels = $$('.panel');
  if (panels.length) {
    var activate = function (p) { panels.forEach(function (x) { x.classList.toggle('active', x === p); }); };
    var wide = function () { return window.matchMedia('(min-width:961px)').matches; };
    var go = function (p) {
      var h = p.getAttribute('data-href') || '';
      if (/^[a-z-]+\.html$/.test(h)) window.location.href = h;   // local pages only
    };
    panels.forEach(function (p) {
      p.addEventListener('mouseenter', function () { if (wide()) activate(p); });
      p.addEventListener('focusin', function () { activate(p); });
      p.addEventListener('click', function (e) {
        if (e.target.closest('a')) return;
        if (!wide() || p.classList.contains('active')) go(p);
        else activate(p);
      });
      p.addEventListener('keydown', function (e) { if (e.key === 'Enter') go(p); });
    });
  }

  // ---- "On this page" scroll-spy ----
  var toc = $$('.toc a');
  if (toc.length && 'IntersectionObserver' in window) {
    var map = {};
    toc.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var so = new IntersectionObserver(function (en) {
      en.forEach(function (e) {
        if (e.isIntersecting) { toc.forEach(function (a) { a.classList.remove('on'); }); map[e.target.id].classList.add('on'); }
      });
    }, { rootMargin: '-35% 0px -55% 0px' });
    $$('.block').forEach(function (b) { if (map[b.id]) so.observe(b); });
  }

  // ---- Gallery: filter + lightbox ----
  var figs = $$('.gallery figure');
  if (figs.length) {
    $$('.filters button').forEach(function (b) {
      b.addEventListener('click', function () {
        $$('.filters button').forEach(function (x) { x.classList.toggle('on', x === b); });
        var f = b.getAttribute('data-f');
        figs.forEach(function (fg) { fg.classList.toggle('hide', f !== 'all' && fg.getAttribute('data-cat') !== f); });
      });
    });
    var lb = $('.lb'), lbi = $('img', lb), idx = 0;
    var vis = function () { return figs.filter(function (f) { return !f.classList.contains('hide'); }); };
    var open = function (i) {
      var v = vis(); idx = (i + v.length) % v.length;
      var im = $('img', v[idx]); lbi.src = v[idx].getAttribute('data-full') || im.src; lbi.alt = im.alt; lb.classList.add('open');
    };
    figs.forEach(function (f) { f.addEventListener('click', function () { open(vis().indexOf(f)); }); });
    $('.x', lb).addEventListener('click', function () { lb.classList.remove('open'); });
    $('.pv', lb).addEventListener('click', function () { open(idx - 1); });
    $('.nx', lb).addEventListener('click', function () { open(idx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) lb.classList.remove('open'); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') lb.classList.remove('open');
      if (e.key === 'ArrowLeft') open(idx - 1);
      if (e.key === 'ArrowRight') open(idx + 1);
    });
  }

  // ---- Enquiry form -> opens the visitor's own email app (static site: nothing is sent to any server) ----
  var form = $('#enquiry');
  if (form) {
    var clean = function (v, max) {                       // strip control chars / line breaks, trim, cap length
      return String(v || '').replace(/[\u0000-\u001f\u007f]+/g, ' ').trim().slice(0, max);
    };
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = form.elements, note = $('.form__note', form);
      var name = clean(f.name.value, 80), phone = clean(f.phone.value, 20), email = clean(f.email.value, 120);
      var services = ['Security', 'Facility', 'Maintenance', 'Other'];
      var service = services.indexOf(f.service.value) > -1 ? f.service.value : 'Other';
      var msg = String(f.message.value || '').replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/g, '').trim().slice(0, 800);
      if (name.length < 2) { note.textContent = 'Please enter your name.'; f.name.focus(); return; }
      if (!/^[0-9+()\-\s]{7,20}$/.test(phone) || phone.replace(/\D/g, '').length < 7) { note.textContent = 'Please enter a valid contact number.'; f.phone.focus(); return; }
      if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) { note.textContent = 'Please enter a valid email address or leave it blank.'; f.email.focus(); return; }
      var body = 'Name: ' + name + '\nPhone: ' + phone + '\nEmail: ' + email + '\nService: ' + service + '\n\n' + msg;
      var url = 'mailto:corp.uniquely@gmail.com?subject=' + encodeURIComponent('Website enquiry - ' + service) + '&body=' + encodeURIComponent(body);
      if (url.length > 1900) { note.textContent = 'Your message is too long — please shorten it a little.'; return; }
      window.location.href = url;
      note.textContent = 'Opening your email app… if nothing happens, write to corp.uniquely@gmail.com.';
    });
  }

  var yr = $('#yr'); if (yr) yr.textContent = new Date().getFullYear();
})();
