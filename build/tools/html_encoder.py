TOOL = {
    "slug": "html-encoder",
    "category": "encoding",
    "icon": "&lt;&gt;",
    "tags": ["html", "encode", "entities", "escape", "xss"],
    "i18n": {
        "en": {
            "name": "HTML Encoder / Decoder",
            "tagline": "Escape HTML special characters or decode entities back. Useful for safely embedding user input or debugging encoded markup.",
            "description": "Free online HTML entity encoder and decoder. Escapes &amp; &lt; &gt; &quot; ' and named entities. Decodes named, numeric, and hex entity references.",
        },
        "de": {"name": "HTML Encoder / Decoder", "tagline": "HTML-Sonderzeichen escapen oder Entities zurück in Klartext.", "description": "Kostenloser HTML-Entity Encoder und Decoder. Escapet &amp; &lt; &gt; &quot; ' und benannte Entities."},
        "es": {"name": "Codificador / Decodificador HTML", "tagline": "Escapa caracteres especiales HTML o decodifica entidades.", "description": "Codificador y decodificador de entidades HTML gratuito. Escapa &amp; &lt; &gt; &quot; ' y entidades con nombre."},
        "fr": {"name": "Encodeur / Décodeur HTML", "tagline": "Échappez les caractères spéciaux HTML ou décodez les entités.", "description": "Encodeur et décodeur d'entités HTML gratuit. Échappe &amp; &lt; &gt; &quot; ' et entités nommées."},
        "it": {"name": "Encoder / Decoder HTML", "tagline": "Escape di caratteri speciali HTML o decodifica delle entità.", "description": "Encoder e decoder di entità HTML gratuito. Escape di &amp; &lt; &gt; &quot; ' e entità con nome."},
    },
    "body": """
<div class="tool-card">
  <label>Mode</label>
  <select id="he-mode" onchange="heRun()">
    <option value="enc">{LBL_ENCODE} (text → entities)</option>
    <option value="dec">{LBL_DECODE} (entities → text)</option>
  </select>
  <label style="margin-top:1rem">{LBL_INPUT}</label>
  <textarea id="he-in" oninput="heRun()" spellcheck="false"></textarea>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="he-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('he-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<script>
function heEnc(s){ return s.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function heDec(s){
  const t = document.createElement('textarea');
  t.innerHTML = s;
  return t.value;
}
function heRun(){
  const mode = document.getElementById('he-mode').value;
  const raw = document.getElementById('he-in').value;
  const out = document.getElementById('he-out');
  if (!raw){ out.textContent = '{LBL_NO_INPUT}'; return; }
  out.textContent = mode === 'enc' ? heEnc(raw) : heDec(raw);
}
document.addEventListener('DOMContentLoaded', heRun);
</script>
""",
    "help": {
        "en": """
<h2>When to use it</h2>
<ul>
  <li>Embedding untrusted user content in HTML — encode first to avoid XSS.</li>
  <li>Decoding scraped or copy-pasted markup that arrived with entities (<code>&amp;amp;</code>, <code>&amp;#x27;</code>).</li>
  <li>Inspecting templates that have been double-escaped accidentally.</li>
</ul>
<h3>What gets escaped</h3>
<p>The five SGML/HTML characters: <code>&amp;</code> <code>&lt;</code> <code>&gt;</code> <code>&quot;</code> <code>'</code>. Decoding handles those plus all named entities and numeric references (decimal and hex) via the browser's parser.</p>
""",
    },
    "related": ["url-encoder", "base64-encoder", "markdown-to-html"],
}
