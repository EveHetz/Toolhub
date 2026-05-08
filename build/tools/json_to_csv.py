TOOL = {
    "slug": "json-to-csv",
    "category": "data",
    "icon": "📋",
    "tags": ["json", "csv", "convert", "data", "export", "excel"],
    "i18n": {
        "en": {
            "name": "JSON to CSV",
            "tagline": "Convert JSON arrays of objects to CSV. Auto-detects fields, supports custom delimiters, escapes properly for Excel and Google Sheets.",
            "description": "Free online JSON to CSV converter. Flattens arrays of objects to rows, escapes quotes per RFC 4180, supports comma/semicolon/tab delimiters.",
        },
        "de": {"name": "JSON zu CSV", "tagline": "Konvertiere JSON-Arrays von Objekten zu CSV. Auto-Felderkennung, eigene Trennzeichen, Excel- und Google-Sheets-kompatibel.", "description": "Kostenloser JSON-zu-CSV-Konverter. Wandelt Objekt-Arrays in Zeilen um, escapet nach RFC 4180, unterstützt Komma/Semikolon/Tab."},
        "es": {"name": "JSON a CSV", "tagline": "Convierte arrays JSON de objetos en CSV. Detecta campos, soporta separadores personalizados, escapado para Excel y Google Sheets.", "description": "Conversor JSON a CSV gratuito. Aplana arrays de objetos en filas, escape conforme a RFC 4180, separadores coma/punto y coma/tab."},
        "fr": {"name": "JSON vers CSV", "tagline": "Convertissez des tableaux JSON d'objets en CSV. Détection des champs, séparateurs personnalisés, échappement compatible Excel et Google Sheets.", "description": "Convertisseur JSON vers CSV gratuit. Aplatit les tableaux d'objets en lignes, échappement RFC 4180, séparateurs virgule/point-virgule/tab."},
        "it": {"name": "JSON a CSV", "tagline": "Converti array JSON di oggetti in CSV. Rilevamento campi, separatori personalizzati, escape compatibile con Excel e Google Sheets.", "description": "Convertitore JSON-CSV gratuito. Appiattisce array di oggetti in righe, escape RFC 4180, separatori virgola/punto e virgola/tab."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Delimiter</label>
      <select id="jc-delim" onchange="jcRun()">
        <option value=",">, comma</option>
        <option value=";">; semicolon</option>
        <option value="\\t">tab</option>
        <option value="|">| pipe</option>
      </select>
    </div>
    <div>
      <label>Output</label>
      <select id="jc-mode" onchange="jcRun()">
        <option value="header">With header row</option>
        <option value="noheader">No header row</option>
      </select>
    </div>
  </div>
  <label style="margin-top:1rem">JSON input (array of objects, or array of arrays)</label>
  <textarea id="jc-in" oninput="jcRun()" spellcheck="false" placeholder='[{"name":"Alice","age":30},{"name":"Bob","age":25}]'></textarea>
</div>
<div class="tool-card">
  <label>CSV output</label>
  <div class="output-row">
    <pre class="output" id="jc-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('jc-out', this)">{LBL_COPY}</button>
  </div>
  <button class="secondary" onclick="jcDownload()" style="margin-top:0.5rem">{LBL_DOWNLOAD} .csv</button>
</div>
""",
    "script": """
<script>
function jcEsc(v, delim){
  if (v === null || v === undefined) return '';
  let s = typeof v === 'object' ? JSON.stringify(v) : String(v);
  if (s.includes('"') || s.includes(delim) || s.includes('\\n') || s.includes('\\r')){
    s = '"' + s.replace(/"/g,'""') + '"';
  }
  return s;
}
function jcRun(){
  const raw = document.getElementById('jc-in').value.trim();
  const delim = document.getElementById('jc-delim').value === '\\\\t' ? '\\t' : document.getElementById('jc-delim').value;
  const withHeader = document.getElementById('jc-mode').value === 'header';
  const out = document.getElementById('jc-out');
  out.classList.remove('error');
  if (!raw){ out.textContent = '{LBL_NO_INPUT}'; return; }
  let data;
  try { data = JSON.parse(raw); }
  catch(e){ out.classList.add('error'); out.textContent = '✗ Invalid JSON: ' + e.message; return; }
  if (!Array.isArray(data)){ out.classList.add('error'); out.textContent = '✗ Expected a JSON array at the top level'; return; }
  if (data.length === 0){ out.textContent = ''; return; }
  let csv = '';
  if (data.every(r => Array.isArray(r))){
    csv = data.map(r => r.map(v => jcEsc(v, delim)).join(delim)).join('\\n');
  } else if (data.every(r => r && typeof r === 'object')){
    const keys = [...new Set(data.flatMap(r => Object.keys(r)))];
    if (withHeader) csv += keys.map(k => jcEsc(k, delim)).join(delim) + '\\n';
    csv += data.map(r => keys.map(k => jcEsc(r[k], delim)).join(delim)).join('\\n');
  } else {
    out.classList.add('error'); out.textContent = '✗ Mixed array — expected uniform objects or arrays'; return;
  }
  out.textContent = csv;
}
function jcDownload(){
  const csv = document.getElementById('jc-out').textContent;
  if (!csv || csv === '{LBL_NO_INPUT}') return;
  const blob = new Blob([csv], {type: 'text/csv'});
  const a = document.createElement('a');
  a.download = 'data.csv';
  a.href = URL.createObjectURL(blob);
  a.click();
}
document.addEventListener('DOMContentLoaded', jcRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>The reverse trip: feed in a JSON array and get out a CSV ready for Excel, Google Sheets, or any data tool that prefers tabular formats. Headers are auto-detected from object keys; nested values get JSON-stringified into single cells so nothing silently disappears.</p>

<h3>When to use it</h3>
<ul>
  <li>Turning an API response into a CSV for a stakeholder who only opens spreadsheets.</li>
  <li>Exporting a pile of records from a JSON dump into something you can pivot/filter in Sheets.</li>
  <li>Generating fixture rows for database imports that take CSV.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Header inference uses the union of all object keys.</strong> A row missing a key becomes an empty cell; the column doesn't disappear.</li>
  <li><strong>Nested objects/arrays are stringified.</strong> If you need a flattened CSV (one column per nested key), pre-flatten the JSON before feeding it in.</li>
  <li><strong>Excel + delimiters.</strong> European locales default to semicolons; switch the delimiter so the file opens with columns instead of one giant line. RFC 4180 escaping is applied either way.</li>
  <li><strong>UTF-8 BOM.</strong> Excel on macOS sometimes garbles non-ASCII without a BOM. This tool does NOT prepend one — paste the output through a BOM-adding step if you see mojibake.</li>
</ul>
""",
    },
    "related": ["csv-to-json", "json-formatter", "yaml-json"],
}
