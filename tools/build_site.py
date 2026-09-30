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
ADDR = 'J-148, LIG Colony, Behind MIG Police Station, Indore, Madhya Pradesh, 452011'
MAPS = 'https://www.google.com/maps/search/?api=1&query=' + ADDR.replace(' ', '+')

SPRITE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
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

NAV = [('index.html', 'Home', 'home'), ('about.html', 'About Us', 'about'), ('SERVICES', 'Our Services', 'services'),
       ('gallery.html', 'Gallery', 'gallery'), ('contact.html', 'Contact Us', 'contact')]


def head(title, desc, page):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#060a1e">
<link rel="icon" type="image/png" href="assets/img/emblem.png">
<link rel="preload" href="assets/fonts/fraunces-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/manrope-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">
<script>document.documentElement.classList.add('js');</script>
</head>
<body data-page="{page}">
<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"></div>
{SPRITE}
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
<p class="lead hero__lead reveal">At USMS, we are dedicated to providing comprehensive and reliable services in the areas of security, facility management, and maintenance. With our team of highly trained professionals and years of industry experience, we strive to deliver top-notch solutions tailored to your specific needs.</p>
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
<article class="panel active" data-href="security.html" tabindex="0"><div class="panel__bg" style="background-image:url(assets/img/hero/1.webp)"></div><span class="panel__no">01</span><svg class="panel__icon"><use href="#i-shield"/></svg>
<div class="panel__body"><h3>Security</h3><div class="panel__more"><p>Our security services are designed to provide you with peace of mind and ensure the safety of your premises. From highly trained security guards to advanced technology solutions, we offer a comprehensive range of security services tailored to your specific needs.</p><a class="link" href="security.html">Know More <svg><use href="#i-arrow"/></svg></a></div></div></article>
<article class="panel" data-href="facility.html" tabindex="0"><div class="panel__bg" style="background-image:url(assets/img/hero/4.webp)"></div><span class="panel__no">02</span><svg class="panel__icon"><use href="#i-building"/></svg>
<div class="panel__body"><h3>Facility</h3><div class="panel__more"><p>Our facility management services are geared towards creating a comfortable and well-maintained environment for your premises. From professional housekeeping to pest control and landscaping, we strive to enhance the overall experience of your facility, making it a pleasant place for everyone.</p><a class="link" href="facility.html">Know More <svg><use href="#i-arrow"/></svg></a></div></div></article>
<article class="panel" data-href="maintenance.html" tabindex="0"><div class="panel__bg" style="background-image:url(assets/img/svc/electrical.webp)"></div><span class="panel__no">03</span><svg class="panel__icon"><use href="#i-wrench"/></svg>
<div class="panel__body"><h3>Maintenance</h3><div class="panel__more"><p>Our maintenance services are aimed at keeping your infrastructure in optimal condition. Whether it’s mechanical, electrical, plumbing, or fire and safety systems, our team of experts provides reliable maintenance solutions to ensure the smooth operation of your facility. We also specialize in the maintenance of sewage treatment plants (STP) and water treatment plants (WTP).</p><a class="link" href="maintenance.html">Know More <svg><use href="#i-arrow"/></svg></a></div></div></article>
</div></div></section>

<section class="section section--ivory" id="about"><div class="wrap about">
<div class="about__visual reveal" aria-hidden="true"><div class="about__year">2012</div><img class="about__emblem" src="assets/img/emblem.png" alt="" width="210" height="170"></div>
<div class="about__copy reveal"><span class="eyebrow">Who We Are</span><h2 class="h2">About <em>Us</em></h2>
<p>USMS Pvt. Ltd. is a leading Integrated Facility Management services provider, delivering tailored solutions since 2012. With a strong network across multiple states, we prioritize operational excellence, sustainability, and client commitment. Our dedicated team upholds core values of discipline, transparency, and mutual respect to ensure high-quality security, facility, and maintenance services for various industries and sectors.</p>
<ul class="chips"><li>Discipline</li><li>Transparency</li><li>Mutual Respect</li></ul>
<a class="btn btn--primary" href="about.html">Know More <svg><use href="#i-arrow"/></svg></a></div>
</div></section>

<section class="section section--dark" id="sectors"><div class="wrap">
<header class="sec-head reveal"><span class="eyebrow eyebrow--gold">Industries</span><h2>Sectors we <em>serve</em></h2><p>Over the years, we have been successfully serving a wide range of operations.</p></header>
<ol class="sectors reveal">{''.join(f'<li><span>{i:02d}</span><b>{n}</b></li>' for i, n in enumerate(['Telecom industries', 'Manufacturing units', 'Residential townships', 'Retail malls', 'Commercial buildings', 'Hospitals', 'Banks', 'Educational institutes', 'Construction sites'], 1))}</ol>
</div></section>

<section class="section" id="team"><div class="wrap">
<header class="sec-head sec-head--center reveal"><span class="eyebrow">The people</span><h2>Our <em>Team</em></h2><p>At USMS, we have a dedicated and skilled team of professionals who are committed to providing the highest level of service to our clients. Our team consists of experts in various fields, including security, facility management, and maintenance. Each team member brings a wealth of knowledge and experience to ensure that we deliver exceptional results. Get to know some of our key team members below:</p></header>
<p class="team__label eyebrow reveal" style="display:flex;justify-content:center">Management Team</p>
<div class="people">
<figure class="person reveal"><div class="person__photo"><img src="assets/img/team/ms-chauhan.webp" alt="M S Chauhan" width="399" height="450" loading="lazy"></div><figcaption><strong>M S Chauhan</strong><span>Director</span></figcaption></figure>
<figure class="person reveal"><div class="person__photo"><img src="assets/img/team/gajendra-singh-chauhan.webp" alt="Gajendra Singh Chauhan" width="798" height="900" loading="lazy"></div><figcaption><strong>Gajendra Singh Chauhan</strong><span>Managing Director</span></figcaption></figure>
</div></div></section>
'''
CLIENTS = [('ism-toys', 'ISM Toys'), ('bcm', 'BCM Group'), ('anand', 'Anand Hospital'), ('vyapaar', 'Vyapaar Vistaar'), ('vantage', 'Vantage'), ('unique', 'Unique Hospital'), ('shree-maruti', 'Shree Maruti'), ('shalby', 'Shalby Hospitals'), ('sankara', 'Sankara Eye Foundation, India'), ('punjab', 'Punjab Jewels'), ('prataap', 'Prataap Snacks Limited'), ('nepra', 'Nepra'), ('lifefirst', 'LifeFirst Pharma'), ('life-care-logistic', 'Life Care Logistic'), ('hnh', 'H&amp;h'), ('dp-jewellers', 'D.P. Jewellers'), ('care-chl', 'CARE CHL Hospitals')]
def mq(items, cls=''):
    lis = ''.join(f'<li><img src="assets/img/clients/{f}.webp" alt="{a}" loading="lazy"></li>' for f, a in items)
    return f'<div class="marquee {cls}" aria-label="Our valued clients"><ul class="marquee__track">{lis}</ul></div>'
home += f'''<section class="section clients" id="clients"><div class="wrap"><header class="sec-head sec-head--center reveal"><span class="eyebrow">Trusted by</span><h2>Valued <em>Clients</em></h2></header></div>
{mq(CLIENTS[:9])}{mq(CLIENTS[9:] + CLIENTS[:2], 'marquee--rev')}</section>
{cta()}
'''
home += FOOT
write('index.html', home)

# ============================== ABOUT ==============================
about = head('About Us – USMS Pvt Ltd', 'USMS stands for Uniquely Security and Management Solutions, established in 2012 by a retired senior police officer.', 'about')
about += f'''
<section class="phero"><div class="phero__bg" aria-hidden="true"></div><div class="grain" aria-hidden="true"></div>
<div class="wrap phero__in"><div>
<nav class="crumbs reveal" aria-label="Breadcrumb"><a href="index.html">Home</a><i></i><span>About Us</span></nav>
<span class="eyebrow eyebrow--gold reveal">Uniquely Security and Management Solutions</span>
<h1 class="reveal">About <em>Us</em></h1>
<p class="lead reveal">USMS stands for Uniquely Security and Management Solutions, established in 2012 by a retired senior police officer.</p></div>
<div class="reveal"><div class="frame phero__frame"><div class="frame__in"><img src="assets/img/hero/6.webp" alt="USMS guards standing in formation on a parade ground under trees" width="1200" height="801"></div></div></div>
</div></section>

<section class="section"><div class="wrap story">
<div class="reveal"><p class="story__lead">USMS Pvt. Ltd. is one of the fastest leading <em>Integrated Facility Management</em> services providers who offers the meticulously crafted and comprehensive services tailored as per specific needs.</p></div>
<ul class="story__pts">
<li class="reveal"><span>01</span><p>Over the years, we have been successfully serving a wide range of operations including telecom industries, manufacturing units, residential townships, retail mall, commercial buildings, hospitals, bankings, educational Institutes, construction sites.</p></li>
<li class="reveal"><span>02</span><p>Our primary focus is to deliver effective solutions that are both efficient and affordable through operational excellence, commercial prudence, Sustainability and highest standard.</p></li>
<li class="reveal"><span>03</span><p>Since inception USMS has expanded its footprint and established a robust network spanning Madhya Pradesh, Chhattisgarh, Uttar Pradesh, and Rajasthan and upheld the highest level of commitment through quality service in security, facility &amp; maintenance to our clients.</p></li>
<li class="reveal"><span>04</span><p>Our dedicated team of professionals adhere to fundamental principles of discipline, attitude, and commitment and form a strong relationship through transparency, trust and mutual respect that are integral to our core value system.</p></li>
</ul></div></section>

<section class="section section--dark"><div class="wrap">
<header class="sec-head reveal"><span class="eyebrow eyebrow--gold">Our footprint</span><h2>Four states, <em>one standard</em></h2></header>
<ul class="states reveal"><li><b>Madhya Pradesh</b><span>Home state</span></li><li><b>Chhattisgarh</b><span>Network</span></li><li><b>Uttar Pradesh</b><span>Network</span></li><li><b>Rajasthan</b><span>Network</span></li></ul>
</div></section>

<section class="section section--ivory"><div class="wrap">
<header class="sec-head reveal"><span class="eyebrow">Industries</span><h2>Sectors we <em>serve</em></h2></header>
<ol class="sectors reveal">{''.join(f'<li><span>{i:02d}</span><b>{n}</b></li>' for i, n in enumerate(['Telecom industries', 'Manufacturing units', 'Residential townships', 'Retail malls', 'Commercial buildings', 'Hospitals', 'Banks', 'Educational institutes', 'Construction sites'], 1))}</ol>
</div></section>

<section class="section section--dark"><div class="wrap">
<header class="sec-head sec-head--center reveal"><span class="eyebrow eyebrow--gold">What guides us</span><h2>Mission, vision <em>&amp; value</em></h2></header>
<div class="mvv">
<article class="reveal"><svg><use href="#i-target"/></svg><h3>Our Mission</h3><p>USMS mission is to be the leading one-stop-solutions for client and exceed their specific and customised service needs by delivering the highest quality of professional services with trust and confidence.</p></article>
<article class="reveal"><svg><use href="#i-eye"/></svg><h3>Our Vision</h3><p>USMS vision is to be the most professional leader among services provider industry by exceeding our customers expectations creating trustworthy partnership with client and value every employee.</p></article>
<article class="reveal"><svg><use href="#i-gem"/></svg><h3>Our Value</h3><p>USMS value trustworthy partnership, integrity, quality service, professional growth and community leadership</p></article>
</div></div></section>
{cta()}
'''
about += FOOT
write('about.html', about)


# ============================== SERVICE PAGES ==============================
def block(i, title, anchor, text, img, alt, kind=''):
    cls = {'': '', 'tall': ' block__media--tall', 'art': ' block__media--art'}[kind]
    return f'''<article class="block" id="{anchor}"><div class="reveal"><span class="block__no">{i:02d}</span><h2>{title}</h2>{text}</div>
<div class="block__media{cls} reveal"><div class="frame frame--light"><div class="frame__in"><img src="{img}" alt="{alt}" loading="lazy"></div></div></div></article>'''


def svc_page(page, title, eyebrow, h1, intro, hero_img, hero_alt, blocks, icon, extra_top='', lead_html=None):
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
<div class="reveal"><div class="frame phero__frame"><div class="frame__in"><img src="{hero_img}" alt="{hero_alt}" width="1200" height="801"></div></div></div>
</div></section>

<section class="section"><div class="wrap">
{extra_top}
<div class="layout"><aside class="toc reveal" aria-label="On this page"><h4>On this page</h4>{toc}</aside>
<div><div class="glance reveal">{glance}</div>{body}</div></div>
</div></section>
{cta('Need <em>' + h1.split()[0].lower() + '</em> support? Let’s talk.')}
'''
    return p + FOOT


security = svc_page('security', 'Security Services – USMS Pvt Ltd', 'Comprehensive Security Solutions', 'Security Services',
    'Our security services are designed to provide you with peace of mind and ensure the safety of your premises. From highly trained security guards to advanced technology solutions, we offer a comprehensive range of security services tailored to your specific needs.',
    'assets/img/hero/1.webp', 'Three USMS armed guards in navy uniforms standing in front of a car', [
    (1, 'Security Guard', 'security-guard', '<p>At our security agency, we offer comprehensive security assessments for our clients. After evaluating their premises, we provide informed recommendations regarding their specific security requirements, including necessary equipment and personnel. Additionally, our training department is equipped to provide specialized training for individuals working in the retail sector. Over the year we have earned an outstanding reputation in the industry for delivering top-notch security services of guards, armed guards &amp; body guards.</p>', 'assets/img/hero/7.webp', 'Two USMS security guards and a woman guard at a hospital pharmacy entrance'),
    (2, 'Personal Protection', 'personal-protection', '<p>We take pride in our exceptional team of young, smart, and well-groomed professionals. Our Personal Protection Officers/ Escorts are meticulously selected and trained in martial arts and combat craft. They possess fluency in both English and Hindi, enabling seamless communication with clients. Our team excels in forming cohesive units, providing immediate and close protection to individuals requiring personal security.</p>', 'assets/img/svc/personal-protection.webp', 'A USMS personal protection officer in a navy uniform', 'tall'),
    (3, 'Armed Guard', 'armed-guard', '<p>Our agency is proud to employ a select group of exceptional individuals who embody youth, intelligence, and professionalism. These highly dedicated Personal Protection Officers/ Escorts are fluent in both English and Hindi, and their training in martial arts and combat craft ensures their readiness for any situation. By working together seamlessly, they form an unbeatable team capable of providing immediate and close protection.</p>', 'assets/img/svc/armed-guard.webp', 'A USMS armed guard holding a rifle', 'tall'),
    (4, 'Security Consultancy', 'security-consultancy', '<p>We specialize in conducting comprehensive security surveys and appreciation for our esteemed clients. Our experienced team thoroughly assesses the existing security measures and identifies potential vulnerabilities. Based on our findings, we provide tailored advice and recommendations on a wide range of security needs, including equipment and manpower requirements necessary to enhance overall safety and protection.</p>', 'assets/img/svc/consultancy.webp', 'Two professionals shaking hands over a contract'),
    (5, 'Cash Management', 'cash-management', '<p>USMS offers security guard cash handling services to ensure the utmost safety and protection of your valuable assets. Our highly trained and professional guards are well-versed in handling cash transactions, adhering to strict protocols and security measures. They possess a deep understanding of risk management and equipped with necessary skills to detect and deter potential threats. They are reliable and proficient in secure cash transportation.</p>', 'assets/img/svc/cash-van.webp', 'Illustration of a bank cash van with a guard', 'art'),
    ], 'i-shield')
write('security.html', security)

facility = svc_page('facility', 'Facility Services – USMS Pvt Ltd', 'Enhancing Your Facility Experience', 'Facility Services',
    'Our facility management services are geared towards creating a comfortable and well-maintained environment for your premises. From professional housekeeping to pest control and landscaping, we strive to enhance the overall experience of your facility, making it a pleasant place for everyone.',
    'assets/img/hero/4.webp', 'USMS housekeeping and support staff lined up in a hospital corridor', [
    (1, 'House Keeping', 'house-keeping', '<p>USMS provides top-notch housekeeping services to ensure a clean and organized environment for our clients. Our team of dedicated professionals is committed to delivering exceptional cleaning solutions tailored to the unique needs of each client. From dusting and vacuuming to disinfecting and sanitizing, we strive to maintain the highest standards of cleanliness. With meticulous attention to detail, we leave no corner untouched, ensuring that every room is pristine and inviting. Our comprehensive housekeeping service guarantees a fresh and comfortable space, allowing our clients to focus on their core activities with peace of mind.</p>', 'assets/img/hero/5.webp', 'A USMS housekeeping staff member mopping a hospital laboratory floor'),
    (2, 'Office Boy', 'office-boy', '<p>Our Office Boy service is designed to cater to your administrative needs, ensuring a smooth and efficient work environment. Our dedicated and professional Office Boys are trained to handle various tasks such as document management, mail handling, inventory management, and general office upkeep. With their attention to detail and excellent organizational skills, they will ensure that your office operations run seamlessly, allowing you to focus on your core business activities.</p>', 'assets/img/svc/office-boy.webp', 'A smiling office attendant carrying a tray'),
    (3, 'Patience Care Service', 'patience-care', '<p>At USMS, we understand the importance of providing compassionate and personalized care for your loved ones. Our Patience Care service offers professional caregivers who are experienced in assisting individuals with patience and empathy. Whether it’s elderly care, post-surgery recovery, or special needs assistance, our caregivers are trained to provide the highest level of care and support. They will ensure the comfort, well-being, and safety of your loved ones, allowing you to have peace of mind knowing that they are in capable hands.</p>', 'assets/img/svc/patient-care.webp', 'A caregiver holding the hands of an elderly patient'),
    (4, 'Home Care', 'home-care', '<p>Our Home Care service provides personalized care in the comfort of your own home. Our caregivers assist with daily activities, medication management, meal preparation, and companionship, promoting independence and enhancing quality of life.</p>', 'assets/img/svc/home-care.webp', 'Two home care staff working in a kitchen'),
    (5, 'Façade Cleaning', 'facade-cleaning', '<p>USMS specializes in providing top-quality facade cleaning services that ensure the immaculate appearance and longevity of your building’s exterior. With a team of skilled professionals equipped with state-of-the-art equipment and environmentally friendly cleaning agents, we offer comprehensive solutions for removing dirt, grime, stains, and pollutants from all types of facades. Our meticulous approach guarantees a thorough and efficient cleaning process, leaving your building looking pristine and revitalized. From high-rise buildings to residential complexes. Trust us to enhance the visual appeal of your property while preserving its structural integrity through our expert facade cleaning solutions.</p>', 'assets/img/svc/facade.webp', 'A technician cleaning a building facade on ropes'),
    (6, 'Pest Control', 'pest-control', '<p>USMS specializes in comprehensive pest control solutions tailored to meet the unique needs of our clients. With a team of highly skilled and experienced professionals, we employ cutting-edge techniques and environmentally friendly products to effectively eradicate pests and ensure long-lasting protection. Whether it’s termites, rodents, bed bugs, or any other pests, we take a proactive approach by conducting thorough inspections, implementing targeted treatments, and providing ongoing monitoring to prevent future infestations. Our commitment to customer satisfaction, coupled with our commitment to the environment, makes us the go-to choice for reliable and sustainable pest control services.</p>', 'assets/img/svc/pest-control.webp', 'A pest control technician in protective gear spraying'),
    (7, 'Landscaping', 'landscaping', '<p>USMS specializes in providing exceptional horticultural services to our valued clients. With a dedicated team of experienced professionals, we offer a comprehensive range of services designed to enhance the beauty and vitality of your outdoor spaces. Whether you require landscape design and installation, regular garden maintenance, or plant care and pruning, we have the expertise and passion to bring your vision to life. From private residences to commercial properties, we tailor our horticultural solutions to meet the unique needs and preferences of each client. With a commitment to sustainability and environmentally friendly practices, we ensure that our services promote the health and longevity of your plants and gardens. We strive to create stunning and sustainable outdoor environments that will delight and inspire you for years to come.</p>', 'assets/img/svc/landscaping.webp', 'A gardener trimming a hedge with shears'),
    ], 'i-building',
    extra_top='<figure class="banner reveal"><div class="frame frame--light"><div class="frame__in"><img src="assets/img/svc/facility-team.webp" alt="The USMS facility team lined up in uniform" loading="lazy"></div></div></figure>')
write('facility.html', facility)

maintenance = svc_page('maintenance', 'Maintenance Services – USMS Pvt Ltd', 'Reliable Maintenance Solution', 'Maintenance Services',
    'Our maintenance services are aimed at keeping your infrastructure in optimal condition. Whether it’s mechanical, electrical, plumbing, or fire and safety systems, our team of experts provides reliable maintenance solutions to ensure the smooth operation of your facility. We also specialize in the maintenance of sewage treatment plants (STP) and water treatment plants (WTP).',
    'assets/img/svc/electrical.webp', 'An electrician testing a distribution panel', [
    (1, 'Mechanical', 'mechanical', '<p>USMS offers a comprehensive range of mechanical services to meet the diverse needs of our clients. Our skilled technicians are proficient in delivering top-notch HVAC services, ensuring optimal performance and efficiency of air conditioning units. Whether it’s installation, maintenance, or repairs, we prioritize customer satisfaction by providing reliable and timely solutions. Additionally, our expertise extends to chiller systems, where we excel in offering professional services such as maintenance, troubleshooting, and repairs, guaranteeing uninterrupted operation and maximum efficiency. With our commitment to excellence and dedication to delivering exceptional mechanical services, we strive to create comfortable and functional environments for our valued customers.</p>', 'assets/img/svc/mechanical.webp', 'A mechanic working under the hood of a vehicle'),
    (2, 'Electrical', 'electrical', '<p>USMS specializes in providing comprehensive electrical services to meet the diverse needs of our clients. With a team of highly skilled and certified electricians, we offer a wide range of services encompassing residential, commercial, and industrial sectors. From electrical installations and repairs to maintenance, troubleshooting, and upgrades, we ensure that our clients receive top-notch solutions that are reliable, efficient, and compliant with industry standards. Whether it’s wiring, lighting, panel upgrades, circuit installations, or electrical safety inspections, our dedicated team is committed to delivering exceptional service, ensuring the utmost satisfaction of our valued customers.</p>', 'assets/img/svc/electrical.webp', 'An electrician testing a distribution panel'),
    (3, 'Plumbing', 'plumbing', '<p>USMS is proud to offer comprehensive plumbing services that cater to all your needs. Our highly skilled team of professional plumbers is equipped with the latest tools and techniques to handle any plumbing issue efficiently and effectively. Whether it’s a leaky faucet, a clogged drain, a burst pipe, or a complete plumbing system installation, our experts are trained to deliver exceptional results. We prioritize customer satisfaction and provide prompt and reliable service, ensuring that your plumbing systems are in optimal condition. With our commitment to quality and expertise, you can trust us to deliver exceptional plumbing solutions for your residential or commercial property.</p>', 'assets/img/svc/plumbing.webp', 'A plumber fitting a water filter'),
    ], 'i-wrench')
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
<div class="ccard reveal"><svg class="ic"><use href="#i-pin"/></svg><div><h3>Address</h3><address style="color:var(--muted);font-weight:600">{ADDR}</address><a class="link mapbtn" href="{MAPS}" target="_blank" rel="noopener">Open in Maps <svg><use href="#i-arrow"/></svg></a></div></div>
</div>
<form class="form reveal" id="enquiry" novalidate>
<h2>Get in touch <em>with us</em></h2>
<label>Your Name<input name="name" type="text" autocomplete="name" placeholder="Your Name" required></label>
<label>Contact Number<input name="phone" type="tel" autocomplete="tel" placeholder="Contact Number" required></label>
<label class="form__full">Email ID<input name="email" type="email" autocomplete="email" placeholder="Email ID"></label>
<label class="form__full">Service<select name="service"><option>Security</option><option>Facility</option><option>Maintenance</option><option>Other</option></select></label>
<label class="form__full">Message<textarea name="message" rows="4" placeholder="Message"></textarea></label>
<button class="btn btn--red form__full" type="submit">Submit <svg><use href="#i-arrow"/></svg></button>
<p class="form__note form__full" role="status" aria-live="polite"></p>
</form></div></section>
'''
contact += FOOT
write('contact.html', contact)

# ============================== GALLERY ==============================
G = [('hero/1.webp', 'Armed guards', 'security', 1200, 801), ('hero/2.webp', 'Security team', 'security', 1200, 801), ('hero/3.webp', 'At the reception desk', 'security', 1200, 801),
     ('hero/4.webp', 'Facility team', 'facility', 1200, 801), ('hero/5.webp', 'Housekeeping', 'facility', 1200, 801), ('hero/6.webp', 'On parade', 'security', 1200, 801),
     ('hero/7.webp', 'Guards at the pharmacy', 'security', 1200, 801), ('svc/personal-protection.webp', 'Personal protection', 'security', 277, 390),
     ('svc/armed-guard.webp', 'Armed guard', 'security', 264, 402), ('svc/facility-team.webp', 'The facility team', 'facility', 1255, 534)]
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
{''.join(f'<figure data-cat="{c}"><img src="assets/img/{f}" alt="{t}" width="{w}" height="{h}" loading="lazy"><figcaption>{t}</figcaption></figure>' for f, t, c, w, h in G)}
</div></div></section>
<div class="lb" role="dialog" aria-modal="true" aria-label="Photo viewer"><button class="x" aria-label="Close">✕</button><button class="pv" aria-label="Previous">‹</button><img alt=""><button class="nx" aria-label="Next">›</button></div>
{cta()}
'''
gal += FOOT
write('gallery.html', gal)
print('built')
