TOOL = {
    "slug": "credit-card-validator",
    "category": "validation",
    "icon": "💳",
    "tags": ["credit card", "validate", "luhn", "visa", "mastercard", "amex", "discover"],
    "i18n": {
        "en": {
            "name": "Credit Card Validator",
            "tagline": "Validate a card number with the Luhn check and detect the card brand. Runs locally — your number is never transmitted.",
            "description": "Free online credit card validator. Luhn (mod-10) checksum, brand detection (Visa, Mastercard, Amex, Discover, JCB, Diners, UnionPay), and length verification. 100% client-side.",
        },
        "de": {"name": "Kreditkarten-Validator", "tagline": "Prüfe Kartennummern per Luhn-Algorithmus und erkenne die Kartenmarke. Läuft lokal — die Nummer wird nie übertragen.", "description": "Kostenloser Kreditkarten-Validator. Luhn-Prüfsumme, Markenerkennung (Visa, Mastercard, Amex, Discover, JCB, Diners, UnionPay) und Längenprüfung. 100% im Browser."},
        "es": {"name": "Validador de Tarjeta de Crédito", "tagline": "Valida un número de tarjeta con Luhn y detecta la marca. Funciona localmente — el número nunca se envía.", "description": "Validador de tarjeta de crédito gratuito. Suma de comprobación Luhn, detección de marca (Visa, Mastercard, Amex, Discover, JCB, Diners, UnionPay) y longitud. 100% en el navegador."},
        "fr": {"name": "Validateur de Carte Bancaire", "tagline": "Validez un numéro de carte avec Luhn et détectez la marque. Fonctionne localement — le numéro n'est jamais envoyé.", "description": "Validateur de carte bancaire gratuit. Somme de contrôle Luhn, détection de marque (Visa, Mastercard, Amex, Discover, JCB, Diners, UnionPay) et longueur. 100% dans le navigateur."},
        "it": {"name": "Validatore Carta di Credito", "tagline": "Valida un numero di carta con Luhn e rileva la marca. Funziona localmente — il numero non viene mai inviato.", "description": "Validatore di carta di credito gratuito. Checksum Luhn, rilevamento marca (Visa, Mastercard, Amex, Discover, JCB, Diners, UnionPay) e lunghezza. 100% nel browser."},
    },
    "body": """
<div class="tool-card">
  <label>Card number</label>
  <input type="text" id="cv-input" oninput="cvRun()" placeholder="4242 4242 4242 4242" inputmode="numeric" autocomplete="off" spellcheck="false">
  <div class="meta" style="margin-top:0.5rem">Spaces and hyphens are ignored. Number is never sent — validation is entirely in your browser.</div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="cv-out" class="output">{LBL_NO_INPUT}</div>
</div>
""",
    "script": """
<style>
.cv-result{display:grid;gap:0.55rem}
.cv-row{display:grid;grid-template-columns:120px 1fr;gap:0.6rem;align-items:center;padding:0.5rem 0.7rem;background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;font-size:0.9rem}
.cv-row .lbl{color:var(--text-muted);font-size:0.78rem;font-family:ui-monospace,monospace}
.cv-pass{color:#10b981;font-weight:600}
.cv-fail{color:#ef4444;font-weight:600}
</style>
<script>
const CV_BRANDS = [
  {name:'Visa',          regex:/^4/,                                             lengths:[13,16,19], cvv:3},
  {name:'Mastercard',    regex:/^(5[1-5]|2[2-7])/,                               lengths:[16],       cvv:3},
  {name:'American Express', regex:/^3[47]/,                                       lengths:[15],       cvv:4},
  {name:'Discover',      regex:/^(6011|65|64[4-9]|622(12[6-9]|1[3-9]\\d|[2-8]\\d{2}|9([01]\\d|2[0-5])))/, lengths:[16,19], cvv:3},
  {name:'JCB',           regex:/^35(2[89]|[3-8])/,                               lengths:[16,19],    cvv:3},
  {name:'Diners Club',   regex:/^3(?:0[0-5]|[68])/,                              lengths:[14,16,19], cvv:3},
  {name:'UnionPay',      regex:/^62/,                                             lengths:[16,17,18,19], cvv:3},
  {name:'Maestro',       regex:/^(5018|5020|5038|6304|6759|676[1-3])/,           lengths:[12,13,14,15,16,17,18,19], cvv:3},
];
function cvDetectBrand(num){
  for(const b of CV_BRANDS) if(b.regex.test(num)) return b;
  return null;
}
function cvLuhn(num){
  let sum=0, alt=false;
  for(let i=num.length-1;i>=0;i--){
    let n = parseInt(num[i],10);
    if(isNaN(n)) return false;
    if(alt){n*=2; if(n>9) n-=9}
    sum += n;
    alt = !alt;
  }
  return sum % 10 === 0;
}
function cvRun(){
  const raw = document.getElementById('cv-input').value;
  const num = raw.replace(/[\\s\\-]/g,'');
  const out = document.getElementById('cv-out');
  out.classList.remove('error');
  if(!num){ out.textContent = '{LBL_NO_INPUT}'; out.className = 'output'; return; }
  if(!/^\\d+$/.test(num)){ out.classList.add('error'); out.textContent = 'Card number must contain only digits.'; return; }
  const brand = cvDetectBrand(num);
  const lenOk = brand ? brand.lengths.includes(num.length) : (num.length>=12 && num.length<=19);
  const luhnOk = cvLuhn(num);
  const valid = lenOk && luhnOk;
  out.className = 'output';
  out.innerHTML = `<div class="cv-result">
    <div class="cv-row"><div class="lbl">Brand</div><div>${brand ? brand.name : '<span class="cv-fail">Unknown</span>'}</div></div>
    <div class="cv-row"><div class="lbl">Length</div><div>${num.length} digits ${lenOk?'<span class="cv-pass">✓</span>':'<span class="cv-fail">✗ expected '+(brand?brand.lengths.join('/'):'12–19')+'</span>'}</div></div>
    <div class="cv-row"><div class="lbl">Luhn check</div><div>${luhnOk?'<span class="cv-pass">✓ Pass</span>':'<span class="cv-fail">✗ Fail</span>'}</div></div>
    <div class="cv-row"><div class="lbl">CVV</div><div>${brand?brand.cvv+' digits':'3–4 digits'}</div></div>
    <div class="cv-row"><div class="lbl">Verdict</div><div>${valid?'<span class="cv-pass">✓ Number is structurally valid</span>':'<span class="cv-fail">✗ Number is not valid</span>'}</div></div>
  </div>`;
}
document.addEventListener('DOMContentLoaded', cvRun);
</script>
""",
    "help": {
        "en": """
<h2>What this checks</h2>
<ul>
  <li><strong>Brand</strong> — matched against issuer prefix ranges.</li>
  <li><strong>Length</strong> — most issuers fix card numbers at a known length (13/15/16/19).</li>
  <li><strong>Luhn (mod-10)</strong> — the checksum every issued card number satisfies. Catches typos but not whether the card is real or active.</li>
</ul>
<h3>Important</h3>
<p>"Structurally valid" means the number could have been issued — not that it is. Card networks need a payment processor for live verification, which would charge or place a hold.</p>
<h3>Test numbers</h3>
<p>Visa <code>4242 4242 4242 4242</code> · Mastercard <code>5555 5555 5555 4444</code> · Amex <code>3782 822463 10005</code> · Discover <code>6011 1111 1111 1117</code></p>
""",
    },
    "related": ["email-validator", "hash-generator", "regex-tester"],
}
