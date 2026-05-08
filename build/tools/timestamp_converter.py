TOOL = {
    "slug": "timestamp-converter",
    "category": "developer",
    "icon": "🕐",
    "tags": ["timestamp", "unix", "epoch", "date", "convert", "iso8601"],
    "i18n": {
        "en": {
            "name": "Unix Timestamp Converter",
            "tagline": "Convert between Unix timestamps and human-readable dates. Seconds and milliseconds, UTC and local.",
            "description": "Free online Unix timestamp converter. Convert between epoch seconds, milliseconds, ISO 8601, and human-readable dates in UTC or local time.",
        },
        "de": {"name": "Unix-Zeitstempel-Konverter", "tagline": "Konvertiere zwischen Unix-Zeitstempeln und lesbarem Datum. Sekunden und Millisekunden, UTC und lokal.", "description": "Kostenloser Unix-Zeitstempel-Konverter. Konvertiere zwischen Epoch-Sekunden, Millisekunden, ISO 8601 und lesbarem Datum."},
        "es": {"name": "Conversor de Timestamp Unix", "tagline": "Convierte entre timestamps Unix y fechas legibles. Segundos y milisegundos, UTC y local.", "description": "Conversor gratuito de timestamps Unix. Convierte entre segundos epoch, milisegundos, ISO 8601 y fechas legibles."},
        "fr": {"name": "Convertisseur Timestamp Unix", "tagline": "Convertissez entre timestamps Unix et dates lisibles. Secondes et millisecondes, UTC et local.", "description": "Convertisseur de timestamp Unix gratuit. Conversion entre secondes epoch, millisecondes, ISO 8601 et dates lisibles."},
        "it": {"name": "Convertitore Timestamp Unix", "tagline": "Converti tra timestamp Unix e date leggibili. Secondi e millisecondi, UTC e locale.", "description": "Convertitore gratuito di timestamp Unix. Conversione tra secondi epoch, millisecondi, ISO 8601 e date leggibili."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Unix timestamp</label>
      <input type="text" id="ts-num" oninput="tsFromNum()" placeholder="1704067200 or 1704067200000" style="font-family:ui-monospace,monospace">
      <div class="meta">Auto-detects seconds vs milliseconds</div>
    </div>
    <div>
      <label>Date &amp; time</label>
      <input type="datetime-local" id="ts-date" step="1" oninput="tsFromDate()">
      <div class="meta">Local timezone</div>
    </div>
  </div>
  <div class="button-row">
    <button onclick="tsNow()">Now</button>
    <button class="secondary" onclick="document.getElementById('ts-num').value=''; tsRender(null)">{LBL_CLEAR}</button>
  </div>
</div>
<div class="tool-card">
  <label>Result</label>
  <pre class="output" id="ts-out">{LBL_NO_INPUT}</pre>
</div>
""",
    "script": """
<script>
function tsRender(d){
  const out = document.getElementById('ts-out');
  if (!d){ out.textContent = '{LBL_NO_INPUT}'; return; }
  const ms = d.getTime();
  const sec = Math.floor(ms / 1000);
  const iso = d.toISOString();
  const local = d.toLocaleString(undefined, { weekday:'long', year:'numeric', month:'short', day:'2-digit', hour:'2-digit', minute:'2-digit', second:'2-digit' });
  const utc = d.toUTCString();
  // Relative
  const now = Date.now();
  const diffMs = ms - now;
  const abs = Math.abs(diffMs);
  let rel;
  const sec_ = Math.floor(abs/1000), min = Math.floor(sec_/60), hr = Math.floor(min/60), day = Math.floor(hr/24), yr = Math.floor(day/365);
  if (yr) rel = yr + 'y ' + (day - yr*365) + 'd';
  else if (day) rel = day + 'd ' + (hr - day*24) + 'h';
  else if (hr) rel = hr + 'h ' + (min - hr*60) + 'm';
  else if (min) rel = min + 'm ' + (sec_ - min*60) + 's';
  else rel = sec_ + 's';
  rel += diffMs >= 0 ? ' from now' : ' ago';
  out.textContent =
    'Unix seconds:       ' + sec + '\\n' +
    'Unix milliseconds:  ' + ms + '\\n' +
    'ISO 8601 (UTC):     ' + iso + '\\n' +
    'UTC:                ' + utc + '\\n' +
    'Local:              ' + local + '\\n' +
    'Relative:           ' + rel;
}
function tsFromNum(){
  const v = document.getElementById('ts-num').value.trim();
  if (!v){ tsRender(null); return; }
  const n = Number(v);
  if (!isFinite(n)){ tsRender(null); return; }
  // Heuristic: <= 10 digits = seconds, else ms
  const ms = (Math.abs(n) >= 1e12) ? n : (Math.abs(n) >= 1e10 ? n : n * 1000);
  const d = new Date(ms);
  // Update date input
  const pad = x => String(x).padStart(2,'0');
  document.getElementById('ts-date').value = d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate())+'T'+pad(d.getHours())+':'+pad(d.getMinutes())+':'+pad(d.getSeconds());
  tsRender(d);
}
function tsFromDate(){
  const v = document.getElementById('ts-date').value;
  if (!v){ tsRender(null); return; }
  const d = new Date(v);
  if (isNaN(d.getTime())){ tsRender(null); return; }
  document.getElementById('ts-num').value = Math.floor(d.getTime()/1000);
  tsRender(d);
}
function tsNow(){
  const d = new Date();
  document.getElementById('ts-num').value = Math.floor(d.getTime()/1000);
  const pad = x => String(x).padStart(2,'0');
  document.getElementById('ts-date').value = d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate())+'T'+pad(d.getHours())+':'+pad(d.getMinutes())+':'+pad(d.getSeconds());
  tsRender(d);
}
document.addEventListener('DOMContentLoaded', tsNow);
</script>
""",
    "help": {
        "en": """
<h2>What's a Unix timestamp?</h2>
<p>The number of seconds since 1970-01-01 00:00:00 UTC. Stored as 32-bit signed in older systems (overflow at 03:14:08 UTC on 2038-01-19) or 64-bit signed everywhere modern.</p>
<h3>Seconds vs milliseconds</h3>
<p>Unix tradition stores seconds. JavaScript and most modern web APIs use milliseconds. This tool auto-detects: 10-digit numbers are read as seconds, 13-digit as milliseconds.</p>
<h3>ISO 8601</h3>
<p>The recommended format for storing/exchanging dates as text: <code>2025-01-01T00:00:00.000Z</code>. Unambiguous, sortable as a string, supported by every database.</p>
""",
    },
    "related": ["timezone-converter", "cron-parser", "date-calculator"],
}
