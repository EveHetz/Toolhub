TOOL = {
    "slug": "hash-generator",
    "category": "security",
    "icon": "🔑",
    "tags": ["hash", "md5", "sha", "sha-256", "sha-512", "checksum"],
    "i18n": {
        "en": {
            "name": "Hash Generator",
            "tagline": "Hash text with SHA-1, SHA-256, SHA-384 or SHA-512 using your browser's WebCrypto. Computed locally — input never leaves the page.",
            "description": "Free online hash generator. SHA-1, SHA-256, SHA-384, SHA-512 via WebCrypto. Hex output, copy-friendly. Runs entirely in your browser.",
        },
        "de": {"name": "Hash-Generator", "tagline": "Text mit SHA-1, SHA-256, SHA-384 oder SHA-512 hashen via WebCrypto. Lokal berechnet — Eingabe verlässt die Seite nicht.", "description": "Kostenloser Hash-Generator. SHA-1, SHA-256, SHA-384, SHA-512 via WebCrypto. Hex-Ausgabe, läuft komplett im Browser."},
        "es": {"name": "Generador de Hash", "tagline": "Genera hashes SHA-1, SHA-256, SHA-384 o SHA-512 con WebCrypto del navegador. Calculado localmente — la entrada no se envía.", "description": "Generador de hash gratuito. SHA-1, SHA-256, SHA-384, SHA-512 vía WebCrypto. Salida en hexadecimal, todo en tu navegador."},
        "fr": {"name": "Générateur de Hash", "tagline": "Hachez du texte avec SHA-1, SHA-256, SHA-384 ou SHA-512 via WebCrypto. Calcul local — l'entrée ne quitte pas la page.", "description": "Générateur de hash gratuit. SHA-1, SHA-256, SHA-384, SHA-512 via WebCrypto. Sortie hex, tout dans votre navigateur."},
        "it": {"name": "Generatore di Hash", "tagline": "Genera hash SHA-1, SHA-256, SHA-384 o SHA-512 con WebCrypto. Calcolato localmente — l'input non lascia la pagina.", "description": "Generatore di hash gratuito. SHA-1, SHA-256, SHA-384, SHA-512 via WebCrypto. Output esadecimale, tutto nel browser."},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="h-in" oninput="hRun()" placeholder="Hello, world!" spellcheck="false"></textarea>
  <div class="meta">Note: MD5 is not provided here — it is broken for security purposes. Use SHA-256 or higher for new applications.</div>
</div>
<div class="tool-card">
  <label>SHA-1 <span class="badge">160 bits</span> <span class="meta">— legacy, do not use for security</span></label>
  <div class="output-row"><code class="output" id="h-sha1">{LBL_NO_INPUT}</code><button class="copy-btn secondary" onclick="copyOutput('h-sha1', this)">{LBL_COPY}</button></div>
</div>
<div class="tool-card">
  <label>SHA-256 <span class="badge">256 bits</span> <span class="meta">— recommended default</span></label>
  <div class="output-row"><code class="output" id="h-sha256">{LBL_NO_INPUT}</code><button class="copy-btn secondary" onclick="copyOutput('h-sha256', this)">{LBL_COPY}</button></div>
</div>
<div class="tool-card">
  <label>SHA-384 <span class="badge">384 bits</span></label>
  <div class="output-row"><code class="output" id="h-sha384">{LBL_NO_INPUT}</code><button class="copy-btn secondary" onclick="copyOutput('h-sha384', this)">{LBL_COPY}</button></div>
</div>
<div class="tool-card">
  <label>SHA-512 <span class="badge">512 bits</span></label>
  <div class="output-row"><code class="output" id="h-sha512">{LBL_NO_INPUT}</code><button class="copy-btn secondary" onclick="copyOutput('h-sha512', this)">{LBL_COPY}</button></div>
</div>
""",
    "script": """
<script>
async function hOne(name, bytes){
  const buf = await crypto.subtle.digest(name, bytes);
  return [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2,'0')).join('');
}
async function hRun(){
  const raw = document.getElementById('h-in').value;
  const ids = ['h-sha1','h-sha256','h-sha384','h-sha512'];
  if (!raw){ ids.forEach(id => document.getElementById(id).textContent = '{LBL_NO_INPUT}'); return; }
  const bytes = new TextEncoder().encode(raw);
  const [s1, s256, s384, s512] = await Promise.all([
    hOne('SHA-1', bytes), hOne('SHA-256', bytes), hOne('SHA-384', bytes), hOne('SHA-512', bytes)
  ]);
  document.getElementById('h-sha1').textContent = s1;
  document.getElementById('h-sha256').textContent = s256;
  document.getElementById('h-sha384').textContent = s384;
  document.getElementById('h-sha512').textContent = s512;
}
document.addEventListener('DOMContentLoaded', hRun);
</script>
""",
    "help": {
        "en": """
<h2>Which hash should I use?</h2>
<ul>
  <li><strong>SHA-256</strong> — sensible default for integrity checks, content addressing, signatures.</li>
  <li><strong>SHA-384 / SHA-512</strong> — useful when you need a wider hash (e.g. PBKDF2/HKDF tuning, larger HMAC keys).</li>
  <li><strong>SHA-1</strong> — shown for compatibility (Git object IDs, legacy CI checksums). Do not use for security-critical purposes — collision attacks are practical since 2017.</li>
  <li><strong>MD5 is intentionally not offered here.</strong> It's been broken since the early 2000s. If you must check an MD5, use a separate dedicated tool.</li>
</ul>
<p>All hashing uses the browser's <code>crypto.subtle.digest</code> — same primitives that power TLS in your browser. Nothing is uploaded.</p>
""",
    },
    "related": ["password-generator", "uuid-generator", "jwt-decoder"],
}
