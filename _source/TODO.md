# Chantier fredlabeye.com — état au 12 octobre 2026

## Fait
- Site reconstruit à l'identique en statique (dépôt fredlabeye/fredlabeye-site), hébergé sur statichost.eu — site « fredlabeye », formule Starter 9 €/mois (prise le 12/10/2026, couvre aussi jekyllnhyde.com)
- Adresse provisoire : https://fredlabeye.statichost.page — publication automatique à chaque push (webhook GitHub OK)
- DNS repris chez Gandi LiveDNS le 12/10/2026, Cloudflare sorti du circuit : @ A 95.217.26.94, @ AAAA 2a01:4f9:c01f:8002::, www CNAME fredlabeye.statichost.page.
- Mail hello@ conservé chez Gandi : MX spool/fb.mail.gandi.net, SPF, DKIM gm1/gm2/gm3._domainkey, SRV, webmail — ne pas toucher
- static.fredlabeye.com supprimé (les médias sont dans le site)
- statichost redirige fredlabeye.com -> www.fredlabeye.com ; canonical, sitemap et robots.txt alignés sur https://www.fredlabeye.com/
- Textes corrigés : « looking forward to new challenges! », « © 2026 Fred Labeye ». Laissés tels quels à la demande de Fred : « after 10 years », « shorts, longs and series »
- Ancien hébergeur prévenu : pas de renouvellement en janvier 2027

## À faire
1. **Contrôle après propagation** (caches DNS jusqu'à 3 h, Gandi annonce 12–24 h pour le changement de serveurs de noms) : www et domaine nu en HTTPS, redirection vers www, mail hello@ (envoi + réception)
2. **Google Search Console** : ajouter fredlabeye.com (propriété Domaine), envoyer https://www.fredlabeye.com/sitemap.xml, demander l'indexation de la page d'accueil
3. **Reel** : Fred fournit l'export master (ProRes ou H.264 haut débit) → réencoder reel.mp4 (~4–5 Mbit/s, 1080p, avec son) et reel-bg.mp4 (fond, 1080p allégé). Le fichier actuel vient du site d'origine, déjà compressé à 1,45 Mbit/s
4. Plus tard : supprimer le site du compte Cloudflare s'il existe (sans urgence)
