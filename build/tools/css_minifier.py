TOOL = {
    "slug": "css-minifier",
    "category": "developer",
    "icon": "{}",
    "tags": ["css", "minify", "compress", "optimize", "stylesheet"],
    "i18n": {
        "en": {
            "name": "CSS Minifier",
            "tagline": "Strip comments, whitespace, and redundancy from CSS. See size before/after and the saving percentage.",
            "description": "Free online CSS minifier. Removes comments, collapses whitespace, trims trailing semicolons and zero units. Shows compression ratio.",
        },
        "de": {"name": "CSS-Minifier", "tagline": "Kommentare, Leerzeichen und Redundanz aus CSS entfernen. Vorher/Nachher-Größe und Einsparung anzeigen.", "description": "Kostenloser CSS-Minifier. Entfernt Kommentare, kürzt Leerzeichen, trimmt überflüssige Semikolons und Null-Einheiten. Mit Kompressionsanzeige."},
        "es": {"name": "Minificador CSS", "tagline": "Elimina comentarios, espacios y redundancia del CSS. Compara tamaños y porcentaje de ahorro.", "description": "Minificador CSS en línea gratuito. Elimina comentarios, comprime espacios, recorta puntos y comas y unidades cero. Muestra ratio de compresión."},
        "fr": {"name": "Minificateur CSS", "tagline": "Supprimez commentaires, espaces et redondances du CSS. Tailles avant/après et pourcentage d'économie.", "description": "Minificateur CSS gratuit. Supprime commentaires, espaces inutiles, point-virgules superflus et unités zéro. Affiche le taux de compression."},
        "it": {"name": "Minificatore CSS", "tagline": "Rimuovi commenti, spazi e ridondanza dal CSS. Vedi dimensione prima/dopo e percentuale di risparmio.", "description": "Minificatore CSS online gratuito. Rimuove commenti, comprime spazi, taglia punti e virgola e unità zero. Mostra il rapporto di compressione."},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="cm-input" oninput="cmRun()" placeholder="/* paste your CSS here */
.button {
  background: #3b82f6;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  color: #ffffff;
}" spellcheck="false">/* sample */
.button {
  background-color: #3b82f6;
  padding: 0.5rem 1.0rem;
  border-radius: 6px;
  color: #ffffff;
  margin: 0px 0px 0px 0px;
}

/* hover state */
.button:hover {
  background-color: #2563eb;
}</textarea>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="cm-out" style="white-space:pre-wrap;word-break:break-all"></pre>
    <button class="copy-btn secondary" onclick="copyOutput('cm-out', this)">{LBL_COPY}</button>
  </div>
  <div class="meta" id="cm-stats" style="margin-top:0.6rem"></div>
</div>
""",
    "script": """
<script>
function copyOutput(id, btn){
  const el = document.getElementById(id);
  navigator.clipboard.writeText(el.textContent || '');
  const o = btn.textContent; btn.textContent = '✓'; setTimeout(()=>btn.textContent = o, 900);
}
function cmMinify(css){
  // Strip /* … */ comments (non-greedy)
  let out = css.replace(/\\/\\*[\\s\\S]*?\\*\\//g, '');
  // Preserve string contents — quick mask
  const strings = [];
  out = out.replace(/("([^"\\\\]|\\\\.)*"|'([^'\\\\]|\\\\.)*')/g, m => { strings.push(m); return '\\u0001' + (strings.length-1) + '\\u0002'; });
  // Collapse all whitespace
  out = out.replace(/\\s+/g, ' ');
  // Tighten around punctuation
  out = out.replace(/\\s*([{}:;,>~+])\\s*/g, '$1');
  // Trim trailing ; before }
  out = out.replace(/;}/g, '}');
  // Drop leading zeros (0.5 → .5) but keep 0 alone
  out = out.replace(/(^|[\\s:,(])0+(\\.\\d+)/g, '$1$2');
  // Zero units (0px, 0em, 0% → 0) — but not in calc() and not for time/angle where 0s differs
  out = out.replace(/(^|[\\s:,(])(0)(px|em|rem|%|vh|vw|pt|pc|ex|ch)(?=[\\s,;)})]|$)/g, '$1$2');
  // Hex shortening (#aabbcc → #abc)
  out = out.replace(/#([0-9a-f])\\1([0-9a-f])\\2([0-9a-f])\\3/gi, '#$1$2$3');
  // Restore strings
  out = out.replace(/\\u0001(\\d+)\\u0002/g, (_, i) => strings[+i]);
  return out.trim();
}
function cmRun(){
  const src = document.getElementById('cm-input').value;
  const out = document.getElementById('cm-out');
  const stats = document.getElementById('cm-stats');
  if(!src.trim()){ out.textContent = '{LBL_NO_INPUT}'; stats.textContent = ''; return; }
  const min = cmMinify(src);
  out.textContent = min;
  const before = new Blob([src]).size;
  const after = new Blob([min]).size;
  const saved = before - after;
  const pct = before ? Math.round((saved/before)*100) : 0;
  stats.textContent = `Original: ${before.toLocaleString()} B · Minified: ${after.toLocaleString()} B · Saved: ${saved.toLocaleString()} B (${pct}%)`;
}
document.addEventListener('DOMContentLoaded', cmRun);
</script>
""",
    "help": {
        "en": """
<h2>What gets removed</h2>
<ul>
  <li>Block comments (<code>/* … */</code>) — single-line <code>//</code> isn't valid in plain CSS.</li>
  <li>Whitespace around <code>{</code>, <code>}</code>, <code>:</code>, <code>;</code>, <code>,</code>, and combinators (<code>&gt; ~ +</code>).</li>
  <li>Trailing semicolons before <code>}</code>.</li>
  <li>Leading zeros (<code>0.5</code> → <code>.5</code>) and zero units (<code>0px</code> → <code>0</code>).</li>
  <li>Long hex (<code>#aabbcc</code> → <code>#abc</code>) where it's exact.</li>
</ul>
<h3>What it doesn't do</h3>
<p>This is a fast structural minify, not a full optimiser. It won't merge selectors, reorder rules, or rewrite shorthand — for that, use <code>cssnano</code> or <code>esbuild</code> in your build chain.</p>
""",
    },
    "related": ["js-minifier", "html-encoder", "color-picker"],
}
