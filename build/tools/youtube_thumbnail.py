TOOL = {
    "slug": "youtube-thumbnail",
    "category": "media",
    "icon": "▶",
    "tags": ["youtube", "thumbnail", "preview", "image", "download", "video"],
    "i18n": {
        "en": {
            "name": "YouTube Thumbnail Downloader",
            "tagline": "Paste any YouTube URL or video ID and grab every available thumbnail size — direct download links, no upload, no signup.",
            "description": "Free YouTube thumbnail downloader. Extracts the video ID from any YouTube URL (watch, youtu.be, shorts, embed, /v/) and shows all available thumbnail resolutions with direct download links.",
        },
        "de": {"name": "YouTube Thumbnail-Downloader", "tagline": "Füge eine YouTube-URL oder Video-ID ein und erhalte alle verfügbaren Thumbnail-Größen — direkte Download-Links, kein Upload.", "description": "Kostenloser YouTube-Thumbnail-Downloader. Extrahiert die Video-ID aus jeder YouTube-URL (watch, youtu.be, shorts, embed) und zeigt alle Thumbnail-Auflösungen mit direkten Download-Links."},
        "es": {"name": "Descargador de Miniaturas de YouTube", "tagline": "Pega cualquier URL de YouTube o ID de vídeo y obtén todos los tamaños de miniatura disponibles — descarga directa, sin registro.", "description": "Descargador gratuito de miniaturas de YouTube. Extrae el ID de vídeo de cualquier URL de YouTube y muestra todas las resoluciones de miniaturas con enlaces de descarga directa."},
        "fr": {"name": "Téléchargeur de Miniatures YouTube", "tagline": "Collez n'importe quelle URL YouTube ou ID vidéo et obtenez toutes les tailles de miniatures disponibles — téléchargement direct, sans inscription.", "description": "Téléchargeur gratuit de miniatures YouTube. Extrait l'ID vidéo de toute URL YouTube et affiche toutes les résolutions de miniatures avec liens de téléchargement directs."},
        "it": {"name": "Download Miniature YouTube", "tagline": "Incolla qualsiasi URL YouTube o ID video e ottieni tutte le dimensioni di miniatura disponibili — link diretti, nessuna registrazione.", "description": "Download gratuito di miniature YouTube. Estrae l'ID video da qualsiasi URL YouTube e mostra tutte le risoluzioni di miniature con link di download diretti."},
    },
    "body": """
<div class="tool-card">
  <label>YouTube URL or video ID</label>
  <input type="text" id="yt-input" oninput="ytRun()" placeholder="https://www.youtube.com/watch?v=dQw4w9WgXcQ" spellcheck="false" autocomplete="off">
  <div class="meta" style="margin-top:0.5rem">Supports <code>youtube.com/watch?v=</code>, <code>youtu.be/</code>, <code>youtube.com/shorts/</code>, <code>youtube.com/embed/</code>, <code>youtube.com/v/</code>, or just the 11-character ID.</div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="yt-out" class="output">{LBL_NO_INPUT}</div>
</div>
""",
    "script": """
<style>
.yt-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:0.8rem}
.yt-card{background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;overflow:hidden;display:flex;flex-direction:column}
.yt-card img{width:100%;height:auto;display:block;background:#000;aspect-ratio:16/9;object-fit:cover}
.yt-card .yt-info{padding:0.55rem 0.7rem;display:flex;flex-direction:column;gap:0.35rem;font-size:0.82rem}
.yt-card .yt-name{font-weight:600;color:var(--text)}
.yt-card .yt-meta{color:var(--text-muted);font-family:ui-monospace,monospace;font-size:0.78rem}
.yt-card .yt-actions{display:flex;gap:0.35rem;margin-top:0.25rem}
.yt-card a.yt-btn{flex:1;text-align:center;background:var(--accent);color:#fff;text-decoration:none;padding:0.4rem 0.55rem;border-radius:6px;font-size:0.78rem;font-weight:600}
.yt-card button.yt-btn{flex:1;font-size:0.78rem;padding:0.4rem 0.55rem}
.yt-id{margin-bottom:0.7rem;font-family:ui-monospace,monospace;font-size:0.85rem;color:var(--text-muted)}
.yt-id code{background:var(--bg-elev);padding:0.15rem 0.4rem;border-radius:4px;color:var(--text)}
</style>
<script>
const YT_VARIANTS = [
  {key:'maxresdefault', name:'Max Resolution', size:'1280×720', note:'Not always available'},
  {key:'sddefault',     name:'Standard',       size:'640×480',  note:''},
  {key:'hqdefault',     name:'High Quality',   size:'480×360',  note:'Always available'},
  {key:'mqdefault',     name:'Medium Quality', size:'320×180',  note:''},
  {key:'default',       name:'Default',        size:'120×90',   note:''},
];
function ytExtractId(s){
  s = s.trim();
  if(!s) return null;
  if(/^[A-Za-z0-9_-]{11}$/.test(s)) return s;
  // youtu.be/<id>
  let m = s.match(/youtu\\.be\\/([A-Za-z0-9_-]{11})/);
  if(m) return m[1];
  // youtube.com/watch?v=<id>
  m = s.match(/[?&]v=([A-Za-z0-9_-]{11})/);
  if(m) return m[1];
  // youtube.com/shorts/<id> | /embed/<id> | /v/<id>
  m = s.match(/youtube\\.com\\/(?:shorts|embed|v)\\/([A-Za-z0-9_-]{11})/);
  if(m) return m[1];
  return null;
}
function ytCopy(text, btn){
  navigator.clipboard.writeText(text);
  const old = btn.textContent;
  btn.textContent = '✓';
  setTimeout(()=>btn.textContent = old, 900);
}
function ytRun(){
  const raw = document.getElementById('yt-input').value;
  const out = document.getElementById('yt-out');
  out.classList.remove('error');
  if(!raw){ out.textContent = '{LBL_NO_INPUT}'; out.className='output'; return; }
  const id = ytExtractId(raw);
  if(!id){ out.classList.add('error'); out.textContent = '✗ Could not find an 11-character YouTube video ID. Check the URL and try again.'; return; }
  out.className = 'output';
  let html = `<div class="yt-id">Video ID: <code>${id}</code> · <a href="https://www.youtube.com/watch?v=${id}" target="_blank" rel="noopener noreferrer">open on YouTube ↗</a></div>`;
  html += '<div class="yt-grid">';
  for(const v of YT_VARIANTS){
    const url = `https://i.ytimg.com/vi/${id}/${v.key}.jpg`;
    html += `<div class="yt-card">
      <img src="${url}" alt="${v.name}" loading="lazy" onerror="this.style.opacity=0.25;this.parentElement.querySelector('.yt-meta').textContent='${v.size} — image returned 404'">
      <div class="yt-info">
        <div class="yt-name">${v.name}</div>
        <div class="yt-meta">${v.size}${v.note?' · '+v.note:''}</div>
        <div class="yt-actions">
          <a class="yt-btn" href="${url}" download="${id}-${v.key}.jpg" target="_blank" rel="noopener noreferrer">{LBL_DOWNLOAD}</a>
          <button class="yt-btn secondary" onclick="ytCopy('${url}', this)">{LBL_COPY}</button>
        </div>
      </div>
    </div>`;
  }
  html += '</div>';
  out.innerHTML = html;
}
document.addEventListener('DOMContentLoaded', ytRun);
</script>
""",
    "help": {
        "en": """
<h2>How it works</h2>
<p>YouTube exposes thumbnails on a predictable URL pattern: <code>https://i.ytimg.com/vi/&lt;VIDEO_ID&gt;/&lt;variant&gt;.jpg</code>. This tool just extracts the video ID and shows every variant. The browser fetches the images directly from YouTube — nothing routes through this site.</p>
<h3>Variants</h3>
<ul>
  <li><strong>maxresdefault</strong> (1280×720) — only exists for videos uploaded in HD; otherwise 404.</li>
  <li><strong>sddefault</strong> (640×480) — generated for most videos.</li>
  <li><strong>hqdefault</strong> (480×360) — always exists; the safe fallback.</li>
  <li><strong>mqdefault</strong> (320×180), <strong>default</strong> (120×90) — small previews.</li>
</ul>
<h3>Supported URL forms</h3>
<ul>
  <li><code>https://www.youtube.com/watch?v=ID</code></li>
  <li><code>https://youtu.be/ID</code></li>
  <li><code>https://www.youtube.com/shorts/ID</code></li>
  <li><code>https://www.youtube.com/embed/ID</code></li>
  <li><code>https://www.youtube.com/v/ID</code></li>
  <li>Or just the 11-character video ID on its own.</li>
</ul>
""",
    },
    "related": ["qr-code-generator", "image-to-base64", "url-encoder"],
}
