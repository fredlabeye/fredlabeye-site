# fredlabeye.com

Site personnel de Fred Labeye, cinematographer (HTML/CSS/JS pur, sans dépendance).

- Page : `index.html` (+ `404.html`), générée par `_source/build.py` à partir de `_source/site.json` (textes et projets)
- Styles : `assets/css/site.css` — Scripts : `assets/js/site.js`
- Médias : `assets/media/` (reel et aperçus vidéo), `assets/img/` (images des projets)
- Les films complets restent sur Vimeo
- Hébergement : statichost.eu (`statichost.yml`), publication automatique à chaque push

Ajouter ou modifier un projet : éditer `_source/site.json`, puis `python3 _source/build.py`.
