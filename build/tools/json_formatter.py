TOOL = {
    "slug": "json-formatter",
    "category": "developer",
    "icon": "{ }",
    "tags": ["json", "format", "beautify", "validate", "minify"],
    "i18n": {
        "en": {
            "name": "JSON Formatter",
            "tagline": "Format, validate, and minify JSON instantly. Errors highlighted with line and column.",
            "description": "Free online JSON formatter and validator. Pretty-print, minify, and check JSON syntax with precise error messages.",
        },
        "de": {
            "name": "JSON-Formatter",
            "tagline": "JSON sofort formatieren, validieren und minimieren. Fehler werden mit Zeile und Spalte hervorgehoben.",
            "description": "Kostenloser Online-JSON-Formatter und Validator. JSON formatieren, minimieren und auf Syntax prüfen.",
        },
        "es": {
            "name": "Formateador JSON",
            "tagline": "Formatea, valida y minifica JSON al instante. Los errores se resaltan con línea y columna.",
            "description": "Formateador y validador JSON gratuito en línea. Formatea, minifica y verifica la sintaxis JSON.",
        },
        "fr": {
            "name": "Formateur JSON",
            "tagline": "Formatez, validez et minifiez du JSON instantanément. Les erreurs sont signalées avec ligne et colonne.",
            "description": "Formateur et validateur JSON gratuit en ligne. Embellissez, minifiez et vérifiez la syntaxe JSON.",
        },
        "it": {
            "name": "Formattatore JSON",
            "tagline": "Formatta, valida e minifica JSON all'istante. Gli errori sono evidenziati con riga e colonna.",
            "description": "Formattatore e validatore JSON gratuito online. Abbellisci, minifica e controlla la sintassi JSON.",
        },
    },
    "body": """
<div class="tool-card">
  <label for="json-input">{LBL_INPUT}</label>
  <textarea id="json-input" placeholder='{{"hello": "world", "n": 42}}' spellcheck="false"></textarea>
  <div class="button-row">
    <button onclick="jfFormat(2)">{LBL_FORMAT}</button>
    <button class="secondary" onclick="jfFormat(4)">Format (4-space)</button>
    <button class="secondary" onclick="jfMinify()">{LBL_MINIFY}</button>
    <button class="secondary" onclick="jfValidate()">{LBL_VALIDATE}</button>
    <button class="secondary" onclick="document.getElementById('json-input').value=''">{LBL_CLEAR}</button>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="json-output">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('json-output', this)">{LBL_COPY}</button>
  </div>
  <div class="meta" id="json-meta"></div>
</div>
""",
    "script": """
<script>
function jfShowError(e, raw){
  const out = document.getElementById('json-output');
  out.classList.add('error');
  out.classList.remove('success');
  let msg = e.message || String(e);
  // Try to extract position
  const m = msg.match(/position (\\d+)/i);
  if (m){
    const pos = parseInt(m[1], 10);
    const before = raw.slice(0, pos);
    const line = (before.match(/\\n/g) || []).length + 1;
    const col = pos - (before.lastIndexOf('\\n') + 1) + 1;
    msg = msg.replace(/position \\d+/i, 'line ' + line + ', col ' + col);
  }
  out.textContent = '✗ ' + msg;
  document.getElementById('json-meta').textContent = '';
}
function jfShowOk(text, label){
  const out = document.getElementById('json-output');
  out.classList.remove('error');
  out.classList.add('success');
  out.textContent = text;
  document.getElementById('json-meta').textContent = label || '';
}
function jfFormat(indent){
  const raw = document.getElementById('json-input').value.trim();
  if (!raw){ document.getElementById('json-output').textContent = '{LBL_NO_INPUT}'; return; }
  try {
    const obj = JSON.parse(raw);
    const out = JSON.stringify(obj, null, indent);
    jfShowOk(out, out.length + ' chars · ' + (out.match(/\\n/g)||[]).length + ' lines');
  } catch(e){ jfShowError(e, raw); }
}
function jfMinify(){
  const raw = document.getElementById('json-input').value.trim();
  if (!raw){ document.getElementById('json-output').textContent = '{LBL_NO_INPUT}'; return; }
  try {
    const obj = JSON.parse(raw);
    const out = JSON.stringify(obj);
    jfShowOk(out, out.length + ' chars (minified)');
  } catch(e){ jfShowError(e, raw); }
}
function jfValidate(){
  const raw = document.getElementById('json-input').value.trim();
  if (!raw){ document.getElementById('json-output').textContent = '{LBL_NO_INPUT}'; return; }
  try {
    const obj = JSON.parse(raw);
    const t = Array.isArray(obj) ? 'array' : typeof obj;
    const sz = JSON.stringify(obj).length;
    jfShowOk('✓ Valid JSON', 'top-level: ' + t + ' · ' + sz + ' chars minified');
  } catch(e){ jfShowError(e, raw); }
}
</script>
""",
    "help": {
        "en": """
<h2>How it works</h2>
<p>This formatter runs entirely in your browser using the native <code>JSON.parse</code> and <code>JSON.stringify</code> APIs. Nothing is uploaded.</p>
<h3>Tips</h3>
<ul>
  <li>Use <strong>Format</strong> for human-readable output (2 or 4 space indent).</li>
  <li>Use <strong>Minify</strong> to strip whitespace before shipping JSON over the network.</li>
  <li>If parsing fails, the error message points to the exact line and column.</li>
  <li>JSON keys must be in double quotes — single quotes are not valid JSON.</li>
  <li>No trailing commas: <code>[1,2,]</code> is invalid.</li>
</ul>
""",
    },
    "related": ["regex-tester", "yaml-json", "json-diff"],
}
