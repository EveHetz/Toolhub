TOOL = {
    "slug": "csv-to-json",
    "category": "data",
    "icon": "📊",
    "tags": ["csv", "json", "convert", "data", "import"],
    "i18n": {
        "en": {
            "name": "CSV to JSON",
            "tagline": "Convert CSV data to JSON arrays. Header detection, custom delimiters, quoted fields, and embedded newlines handled.",
            "description": "Free online CSV to JSON converter. Auto-detects headers, supports custom delimiters and quoted multi-line fields. Runs in your browser.",
        },
        "de": {"name": "CSV zu JSON", "tagline": "CSV-Daten in JSON-Arrays konvertieren. Header-Erkennung, eigene Trennzeichen, zitierte Felder und eingebettete Zeilenumbrüche.", "description": "Kostenloser CSV-zu-JSON-Konverter. Auto-Header-Erkennung, beliebige Trennzeichen, zitierte mehrzeilige Felder. Läuft im Browser."},
        "es": {"name": "CSV a JSON", "tagline": "Convierte datos CSV en arrays JSON. Detección de cabeceras, separadores personalizados y campos entre comillas.", "description": "Conversor CSV a JSON gratuito. Detecta cabeceras automáticamente, soporta separadores personalizados y campos entre comillas multilínea."},
        "fr": {"name": "CSV vers JSON", "tagline": "Convertissez du CSV en tableaux JSON. Détection d'en-têtes, séparateurs personnalisés, champs avec guillemets et sauts de ligne.", "description": "Convertisseur CSV vers JSON gratuit. Détection automatique d'en-têtes, séparateurs personnalisés, champs entre guillemets multi-lignes."},
        "it": {"name": "CSV a JSON", "tagline": "Converti dati CSV in array JSON. Riconoscimento intestazioni, separatori personalizzati, campi tra virgolette e a capo.", "description": "Convertitore CSV-JSON gratuito. Rileva intestazioni, supporta separatori personalizzati e campi multi-riga tra virgolette."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Delimiter</label>
      <select id="cj-delim" onchange="cjRun()">
        <option value=",">, comma</option>
        <option value=";">; semicolon</option>
        <option value="\\t">tab</option>
        <option value="|">| pipe</option>
      </select>
    </div>
    <div>
      <label>Has header row?</label>
      <select id="cj-header" onchange="cjRun()">
        <option value="yes">Yes — use as keys</option>
        <option value="no">No — emit arrays</option>
      </select>
    </div>
  </div>
  <label style="margin-top:1rem">CSV input</label>
  <textarea id="cj-in" oninput="cjRun()" spellcheck="false" placeholder='name,age,city
Alice,30,Bratislava
Bob,25,"Vienna, Austria"'></textarea>
</div>
<div class="tool-card">
  <label>JSON output</label>
  <div class="output-row">
    <pre class="output" id="cj-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('cj-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<script>
function csvParse(text, delim){
  // RFC 4180-ish parser: handles quoted fields with embedded delim and newlines, escaped quotes via ""
  const rows = [];
  let row = [], field = '', i = 0, inQ = false;
  while (i < text.length){
    const c = text[i];
    if (inQ){
      if (c === '"'){
        if (text[i+1] === '"'){ field += '"'; i += 2; continue; }
        inQ = false; i++; continue;
      }
      field += c; i++; continue;
    }
    if (c === '"'){ inQ = true; i++; continue; }
    if (c === delim){ row.push(field); field = ''; i++; continue; }
    if (c === '\\n' || c === '\\r'){
      if (c === '\\r' && text[i+1] === '\\n') i++;
      row.push(field); rows.push(row); row = []; field = ''; i++; continue;
    }
    field += c; i++;
  }
  if (field !== '' || row.length){ row.push(field); rows.push(row); }
  return rows;
}
function cjRun(){
  const raw = document.getElementById('cj-in').value;
  const delim = document.getElementById('cj-delim').value === '\\\\t' ? '\\t' : document.getElementById('cj-delim').value;
  const useHeader = document.getElementById('cj-header').value === 'yes';
  const out = document.getElementById('cj-out');
  out.classList.remove('error');
  if (!raw.trim()){ out.textContent = '{LBL_NO_INPUT}'; return; }
  try {
    const rows = csvParse(raw, delim);
    let result;
    if (useHeader && rows.length){
      const keys = rows[0];
      result = rows.slice(1).map(r => {
        const o = {};
        for (let k = 0; k < keys.length; k++){
          let v = r[k] ?? '';
          // type-coerce numbers/bools/null
          if (v === 'true') v = true;
          else if (v === 'false') v = false;
          else if (v === 'null' || v === '') v = v === 'null' ? null : '';
          else if (/^-?\\d+(?:\\.\\d+)?(?:[eE][-+]?\\d+)?$/.test(v)) v = Number(v);
          o[keys[k]] = v;
        }
        return o;
      });
    } else {
      result = rows;
    }
    out.textContent = JSON.stringify(result, null, 2);
  } catch(e){ out.classList.add('error'); out.textContent = '✗ ' + e.message; }
}
document.addEventListener('DOMContentLoaded', cjRun);
</script>
""",
    "help": {
        "en": """
<h2>How it works</h2>
<p>The parser follows RFC 4180 conventions: fields can be wrapped in double quotes, embedded delimiters and newlines work inside quotes, and a literal quote inside a quoted field is escaped by doubling it (<code>""</code>).</p>
<h3>Type coercion</h3>
<p>When emitting objects, numeric values, <code>true</code>, <code>false</code>, and the literal string <code>null</code> are converted to the equivalent JSON types. Empty cells become empty strings.</p>
<h3>Tips</h3>
<ul>
  <li>If your file uses semicolons (common in EU locales), switch the delimiter dropdown.</li>
  <li>For TSV files, choose tab.</li>
  <li>To preserve everything as strings, post-process the output rather than relying on auto-coercion.</li>
</ul>
""",
    },
    "related": ["json-to-csv", "json-formatter", "yaml-json"],
}
