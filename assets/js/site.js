/* fredlabeye.com — scripts (aucune dépendance) */
(function () {
  "use strict";
  var canHover = window.matchMedia && window.matchMedia("(hover: hover)").matches;

  /* Reel d'introduction : boucle muette, plein écran avec le son au clic */
  var reel = document.querySelector(".reel");
  if (reel) {
    var bg = reel.querySelector("video");
    var close = reel.querySelector(".reel-close");
    var full = false;
    var openFull = function () {
      if (full) return;
      full = true;
      reel.classList.add("full");
      window.scrollTo({ top: 0, behavior: "smooth" });
      var hd = reel.getAttribute("data-full");
      if (hd && bg.getAttribute("src") !== hd) {
        bg.src = hd;
        bg.addEventListener("loadedmetadata", function once() {
          bg.removeEventListener("loadedmetadata", once);
          try { bg.currentTime = 0; } catch (e) {}
        });
      } else { bg.currentTime = 0; }
      bg.muted = false;
      bg.loop = false;
      bg.controls = false;
      bg.play();
      close.focus();
    };
    var exitFull = function (e) {
      if (e) e.stopPropagation();
      if (!full) return;
      full = false;
      reel.classList.remove("full");
      bg.muted = true;
      bg.loop = true;
      bg.play();
    };
    reel.addEventListener("click", function (e) { if (!full) openFull(); });
    reel.addEventListener("keydown", function (e) { if ((e.key === "Enter" || e.key === " ") && !full) { e.preventDefault(); openFull(); } });
    close.addEventListener("click", exitFull);
    bg.addEventListener("ended", function () { exitFull(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") exitFull(); });
    /* met la vidéo en pause quand elle sort de l'écran */
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (en) {
        en.forEach(function (x) { if (x.isIntersecting) bg.play().catch(function () {}); else bg.pause(); });
      }).observe(reel);
    }
  }

  /* Aperçus vidéo : lecture au survol (ordinateur) ou à l'écran (mobile) */
  var previews = document.querySelectorAll("[data-preview]");
  previews.forEach(function (el) {
    var v = el.querySelector("video");
    if (!v) return;
    var load = function () { if (!v.src) v.src = v.getAttribute("data-src"); };
    if (canHover) {
      el.addEventListener("mouseenter", function () { load(); v.play().catch(function () {}); });
      el.addEventListener("mouseleave", function () { v.pause(); });
    } else if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (en) {
        en.forEach(function (x) {
          if (x.isIntersecting) { load(); v.style.opacity = 1; v.play().catch(function () {}); }
          else { v.pause(); }
        });
      }, { threshold: 0.6 }).observe(el);
    }
  });

  /* Lecteur Vimeo plein écran */
  var player = document.querySelector(".player");
  if (player) {
    var frame = player.querySelector(".player-frame");
    var pinfos = player.querySelector(".infos");
    var pclose = player.querySelector(".player-close");
    var last = null;
    var shut = function () {
      player.classList.remove("open");
      frame.innerHTML = "";
      document.body.style.overflow = "";
      if (last) last.focus();
    };
    document.querySelectorAll("[data-vimeo]").forEach(function (b) {
      b.addEventListener("click", function (ev) {
        ev.preventDefault();
        last = b;
        if (reel && reel.classList.contains("full")) reel.querySelector(".reel-close").click();
        var f = document.createElement("iframe");
        f.src = "https://player.vimeo.com/video/" + b.getAttribute("data-vimeo") + "?autoplay=1&dnt=1&title=0&byline=0&portrait=0";
        f.allow = "autoplay; fullscreen; picture-in-picture";
        f.allowFullscreen = true;
        f.title = b.getAttribute("aria-label") || "Vidéo";
        frame.innerHTML = "";
        frame.appendChild(f);
        var src = b.closest(".case");
        var inf = src ? src.querySelector(".infos") : null;
        pinfos.innerHTML = inf ? inf.innerHTML : "";
        pinfos.style.display = inf ? "" : "none";
        player.classList.add("open");
        document.body.style.overflow = "hidden";
        pclose.focus();
      });
    });
    pclose.addEventListener("click", shut);
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && player.classList.contains("open")) shut(); });
  }
})();
