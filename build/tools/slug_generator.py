TOOL = {
    "slug": "slug-generator",
    "category": "text",
    "icon": "/-",
    "tags": ["slug", "url", "seo", "kebab", "permalink", "transliterate"],
    "i18n": {
        "en": {
            "name": "Slug Generator",
            "tagline": "Turn any title into a clean URL slug — transliterates accents, strips punctuation, joins with hyphens.",
            "description": "Free online URL slug generator. Lowercases, transliterates accented characters (à → a, ñ → n), strips punctuation, and joins words with a chosen separator. Stop-word removal optional.",
        },
        "de": {"name": "Slug-Generator", "tagline": "Wandle jeden Titel in einen sauberen URL-Slug um — transliteriert Akzente, entfernt Satzzeichen, verbindet mit Bindestrichen.", "description": "Kostenloser URL-Slug-Generator. Kleinbuchstaben, Transliteration von Akzentzeichen (à → a, ñ → n), Satzzeichen entfernen, Wörter mit Trennzeichen verbinden."},
        "es": {"name": "Generador de Slug", "tagline": "Convierte cualquier título en un slug URL limpio — translitera acentos, elimina puntuación, une con guiones.", "description": "Generador de slugs URL gratuito. Minúsculas, transliteración de acentos (à → a, ñ → n), eliminación de puntuación y unión de palabras con separador."},
        "fr": {"name": "Générateur de Slug", "tagline": "Transformez tout titre en slug URL propre — translittère les accents, supprime la ponctuation, joint avec tirets.", "description": "Générateur de slug URL gratuit. Minuscules, translittération des accents (à → a, ñ → n), suppression de la ponctuation et jonction des mots."},
        "it": {"name": "Generatore di Slug", "tagline": "Trasforma qualsiasi titolo in uno slug URL pulito — translittera accenti, rimuove punteggiatura, unisce con trattini.", "description": "Generatore di slug URL gratuito. Minuscole, traslitterazione di accenti (à → a, ñ → n), rimozione punteggiatura e unione parole con separatore."},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="sg-input" oninput="sgRun()" placeholder="The Quick Brown Fox: A Café Story (1956)" spellcheck="false">The Quick Brown Fox: A Café Story (1956)</textarea>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Separator</label>
      <select id="sg-sep" onchange="sgRun()">
        <option value="-">- (hyphen, default)</option>
        <option value="_">_ (underscore)</option>
        <option value=".">. (dot)</option>
        <option value="">none</option>
      </select>
    </div>
    <div>
      <label>Case</label>
      <select id="sg-case" onchange="sgRun()">
        <option value="lower">lowercase</option>
        <option value="upper">UPPERCASE</option>
        <option value="preserve">preserve</option>
      </select>
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.5rem">
    <div>
      <label><input type="checkbox" id="sg-stop" onchange="sgRun()"> Strip English stop words</label>
    </div>
    <div>
      <label>Max length <input type="number" id="sg-max" value="80" min="1" max="500" oninput="sgRun()" style="width:80px;display:inline-block"></label>
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="sg-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('sg-out', this)">{LBL_COPY}</button>
  </div>
  <div id="sg-meta" class="meta" style="margin-top:0.5rem"></div>
</div>
""",
    "script": """
<script>
const SG_STOP = new Set(['a','an','and','the','of','to','in','on','at','for','by','with','from','is','are','was','were','be','been','as','it','this','that','these','those']);
function sgTransliterate(s){
  // NFD normalize then strip combining diacritics
  s = s.normalize('NFD').replace(/[\\u0300-\\u036f]/g, '');
  // common European ligatures + special letters
  const map = {
    'ß':'ss','æ':'ae','Æ':'AE','œ':'oe','Œ':'OE',
    'ø':'o','Ø':'O','å':'a','Å':'A','ł':'l','Ł':'L',
    'ð':'d','Ð':'D','þ':'th','Þ':'Th',
    '€':'eur','£':'gbp','$':'usd','¥':'jpy','%':'pct','&':'and','@':'at','+':'plus','=':'eq'
  };
  return s.replace(/[ßæÆœŒøØåÅłŁðÐþÞ€£$¥%&@+=]/g, c => map[c] || c);
}
function sgRun(){
  const raw = document.getElementById('sg-input').value;
  const sep = document.getElementById('sg-sep').value;
  const cas = document.getElementById('sg-case').value;
  const strip = document.getElementById('sg-stop').checked;
  const maxLen = Math.max(1, parseInt(document.getElementById('sg-max').value) || 80);
  const out = document.getElementById('sg-out');
  const meta = document.getElementById('sg-meta');
  if(!raw.trim()){ out.textContent = '{LBL_NO_INPUT}'; meta.textContent=''; return; }
  let s = sgTransliterate(raw);
  // collapse anything not letter/digit to a space
  s = s.replace(/[^A-Za-z0-9]+/g, ' ').trim();
  let words = s.split(/\\s+/);
  if(strip) words = words.filter(w => !SG_STOP.has(w.toLowerCase()));
  if(words.length === 0) words = [s.replace(/\\s+/g,'')];
  if(cas === 'lower') words = words.map(w => w.toLowerCase());
  else if(cas === 'upper') words = words.map(w => w.toUpperCase());
  let slug = words.join(sep);
  if(slug.length > maxLen){
    slug = slug.slice(0, maxLen);
    if(sep) slug = slug.replace(new RegExp('\\\\' + sep + '+$'), '');
  }
  out.textContent = slug || '—';
  meta.textContent = `${slug.length} characters · ${words.length} words${strip?' (after stop-word removal)':''}`;
}
document.addEventListener('DOMContentLoaded', sgRun);
</script>
""",
    "help": {
        "en": """
<h2>What it does</h2>
<ol>
  <li>NFD-normalizes Unicode then strips combining diacritics (so <code>café</code> → <code>cafe</code>).</li>
  <li>Maps a handful of European ligatures and special letters (<code>ß → ss</code>, <code>æ → ae</code>, <code>ø → o</code>, <code>Ł → L</code>, …).</li>
  <li>Replaces any non-alphanumeric run with a single space.</li>
  <li>Optionally strips a small set of common English stop words.</li>
  <li>Lowercases (or your chosen case), joins with the separator, and truncates to your limit at a clean boundary.</li>
</ol>
<h3>What it doesn't do</h3>
<p>It doesn't romanize CJK, Cyrillic, Arabic, or other non-Latin scripts character-by-character — those need language-specific tables this tool deliberately keeps out of scope. Such characters are dropped after diacritic stripping.</p>
""",
    },
    "related": ["case-converter", "url-encoder", "lorem-ipsum"],
}
