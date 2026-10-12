#!/usr/bin/env python3
"""Génère index.html et 404.html de fredlabeye.com à partir de _source/site.json.

    python3 _source/build.py
"""
import json, html, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = json.load(open(os.path.join(ROOT, "_source", "site.json"), encoding="utf8"))
SITE = "https://fredlabeye.com"
V = "1"

ICONS = {
    "facebook": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M24 12a12 12 0 1 0-13.9 11.9v-8.4H7.1V12h3V9.4c0-3 1.8-4.7 4.6-4.7 1.3 0 2.7.2 2.7.2v3h-1.5c-1.5 0-2 .9-2 1.9V12h3.4l-.5 3.5h-2.9v8.4A12 12 0 0 0 24 12z"/></svg>',
    "instagram": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.8.1 3.3.1 4.8 1.7 4.9 4.9.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 3.2-1.7 4.8-4.9 4.9-1.3.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-3.3-.1-4.8-1.7-4.9-4.9C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8C2.4 3.9 3.9 2.4 7.2 2.3 8.4 2.2 8.8 2.2 12 2.2zM12 0C8.7 0 8.3 0 7.1.1 2.7.3.3 2.7.1 7.1 0 8.3 0 8.7 0 12s0 3.7.1 4.9c.2 4.4 2.6 6.8 7 7 1.2.1 1.6.1 4.9.1s3.7 0 4.9-.1c4.4-.2 6.8-2.6 7-7 .1-1.2.1-1.6.1-4.9s0-3.7-.1-4.9c-.2-4.4-2.6-6.8-7-7C15.7 0 15.3 0 12 0zm0 5.8a6.2 6.2 0 1 0 0 12.4 6.2 6.2 0 0 0 0-12.4zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.4-11.8a1.4 1.4 0 1 0 0 2.9 1.4 1.4 0 0 0 0-2.9z"/></svg>',
    "vimeo": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 0a12 12 0 1 0 0 24 12 12 0 0 0 0-24zm5.6 9.1c-.1 1.4-1 3.3-2.9 5.7-1.9 2.5-3.5 3.7-4.8 3.7-.8 0-1.5-.7-2-2.2l-1.1-4c-.4-1.5-.8-2.2-1.3-2.2-.1 0-.4.2-1 .7l-.6-.8c.7-.6 1.3-1.2 2-1.8.9-.8 1.6-1.2 2-1.2 1.1-.1 1.7.6 2 2.2.3 1.7.5 2.8.6 3.2.3 1.4.7 2.1 1 2.1.3 0 .7-.4 1.3-1.3.6-.9.9-1.6.9-2.1.1-.8-.2-1.2-.9-1.2-.3 0-.7.1-1 .2.7-2.2 2-3.2 3.9-3.2 1.4.1 2 1 1.9 2.4z"/></svg>',
}
SOCIAL = [("facebook", "Facebook", "https://www.facebook.com/fred.labeye"),
          ("instagram", "Instagram", "https://www.instagram.com/fredlabeye/"),
          ("vimeo", "Vimeo", "https://vimeo.com/fredlabeye")]
CLOCK = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'


def e(s):
    return html.escape(s, quote=True)


def social():
    return "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{ICONS[k]}</a>' for k, n, u in SOCIAL)


def tl(p):
    return f'<div class="type-length"><span class="type">{e(p["type"])}</span><span class="length">{CLOCK}{e(p["duration"])}</span></div>'


feat, others = [], []
for p in D["projects"]:
    vid = (f'<video muted loop playsinline preload="none" data-src="assets/media/{p["slug"]}.mp4"></video>')
    img = (f'<img src="assets/img/{p["slug"]}.webp" width="{p["iw"]}" height="{p["ih"]}" loading="lazy" decoding="async" '
           f'alt="{e(p["title"])} – {e(p["type"].lower())}, cinematography by Fred Labeye">')
    if p["featured"]:
        cols = "".join(f'<div class="col"><span class="cap">{e(c["title"])}</span>' + "".join(f'<span class="val">{e(b)}</span>' for b in c["body"]) + "</div>" for c in p["credits"])
        feat.append(f'''<article class="case">
<a class="preview" href="https://vimeo.com/{p["vimeo"]}" data-preview data-vimeo="{p["vimeo"]}" aria-label="Play {e(p["title"])}">
<div class="media">{img}{vid}</div>
<div class="case-title">{tl(p)}<h2>{e(p["title"])}</h2></div>
</a>
<div class="infos">{cols}</div>
</article>''')
    else:
        others.append(f'''<a class="thumb" href="https://vimeo.com/{p["vimeo"]}" data-preview data-vimeo="{p["vimeo"]}" aria-label="Play {e(p["title"])}">
<div class="media">{img}{vid}</div>
<h3>{e(p["title"])}</h3>{tl(p)}
</a>''')

works = [{"@type": "CreativeWork", "name": p["title"], "genre": p["type"], "url": f"https://vimeo.com/{p['vimeo']}"} for p in D["projects"]]
LD = {"@context": "https://schema.org", "@type": "Person", "name": "Fred Labeye", "jobTitle": "Cinematographer – Director of photography",
      "url": SITE + "/", "email": "hello@fredlabeye.com", "telephone": "+32478760289",
      "address": {"@type": "PostalAddress", "streetAddress": "Rue des Glands 70", "postalCode": "1190", "addressLocality": "Bruxelles", "addressCountry": "BE"},
      "sameAs": [s[2] for s in SOCIAL], "worksFor": {"@type": "Organization", "name": "Jekyll N'Hyde", "url": "https://jekyllnhyde.com/"},
      "subjectOf": works}

TITLE = "Fred Labeye - Cinematographer"
DESC = "Fred Labeye - Cinematographer - Director of photography. Based in Belgium, Brussels. Working on commercials, music videos and narrative (shorts, longs and series)."


def head(title, desc, canonical, extra=""):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#171515">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/montserrat-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css?v={V}">
{extra}
</head>'''


FOOT = f'''<footer class="footer"><div class="wrap">
<div>Fred Labeye<br>{e(D["copyright"])}</div>
<div><a href="mailto:hello@fredlabeye.com">hello@fredlabeye.com</a><br><a href="tel:+32478760289">+32 478 76 02 89</a></div>
<address style="font-style:normal">Rue des Glands 70,<br>1190 Bruxelles</address>
<div class="follow">Follow me <div class="social">{social()}</div></div>
</div></footer>'''

index = head(TITLE, DESC, SITE + "/", f'<script type="application/ld+json">{json.dumps(LD, ensure_ascii=False)}</script>') + f'''
<body>
<header class="header"><a class="name" href="/">Fred Labeye</a><nav class="social" aria-label="Social">{social()}</nav></header>
<main>
<section class="reel" data-full="assets/media/reel.mp4" tabindex="0" aria-label="Play the showreel with sound">
<img class="reel-poster" src="assets/img/reel-poster.webp" alt="" fetchpriority="high"><video autoplay muted loop playsinline src="assets/media/reel-bg.mp4"></video>
<h1 class="reel-title"><span class="t1">Fred Labeye /</span><span class="t2">Cinematographer</span></h1>
<span class="reel-play" aria-hidden="true"></span>
<span class="reel-scroll" aria-hidden="true"></span>
<button class="reel-close" aria-label="Close the showreel">&times;</button>
</section>
<section class="about wrap"><p>{e(D["intro"])}</p></section>
<section class="featured wrap" aria-label="Featured work">
{"".join(feat)}
</section>
<section class="others wrap" aria-label="More work">
{"".join(others)}
</section>
<section class="outro wrap"><p>{e(D["outro"])}</p></section>
<section class="contact wrap"><h2>Let’s Work Together</h2><a class="big" href="mailto:hello@fredlabeye.com">hello@fredlabeye.com</a></section>
</main>
{FOOT}
<div class="player" role="dialog" aria-modal="true" aria-label="Video player"><button class="player-close" aria-label="Close">&times;</button><div class="player-frame"></div><div class="infos"></div></div>
<script src="/assets/js/site.js?v={V}" defer></script>
</body>
</html>
'''
open(os.path.join(ROOT, "index.html"), "w", encoding="utf8").write(index)

nf = head("Page not found | Fred Labeye", "This page could not be found.", SITE + "/") + f'''
<body>
<header class="header"><a class="name" href="/">Fred Labeye</a><nav class="social" aria-label="Social">{social()}</nav></header>
<main><section class="wrap" style="padding:220px 20px 0"><h1 style="font-size:52px;line-height:1.15;margin:0 0 20px">Page not found</h1><p><a href="/" style="text-decoration:underline">Back to the homepage</a></p></section></main>
{FOOT}
</body>
</html>
'''
open(os.path.join(ROOT, "404.html"), "w", encoding="utf8").write(nf)
print("built")
