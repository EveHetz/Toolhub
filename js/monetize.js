/*!
 * Toolhub monetization & consent — privacy-respecting boot.
 *
 * Edit window.TOOLHUB_CONFIG (set on the page before this loads, OR fill the
 * defaults in this file once you have your IDs):
 *   adsenseClientId    'ca-pub-XXXXXXXXXXXXXXXX'   // empty = no ads
 *   adSlotIds          { content, footer, indexTop, indexBottom }
 *   digitalOceanRef    'https://m.do.co/c/XXXX'    // empty = no affiliate
 *   githubSponsorsUrl  'https://github.com/sponsors/EveHetz'
 *
 * Behaviour:
 *   - No third-party requests until the visitor explicitly consents
 *     (or the site has no AdSense client configured, in which case
 *     consent is irrelevant and the banner doesn't appear).
 *   - Consent choice is stored in localStorage as 'toolhub:consent'
 *     ('granted' | 'denied'). Resettable.
 *   - Ad slot DIVs (`<div class="ad-slot" data-slot="content"></div>`)
 *     are populated post-consent; otherwise removed cleanly.
 *   - Footer affiliate + sponsor links rendered into
 *     `[data-toolhub-footer-extras]` if configured.
 */
(function () {
  "use strict";

  // ----- Defaults — overwrite these once you have real IDs --------------
  const DEFAULTS = {
    adsenseClientId: "",                                   // e.g. 'ca-pub-1234567890123456'
    adSlotIds: {                                           // AdSense slot IDs (data-ad-slot)
      content: "",
      footer: "",
      indexTop: "",
      indexBottom: "",
    },
    digitalOceanRef: "",                                   // e.g. 'https://m.do.co/c/abc123def456'
    githubSponsorsUrl: "",                                 // e.g. 'https://github.com/sponsors/EveHetz'
  };
  const cfg = Object.assign({}, DEFAULTS, window.TOOLHUB_CONFIG || {});
  cfg.adSlotIds = Object.assign({}, DEFAULTS.adSlotIds, (window.TOOLHUB_CONFIG || {}).adSlotIds || {});
  window.TOOLHUB_CONFIG = cfg;

  // ----- i18n strings ----------------------------------------------------
  const LANG = (document.documentElement.lang || "en").slice(0, 2).toLowerCase();
  const I18N = {
    en: {
      banner: "We use cookies to serve relevant ads. Anonymous Plausible analytics runs either way and never uses cookies.",
      accept: "Accept",
      reject: "Reject",
      learn:  "Privacy",
      sponsor: "Sponsor on GitHub",
      hosting: "Hosting recommendation",
      adLabel: "Advertisement",
    },
    de: {
      banner: "Wir verwenden Cookies, um relevante Anzeigen zu zeigen. Anonyme Plausible-Statistiken laufen ohne Cookies.",
      accept: "Akzeptieren",
      reject: "Ablehnen",
      learn:  "Datenschutz",
      sponsor: "Auf GitHub sponsern",
      hosting: "Hosting-Empfehlung",
      adLabel: "Werbung",
    },
    es: {
      banner: "Usamos cookies para mostrar anuncios relevantes. Las estadísticas anónimas de Plausible funcionan sin cookies.",
      accept: "Aceptar",
      reject: "Rechazar",
      learn:  "Privacidad",
      sponsor: "Patrocinar en GitHub",
      hosting: "Recomendación de hosting",
      adLabel: "Publicidad",
    },
    fr: {
      banner: "Nous utilisons des cookies pour afficher des annonces pertinentes. Plausible (statistiques anonymes) fonctionne sans cookies.",
      accept: "Accepter",
      reject: "Refuser",
      learn:  "Confidentialité",
      sponsor: "Sponsoriser sur GitHub",
      hosting: "Recommandation d'hébergement",
      adLabel: "Publicité",
    },
    it: {
      banner: "Usiamo cookie per mostrare annunci pertinenti. Le statistiche anonime di Plausible non usano cookie.",
      accept: "Accetta",
      reject: "Rifiuta",
      learn:  "Privacy",
      sponsor: "Sponsorizza su GitHub",
      hosting: "Hosting consigliato",
      adLabel: "Pubblicità",
    },
  };
  const t = I18N[LANG] || I18N.en;

  // ----- Consent storage ------------------------------------------------
  const CONSENT_KEY = "toolhub:consent";
  function getConsent() {
    try { return localStorage.getItem(CONSENT_KEY) || ""; } catch (_) { return ""; }
  }
  function setConsent(v) {
    try { localStorage.setItem(CONSENT_KEY, v); } catch (_) { /* private mode */ }
  }
  window.toolhubConsentGiven = function () { return getConsent() === "granted"; };
  window.toolhubResetConsent = function () { setConsent(""); location.reload(); };

  // ----- Footer extras (sponsor + affiliate) ---------------------------
  function renderFooterExtras() {
    const slot = document.querySelector("[data-toolhub-footer-extras]");
    if (!slot) return;
    const parts = [];
    if (cfg.githubSponsorsUrl) {
      parts.push(`<a href="${cfg.githubSponsorsUrl}" target="_blank" rel="noopener noreferrer">♥ ${t.sponsor}</a>`);
    }
    if (cfg.digitalOceanRef) {
      parts.push(`<a href="${cfg.digitalOceanRef}" target="_blank" rel="noopener sponsored" data-affiliate="digitalocean">${t.hosting}</a>`);
    }
    if (parts.length) slot.innerHTML = parts.join(" · ");
  }

  // ----- Consent banner -------------------------------------------------
  function showConsentBanner() {
    if (document.getElementById("toolhub-consent")) return;
    const div = document.createElement("div");
    div.id = "toolhub-consent";
    div.setAttribute("role", "dialog");
    div.setAttribute("aria-label", "Cookie consent");
    div.innerHTML = `
      <div class="toolhub-consent-inner">
        <p class="toolhub-consent-msg">${t.banner}
          <a href="/privacy/" class="toolhub-consent-learn">${t.learn} →</a>
        </p>
        <div class="toolhub-consent-actions">
          <button type="button" class="toolhub-consent-btn toolhub-consent-reject">${t.reject}</button>
          <button type="button" class="toolhub-consent-btn toolhub-consent-accept">${t.accept}</button>
        </div>
      </div>
    `;
    document.body.appendChild(div);
    document.querySelector(".toolhub-consent-accept").addEventListener("click", function () {
      setConsent("granted");
      div.remove();
      bootAdsense();
      renderAdSlots();
    });
    document.querySelector(".toolhub-consent-reject").addEventListener("click", function () {
      setConsent("denied");
      div.remove();
      removeAdSlots();
    });
  }

  // ----- AdSense bootstrap ---------------------------------------------
  let adsenseLoaded = false;
  function bootAdsense() {
    if (adsenseLoaded || !cfg.adsenseClientId) return;
    const s = document.createElement("script");
    s.async = true;
    s.crossOrigin = "anonymous";
    s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + encodeURIComponent(cfg.adsenseClientId);
    document.head.appendChild(s);
    adsenseLoaded = true;
  }

  function renderAdSlots() {
    if (!cfg.adsenseClientId) return;
    document.querySelectorAll(".ad-slot[data-slot]").forEach(function (el) {
      if (el.dataset.rendered) return;
      const slotKey = el.getAttribute("data-slot");
      const slotId = cfg.adSlotIds[slotKey] || "";
      if (!slotId) return; // no slot ID → leave empty (no error)
      el.innerHTML =
        '<div class="ad-label">' + t.adLabel + "</div>" +
        '<ins class="adsbygoogle" style="display:block" data-ad-client="' +
        cfg.adsenseClientId + '" data-ad-slot="' + slotId +
        '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (_) {}
      el.dataset.rendered = "1";
    });
  }

  function removeAdSlots() {
    document.querySelectorAll(".ad-slot[data-slot]").forEach(function (el) { el.remove(); });
  }

  // ----- Boot ----------------------------------------------------------
  function boot() {
    renderFooterExtras();

    // No AdSense client → nothing to consent to. Just remove ad slots.
    if (!cfg.adsenseClientId) {
      removeAdSlots();
      return;
    }
    const consent = getConsent();
    if (consent === "granted") {
      bootAdsense();
      renderAdSlots();
    } else if (consent === "denied") {
      removeAdSlots();
    } else {
      showConsentBanner();
    }
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
