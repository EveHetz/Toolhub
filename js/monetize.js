/*!
 * Toolhub monetization & consent — privacy-respecting boot.
 *
 * Edit window.TOOLHUB_CONFIG (set on the page before this loads, OR fill the
 * defaults in this file once you have your IDs):
 *   deploy_env         'sandbox' | 'production' (default: 'sandbox')
 *   adsenseClientId    'ca-pub-XXXXXXXXXXXXXXXX'   // empty = no ads
 *   adSlotIds          { content, footer, indexTop, indexBottom }
 *   digitalOceanRef    'https://m.do.co/c/XXXX'    // empty = no affiliate
 *   githubSponsorsUrl  'https://github.com/sponsors/EveHetz'
 *   buyMeACoffeeUrl    'https://www.buymeacoffee.com/XXXX'
 *
 * Behaviour:
 *   - deploy_env === 'sandbox': adsbygoogle.js is NEVER loaded. Ad slots
 *     render as placeholder boxes and a small SANDBOX badge is shown.
 *   - deploy_env === 'production': AdSense loads only if adsenseClientId
 *     matches /^ca-pub-\d{16}$/. Invalid config falls back to placeholders
 *     and logs to console — broken config can't accidentally load ads.
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
    deploy_env: "sandbox",                                 // 'sandbox' | 'production'
    adsenseClientId: "",                                   // e.g. 'ca-pub-1234567890123456'
    adSlotIds: {                                           // AdSense slot IDs (data-ad-slot)
      content: "",
      footer: "",
      indexTop: "",
      indexBottom: "",
    },
    digitalOceanRef: "",                                   // e.g. 'https://m.do.co/c/abc123def456'
    githubSponsorsUrl: "",                                 // e.g. 'https://github.com/sponsors/EveHetz'
    buyMeACoffeeUrl: "",                                   // e.g. 'https://www.buymeacoffee.com/Tool_hub'
  };
  const cfg = Object.assign({}, DEFAULTS, window.TOOLHUB_CONFIG || {});
  cfg.adSlotIds = Object.assign({}, DEFAULTS.adSlotIds, (window.TOOLHUB_CONFIG || {}).adSlotIds || {});
  window.TOOLHUB_CONFIG = cfg;

  const ADSENSE_CLIENT_RE = /^ca-pub-\d{16}$/;
  const IS_SANDBOX = cfg.deploy_env !== "production";
  const CLIENT_OK = !IS_SANDBOX && ADSENSE_CLIENT_RE.test(cfg.adsenseClientId || "");
  if (!IS_SANDBOX && cfg.adsenseClientId && !CLIENT_OK) {
    try {
      console.warn(
        "[toolhub] deploy_env=production but adsenseClientId does not match ca-pub-NNNNNNNNNNNNNNNN; " +
        "falling back to placeholder ad slots."
      );
    } catch (_) {}
  }

  // ----- i18n strings ----------------------------------------------------
  const LANG = (document.documentElement.lang || "en").slice(0, 2).toLowerCase();
  const I18N = {
    en: {
      banner: "We use cookies to serve relevant ads. Anonymous Plausible analytics runs either way and never uses cookies.",
      accept: "Accept",
      reject: "Reject",
      learn:  "Privacy",
      sponsor: "Sponsor on GitHub",
      hosting: "DigitalOcean hosting",
      tip:     "Buy me a coffee",
      affiliate: "affiliate",
      supportIntro: "Built by an indie maintainer. If Toolhub saved you time:",
      adLabel: "Advertisement",
    },
    de: {
      banner: "Wir verwenden Cookies, um relevante Anzeigen zu zeigen. Anonyme Plausible-Statistiken laufen ohne Cookies.",
      accept: "Akzeptieren",
      reject: "Ablehnen",
      learn:  "Datenschutz",
      sponsor: "Auf GitHub sponsern",
      hosting: "DigitalOcean Hosting",
      tip:     "Spendier mir einen Kaffee",
      affiliate: "Affiliate",
      supportIntro: "Von einem unabhängigen Maintainer gebaut. Wenn Toolhub dir Zeit gespart hat:",
      adLabel: "Werbung",
    },
    es: {
      banner: "Usamos cookies para mostrar anuncios relevantes. Las estadísticas anónimas de Plausible funcionan sin cookies.",
      accept: "Aceptar",
      reject: "Rechazar",
      learn:  "Privacidad",
      sponsor: "Patrocinar en GitHub",
      hosting: "Hosting DigitalOcean",
      tip:     "Invítame un café",
      affiliate: "afiliado",
      supportIntro: "Construido por un mantenedor independiente. Si Toolhub te ahorró tiempo:",
      adLabel: "Publicidad",
    },
    fr: {
      banner: "Nous utilisons des cookies pour afficher des annonces pertinentes. Plausible (statistiques anonymes) fonctionne sans cookies.",
      accept: "Accepter",
      reject: "Refuser",
      learn:  "Confidentialité",
      sponsor: "Sponsoriser sur GitHub",
      hosting: "Hébergement DigitalOcean",
      tip:     "Offre-moi un café",
      affiliate: "affiliation",
      supportIntro: "Construit par un mainteneur indépendant. Si Toolhub t'a fait gagner du temps :",
      adLabel: "Publicité",
    },
    it: {
      banner: "Usiamo cookie per mostrare annunci pertinenti. Le statistiche anonime di Plausible non usano cookie.",
      accept: "Accetta",
      reject: "Rifiuta",
      learn:  "Privacy",
      sponsor: "Sponsorizza su GitHub",
      hosting: "Hosting DigitalOcean",
      tip:     "Offrimi un caffè",
      affiliate: "affiliato",
      supportIntro: "Costruito da un manutentore indipendente. Se Toolhub ti ha fatto risparmiare tempo:",
      adLabel: "Pubblicità",
    },
    pt: {
      banner: "Usamos cookies para exibir anúncios relevantes. As estatísticas anônimas do Plausible funcionam sem cookies.",
      accept: "Aceitar",
      reject: "Recusar",
      learn:  "Privacidade",
      sponsor: "Apoiar no GitHub",
      hosting: "Hospedagem DigitalOcean",
      tip:     "Me paga um café",
      affiliate: "afiliado",
      supportIntro: "Construído por um mantenedor independente. Se o Toolhub te economizou tempo:",
      adLabel: "Publicidade",
    },
    pl: {
      banner: "Używamy plików cookie, aby pokazywać dopasowane reklamy. Anonimowe statystyki Plausible działają bez cookies.",
      accept: "Akceptuj",
      reject: "Odrzuć",
      learn:  "Prywatność",
      sponsor: "Wesprzyj na GitHub",
      hosting: "Hosting DigitalOcean",
      tip:     "Postaw mi kawę",
      affiliate: "partner",
      supportIntro: "Stworzone przez niezależnego maintainera. Jeśli Toolhub oszczędził Ci czas:",
      adLabel: "Reklama",
    },
    ja: {
      banner: "関連性の高い広告を配信するためにクッキーを使用します。匿名の Plausible 統計はクッキーを使わずに動作します。",
      accept: "同意する",
      reject: "拒否する",
      learn:  "プライバシー",
      sponsor: "GitHub でスポンサー",
      hosting: "DigitalOcean ホスティング",
      tip:     "コーヒーをおごる",
      affiliate: "アフィリエイト",
      supportIntro: "個人メンテナによる開発です。Toolhub が時短に役立ったら：",
      adLabel: "広告",
    },
    nl: {
      banner: "We gebruiken cookies om relevante advertenties te tonen. Anonieme Plausible-statistieken werken zonder cookies.",
      accept: "Accepteren",
      reject: "Weigeren",
      learn:  "Privacy",
      sponsor: "Sponsor op GitHub",
      hosting: "DigitalOcean-hosting",
      tip:     "Trakteer me op een koffie",
      affiliate: "affiliate",
      supportIntro: "Gemaakt door een onafhankelijke maintainer. Als Toolhub je tijd heeft bespaard:",
      adLabel: "Advertentie",
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

  // ----- Footer extras (Support Toolhub block) -------------------------
  // Renders an intro line + three optional links: GitHub Sponsors, DigitalOcean
  // (affiliate, FTC-marked), Buy Me a Coffee. Each link is only rendered if its
  // URL is configured. Affiliate links carry rel="sponsored" per Google's spec.
  function renderFooterExtras() {
    const slot = document.querySelector("[data-toolhub-footer-extras]");
    if (!slot) return;
    const parts = [];
    if (cfg.githubSponsorsUrl) {
      parts.push(`<a href="${cfg.githubSponsorsUrl}" target="_blank" rel="noopener noreferrer">♥ ${t.sponsor}</a>`);
    }
    if (cfg.digitalOceanRef) {
      parts.push(
        `<a href="${cfg.digitalOceanRef}" target="_blank" rel="noopener sponsored" data-affiliate="digitalocean">${t.hosting}</a>` +
        ` <span class="toolhub-affiliate-tag">(${t.affiliate})</span>`
      );
    }
    if (cfg.buyMeACoffeeUrl) {
      parts.push(`<a href="${cfg.buyMeACoffeeUrl}" target="_blank" rel="noopener noreferrer">☕ ${t.tip}</a>`);
    }
    if (!parts.length) return;
    slot.innerHTML =
      `<span class="toolhub-support-intro">${t.supportIntro}</span> ` +
      parts.join(" · ");
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
    if (adsenseLoaded || !CLIENT_OK) return;
    const s = document.createElement("script");
    s.async = true;
    s.crossOrigin = "anonymous";
    s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + encodeURIComponent(cfg.adsenseClientId);
    document.head.appendChild(s);
    adsenseLoaded = true;
  }

  function renderPlaceholder(el) {
    if (el.dataset.rendered) return;
    el.innerHTML =
      '<div class="ad-label">' + t.adLabel + "</div>" +
      '<div class="ad-placeholder">SANDBOX MODE — no real ads</div>';
    el.dataset.rendered = "placeholder";
  }

  function renderSandboxBadge() {
    if (document.getElementById("toolhub-sandbox-badge")) return;
    const b = document.createElement("div");
    b.id = "toolhub-sandbox-badge";
    b.textContent = "SANDBOX";
    b.title = "deploy_env=sandbox — no real ads are loaded";
    document.body.appendChild(b);
  }

  function renderAdSlots() {
    // Sandbox: render placeholder boxes, never load AdSense.
    if (IS_SANDBOX) {
      document.querySelectorAll(".ad-slot[data-slot]").forEach(renderPlaceholder);
      return;
    }
    // Production but client ID invalid/missing: same placeholder fallback.
    if (!CLIENT_OK) {
      document.querySelectorAll(".ad-slot[data-slot]").forEach(renderPlaceholder);
      return;
    }
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

    // Sandbox: render placeholders + badge, no consent banner, no AdSense.
    if (IS_SANDBOX) {
      renderAdSlots();
      renderSandboxBadge();
      return;
    }

    // Production with no/invalid AdSense client → nothing to consent to.
    if (!CLIENT_OK) {
      renderAdSlots(); // placeholders
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
