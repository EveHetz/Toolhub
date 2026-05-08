TOOL = {
    "slug": "url-encoder",
    "category": "encoding",
    "icon": "🔗",
    "tags": ["url", "encode", "decode", "percent", "querystring"],
    "i18n": {
        "en": {
            "name": "URL Encoder / Decoder",
            "tagline": "Percent-encode strings for URLs or decode percent-encoded ones back to plain text.",
            "description": "Free online URL encoder and decoder. Encodes special characters as percent-escapes for URLs, query strings, and form data. Component-safe.",
        },
        "de": {"name": "URL Encoder / Decoder", "tagline": "Strings für URLs prozent-codieren oder zurück in Klartext decodieren.", "description": "Kostenloser URL Encoder und Decoder. Sonderzeichen für URLs, Query-Strings und Formulardaten escapen."},
        "es": {"name": "Codificador / Decodificador URL", "tagline": "Codifica cadenas para URLs (porcentaje) o decodifica de vuelta a texto plano.", "description": "Codificador y decodificador URL gratuito. Escapa caracteres especiales para URLs, query strings y datos de formulario."},
        "fr": {"name": "Encodeur / Décodeur URL", "tagline": "Encodez en pourcentage pour URLs ou décodez vers texte brut.", "description": "Encodeur et décodeur URL gratuit. Échappe les caractères spéciaux pour URLs, query strings et formulaires."},
        "it": {"name": "Encoder / Decoder URL", "tagline": "Codifica stringhe per URL (percent-encoding) o decodifica in testo semplice.", "description": "Encoder e decoder URL gratuito. Escape di caratteri speciali per URL, query string e dati form."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Mode</label>
      <select id="url-mode" onchange="urlRun()">
        <option value="enc">{LBL_ENCODE}</option>
        <option value="dec">{LBL_DECODE}</option>
      </select>
    </div>
    <div>
      <label>Scope</label>
      <select id="url-scope" onchange="urlRun()">
        <option value="component">Component (encodes /, ?, #, &amp;)</option>
        <option value="uri">Full URI (preserves /, ?, #, &amp;)</option>
      </select>
    </div>
  </div>
  <label style="margin-top:1rem">{LBL_INPUT}</label>
  <textarea id="url-in" oninput="urlRun()" spellcheck="false"></textarea>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="url-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('url-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<script>
function urlRun(){
  const mode = document.getElementById('url-mode').value;
  const scope = document.getElementById('url-scope').value;
  const raw = document.getElementById('url-in').value;
  const out = document.getElementById('url-out');
  out.classList.remove('error');
  if (!raw){ out.textContent = '{LBL_NO_INPUT}'; return; }
  try {
    let res;
    if (mode === 'enc') res = scope === 'component' ? encodeURIComponent(raw) : encodeURI(raw);
    else                res = scope === 'component' ? decodeURIComponent(raw) : decodeURI(raw);
    out.textContent = res;
  } catch(e){ out.classList.add('error'); out.textContent = '✗ ' + e.message; }
}
document.addEventListener('DOMContentLoaded', urlRun);
</script>
""",
    "help": {
        "en": """
<h2>Component vs Full URI</h2>
<ul>
  <li><strong>Component</strong> — for individual query-string values. Encodes <code>/?#&amp;=</code>. Use this for values you'll plug into <code>?key=…</code>.</li>
  <li><strong>Full URI</strong> — for whole URLs. Preserves URL structural characters. Use this when encoding a complete URL string.</li>
</ul>
""",
    },
    "related": ["base64-encoder", "html-encoder", "qr-code-generator"],
}
