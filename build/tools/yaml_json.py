TOOL = {
    "slug": "yaml-json",
    "category": "data",
    "icon": "🔁",
    "tags": ["yaml", "json", "convert", "kubernetes", "config", "data"],
    "i18n": {
        "en": {
            "name": "YAML ↔ JSON Converter",
            "tagline": "Convert between YAML and JSON in either direction. Useful for Kubernetes manifests, CI configs, and OpenAPI specs.",
            "description": "Free online YAML to JSON and JSON to YAML converter. Bidirectional, runs entirely in your browser. Handles anchors, aliases, and multi-document YAML.",
        },
        "de": {
            "name": "YAML ↔ JSON Konverter",
            "tagline": "Konvertiere zwischen YAML und JSON in beide Richtungen. Für Kubernetes-Manifeste, CI-Configs und OpenAPI-Specs.",
            "description": "Kostenloser YAML-zu-JSON und JSON-zu-YAML Konverter. Bidirektional, läuft komplett im Browser. Anker, Aliase und Multi-Dokument-YAML unterstützt.",
        },
        "es": {
            "name": "Conversor YAML ↔ JSON",
            "tagline": "Convierte entre YAML y JSON en ambas direcciones. Útil para manifiestos Kubernetes, configs CI y specs OpenAPI.",
            "description": "Conversor YAML a JSON y JSON a YAML gratuito. Bidireccional, todo en tu navegador. Soporta anclas, alias y YAML multi-documento.",
        },
        "fr": {
            "name": "Convertisseur YAML ↔ JSON",
            "tagline": "Convertissez entre YAML et JSON dans les deux sens. Idéal pour manifestes Kubernetes, configs CI et specs OpenAPI.",
            "description": "Convertisseur YAML vers JSON et JSON vers YAML gratuit. Bidirectionnel, tout dans votre navigateur. Ancres, alias et YAML multi-documents supportés.",
        },
        "it": {
            "name": "Convertitore YAML ↔ JSON",
            "tagline": "Converti tra YAML e JSON in entrambe le direzioni. Utile per manifesti Kubernetes, config CI e specifiche OpenAPI.",
            "description": "Convertitore YAML-JSON e JSON-YAML gratuito. Bidirezionale, tutto nel browser. Supporta ancore, alias e YAML multi-documento.",
        },
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>{LBL_FROM}</label>
      <select id="yj-from" onchange="yjSwap()">
        <option value="yaml">YAML</option>
        <option value="json">JSON</option>
      </select>
    </div>
    <div>
      <label>{LBL_TO}</label>
      <select id="yj-to" onchange="yjConv()">
        <option value="json">JSON</option>
        <option value="yaml">YAML</option>
      </select>
    </div>
  </div>
  <label style="margin-top:1rem">{LBL_INPUT}</label>
  <textarea id="yj-in" oninput="yjConv()" spellcheck="false" placeholder="apiVersion: v1
kind: ConfigMap
metadata:
  name: example
data:
  message: hello"></textarea>
  <div class="button-row">
    <button onclick="yjConv()">{LBL_CONVERT}</button>
    <button class="secondary" onclick="document.getElementById('yj-in').value=''; yjConv()">{LBL_CLEAR}</button>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="yj-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('yj-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<script src="https://cdn.jsdelivr.net/npm/js-yaml@4.1.0/dist/js-yaml.min.js"></script>
<script>
function yjSwap(){
  const f = document.getElementById('yj-from').value;
  const t = document.getElementById('yj-to');
  // ensure 'to' is the OTHER format
  t.value = (f === 'yaml') ? 'json' : 'yaml';
  yjConv();
}
function yjConv(){
  const from = document.getElementById('yj-from').value;
  const to = document.getElementById('yj-to').value;
  const raw = document.getElementById('yj-in').value;
  const out = document.getElementById('yj-out');
  out.classList.remove('error');
  if (!raw.trim()){ out.textContent = '{LBL_NO_INPUT}'; return; }
  try {
    let data;
    if (from === 'yaml') data = jsyaml.load(raw);
    else data = JSON.parse(raw);
    if (to === 'json') out.textContent = JSON.stringify(data, null, 2);
    else out.textContent = jsyaml.dump(data, { indent: 2, lineWidth: 120 });
  } catch(e){
    out.classList.add('error');
    out.textContent = '✗ ' + (e.message || String(e));
  }
}
document.addEventListener('DOMContentLoaded', yjConv);
</script>
""",
    "help": {
        "en": """
<h2>How it works</h2>
<p>YAML parsing uses <a href="https://github.com/nodeca/js-yaml" rel="noopener">js-yaml</a> (YAML 1.2 compliant). JSON uses the native <code>JSON</code> API. All conversion happens in your browser.</p>
<h3>What it handles</h3>
<ul>
  <li>Anchors and aliases (<code>&amp;ref</code>, <code>*ref</code>) — resolved on YAML→JSON</li>
  <li>Block-style and flow-style YAML</li>
  <li>Numbers, booleans, null, dates auto-typed per YAML 1.2</li>
  <li>Order is preserved on JSON→YAML</li>
</ul>
<h3>What it doesn't handle</h3>
<ul>
  <li>Custom YAML tags (<code>!!python/object</code>, etc.) — strict YAML 1.2 only, no language-specific tags</li>
  <li>Multi-document YAML (<code>---</code> separators) is parsed as the first document only</li>
</ul>
""",
    },
    "related": ["json-formatter", "json-diff", "csv-to-json"],
}
