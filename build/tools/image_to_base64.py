TOOL = {
    "slug": "image-to-base64",
    "category": "encoding",
    "icon": "🖼️",
    "tags": ["image", "base64", "data-uri", "convert", "embed"],
    "i18n": {
        "en": {
            "name": "Image to Base64",
            "tagline": "Convert any image to a Base64 data URI ready for inline use in HTML, CSS, or Markdown. Files stay in your browser.",
            "description": "Free online image to Base64 data URI encoder. Drop or pick an image and get a ready-to-paste data: URL for inline HTML, CSS background-image, or email.",
        },
        "de": {"name": "Bild zu Base64", "tagline": "Bilder in Base64-Data-URIs umwandeln, fertig zum Einfügen in HTML, CSS oder Markdown. Datei bleibt im Browser.", "description": "Kostenloser Bild-zu-Base64-Data-URI-Encoder. Bild auswählen und einsatzbereite data:-URL erhalten."},
        "es": {"name": "Imagen a Base64", "tagline": "Convierte cualquier imagen en un data URI Base64 para HTML, CSS o Markdown. El archivo nunca sale de tu navegador.", "description": "Codificador gratuito de imágenes a data URI Base64. Selecciona una imagen y obtén la URL data: lista para pegar."},
        "fr": {"name": "Image vers Base64", "tagline": "Convertissez n'importe quelle image en data URI Base64 pour HTML, CSS ou Markdown. Le fichier ne quitte pas votre navigateur.", "description": "Encodeur gratuit d'image en data URI Base64. Sélectionnez une image et obtenez l'URL data: prête à coller."},
        "it": {"name": "Immagine a Base64", "tagline": "Converti qualsiasi immagine in un data URI Base64 per HTML, CSS o Markdown. Il file non lascia il browser.", "description": "Encoder gratuito di immagini in data URI Base64. Seleziona un'immagine e ottieni l'URL data: pronta da incollare."},
    },
    "body": """
<div class="tool-card">
  <label>Pick or drop an image</label>
  <input type="file" id="i2b-file" accept="image/*" oninput="i2bRun()" style="padding:0.5rem;background:var(--code-bg);border:1px dashed var(--border);border-radius:6px">
  <div class="meta" id="i2b-meta"></div>
</div>
<div class="tool-card">
  <label>Preview</label>
  <div id="i2b-prev" style="text-align:center;padding:1rem;background:var(--code-bg);border:1px solid var(--border);border-radius:6px;min-height:60px"><span style="color:var(--text-muted)">No image yet.</span></div>
</div>
<div class="tool-card">
  <label>Data URI</label>
  <div class="output-row">
    <pre class="output" id="i2b-out" style="max-height:240px;overflow:auto;font-size:0.78rem">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('i2b-out', this)">{LBL_COPY}</button>
  </div>
</div>
<div class="tool-card">
  <label>Snippets</label>
  <div class="output-row"><pre class="output" id="i2b-html" style="font-size:0.85rem"></pre><button class="copy-btn secondary" onclick="copyOutput('i2b-html', this)">{LBL_COPY}</button></div>
  <div class="output-row" style="margin-top:0.5rem"><pre class="output" id="i2b-css" style="font-size:0.85rem"></pre><button class="copy-btn secondary" onclick="copyOutput('i2b-css', this)">{LBL_COPY}</button></div>
  <div class="output-row" style="margin-top:0.5rem"><pre class="output" id="i2b-md" style="font-size:0.85rem"></pre><button class="copy-btn secondary" onclick="copyOutput('i2b-md', this)">{LBL_COPY}</button></div>
</div>
""",
    "script": """
<script>
function i2bRun(){
  const f = document.getElementById('i2b-file').files[0];
  const out = document.getElementById('i2b-out');
  const meta = document.getElementById('i2b-meta');
  const prev = document.getElementById('i2b-prev');
  if (!f){ out.textContent = '{LBL_NO_INPUT}'; meta.textContent=''; prev.innerHTML='<span style="color:var(--text-muted)">No image yet.</span>'; document.getElementById('i2b-html').textContent=''; document.getElementById('i2b-css').textContent=''; document.getElementById('i2b-md').textContent=''; return; }
  if (f.size > 5 * 1024 * 1024){ out.classList.add('error'); out.textContent = '✗ File larger than 5 MB. Inline data URIs that big are usually a bad idea — use a real image URL.'; return; }
  out.classList.remove('error');
  const r = new FileReader();
  r.onload = () => {
    const uri = r.result;
    out.textContent = uri;
    meta.textContent = f.name + ' · ' + f.type + ' · ' + (f.size/1024).toFixed(1) + ' KB → ' + (uri.length/1024).toFixed(1) + ' KB encoded';
    prev.innerHTML = '<img src="' + uri + '" style="max-width:100%;max-height:280px;border-radius:6px">';
    document.getElementById('i2b-html').textContent = '<img src="' + uri.slice(0, 60) + '…" alt="">';
    document.getElementById('i2b-css').textContent = 'background-image: url("' + uri.slice(0, 60) + '…");';
    document.getElementById('i2b-md').textContent = '![alt](' + uri.slice(0, 60) + '…)';
  };
  r.readAsDataURL(f);
}
</script>
""",
    "help": {
        "en": """
<h2>When to use a data URI</h2>
<ul>
  <li>Tiny icons (&lt; 4 KB) inline in CSS — saves an HTTP request.</li>
  <li>Self-contained HTML emails or single-file demos.</li>
  <li>Quick pastes into Markdown notes that need to travel without a separate image file.</li>
</ul>
<h3>When NOT to use it</h3>
<ul>
  <li>Larger images — base64 is ~33% bigger than the binary, and inline data can't be cached separately.</li>
  <li>Anything reused across pages — keep it as a real URL so it caches once.</li>
</ul>
<p>The image is read by your browser via <code>FileReader.readAsDataURL</code>. Nothing is uploaded.</p>
""",
    },
    "related": ["base64-encoder", "qr-code-generator", "url-encoder"],
}
