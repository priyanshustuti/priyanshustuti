#!/usr/bin/env python3
"""Optional helper: regenerates the static pages (index, about, security, facility,
maintenance, contact, gallery) so the shared header/footer/nav live in ONE place.

Usage:  python3 tools/build_site.py
WARNING: this overwrites the *.html files in the repo root. Either edit the text
in this script and re-run it, OR edit the .html files by hand and never run it.
"""
import os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHONE_T, PHONE = '07314230508', '0731-4230508'
MAIL = 'corp.uniquely@gmail.com'
ADDR = 'G-55, M.I.G. Colony, behind M.I.G. Police Station, near Kankeshwari Devi School, Indore, 452011 (M.P.)'
COMPANY = 'Uniquely Security and Management Solutions Private Limited'
MAPS = 'https://maps.app.goo.gl/9SYsRfpvtH8vKHij6'

SPRITE = '''<svg class="sprite" width="0" height="0" aria-hidden="true">
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24"><path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm1 2.6V17h16V7.6l-8 5.4-8-5.4zM5.3 7l6.7 4.5L18.7 7H5.3z"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></symbol>
<symbol id="i-fb" viewBox="0 0 24 24"><path d="M13.5 22v-8.2h2.8l.5-3.3h-3.3V8.4c0-.95.4-1.7 1.8-1.7h1.6V3.8c-.3 0-1.3-.15-2.4-.15-2.5 0-4.1 1.5-4.1 4.2v2.45H7.6v3.3h2.8V22z"/></symbol>
<symbol id="i-x" viewBox="0 0 24 24"><path d="M17.8 3h3.1l-6.8 7.7L22 21h-6.2l-4.9-6.3L5.3 21H2.2l7.2-8.3L2 3h6.4l4.4 5.8L17.8 3zm-1.1 16.2h1.7L7.4 4.7H5.6l11.1 14.5z"/></symbol>
<symbol id="i-yt" viewBox="0 0 24 24"><path d="M21.6 7.2a2.5 2.5 0 0 0-1.76-1.77C18.3 5 12 5 12 5s-6.3 0-7.84.43A2.5 2.5 0 0 0 2.4 7.2C2 8.75 2 12 2 12s0 3.25.4 4.8a2.5 2.5 0 0 0 1.76 1.77C5.7 19 12 19 12 19s6.3 0 7.84-.43a2.5 2.5 0 0 0 1.76-1.77C22 15.25 22 12 22 12s0-3.25-.4-4.8zM10 15V9l5.2 3z"/></symbol>
<symbol id="i-wp" viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM3.3 12c0-1.4.3-2.7.85-3.9l4.7 12.8A8.7 8.7 0 0 1 3.3 12zm8.7 8.7c-.85 0-1.7-.13-2.5-.36l2.65-7.7 2.7 7.4.06.12a8.7 8.7 0 0 1-2.9.54zm1.2-12.8c.5-.03.95-.08.95-.08.45-.05.4-.72-.05-.7 0 0-1.35.1-2.2.1-.8 0-2.2-.1-2.2-.1-.45-.02-.5.67-.05.7 0 0 .42.05.87.08l1.3 3.55-1.8 5.45L6.9 7.9c.5-.03.95-.08.95-.08.45-.05.4-.72-.05-.7 0 0-1.35.1-2.2.1h-.55A8.7 8.7 0 0 1 12 3.3c2.25 0 4.3.85 5.85 2.25h-.12c-.85 0-1.4.73-1.4 1.52 0 .7.4 1.3.85 2 .33.57.7 1.3.7 2.35 0 .73-.28 1.58-.65 2.75l-.85 2.85zm5.45-.05a8.7 8.7 0 0 1-3.2 11.6l2.7-7.8c.5-1.25.67-2.25.67-3.15 0-.33-.02-.63-.06-.9z"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M4 12h16M14 6l6 6-6 6" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-chev" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6" fill="none" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-shield" viewBox="0 0 48 48"><path d="M24 4 7 10v12c0 10.5 7.2 18.6 17 22 9.8-3.4 17-11.5 17-22V10L24 4z" fill="none" stroke-width="2" stroke-linejoin="round"/><path d="m16 24 6 6 11-12" fill="none" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-building" viewBox="0 0 48 48"><path d="M8 42V12l16-7 16 7v30M4 42h40" fill="none" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/><path d="M16 18h4m8 0h4M16 25h4m8 0h4M16 32h4m8 0h4M21 42v-6h6v6" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-wrench" viewBox="0 0 48 48"><path d="M33 6a10 10 0 0 0-9.4 13.3L6.5 36.4a4 4 0 0 0 5.7 5.7l17.1-17.1A10 10 0 0 0 42 15l-6.2 6.2-5-1-1-5L36 9a10 10 0 0 0-3-3z" fill="none" stroke-width="2" stroke-linejoin="round"/></symbol>
<symbol id="i-target" viewBox="0 0 48 48"><circle cx="22" cy="26" r="16" fill="none" stroke-width="2"/><circle cx="22" cy="26" r="9" fill="none" stroke-width="2"/><circle cx="22" cy="26" r="2.5"/><path d="M22 26 40 8M34 6l8 0 0 8" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-eye" viewBox="0 0 48 48"><path d="M3 24s8-14 21-14 21 14 21 14-8 14-21 14S3 24 3 24z" fill="none" stroke-width="2" stroke-linejoin="round"/><circle cx="24" cy="24" r="7" fill="none" stroke-width="2"/><circle cx="24" cy="24" r="2.2"/></symbol>
<symbol id="i-gem" viewBox="0 0 48 48"><path d="M13 7h22l8 11-19 23L5 18z" fill="none" stroke-width="2" stroke-linejoin="round"/><path d="M5 18h38M17 7l-4 11 11 23 11-23-4-11" fill="none" stroke-width="2" stroke-linejoin="round"/></symbol>
</svg>'''

ART = '''<svg class="sprite" width="0" height="0" aria-hidden="true">
<symbol id="a-consult" viewBox="0 0 96 96"><rect x="20" y="16" width="44" height="60" rx="5"/><rect x="32" y="9" width="20" height="13" rx="3"/><path d="M29 38h26M29 49h26M29 60h14"/><path class="gd" d="M27 36l2 2 3-4z"/><circle class="ac" cx="64" cy="62" r="14"/><path class="ac" d="M74 72l13 13"/><path class="ac" d="M58 62l4 4 7-8"/></symbol>
<symbol id="a-cash" viewBox="0 0 96 96"><rect x="22" y="44" width="46" height="34" rx="6"/><path d="M31 44V33a14 14 0 0 1 28 0v11"/><circle class="gd" cx="45" cy="59" r="4.5"/><path d="M45 63v8"/><path class="ac" d="M72 84h10M66 78a14 5 0 0 0 28 0M66 70a14 5 0 0 0 28 0"/><ellipse class="ac" cx="80" cy="62" rx="14" ry="5"/><path class="ac" d="M66 62v16M94 62v16"/></symbol>
<symbol id="a-office" viewBox="0 0 96 96"><rect x="14" y="30" width="34" height="46" rx="3"/><path d="M21 42h20M21 52h20M21 62h12"/><path class="ac" d="M56 50h24v16a12 12 0 0 1-24 0z"/><path class="ac" d="M80 54h3a5 5 0 0 1 0 10h-3"/><path class="go" d="M63 40c-4-4 3-6-1-11M72 40c-4-4 3-6-1-11"/><path d="M8 84h80"/></symbol>
<symbol id="a-patient" viewBox="0 0 96 96"><path class="go" d="M48 54C30 42 26 30 34 22c6-6 14-3 14 4 0-7 8-10 14-4 8 8 4 20-14 32z"/><path class="ac" d="M8 64h16v20H8zM24 68l14-4h22a6 6 0 0 1 0 12H40M60 70l16-8a5 5 0 0 1 6 8L62 84H24"/></symbol>
<symbol id="a-home" viewBox="0 0 96 96"><path d="M10 48 48 14l38 34M20 42v38h56V42"/><path class="ac" d="M48 72c-11-7-15-14-10-19 4-4 10-2 10 3 0-5 6-7 10-3 5 5 1 12-10 19z"/><path d="M8 84h80"/></symbol>
<symbol id="a-facade" viewBox="0 0 96 96"><rect x="18" y="12" width="36" height="70"/><path d="M26 22h8M40 22h8M26 34h8M40 34h8M26 46h8M40 46h8M26 58h8M40 58h8M34 82V70h8v12"/><path class="gd" d="M72 14l4 10 10 4-10 4-4 10-4-10-10-4 10-4z"/><path class="ac" d="M62 70l18-18M76 46l12 12"/><path d="M10 84h76"/></symbol>
<symbol id="a-pest" viewBox="0 0 96 96"><ellipse cx="48" cy="54" rx="11" ry="16"/><circle cx="48" cy="34" r="6"/><path d="M44 29l-6-9M52 29l6-9M37 48l-12-6M37 57H23M38 66l-12 8M59 48l12-6M59 57h14M58 66l12 8M48 42v28"/><circle class="ac" cx="48" cy="48" r="40"/><path class="rd" d="M20 76 76 20"/></symbol>
<symbol id="a-land" viewBox="0 0 96 96"><circle cx="48" cy="36" r="24"/><path d="M48 84V52M48 60l-12-10M48 68l12-12"/><path class="ac" d="M14 84h68M16 84c0-9 5-13 11-15 0 9-4 13-11 15zM80 84c0-9-5-13-11-15 0 9 4 13 11 15z"/><path class="gd" d="M36 30l6 4M56 24l-6 6"/></symbol>
<symbol id="a-mech" viewBox="0 0 96 96"><circle cx="48" cy="48" r="28" stroke-width="9" stroke-dasharray="9.4 12.1" stroke-linecap="butt" stroke-linejoin="miter"/><circle cx="48" cy="48" r="21"/><circle cx="48" cy="48" r="8"/><path class="ac" d="M80 10v14M73 17h14M75 12l10 10M85 12 75 22"/></symbol>
<symbol id="a-elec" viewBox="0 0 96 96"><path d="M55 8 27 54h19l-5 34 28-48H50z"/><circle class="ac" cx="48" cy="48" r="42" stroke-dasharray="3 7"/><path class="gd" d="M20 20l4 4M76 72l4 4M76 20l-4 4M20 76l4-4"/></symbol>
<symbol id="a-plumb" viewBox="0 0 96 96"><path d="M12 24h34a14 14 0 0 1 14 14v38"/><path d="M12 38h20a4 4 0 0 1 4 4v34"/><rect x="54" y="76" width="18" height="8" rx="2"/><rect x="30" y="76" width="18" height="8" rx="2"/><path class="ac" d="M76 22c-6 8-9 12-9 16a9 9 0 0 0 18 0c0-4-3-8-9-16z"/></symbol>
<symbol id="a-fire" viewBox="0 0 96 96"><path d="M48 8c4 14 20 22 20 40a20 20 0 0 1-40 0c0-10 6-15 10-24 2 6 4 8 8 8-1-8-3-14 2-24z"/><path class="ac" d="M48 86a9 9 0 0 1-9-9c0-7 6-9 9-18 5 7 9 11 9 18a9 9 0 0 1-9 9z"/></symbol>
<symbol id="a-stp" viewBox="0 0 96 96"><rect x="12" y="36" width="72" height="48" rx="4"/><path d="M28 36V22h40v14"/><path class="ac" d="M20 58q7-7 14 0t14 0 14 0 14 0M20 72q7-7 14 0t14 0 14 0 14 0"/><path class="gd" d="M48 6c-5 7-8 10-8 14a8 8 0 0 0 16 0c0-4-3-7-8-14z"/></symbol>
<symbol id="a-support" viewBox="0 0 96 96"><path d="M20 54a28 28 0 0 1 56 0"/><rect x="13" y="52" width="11" height="20" rx="4"/><rect x="72" y="52" width="11" height="20" rx="4"/><path class="ac" d="M77 72c0 11-9 15-25 15"/><circle class="gd" cx="50" cy="87" r="3.5"/></symbol>
</svg>'''
NAV = [('index.html', 'Home', 'home'), ('about.html', 'About Us', 'about'), ('SERVICES', 'Our Services', 'services'),
       ('gallery.html', 'Gallery', 'gallery'), ('contact.html', 'Contact Us', 'contact')]


def head(title, desc, page):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; frame-src 'none'; manifest-src 'self'">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#060a1e">
<link rel="icon" type="image/png" href="assets/img/emblem.png">
<link rel="preload" href="assets/fonts/fraunces-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/manrope-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">
<script src="assets/js/init.js"></script>
</head>
<body data-page="{page}">
<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"></div>
{SPRITE}
{ART}
<div class="topbar"><div class="wrap topbar__in">
<div class="social" aria-label="Social media"><a href="#" aria-label="Facebook"><svg><use href="#i-fb"/></svg></a><a href="#" aria-label="X (Twitter)"><svg><use href="#i-x"/></svg></a><a href="#" aria-label="YouTube"><svg><use href="#i-yt"/></svg></a></div>
<div class="topbar__contact"><a href="tel:{PHONE_T}"><svg><use href="#i-phone"/></svg><span>{PHONE}</span></a><a href="mailto:{MAIL}"><svg><use href="#i-mail"/></svg><span>{MAIL}</span></a></div>
</div></div>
<header class="header" id="top"><div class="header__in">
<a class="brand" href="index.html" aria-label="USMS Private Limited – Home"><img src="assets/img/logo.webp" alt="USMS Private Limited – Security | Facility | Maintenance" width="184" height="59"></a>
<button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
<nav class="nav" id="nav" aria-label="Main"><ul>
{nav_items(page)}
</ul><a class="btn btn--red btn--sm nav__cta" href="contact.html">Enquire Now <svg><use href="#i-arrow"/></svg></a></nav>
</div></header>
<main id="main">
'''


def nav_items(page):
    out = []
    for href, label, key in NAV:
        act = ' class="is-active"' if (key == page or (key == 'services' and page in ('security', 'facility', 'maintenance'))) else ''
        if href == 'SERVICES':
            out.append(f'<li class="has-sub"><a href="index.html#services"{act}>{label}</a><button class="sub-toggle" aria-label="Toggle services menu" aria-expanded="false"><svg><use href="#i-chev"/></svg></button>'
                       '<ul class="sub"><li><a href="security.html">Security</a></li><li><a href="facility.html">Facility</a></li><li><a href="maintenance.html">Maintenance</a></li></ul></li>')
        else:
            out.append(f'<li><a href="{href}"{act}>{label}</a></li>')
    return '\n'.join(out)


def cta(title='Let’s keep your premises <em>safe, clean</em> &amp; running.'):
    return f'''<section class="cta" id="enquire"><div class="wrap cta__in">
<div class="reveal"><span class="eyebrow eyebrow--gold">Enquire Now</span><h2>{title}</h2><p>Your trusted partner for integrated facility management and security solutions.</p></div>
<div class="cta__box reveal"><ul class="cta__list">
<li><svg class="ic"><use href="#i-phone"/></svg><a href="tel:{PHONE_T}">{PHONE}</a></li>
<li><svg class="ic"><use href="#i-mail"/></svg><a href="mailto:{MAIL}">{MAIL}</a></li>
<li><svg class="ic"><use href="#i-pin"/></svg><address>{ADDR}</address></li></ul>
<a class="btn btn--red" href="contact.html">Enquire Now <svg><use href="#i-arrow"/></svg></a></div>
</div></section>'''


FOOT = f'''</main>
<footer class="footer"><div class="footer__mark" aria-hidden="true">USMS</div>
<div class="wrap footer__in">
<div><a class="footer__logo" href="index.html"><img src="assets/img/logo.webp" alt="USMS Private Limited" width="190" height="61" loading="lazy"></a><p>Your trusted partner for integrated facility management and security solutions.</p></div>
<nav aria-label="Information"><h4>Information</h4><ul><li><a href="index.html">Home</a></li><li><a href="about.html">About Us</a></li><li><a href="gallery.html">Gallery</a></li><li><a href="contact.html">Contact Us</a></li></ul></nav>
<nav aria-label="Our services"><h4>Our Services</h4><ul><li><a href="security.html">Security</a></li><li><a href="facility.html">Facility</a></li><li><a href="maintenance.html">Maintenance</a></li></ul></nav>
<div><h4>Contact Us</h4><ul class="footer__contact">
<li><svg><use href="#i-phone"/></svg><a href="tel:{PHONE_T}">{PHONE}</a></li>
<li><svg><use href="#i-mail"/></svg><a href="mailto:{MAIL}">{MAIL}</a></li>
<li><svg><use href="#i-pin"/></svg><span>{ADDR}</span></li></ul>
<div class="social social--footer"><a href="#" aria-label="Facebook"><svg><use href="#i-fb"/></svg></a><a href="#" aria-label="YouTube"><svg><use href="#i-yt"/></svg></a><a href="#" aria-label="X (Twitter)"><svg><use href="#i-x"/></svg></a><a href="#" aria-label="WordPress"><svg><use href="#i-wp"/></svg></a></div></div>
</div>
<div class="footer__bar"><div class="wrap">© 2012–<span id="yr">2026</span> USMS Private Limited. All rights reserved.</div></div>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>
'''


def write(name, body):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(body)


def phero_bg():
    return '<div class="phero__bg" aria-hidden="true"></div><div class="grain" aria-hidden="true"></div>'


# ============================== HOME ==============================
HERO_ALTS = ["Three USMS armed guards in navy uniforms standing in front of a car",
             "USMS security team greeting with folded hands outside a hospital",
             "A USMS security guard writing in the visitor register at a reception desk",
             "USMS housekeeping and support staff lined up in a hospital corridor",
             "A USMS housekeeping staff member mopping a hospital laboratory floor",
             "USMS guards standing in formation on a parade ground under trees",
             "Two USMS security guards and a woman guard at a hospital pharmacy entrance"]
slides = ''.join(f'<img src="assets/img/hero/{i}.webp" alt="{a}" width="1200" height="801"' + (' fetchpriority="high"' if i == 1 else ' loading="lazy"') + '>' for i, a in enumerate(HERO_ALTS, 1))
thumbs = ''.join(f'<button type="button" aria-label="Show photo {i}"><img src="assets/img/hero/{i}.webp" alt="" loading="lazy" width="120" height="80"></button>' for i in range(1, 8))
SEAL = '<div class="seal" aria-hidden="true"><svg viewBox="0 0 120 120"><defs><path id="circ" d="M60 60m-47 0a47 47 0 1 1 94 0a47 47 0 1 1-94 0"/></defs><text><textPath href="#circ" startOffset="0" textLength="290" lengthAdjust="spacing">Uniquely Security · Facility · Maintenance ·</textPath></text></svg><i></i></div>'

home = head('USMS Pvt Ltd – Security, Facility & Maintenance Services in Indore',
            'USMS Pvt. Ltd. is a leading Integrated Facility Management services provider – security, facility management and maintenance – serving clients across multiple states since 2012.', 'home')
home += f'''
<section class="hero"><div class="hero__bg" aria-hidden="true"></div><div class="grain" aria-hidden="true"></div><div class="hero__ghost" aria-hidden="true"></div>
<div class="wrap hero__in">
<div class="hero__copy">
<span class="eyebrow eyebrow--gold reveal">Welcome to USMS PVT LTD</span>
<h1 class="reveal">Your Trusted <em>Maintenance</em> Solution Provider</h1>
<p class="lead hero__lead reveal">At USMS we deliver comprehensive, reliable security, facility management and maintenance services. Backed by highly trained professionals and years of industry experience, we build top-notch solutions around your specific needs.</p>
<div class="hero__actions reveal"><a class="btn btn--red" href="contact.html">Enquire Now <svg><use href="#i-arrow"/></svg></a><a class="btn btn--ghost" href="#services">Explore Services</a></div>
<ul class="stats reveal"><li><b data-count="4">4</b><span>States of operation</span></li><li><b data-count="9">9</b><span>Sectors served</span></li><li><b data-count="3">3</b><span>Service verticals</span></li></ul>
</div>
<div class="hero__media reveal">
{SEAL}
<div class="frame hero__frame" role="group" aria-roledescription="carousel" aria-label="USMS team photos"><div class="frame__in"><div class="slides">{slides}</div>
<button class="car-btn car-btn--prev" type="button" aria-label="Previous photo"><svg><use href="#i-arrow"/></svg></button><button class="car-btn car-btn--next" type="button" aria-label="Next photo"><svg><use href="#i-arrow"/></svg></button></div></div>
<div class="glass"><b>2012</b><span>Serving clients<br>since</span></div>
<div class="thumbs" role="group" aria-label="Choose photo">{thumbs}</div>
</div></div>
<div class="hero__wave" aria-hidden="true"><svg viewBox="0 0 1440 60" preserveAspectRatio="none"><path d="M0 60V30C240 2 480 2 720 24s480 30 720 4v32z" fill="var(--ink)"/></svg></div>
</section>
<div class="strip" aria-hidden="true"><div class="strip__track">{'<span>Security</span><i></i><span>Facility</span><i></i><span>Maintenance</span><i></i><span>Uniquely Security</span><i></i>' * 6}</div></div>

<section class="section" id="services"><div class="wrap">
<header class="sec-head reveal"><span class="eyebrow">What we do</span><h2>Our <em>Services</em></h2><p>Experience peace of mind with our trusted services tailored to your specific needs.</p></header>
<div class="panels reveal">
<article class="panel active" data-href="security.html" tabindex="0"><div class="panel__bg panel__bg--security"></div><span class="panel__no">01</span><svg class="panel__icon"><use href="#i-shield"/></svg>
<div class="panel__body"><h3>Security</h3><div class="panel__more"><p>Peace of mind, built into every post. From highly trained security guards to advanced technology solutions, our security services are designed around the specific needs of your premises.</p><a class="link" href="security.html">Know More <svg><use href="#i-arrow"/></svg></a></div></div></article>
<article class="panel" data-href="facility.html" tabindex="0"><div class="panel__bg panel__bg--facility"></div><span class="panel__no">02</span><svg class="panel__icon"><use href="#i-building"/></svg>
<div class="panel__body"><h3>Facility</h3><div class="panel__more"><p>A comfortable, well-maintained environment for your premises. From professional housekeeping to pest control and landscaping, we enhance the overall experience of your facility and make it a pleasant place for everyone.</p><a class="link" href="facility.html">Know More <svg><use href="#i-arrow"/></svg></a></div></div></article>
<article class="panel" data-href="maintenance.html" tabindex="0"><div class="panel__bg panel__bg--art"><svg viewBox="0 0 96 96" aria-hidden="true"><use href="#a-mech"/></svg></div><span class="panel__no">03</span><svg class="panel__icon"><use href="#i-wrench"/></svg>
<div class="panel__body"><h3>Maintenance</h3><div class="panel__more"><p>Keep your infrastructure in optimal condition. Whether it’s mechanical, electrical, plumbing, or fire and safety systems, our experts provide reliable maintenance for the smooth operation of your facility — including sewage treatment plants (STP) and water treatment plants (WTP).</p><a class="link" href="maintenance.html">Know More <svg><use href="#i-arrow"/></svg></a></div></div></article>
</div></div></section>

<section class="section section--ivory" id="about"><div class="wrap about">
<div class="about__visual reveal" aria-hidden="true"><div class="about__year">2012</div><img class="about__emblem" src="assets/img/emblem.png" alt="" width="210" height="170"></div>
<div class="about__copy reveal"><span class="eyebrow">Who We Are</span><h2 class="h2">About <em>Us</em></h2>
<p>USMS Pvt. Ltd. is a leading Integrated Facility Management services provider, delivering tailored solutions since 2012. With a strong network across multiple states, we put operational excellence, sustainability and client commitment first. Our dedicated team upholds the core values of discipline, transparency and mutual respect to deliver high-quality security, facility and maintenance services across industries and sectors.</p>
<ul class="chips"><li>Discipline</li><li>Transparency</li><li>Mutual Respect</li></ul>
<a class="btn btn--primary" href="about.html">Know More <svg><use href="#i-arrow"/></svg></a></div>
</div></section>

<section class="section section--dark" id="sectors"><div class="wrap">
<header class="sec-head reveal"><span class="eyebrow eyebrow--gold">Industries</span><h2>Sectors we <em>serve</em></h2><p>Over the years, we have been successfully serving a wide range of operations.</p></header>
<ol class="sectors reveal">{''.join(f'<li><span>{i:02d}</span><b>{n}</b></li>' for i, n in enumerate(['Telecom industries', 'Manufacturing units', 'Residential townships', 'Retail malls', 'Commercial buildings', 'Hospitals', 'Banks', 'Educational institutes', 'Construction sites'], 1))}</ol>
</div></section>

<section class="section" id="team"><div class="wrap">
<header class="sec-head sec-head--center reveal"><span class="eyebrow">The people</span><h2>Our <em>Team</em></h2><p>At USMS, a dedicated and skilled team of professionals is committed to giving our clients the highest level of service. Our experts span security, facility management and maintenance, and each team member brings a wealth of knowledge and experience to deliver exceptional results. Meet some of our key team members below.</p></header>
<p class="team__label eyebrow reveal">Management Team</p>
<div class="people">
<figure class="person reveal"><div class="person__photo"><img src="assets/img/team/ms-chauhan.webp" alt="M S Chauhan" width="399" height="450" loading="lazy"></div><figcaption><strong>M S Chauhan</strong><span>Director</span></figcaption></figure>
<figure class="person reveal"><div class="person__photo"><img src="assets/img/team/gajendra-singh-chauhan.webp" alt="Gajendra Singh Chauhan" width="798" height="900" loading="lazy"></div><figcaption><strong>Gajendra Singh Chauhan</strong><span>Managing Director</span></figcaption></figure>
</div></div></section>
'''
CLIENTS = [('ism-toys', 'ISM Toys'), ('bcm', 'BCM Group'), ('anand', 'Anand Hospital'), ('vyapaar', 'Vyapaar Vistaar'), ('vantage', 'Vantage'), ('unique', 'Unique Hospital'), ('shree-maruti', 'Shree Maruti'), ('shalby', 'Shalby Hospitals'), ('sankara', 'Sankara Eye Foundation, India'), ('punjab', 'Punjab Jewels'), ('prataap', 'Prataap Snacks Limited'), ('nepra', 'Nepra'), ('lifefirst', 'LifeFirst Pharma'), ('life-care-logistic', 'Life Care Logistic'), ('hnh', 'H&amp;h'), ('dp-jewellers', 'D.P. Jewellers'), ('care-chl', 'CARE CHL Hospitals')]
def mq(items, cls=''):
    lis = ''.join(f'<li><img class="cg" src="assets/img/clients/gray/{f}.webp" alt="" loading="lazy"><img class="cc" src="assets/img/clients/{f}.webp" alt="{a}" loading="lazy"></li>' for f, a in items)
    return f'<div class="marquee {cls}" aria-label="Our valued clients"><ul class="marquee__track">{lis}</ul></div>'
home += f'''<section class="section clients" id="clients"><div class="wrap"><header class="sec-head sec-head--center reveal"><span class="eyebrow">Trusted by</span><h2>Valued <em>Clients</em></h2></header></div>
{mq(CLIENTS[:9])}{mq(CLIENTS[9:] + CLIENTS[:2], 'marquee--rev')}</section>
{cta()}
'''
home += FOOT
write('index.html', home)

# ============================== ABOUT ==============================
SECTORS = ['Telecom industries', 'Manufacturing units', 'Residential townships', 'Retail malls', 'Commercial buildings', 'Hospitals', 'Banks', 'Educational institutes', 'Construction sites']
about = head('About Us – USMS Pvt Ltd', 'USMS stands for Uniquely Security and Management Solutions, established in 2012 by a retired senior police officer.', 'about')
about += f'''
<section class="phero"><div class="phero__bg" aria-hidden="true"></div><div class="grain" aria-hidden="true"></div>
<div class="wrap phero__in"><div>
<nav class="crumbs reveal" aria-label="Breadcrumb"><a href="index.html">Home</a><i></i><span>About Us</span></nav>
<span class="eyebrow eyebrow--gold reveal">Uniquely Security and Management Solutions</span>
<h1 class="reveal">About <em>Us</em></h1>
<p class="lead reveal">USMS stands for Uniquely Security and Management Solutions — established in 2012 by a retired senior police officer.</p></div>
<div class="reveal"><div class="frame phero__frame"><div class="frame__in"><img src="assets/img/gallery/full/01.webp" alt="USMS guards standing in formation on a parade ground under trees" width="1600" height="1068"></div></div></div>
</div></section>

<section class="section"><div class="wrap story">
<div class="reveal"><p class="story__lead">USMS Pvt. Ltd. is one of the leading <em>Integrated Facility Management</em> providers — offering meticulously crafted, comprehensive services tailored to your specific needs.</p></div>
<ul class="story__pts">
<li class="reveal"><span>01</span><p>Over the years we have successfully served a wide range of operations, including telecom industries, manufacturing units, residential townships, retail malls, commercial buildings, hospitals, banks, educational institutes and construction sites.</p></li>
<li class="reveal"><span>02</span><p>Our primary focus is to deliver solutions that are both efficient and affordable — through operational excellence, commercial prudence, sustainability and the highest standards.</p></li>
<li class="reveal"><span>03</span><p>Since inception, USMS has expanded its footprint and built a robust network across Madhya Pradesh, Chhattisgarh, Uttar Pradesh and Rajasthan, upholding the highest level of commitment through quality security, facility and maintenance services.</p></li>
<li class="reveal"><span>04</span><p>Our dedicated team of professionals adheres to the fundamental principles of discipline, attitude and commitment, and builds strong relationships through transparency, trust and mutual respect — the core of our value system.</p></li>
</ul></div></section>

<section class="section section--dark"><div class="wrap">
<header class="sec-head reveal"><span class="eyebrow eyebrow--gold">Our footprint</span><h2>Four states, <em>one standard</em></h2></header>
<ul class="states reveal"><li><b>Madhya Pradesh</b><span>Home state</span></li><li><b>Chhattisgarh</b><span>Network</span></li><li><b>Uttar Pradesh</b><span>Network</span></li><li><b>Rajasthan</b><span>Network</span></li></ul>
</div></section>

<section class="section section--ivory"><div class="wrap">
<header class="sec-head reveal"><span class="eyebrow">Industries</span><h2>Sectors we <em>serve</em></h2></header>
<ol class="sectors reveal">{''.join(f'<li><span>{i:02d}</span><b>{n}</b></li>' for i, n in enumerate(SECTORS, 1))}</ol>
</div></section>

<section class="section section--dark"><div class="wrap">
<header class="sec-head sec-head--center reveal"><span class="eyebrow eyebrow--gold">What guides us</span><h2>Mission, vision <em>&amp; value</em></h2></header>
<div class="mvv">
<article class="reveal"><svg><use href="#i-target"/></svg><h3>Our Mission</h3><p>To be the leading one-stop solutions provider for our clients — exceeding their specific, customised service needs by delivering the highest quality of professional services with trust and confidence.</p></article>
<article class="reveal"><svg><use href="#i-eye"/></svg><h3>Our Vision</h3><p>To be the most professional leader among service providers by exceeding customer expectations, building trustworthy partnerships with our clients, and valuing every employee.</p></article>
<article class="reveal"><svg><use href="#i-gem"/></svg><h3>Our Value</h3><p>We value trustworthy partnership, integrity, quality service, professional growth and community leadership.</p></article>
</div></div></section>
{cta()}
'''
about += FOOT
write('about.html', about)


# ============================== SERVICE PAGES ==============================
def media(img, alt):
    if img.startswith('art:'):
        return f'<div class="art" role="img" aria-label="{alt}"><svg viewBox="0 0 96 96" aria-hidden="true"><use href="#{img[4:]}"/></svg></div>'
    return f'<img src="{img}" alt="{alt}" loading="lazy">'


def block(i, title, anchor, text, img, alt, kind='', extra=''):
    cls = {'': '', 'tall': ' block__media--tall'}[kind]
    return f'''<article class="block" id="{anchor}"><div class="reveal"><span class="block__no">{i:02d}</span><h2>{title}</h2><p>{text}</p></div>
<div class="block__media{cls} reveal"><div class="frame frame--light"><div class="frame__in">{media(img, alt)}</div></div>{extra}</div></article>'''


def svc_page(page, title, eyebrow, h1, intro, hero, blocks, extra_top=''):
    blocks = [(n,) + tuple(b[1:]) for n, b in enumerate(blocks, 1)]
    p = head(title, intro, page)
    toc = ''.join(f'<a href="#{b[2]}"><span>{b[0]:02d}</span>{b[1]}</a>' for b in blocks)
    glance = ''.join(f'<a href="#{b[2]}">{b[1]}</a>' for b in blocks)
    body = ''.join(block(*b) for b in blocks)
    p += f'''
<section class="phero"><div class="phero__bg" aria-hidden="true"></div><div class="grain" aria-hidden="true"></div>
<div class="wrap phero__in"><div>
<nav class="crumbs reveal" aria-label="Breadcrumb"><a href="index.html">Home</a><i></i><a href="index.html#services">Our Services</a><i></i><span>{h1}</span></nav>
<span class="eyebrow eyebrow--gold reveal">{eyebrow}</span>
<h1 class="reveal">{h1.split()[0]} <em>{' '.join(h1.split()[1:])}</em></h1>
<p class="lead reveal">{intro}</p></div>
<div class="reveal"><div class="frame phero__frame"><div class="frame__in">{hero}</div></div></div>
</div></section>

<section class="section"><div class="wrap">
{extra_top}
<div class="layout"><aside class="toc reveal" aria-label="On this page"><h4>On this page</h4>{toc}</aside>
<div><div class="glance reveal">{glance}</div>{body}</div></div>
</div></section>
{cta('Need <em>' + h1.split()[0].lower() + '</em> support? Let’s talk.')}
'''
    return p + FOOT


def photo(src, alt, w=1200, h=801):
    return f'<img src="{src}" alt="{alt}" width="{w}" height="{h}">'


security = svc_page('security', 'Security Services – USMS Pvt Ltd', 'Comprehensive Security Solutions', 'Security Services',
    'Peace of mind, built into every post. From highly trained guards to advanced technology solutions, our security services are designed around the specific needs of your premises.',
    photo('assets/img/hero/1.webp', 'Three USMS armed guards in navy uniforms standing in front of a car'), [
    (1, 'Security Guard', 'security-guard', 'We begin with a comprehensive security assessment of your premises, then recommend the equipment and personnel you actually need. Our training department also provides specialised training for people working in the retail sector. Over the years we have earned an outstanding reputation for top-notch security — from guards and armed guards to bodyguards.', 'assets/img/gallery/full/11.webp', 'Two USMS security guards and a woman guard at a hospital pharmacy entrance'),
    (2, 'Personal Protection', 'personal-protection', 'Our Personal Protection Officers and escorts are young, smart and well-groomed professionals, carefully selected and trained in martial arts and combat craft. Fluent in both English and Hindi, they communicate seamlessly with clients — and they work as cohesive units, providing immediate, close protection to anyone who needs personal security.', 'assets/img/svc/personal-protection.webp', 'A USMS personal protection officer in a navy uniform', 'tall'),
    (3, 'Armed Guard', 'armed-guard', 'Our armed guards are a select group of dedicated, intelligent and professional individuals. Trained in martial arts and combat craft and fluent in English and Hindi, they are ready for any situation — and, working together seamlessly, they provide immediate, close protection.', 'assets/img/svc/armed-guard.webp', 'A USMS armed guard holding a rifle', 'tall'),
    (4, 'Security Consultancy', 'security-consultancy', 'We conduct comprehensive security surveys and appraisals for our clients. Our experienced team assesses your existing security measures and identifies potential vulnerabilities — then, based on the findings, gives tailored advice on equipment and manpower to strengthen overall safety and protection.', 'art:a-consult', 'Illustration of a clipboard checklist and a magnifying glass'),
    (5, 'Cash Management', 'cash-management', 'USMS provides security guard cash-handling services to keep your valuable assets safe. Our trained, professional guards follow strict protocols, understand risk management, and have the skills to detect and deter threats. They are reliable and proficient in secure cash transportation.', 'art:a-cash', 'Illustration of a padlock and a stack of coins'),
    ])
write('security.html', security)

hk_extra = '<div class="strip3">' + ''.join(f'<img src="assets/img/gallery/{n}.webp" alt="USMS housekeeping staff at work in a hospital" loading="lazy">' for n in ('19', '21', '23')) + '</div>'
facility = svc_page('facility', 'Facility Services – USMS Pvt Ltd', 'Enhancing Your Facility Experience', 'Facility Services',
    'A comfortable, well-maintained environment for your premises. From professional housekeeping to pest control and landscaping, we enhance the overall experience of your facility and make it a pleasant place for everyone.',
    photo('assets/img/gallery/full/15.webp', 'USMS housekeeping and support staff lined up in a hospital corridor', 1600, 1068), [
    (1, 'House Keeping', 'house-keeping', 'USMS provides top-notch housekeeping that keeps your premises clean, organised and welcoming. Our dedicated team tailors its cleaning to each client’s needs — from dusting and vacuuming to disinfecting and sanitising — with meticulous attention to detail, so no corner is left untouched. The result is a fresh, comfortable space that lets you focus on your core activities with peace of mind.', 'assets/img/gallery/full/22.webp', 'A USMS housekeeping staff member mopping a hospital laboratory floor', '', hk_extra),
    (2, 'Office Boy', 'office-boy', 'Our Office Boy service supports your administrative needs and keeps your workplace running smoothly. Our dedicated, professional staff are trained in document management, mail handling, inventory management and general office upkeep — so you can focus on your core business.', 'art:a-office', 'Illustration of a document stack and a cup of tea'),
    (4, 'Patient Care Service', 'patient-care', 'We understand how important compassionate, personalised care is for your loved ones. Our caregivers are experienced in assisting people with patience and empathy — whether it’s elderly care, post-surgery recovery or special-needs assistance — and are trained to ensure comfort, well-being and safety, so you can rest easy knowing your loved ones are in capable hands.', 'art:a-patient', 'Illustration of a heart held in a caring hand'),
    (5, 'Home Care', 'home-care', 'Personalised care in the comfort of your own home. Our caregivers assist with daily activities, medication management, meal preparation and companionship — promoting independence and improving quality of life.', 'art:a-home', 'Illustration of a house with a heart'),
    (6, 'Façade Cleaning', 'facade-cleaning', 'We provide top-quality façade cleaning that protects the appearance and longevity of your building’s exterior. Skilled professionals with modern equipment and environmentally friendly cleaning agents remove dirt, grime, stains and pollutants from every type of façade — from high-rise buildings to residential complexes — leaving your property pristine while preserving its structural integrity.', 'art:a-facade', 'Illustration of a building facade being cleaned'),
    (7, 'Pest Control', 'pest-control', 'We deliver comprehensive pest control tailored to each client. Our experienced professionals use cutting-edge techniques and environmentally friendly products to eradicate pests and provide lasting protection — whether it’s termites, rodents, bed bugs or anything else. Through thorough inspections, targeted treatments and ongoing monitoring, we prevent future infestations.', 'art:a-pest', 'Illustration of a bug inside a prohibited sign'),
    (8, 'Landscaping', 'landscaping', 'We provide exceptional horticultural services that enhance the beauty and vitality of your outdoor spaces — landscape design and installation, regular garden maintenance, plant care and pruning — for private residences and commercial properties alike. Our commitment to sustainability and environmentally friendly practices promotes the health and longevity of your plants and gardens, creating outdoor environments that delight for years to come.', 'art:a-land', 'Illustration of a tree and young plants'),
    ],
    extra_top='<figure class="banner reveal"><div class="frame frame--light"><div class="frame__in"><img src="assets/img/gallery/full/17.webp" alt="The USMS facility team lined up in uniform" width="1600" height="1068" loading="lazy"></div></div></figure>')
write('facility.html', facility)

maintenance = svc_page('maintenance', 'Maintenance Services – USMS Pvt Ltd', 'Reliable Maintenance Solution', 'Maintenance Services',
    'Keep your infrastructure in optimal condition. Whether it’s mechanical, electrical, plumbing, or fire and safety systems, our experts provide reliable maintenance for the smooth operation of your facility — including sewage treatment plants (STP) and water treatment plants (WTP).',
    '<div class="art art--hero" role="img" aria-label="Illustration of a gear"><svg viewBox="0 0 96 96" aria-hidden="true"><use href="#a-mech"/></svg></div>', [
    (1, 'Mechanical', 'mechanical', 'We offer a comprehensive range of mechanical services. Our skilled technicians deliver top-notch HVAC services — installation, maintenance and repair of air-conditioning units for optimal performance and efficiency — and our expertise extends to chiller systems, including maintenance, troubleshooting and repairs that keep operation uninterrupted and efficient.', 'art:a-mech', 'Illustration of a gear and a cooling symbol'),
    (2, 'Electrical', 'electrical', 'Our highly skilled, certified electricians cover residential, commercial and industrial needs — from installations and repairs to maintenance, troubleshooting and upgrades. Whether it’s wiring, lighting, panel upgrades, circuit installation or electrical safety inspections, we deliver reliable, efficient solutions that comply with industry standards.', 'art:a-elec', 'Illustration of a lightning bolt'),
    (3, 'Plumbing', 'plumbing', 'Our skilled plumbers use the latest tools and techniques to handle any plumbing issue efficiently — a leaking faucet, a clogged drain, a burst pipe or a complete system installation. We prioritise prompt, reliable service so your plumbing stays in optimal condition, for residential and commercial properties alike.', 'art:a-plumb', 'Illustration of a pipe and a water drop'),
    ])
write('maintenance.html', maintenance)

# ============================== CONTACT ==============================
contact = head('Contact Us – USMS Pvt Ltd', 'Get in touch with USMS Pvt Ltd, Indore – phone 0731-4230508, email corp.uniquely@gmail.com.', 'contact')
contact += f'''
<section class="phero phero--solo"><div class="phero__bg" aria-hidden="true"></div><div class="grain" aria-hidden="true"></div>
<div class="wrap phero__in"><div>
<nav class="crumbs reveal" aria-label="Breadcrumb"><a href="index.html">Home</a><i></i><span>Contact Us</span></nav>
<span class="eyebrow eyebrow--gold reveal">Get in touch with us</span>
<h1 class="reveal">Contact <em>Us</em></h1></div></div></section>
<section class="section"><div class="wrap contact-grid">
<div class="ccards">
<a class="ccard reveal" href="tel:{PHONE_T}"><svg class="ic"><use href="#i-phone"/></svg><div><h3>Phone</h3><p>{PHONE}</p></div></a>
<a class="ccard reveal" href="mailto:{MAIL}"><svg class="ic"><use href="#i-mail"/></svg><div><h3>Email</h3><p>{MAIL}</p></div></a>
<div class="ccard reveal"><svg class="ic"><use href="#i-pin"/></svg><div><h3>Office</h3><address><strong>{COMPANY}</strong><br>{ADDR}</address><a class="link mapbtn" href="{MAPS}" target="_blank" rel="noopener noreferrer">Open in Maps <svg><use href="#i-arrow"/></svg></a></div></div>
</div>
<form class="form reveal" id="enquiry" method="post" action="contact.html" autocomplete="on" novalidate>
<h2>Get in touch <em>with us</em></h2>
<label>Your Name<input name="name" type="text" autocomplete="name" placeholder="Your Name" required minlength="2" maxlength="80"></label>
<label>Contact Number<input name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="Contact Number" required maxlength="20"></label>
<label class="form__full">Email ID<input name="email" type="email" autocomplete="email" placeholder="Email ID" maxlength="120"></label>
<label class="form__full">Service<select name="service"><option>Security</option><option>Facility</option><option>Maintenance</option><option>Other</option></select></label>
<label class="form__full">Message<textarea name="message" rows="4" placeholder="Message" maxlength="800"></textarea></label>
<button class="btn btn--red form__full" type="submit">Submit <svg><use href="#i-arrow"/></svg></button>
<p class="form__note form__full" role="status" aria-live="polite"></p>
</form></div></section>
'''
contact += FOOT
write('contact.html', contact)

# ============================== GALLERY ==============================
GAL = [(1, 'security', 'USMS guards standing in formation on a parade ground'), (2, 'security', 'USMS security team greeting with folded hands outside a hospital'),
       (3, 'security', 'Three USMS security guards standing at attention'), (4, 'security', 'A USMS guard writing in the visitor register'),
       (5, 'security', 'USMS guards assisting at the hospital gate'), (6, 'security', 'The USMS security team outside Shalby Hospital'),
       (7, 'security', 'A man and woman USMS security guard'), (8, 'security', 'A USMS guard at the hospital entrance'),
       (9, 'security', 'USMS guards assisting at the hospital gate'), (10, 'security', 'A USMS guard at the reception desk'),
       (11, 'security', 'USMS security guards at the 24 hour pharmacy'), (12, 'security', 'A USMS guard on duty at the help desk'),
       (13, 'security', 'Three USMS security guards in front of a notice board'), (14, 'security', 'USMS armed guards with rifles'),
       (15, 'facility', 'The USMS facility and support team in a hospital corridor'), (16, 'facility', 'A USMS housekeeping staff member sanitising a hospital ward'),
       (17, 'facility', 'The USMS housekeeping team lined up in uniform'), (18, 'facility', 'A USMS housekeeping staff member cleaning a hospital room'),
       (19, 'facility', 'A USMS housekeeping staff member mopping a hospital ward'), (20, 'facility', 'A USMS housekeeping staff member mopping a hospital ward'),
       (21, 'facility', 'A USMS housekeeping staff member cleaning a laboratory'), (22, 'facility', 'A USMS housekeeping staff member mopping a laboratory floor'),
       (23, 'facility', 'A USMS housekeeping staff member mopping the hospital lobby')]
gal = head('Gallery – USMS Pvt Ltd', 'Photos of the USMS security and facility teams at work.', 'gallery')
gal += f'''
<section class="phero phero--solo"><div class="phero__bg" aria-hidden="true"></div><div class="grain" aria-hidden="true"></div>
<div class="wrap phero__in"><div>
<nav class="crumbs reveal" aria-label="Breadcrumb"><a href="index.html">Home</a><i></i><span>Gallery</span></nav>
<span class="eyebrow eyebrow--gold reveal">Our people at work</span>
<h1 class="reveal"><em>Gallery</em></h1></div></div></section>
<section class="section"><div class="wrap">
<div class="filters reveal" role="group" aria-label="Filter photos"><button class="on" data-f="all">All</button><button data-f="security">Security</button><button data-f="facility">Facility</button></div>
<div class="gallery">
{''.join(f'<figure data-cat="{c}" data-full="assets/img/gallery/full/{i:02d}.webp"><img src="assets/img/gallery/{i:02d}.webp" alt="{t}" width="640" height="427" loading="lazy"></figure>' for i, c, t in GAL)}
</div></div></section>
<div class="lb" role="dialog" aria-modal="true" aria-label="Photo viewer"><button class="x" aria-label="Close">✕</button><button class="pv" aria-label="Previous">‹</button><img alt=""><button class="nx" aria-label="Next">›</button></div>
{cta()}
'''
gal += FOOT
write('gallery.html', gal)
print('built')
