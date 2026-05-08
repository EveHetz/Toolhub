TOOL = {
    "slug": "email-validator",
    "category": "validation",
    "icon": "✉",
    "tags": ["email", "validate", "rfc", "syntax", "mx", "domain"],
    "i18n": {
        "en": {
            "name": "Email Validator",
            "tagline": "Check whether an email address is syntactically valid (RFC 5322 friendly), with breakdown of local part, domain, and common pitfalls.",
            "description": "Free online email validator. RFC 5322-aware syntax check, local-part and domain analysis, disposable-domain hint, and length verification.",
        },
        "de": {"name": "E-Mail-Validator", "tagline": "Prüfe, ob eine E-Mail-Adresse syntaktisch korrekt ist (RFC 5322), mit Aufschlüsselung von Local-Part und Domain.", "description": "Kostenloser E-Mail-Validator. RFC-5322-kompatible Syntaxprüfung, Local-Part- und Domain-Analyse, Hinweis auf Wegwerfdomains und Längenprüfung."},
        "es": {"name": "Validador de Email", "tagline": "Comprueba si una dirección de email es sintácticamente válida (RFC 5322), con desglose de la parte local y el dominio.", "description": "Validador de email en línea gratuito. Verificación sintáctica compatible con RFC 5322, análisis de parte local y dominio, aviso de dominios desechables."},
        "fr": {"name": "Validateur d'Email", "tagline": "Vérifiez si une adresse email est syntaxiquement valide (RFC 5322), avec analyse de la partie locale et du domaine.", "description": "Validateur d'email gratuit en ligne. Vérification syntaxique compatible RFC 5322, analyse de la partie locale et du domaine, alerte domaines jetables."},
        "it": {"name": "Validatore Email", "tagline": "Verifica se un indirizzo email è sintatticamente valido (RFC 5322), con analisi della parte locale e del dominio.", "description": "Validatore email online gratuito. Verifica sintattica conforme RFC 5322, analisi della parte locale e del dominio, segnalazione domini usa-e-getta."},
    },
    "body": """
<div class="tool-card">
  <label>Email address</label>
  <input type="text" id="ev-input" oninput="evRun()" placeholder="hello@example.com" autocomplete="off" spellcheck="false">
  <div class="meta" style="margin-top:0.5rem">Or paste a list (one per line) below to bulk-check.</div>
  <textarea id="ev-bulk" oninput="evRun()" placeholder="Optional: bulk check, one address per line" spellcheck="false" style="margin-top:0.6rem"></textarea>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="ev-out" class="output">{LBL_NO_INPUT}</div>
</div>
""",
    "script": """
<style>
.ev-result{display:grid;gap:0.5rem}
.ev-row{display:grid;grid-template-columns:140px 1fr;gap:0.6rem;align-items:center;padding:0.45rem 0.7rem;background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;font-size:0.88rem}
.ev-row .lbl{color:var(--text-muted);font-size:0.78rem;font-family:ui-monospace,monospace}
.ev-pass{color:#10b981;font-weight:600}
.ev-fail{color:#ef4444;font-weight:600}
.ev-warn{color:#f59e0b;font-weight:600}
.ev-bulk-row{display:grid;grid-template-columns:1fr 90px;gap:0.5rem;padding:0.4rem 0.7rem;background:var(--bg-elev);border:1px solid var(--border);border-radius:6px;font-family:ui-monospace,monospace;font-size:0.85rem;margin-bottom:0.3rem;word-break:break-all}
</style>
<script>
const EV_DISPOSABLE = new Set(['mailinator.com','tempmail.com','10minutemail.com','guerrillamail.com','yopmail.com','throwawaymail.com','trashmail.com','maildrop.cc','sharklasers.com','dispostable.com','fakeinbox.com','getnada.com']);
const EV_LOCAL_RX = /^[A-Za-z0-9!#$%&'*+\\-/=?^_`{|}~]+(\\.[A-Za-z0-9!#$%&'*+\\-/=?^_`{|}~]+)*$/;
const EV_DOMAIN_LABEL_RX = /^[A-Za-z0-9](?:[A-Za-z0-9\\-]{0,61}[A-Za-z0-9])?$/;
function evCheck(addr){
  const r = {addr, valid:false, problems:[], warnings:[]};
  if(!addr) return r;
  if(addr.length > 254) r.problems.push('Total length over 254 chars (RFC 5321 limit)');
  const at = addr.lastIndexOf('@');
  if(at <= 0 || at === addr.length-1){ r.problems.push('Missing local part or domain (no @ separator)'); return r; }
  const local = addr.slice(0, at);
  const domain = addr.slice(at+1);
  r.local = local; r.domain = domain;
  if(local.length > 64) r.problems.push('Local part over 64 chars (RFC 5321 limit)');
  if(local.startsWith('.') || local.endsWith('.')) r.problems.push('Local part cannot start or end with a dot');
  if(local.includes('..')) r.problems.push('Local part contains consecutive dots');
  if(!EV_LOCAL_RX.test(local) && !(local.startsWith('"') && local.endsWith('"'))) r.problems.push('Local part has invalid characters');
  if(!domain.includes('.')) r.problems.push('Domain has no TLD (no dot)');
  const labels = domain.split('.');
  for(const lab of labels){
    if(!lab){ r.problems.push('Empty label in domain (consecutive dots?)'); continue; }
    if(lab.length > 63){ r.problems.push('Domain label "'+lab+'" over 63 chars'); continue; }
    if(!EV_DOMAIN_LABEL_RX.test(lab)) r.problems.push('Invalid domain label "'+lab+'"');
  }
  const tld = labels[labels.length-1] || '';
  if(tld.length < 2) r.problems.push('TLD too short');
  if(/^\\d+$/.test(tld)) r.problems.push('TLD cannot be all-numeric');
  if(EV_DISPOSABLE.has(domain.toLowerCase())) r.warnings.push('Disposable / throwaway domain');
  if(domain.toLowerCase()==='gmail.com' && local.includes('+')) r.warnings.push('Gmail "+" alias — routes to base address');
  r.valid = r.problems.length === 0;
  return r;
}
function evRow(label, val){return `<div class="ev-row"><div class="lbl">${label}</div><div>${val}</div></div>`}
function evRender(c){
  if(!c.local && !c.domain) return `<div class="ev-result">${evRow('Status','<span class="ev-fail">'+c.problems.join('; ')+'</span>')}</div>`;
  const verdict = c.valid ? '<span class="ev-pass">✓ Syntactically valid</span>' : '<span class="ev-fail">✗ Invalid</span>';
  let html = '<div class="ev-result">';
  html += evRow('Verdict', verdict);
  html += evRow('Local part', '<code>'+c.local+'</code>');
  html += evRow('Domain', '<code>'+c.domain+'</code>');
  if(c.problems.length) html += evRow('Problems', '<span class="ev-fail">'+c.problems.join('<br>')+'</span>');
  if(c.warnings.length) html += evRow('Notes', '<span class="ev-warn">'+c.warnings.join('<br>')+'</span>');
  html += '</div>';
  return html;
}
function evRun(){
  const single = document.getElementById('ev-input').value.trim();
  const bulk = document.getElementById('ev-bulk').value.trim();
  const out = document.getElementById('ev-out');
  out.classList.remove('error');
  if(!single && !bulk){ out.textContent = '{LBL_NO_INPUT}'; return; }
  if(single && !bulk){
    out.innerHTML = evRender(evCheck(single));
    return;
  }
  const list = (bulk || single).split(/\\r?\\n/).map(s=>s.trim()).filter(Boolean);
  let html = '';
  let pass = 0, fail = 0;
  for(const a of list){
    const c = evCheck(a);
    if(c.valid) pass++; else fail++;
    const cls = c.valid ? 'ev-pass' : 'ev-fail';
    html += `<div class="ev-bulk-row"><div>${a}</div><div class="${cls}">${c.valid?'✓ valid':'✗ invalid'}</div></div>`;
  }
  out.innerHTML = `<div class="meta" style="margin-bottom:0.6rem">${pass} valid · ${fail} invalid · ${list.length} total</div>` + html;
}
document.addEventListener('DOMContentLoaded', evRun);
</script>
""",
    "help": {
        "en": """
<h2>What this checks</h2>
<ul>
  <li>Presence of exactly one <code>@</code> separating local part and domain.</li>
  <li>RFC 5322-friendly local part (alphanumeric plus <code>!#$%&amp;'*+-/=?^_`{|}~</code> and dots, never leading/trailing or consecutive).</li>
  <li>Domain length, label length (≤63), and label charset (LDH only).</li>
  <li>TLD must exist and not be all-numeric.</li>
  <li>RFC 5321 hard limits: 64 chars for local, 254 chars total.</li>
</ul>
<h3>What it doesn't check</h3>
<p>No DNS / MX lookup — that requires a server. The address can be syntactically valid but have no mailbox at the other end. Our disposable-domain list flags some common throwaway hosts.</p>
""",
    },
    "related": ["regex-tester", "credit-card-validator", "url-encoder"],
}
