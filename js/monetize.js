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
      supportCallout: "If Toolhub saved you time, you can support development →",
      dismiss: "Dismiss",
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
      supportCallout: "Wenn Toolhub dir Zeit gespart hat, kannst du die Entwicklung unterstützen →",
      dismiss: "Schließen",
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
      supportCallout: "Si Toolhub te ahorró tiempo, puedes apoyar el desarrollo →",
      dismiss: "Cerrar",
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
      supportCallout: "Si Toolhub t'a fait gagner du temps, tu peux soutenir le développement →",
      dismiss: "Fermer",
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
      supportCallout: "Se Toolhub ti ha fatto risparmiare tempo, puoi supportare lo sviluppo →",
      dismiss: "Chiudi",
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
      supportCallout: "Se o Toolhub te economizou tempo, você pode apoiar o desenvolvimento →",
      dismiss: "Fechar",
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
      supportCallout: "Jeśli Toolhub oszczędził Ci czas, możesz wesprzeć rozwój →",
      dismiss: "Zamknij",
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
      supportCallout: "Toolhub が時短に役立ったら、開発を応援できます →",
      dismiss: "閉じる",
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
      supportCallout: "Als Toolhub je tijd heeft bespaard, kun je de ontwikkeling steunen →",
      dismiss: "Sluiten",
      adLabel: "Advertentie",
    },
    tr: {
      banner: "İlgili reklamları sunmak için cookie kullanıyoruz. Anonim Plausible istatistikleri her durumda cookie kullanmadan çalışır.",
      accept: "Kabul et",
      reject: "Reddet",
      learn:  "Gizlilik",
      sponsor: "GitHub'ta sponsor ol",
      hosting: "DigitalOcean hosting",
      tip:     "Bana bir kahve ısmarla",
      affiliate: "affiliate",
      supportIntro: "Bağımsız bir maintainer tarafından yapıldı. Toolhub sana zaman kazandırdıysa:",
      supportCallout: "Toolhub sana zaman kazandırdıysa, geliştirmeyi destekleyebilirsin →",
      dismiss: "Kapat",
      adLabel: "Reklam",
    },
    id: {
      banner: "Kami menggunakan cookie untuk menampilkan iklan yang relevan. Statistik Plausible anonim tetap berjalan tanpa cookie.",
      accept: "Terima",
      reject: "Tolak",
      learn:  "Privasi",
      sponsor: "Jadi sponsor di GitHub",
      hosting: "Hosting DigitalOcean",
      tip:     "Belikan saya kopi",
      affiliate: "afiliasi",
      supportIntro: "Dibangun oleh maintainer independen. Jika Toolhub menghemat waktumu:",
      supportCallout: "Jika Toolhub menghemat waktumu, kamu bisa mendukung pengembangan →",
      dismiss: "Tutup",
      adLabel: "Iklan",
    },
    vi: {
      banner: "Chúng tôi sử dụng cookie để hiển thị quảng cáo phù hợp. Thống kê Plausible ẩn danh chạy mà không cần cookie.",
      accept: "Đồng ý",
      reject: "Từ chối",
      learn:  "Quyền riêng tư",
      sponsor: "Tài trợ trên GitHub",
      hosting: "Hosting DigitalOcean",
      tip:     "Mời tôi một ly cà phê",
      affiliate: "affiliate",
      supportIntro: "Được tạo bởi một maintainer độc lập. Nếu Toolhub đã giúp bạn tiết kiệm thời gian:",
      supportCallout: "Nếu Toolhub đã giúp bạn tiết kiệm thời gian, bạn có thể ủng hộ việc phát triển →",
      dismiss: "Đóng",
      adLabel: "Quảng cáo",
    },
    hi: {
      banner: "हम प्रासंगिक विज्ञापन दिखाने के लिए cookies का उपयोग करते हैं। अनाम Plausible analytics बिना cookies के चलता है।",
      accept: "स्वीकार करें",
      reject: "अस्वीकार",
      learn:  "गोपनीयता",
      sponsor: "GitHub पर sponsor करें",
      hosting: "DigitalOcean hosting",
      tip:     "मुझे coffee दिलाएं",
      affiliate: "affiliate",
      supportIntro: "एक indie maintainer द्वारा बनाया गया। अगर Toolhub से आपका समय बचा:",
      supportCallout: "अगर Toolhub से आपका समय बचा, तो आप development को support कर सकते हैं →",
      dismiss: "बंद करें",
      adLabel: "विज्ञापन",
    },
    sk: {
      banner: "Používame cookies na zobrazenie relevantných reklám. Anonymná Plausible štatistika beží aj bez cookies.",
      accept: "Prijať",
      reject: "Odmietnuť",
      learn:  "Súkromie",
      sponsor: "Sponzorovať na GitHub",
      hosting: "DigitalOcean hosting",
      tip:     "Kúp mi kávu",
      affiliate: "affiliate",
      supportIntro: "Postavené nezávislým maintainerom. Ak ti Toolhub ušetril čas:",
      supportCallout: "Ak ti Toolhub ušetril čas, môžeš podporiť vývoj →",
      dismiss: "Zavrieť",
      adLabel: "Reklama",
    },
    cs: {
      banner: "Používáme cookies k zobrazení relevantních reklam. Anonymní Plausible statistika běží i bez cookies.",
      accept: "Přijmout",
      reject: "Odmítnout",
      learn:  "Soukromí",
      sponsor: "Sponzorovat na GitHub",
      hosting: "DigitalOcean hosting",
      tip:     "Kup mi kávu",
      affiliate: "affiliate",
      supportIntro: "Postaveno nezávislým maintainerem. Pokud ti Toolhub ušetřil čas:",
      supportCallout: "Pokud ti Toolhub ušetřil čas, můžeš podpořit vývoj →",
      dismiss: "Zavřít",
      adLabel: "Reklama",
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

  // ----- After-result support callout ----------------------------------
  // Shown once per session, the first time the user clicks a copy button —
  // a clear "got a result and is taking it away" signal. Subtle, dismissable,
  // honours sessionStorage so it does not re-show after dismissal.
  const CALLOUT_SHOWN_KEY = "toolhub:callout-shown";
  function calloutAlreadyShown() {
    try { return sessionStorage.getItem(CALLOUT_SHOWN_KEY) === "1"; } catch (_) { return false; }
  }
  function markCalloutShown() {
    try { sessionStorage.setItem(CALLOUT_SHOWN_KEY, "1"); } catch (_) {}
  }
  function renderSupportCallout() {
    const el = document.querySelector(".support-callout");
    if (!el || el.dataset.rendered) return;
    const parts = [];
    if (cfg.buyMeACoffeeUrl) {
      parts.push(`<a href="${cfg.buyMeACoffeeUrl}" target="_blank" rel="noopener noreferrer">☕ ${t.tip}</a>`);
    }
    if (cfg.githubSponsorsUrl) {
      parts.push(`<a href="${cfg.githubSponsorsUrl}" target="_blank" rel="noopener noreferrer">♥ ${t.sponsor}</a>`);
    }
    if (cfg.digitalOceanRef) {
      parts.push(`<a href="${cfg.digitalOceanRef}" target="_blank" rel="noopener sponsored" data-affiliate="digitalocean">🌊 ${t.hosting}</a>`);
    }
    if (!parts.length) return;
    el.innerHTML =
      `<span>${t.supportCallout}</span> ` +
      parts.join(" · ") +
      ` <button type="button" class="support-callout-dismiss" aria-label="${t.dismiss}">×</button>`;
    el.hidden = false;
    el.dataset.rendered = "1";
    const btn = el.querySelector(".support-callout-dismiss");
    if (btn) btn.addEventListener("click", function () { el.hidden = true; });
  }
  function installCalloutTriggers() {
    if (!document.querySelector(".support-callout")) return;
    function trip() {
      if (calloutAlreadyShown()) return;
      markCalloutShown();
      renderSupportCallout();
    }
    document.addEventListener("click", function (e) {
      const btn = e.target && e.target.closest && e.target.closest(".copy-btn");
      if (btn) trip();
    }, { passive: true });
    // Also trip on the first time an .output element gets non-empty content,
    // which catches Format / Generate / etc. actions even on tools without a
    // copy button.
    if ("MutationObserver" in window) {
      document.querySelectorAll(".output").forEach(function (out) {
        const mo = new MutationObserver(function () {
          if ((out.textContent || "").trim().length > 0) {
            mo.disconnect();
            trip();
          }
        });
        mo.observe(out, { childList: true, characterData: true, subtree: true });
      });
    }
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
    installCalloutTriggers();

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
