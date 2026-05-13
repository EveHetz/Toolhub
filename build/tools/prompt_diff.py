TOOL = {
    "slug": "prompt-diff",
    "category": "ai",
    "icon": "🔀",
    "tags": ["diff", "prompt", "compare", "text", "llm", "ai", "version", "side-by-side"],
    "i18n": {
        "en": {
            "name": "Prompt Diff",
            "tagline": "Compare two prompts (or two versions of a prompt) side by side. Line-level diff with highlighted changes. Designed for iterating on LLM prompts.",
            "description": "Free in-browser prompt diff tool. Paste version A and version B — see line-by-line changes with red/green highlighting. Useful for prompt engineers comparing iterations, A/B testing prompts, or auditing what changed in a system prompt across deployments. Standard LCS diff algorithm.",
        },
        "de": {
            "name": "Prompt-Diff",
            "tagline": "Vergleiche zwei Prompts (oder zwei Versionen eines Prompts) Seite an Seite. Zeilen-Diff mit hervorgehobenen Änderungen. Für Iteration an LLM-Prompts.",
            "description": "Kostenloses Prompt-Diff-Tool im Browser. Füge Version A und Version B ein — sieh zeilenweise Änderungen mit Rot/Grün-Hervorhebung. Nützlich für Prompt Engineers, die Iterationen vergleichen, Prompts A/B-testen oder prüfen, was sich in einem System-Prompt zwischen Deployments geändert hat. Klassischer LCS-Diff-Algorithmus.",
        },
        "es": {
            "name": "Diff de Prompts",
            "tagline": "Compara dos prompts (o dos versiones del mismo prompt) lado a lado. Diff línea a línea con cambios resaltados. Diseñado para iterar prompts de LLM.",
            "description": "Diff de prompts gratuito en el navegador. Pega la versión A y la versión B — verás los cambios línea por línea con resaltado rojo/verde. Útil para prompt engineers que comparan iteraciones, prueban A/B de prompts o auditan qué ha cambiado en un system prompt entre despliegues. Algoritmo LCS estándar.",
        },
        "fr": {
            "name": "Diff de Prompts",
            "tagline": "Comparez deux prompts (ou deux versions d'un prompt) côte à côte. Diff ligne par ligne avec changements surlignés. Conçu pour itérer sur des prompts LLM.",
            "description": "Outil de diff de prompts gratuit dans le navigateur. Collez la version A et la version B — voyez les changements ligne par ligne avec surlignage rouge/vert. Utile pour les prompt engineers qui comparent des itérations, font de l'A/B testing de prompts ou auditent ce qui a changé dans un system prompt entre déploiements. Algorithme LCS standard.",
        },
        "it": {
            "name": "Diff di Prompt",
            "tagline": "Confronta due prompt (o due versioni dello stesso prompt) affiancati. Diff a livello di riga con modifiche evidenziate. Pensato per iterare sui prompt LLM.",
            "description": "Strumento gratuito di diff prompt nel browser. Incolla la versione A e la versione B — vedi le modifiche riga per riga con evidenziazione rossa/verde. Utile per prompt engineer che confrontano iterazioni, fanno A/B test di prompt o controllano cosa è cambiato in un system prompt tra deployment. Algoritmo LCS standard.",
        },
        "pt": {
            "name": "Diff de Prompt",
            "tagline": "Compare dois prompts (ou duas versões do mesmo prompt) lado a lado. Diff linha a linha com mudanças destacadas. Pensado pra iterar prompts de LLM.",
            "description": "Ferramenta grátis de diff de prompt no navegador. Cole a versão A e a versão B — veja as mudanças linha por linha com destaque vermelho/verde. Útil pra prompt engineers comparando iterações, fazendo A/B test de prompts ou auditando o que mudou em um system prompt entre deploys. Algoritmo LCS padrão.",
        },
        "pl": {
            "name": "Diff Promptów",
            "tagline": "Porównaj dwa prompty (albo dwie wersje promptu) obok siebie. Diff na poziomie linii z podświetlonymi zmianami. Zaprojektowany do iterowania promptów LLM.",
            "description": "Darmowe in-browser narzędzie do diffowania promptów. Wklej wersję A i wersję B — zobacz zmiany linia po linii z czerwono-zielonym podświetleniem. Przydatne dla prompt engineerów porównujących iteracje, A/B-testujących prompty albo audytujących, co zmieniło się w system promptcie między deploymentami. Klasyczny algorytm LCS.",
        },
        "ja": {
            "name": "プロンプト Diff",
            "tagline": "2 つのプロンプト（または同じプロンプトの 2 バージョン）を並べて比較。行単位の差分を赤／緑でハイライト。LLM プロンプト改良用。",
            "description": "ブラウザ完結のプロンプト差分ツール（無料）。バージョン A とバージョン B を貼り付けると、行単位の変更が赤／緑のハイライトで表示されます。プロンプトを改良するエンジニア、プロンプトを A/B テストする人、デプロイ間で system prompt が何変わったかを監査したい人に便利。一般的な LCS ベースの差分アルゴリズムを使用。",
        },
        "nl": {
            "name": "Prompt Diff",
            "tagline": "Vergelijk twee prompts (of twee versies van een prompt) naast elkaar. Line-level diff met gemarkeerde wijzigingen. Ontworpen voor het itereren op LLM-prompts.",
            "description": "Gratis in-browser prompt diff tool. Plak versie A en versie B — zie regel-voor-regel wijzigingen met rood/groen highlighting. Handig voor prompt engineers die iteraties vergelijken, prompts A/B-testen, of auditen wat er in een system prompt veranderd is tussen deployments. Klassiek LCS diff-algoritme.",
        },
        "tr": {
            "name": "Prompt Diff",
            "tagline": "İki prompt'u (veya bir prompt'un iki sürümünü) yan yana karşılaştır. Vurgulanmış değişikliklerle satır seviyesi diff. LLM prompt'ları üzerinde iterasyon için tasarlandı.",
            "description": "Ücretsiz tarayıcı içi prompt diff aracı. Sürüm A ve sürüm B'yi yapıştır — satır satır değişiklikleri kırmızı/yeşil vurgu ile gör. İterasyonları karşılaştıran, prompt'ları A/B test eden veya deployment'lar arasında system prompt'ta ne değiştiğini denetleyen prompt engineer'lar için yararlı. Standart LCS diff algoritması.",
        },
        "id": {
            "name": "Prompt Diff",
            "tagline": "Bandingkan dua prompt (atau dua versi prompt) berdampingan. Diff level baris dengan perubahan disorot. Dirancang untuk iterasi prompt LLM.",
            "description": "Tool diff prompt gratis di browser. Tempel versi A dan versi B — lihat perubahan baris demi baris dengan sorotan merah/hijau. Berguna untuk prompt engineer yang membandingkan iterasi, melakukan A/B test prompt, atau mengaudit apa yang berubah pada system prompt antar deployment. Algoritma LCS standar.",
        },
        "vi": {
            "name": "Diff Prompt",
            "tagline": "So sánh hai prompt (hoặc hai phiên bản của một prompt) cạnh nhau. Diff theo từng dòng với các thay đổi được làm nổi bật. Thiết kế cho việc lặp lại các prompt LLM.",
            "description": "Công cụ diff prompt miễn phí trên trình duyệt. Dán phiên bản A và phiên bản B — xem các thay đổi từng dòng với highlight đỏ/xanh. Hữu ích cho prompt engineer so sánh các phiên bản, A/B test prompt, hoặc audit những gì đã thay đổi trong system prompt giữa các lần deploy. Thuật toán LCS chuẩn.",
        },
        "hi": {
            "name": "Prompt Diff",
            "tagline": "दो prompts (या एक prompt के दो versions) की साथ-साथ तुलना करें। हाइलाइट किए गए बदलावों के साथ line-level diff। LLM prompts पर iterate करने के लिए designed।",
            "description": "मुफ़्त in-browser prompt diff tool। Version A और version B paste करें — लाल/हरे highlighting के साथ line-by-line changes देखें। Iterations की तुलना करने वाले prompt engineers, prompts का A/B testing करने वालों, या deployments के बीच system prompt में क्या बदला यह audit करने के लिए उपयोगी। Standard LCS diff algorithm।",
        },
        "sk": {
            "name": "Prompt Diff",
            "tagline": "Porovnaj dva prompty (alebo dve verzie toho istého promptu) vedľa seba. Riadkový diff so zvýraznenými zmenami. Navrhnuté pre iteráciu LLM promptov.",
            "description": "Bezplatný in-browser prompt diff nástroj. Vlož verziu A a verziu B — uvidíš zmeny riadok po riadku s červeno-zeleným zvýraznením. Užitočné pre prompt engineerov porovnávajúcich iterácie, A/B testujúcich prompty alebo audit toho, čo sa zmenilo v system prompte medzi deploymentmi. Štandardný LCS diff algoritmus.",
        },
        "cs": {
            "name": "Prompt Diff",
            "tagline": "Porovnej dva prompty (nebo dvě verze téhož promptu) vedle sebe. Řádkový diff se zvýrazněnými změnami. Navržené pro iteraci LLM promptů.",
            "description": "Bezplatný in-browser prompt diff nástroj. Vlož verzi A a verzi B — uvidíš změny řádek po řádku s červeno-zeleným zvýrazněním. Užitečné pro prompt engineery porovnávající iterace, A/B testující prompty nebo audit toho, co se změnilo v system promptu mezi deploymenty. Standardní LCS diff algoritmus.",
        },
    },
    "body": """
<div class="pd-grid">
  <div class="tool-card">
    <label>Version A</label>
    <textarea id="pd-a" oninput="pdRun()" spellcheck="false" placeholder="You are a helpful assistant. Answer concisely.">You are a helpful assistant.
Answer the user concisely.
Use markdown for code.
Cite sources when possible.</textarea>
  </div>
  <div class="tool-card">
    <label>Version B</label>
    <textarea id="pd-b" oninput="pdRun()" spellcheck="false" placeholder="You are a helpful assistant. Answer concisely.">You are a helpful, careful assistant.
Answer the user concisely.
Use markdown for code blocks.
Cite sources when possible.
Refuse if the request is harmful.</textarea>
  </div>
</div>
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>View</label>
      <select id="pd-view" onchange="pdRun()">
        <option value="split">Side-by-side</option>
        <option value="unified">Unified</option>
      </select>
    </div>
    <div style="display:flex;flex-direction:column;gap:0.4rem;font-size:0.9rem;justify-content:end">
      <label><input type="checkbox" id="pd-ws" onchange="pdRun()"> Ignore trailing whitespace</label>
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="pd-out" class="pd-result"></div>
  <div class="meta" id="pd-stats" style="margin-top:0.5rem"></div>
</div>
""",
    "script": """
<style>
.pd-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.pd-grid textarea{min-height:200px;font-family:ui-monospace,monospace;font-size:0.88rem}
.pd-result{font-family:ui-monospace,monospace;font-size:0.86rem;background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;overflow:auto;max-height:600px}
.pd-line{display:grid;grid-template-columns:50px 1fr;gap:0;align-items:start;border-bottom:1px solid var(--border)}
.pd-line:last-child{border-bottom:none}
.pd-line .gut{padding:0.2rem 0.5rem;color:var(--text-muted);font-size:0.78rem;text-align:right;background:var(--bg);user-select:none;font-variant-numeric:tabular-nums}
.pd-line .body{padding:0.2rem 0.6rem;white-space:pre-wrap;word-break:break-word}
.pd-add{background:rgba(16,185,129,0.12)}
.pd-add .body{color:#10b981}
.pd-add .body::before{content:'+ '}
.pd-del{background:rgba(239,68,68,0.12)}
.pd-del .body{color:#ef4444}
.pd-del .body::before{content:'− '}
.pd-eq .body::before{content:'  '}
.pd-split{display:grid;grid-template-columns:1fr 1fr}
.pd-split>div{overflow:auto;border-right:1px solid var(--border)}
.pd-split>div:last-child{border-right:none}
@media(max-width:760px){.pd-grid{grid-template-columns:1fr}.pd-split{grid-template-columns:1fr}.pd-split>div:not(:last-child){border-right:none;border-bottom:1px solid var(--border)}}
</style>
<script>
function pdEsc(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;') || '&nbsp;'}
function pdLcs(a, b){
  const m = a.length, n = b.length;
  const dp = Array.from({length:m+1}, () => new Uint32Array(n+1));
  for(let i = m - 1; i >= 0; i--){
    for(let j = n - 1; j >= 0; j--){
      dp[i][j] = a[i] === b[j] ? dp[i+1][j+1] + 1 : Math.max(dp[i+1][j], dp[i][j+1]);
    }
  }
  const ops = [];
  let i = 0, j = 0;
  while(i < m && j < n){
    if(a[i] === b[j]){ ops.push(['eq', i, j]); i++; j++; }
    else if(dp[i+1][j] >= dp[i][j+1]){ ops.push(['del', i, null]); i++; }
    else { ops.push(['add', null, j]); j++; }
  }
  while(i < m){ ops.push(['del', i, null]); i++; }
  while(j < n){ ops.push(['add', null, j]); j++; }
  return ops;
}
function pdRun(){
  const rawA = document.getElementById('pd-a').value;
  const rawB = document.getElementById('pd-b').value;
  const view = document.getElementById('pd-view').value;
  const wsTrim = document.getElementById('pd-ws').checked;
  const norm = s => wsTrim ? s.replace(/\\s+$/, '') : s;
  const linesA = rawA.split('\\n');
  const linesB = rawB.split('\\n');
  const cmpA = linesA.map(norm);
  const cmpB = linesB.map(norm);
  const ops = pdLcs(cmpA, cmpB);
  let adds = 0, dels = 0, eqs = 0;
  ops.forEach(o => { if(o[0] === 'add') adds++; else if(o[0] === 'del') dels++; else eqs++; });
  const out = document.getElementById('pd-out');
  if(view === 'unified'){
    const rows = ops.map(o => {
      if(o[0] === 'eq')  return `<div class="pd-line pd-eq"><div class="gut">${o[1]+1}</div><div class="body">${pdEsc(linesA[o[1]])}</div></div>`;
      if(o[0] === 'del') return `<div class="pd-line pd-del"><div class="gut">${o[1]+1}</div><div class="body">${pdEsc(linesA[o[1]])}</div></div>`;
      return `<div class="pd-line pd-add"><div class="gut">${o[2]+1}</div><div class="body">${pdEsc(linesB[o[2]])}</div></div>`;
    });
    out.innerHTML = rows.join('');
  } else {
    const left = [], right = [];
    let k = 0;
    while(k < ops.length){
      if(ops[k][0] === 'eq'){
        left.push(`<div class="pd-line pd-eq"><div class="gut">${ops[k][1]+1}</div><div class="body">${pdEsc(linesA[ops[k][1]])}</div></div>`);
        right.push(`<div class="pd-line pd-eq"><div class="gut">${ops[k][2]+1}</div><div class="body">${pdEsc(linesB[ops[k][2]])}</div></div>`);
        k++;
      } else {
        const ds = [], as = [];
        while(k < ops.length && ops[k][0] === 'del'){ ds.push(ops[k]); k++; }
        while(k < ops.length && ops[k][0] === 'add'){ as.push(ops[k]); k++; }
        const max = Math.max(ds.length, as.length);
        for(let x = 0; x < max; x++){
          if(ds[x]) left.push(`<div class="pd-line pd-del"><div class="gut">${ds[x][1]+1}</div><div class="body">${pdEsc(linesA[ds[x][1]])}</div></div>`);
          else      left.push(`<div class="pd-line pd-eq"><div class="gut"></div><div class="body"></div></div>`);
          if(as[x]) right.push(`<div class="pd-line pd-add"><div class="gut">${as[x][2]+1}</div><div class="body">${pdEsc(linesB[as[x][2]])}</div></div>`);
          else      right.push(`<div class="pd-line pd-eq"><div class="gut"></div><div class="body"></div></div>`);
        }
      }
    }
    out.innerHTML = `<div class="pd-split"><div>${left.join('')}</div><div>${right.join('')}</div></div>`;
  }
  document.getElementById('pd-stats').textContent =
    `+${adds} added · −${dels} removed · ${eqs} unchanged · ${linesA.length} → ${linesB.length} lines`;
}
document.addEventListener('DOMContentLoaded', pdRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Prompt engineering is iteration: you write a prompt, test it, tweak one phrase, test again. After a dozen rounds, you've got a "version 1" and a "version 14" and no clean record of what changed where. This tool gives you that record on demand — paste any two prompts and see exactly which lines were added, removed, or left alone. No git, no setup, no upload.</p>

<h3>When to use it</h3>
<ul>
  <li><strong>Auditing a deployed change.</strong> Marketing tweaked the system prompt last week — what exactly is different? Paste both versions and read the diff.</li>
  <li><strong>A/B testing prompts.</strong> Two candidate prompts, one runs better on evals. Diff them to isolate what the difference might be doing.</li>
  <li><strong>Reverting a regression.</strong> The latest prompt is worse than two iterations ago — which line did you change?</li>
  <li><strong>Reviewing a teammate's edit.</strong> They sent you a "small tweak" to the system prompt — did they only touch the part they said they did?</li>
  <li><strong>Migrating between model families.</strong> Adapting a prompt from GPT to Claude often means small wording changes — diff after rewriting to confirm the structure stayed the same.</li>
</ul>

<h3>Side-by-side vs unified</h3>
<ul>
  <li><strong>Side-by-side</strong> — A on the left, B on the right. Good when both versions are similar length and you want to scan visually.</li>
  <li><strong>Unified</strong> — single column with + / − markers, mirroring <code>git diff</code> output. Better for sharing the diff in a Slack message or for sparse changes.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>This is a line-level diff.</strong> A single word changed in the middle of a long line marks the whole line as added+removed. For prose-level diff of a sentence, you may prefer a word-level tool.</li>
  <li><strong>Trailing whitespace.</strong> Hidden spaces at the end of a line will mark it as different — useful or noisy depending on the case. Use the "Ignore trailing whitespace" toggle if you only care about visible content.</li>
  <li><strong>Reordered blocks look like delete+add.</strong> If you moved a paragraph from position 1 to position 3, the diff shows it as removed at position 1 and added at position 3. There's no "moved" detection.</li>
  <li><strong>Lines, not tokens.</strong> This diff doesn't speak token; it speaks lines. If your two prompts have the same content rewrapped to different line lengths, every line will look different. Normalise line breaks first.</li>
  <li><strong>Privacy.</strong> Everything stays in your tab. Don't paste secrets into the tool's example placeholder, mind you — the placeholder text is hard-coded, not connected to your input.</li>
</ul>
""",
        "de": """
<h2>Wozu ist das gut?</h2>
<p>Prompt-Engineering ist Iteration: einen Prompt schreiben, testen, eine Formulierung anpassen, wieder testen. Nach einem Dutzend Runden hast du eine „Version 1" und eine „Version 14" und keine saubere Aufzeichnung, was sich wo geändert hat. Dieses Tool gibt dir diese Aufzeichnung auf Knopfdruck — füge zwei Prompts ein und sieh genau, welche Zeilen hinzugefügt, entfernt oder gleich geblieben sind. Kein Git, kein Setup, kein Upload.</p>

<h3>Wann nützlich</h3>
<ul>
  <li><strong>Audit einer Deployment-Änderung.</strong> Marketing hat den System-Prompt letzte Woche angepasst — was genau ist anders? Beide Versionen einfügen, Diff lesen.</li>
  <li><strong>A/B-Test von Prompts.</strong> Zwei Kandidaten, einer schneidet besser ab. Diff, um den entscheidenden Unterschied einzukreisen.</li>
  <li><strong>Regression rückgängig machen.</strong> Der neueste Prompt ist schlechter als der von vor zwei Iterationen — welche Zeile war's?</li>
  <li><strong>Edit eines Kollegen reviewen.</strong> „Kleine Anpassung" am System-Prompt — hat er wirklich nur das angefasst, was er sagt?</li>
  <li><strong>Wechsel zwischen Modell-Familien.</strong> Ein Prompt von GPT zu Claude zu portieren bedeutet meist kleine Wortänderungen — danach diffen, um zu prüfen, dass die Struktur erhalten blieb.</li>
</ul>

<h3>Side-by-side vs Unified</h3>
<ul>
  <li><strong>Side-by-side</strong> — A links, B rechts. Gut, wenn beide Versionen ähnlich lang sind und du visuell vergleichen willst.</li>
  <li><strong>Unified</strong> — eine Spalte mit + / − Markern, wie <code>git diff</code>. Besser zum Teilen in Slack oder bei wenigen Änderungen.</li>
</ul>

<h3>Typische Stolperfallen</h3>
<ul>
  <li><strong>Zeilen-Diff, kein Wort-Diff.</strong> Ein Wort mitten in einer langen Zeile geändert markiert die ganze Zeile als entfernt+hinzugefügt. Für Satz-Ebene besser ein Wort-Diff-Tool.</li>
  <li><strong>Trailing Whitespace.</strong> Versteckte Leerzeichen am Zeilenende markieren die Zeile als unterschiedlich — manchmal nützlich, manchmal Rauschen. „Trailing Whitespace ignorieren" einschalten, wenn nur sichtbarer Inhalt zählt.</li>
  <li><strong>Verschobene Blöcke sehen aus wie Delete+Add.</strong> Ein Absatz von Position 1 nach 3 verschoben zeigt sich als Remove bei 1 und Add bei 3. Keine „Moved"-Erkennung.</li>
  <li><strong>Zeilen, keine Tokens.</strong> Der Diff spricht Zeilen. Wenn beide Prompts denselben Inhalt anders umbrochen haben, sieht jede Zeile anders aus. Vorher Zeilenumbrüche normalisieren.</li>
  <li><strong>Privacy.</strong> Alles bleibt im Tab. Keine Geheimnisse in den Placeholder einfügen — der ist hartkodiert.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>El prompt engineering es iteración: escribes un prompt, lo pruebas, ajustas una frase, vuelves a probar. Después de una docena de rondas tienes una "versión 1" y una "versión 14" y ningún registro limpio de qué cambió y dónde. Esta herramienta te da ese registro a demanda — pega dos prompts y mira exactamente qué líneas se añadieron, eliminaron o quedaron iguales. Sin git, sin setup, sin subida.</p>

<h3>Cuándo usarla</h3>
<ul>
  <li><strong>Auditar un cambio desplegado.</strong> Marketing ajustó el system prompt la semana pasada — ¿qué cambió exactamente? Pega ambas versiones y lee el diff.</li>
  <li><strong>A/B testing de prompts.</strong> Dos candidatos, uno da mejor en las evals. Diff para aislar qué podría estar marcando la diferencia.</li>
  <li><strong>Revertir una regresión.</strong> El último prompt es peor que el de hace dos iteraciones — ¿qué línea cambiaste?</li>
  <li><strong>Revisar la edición de un compañero.</strong> Te mandó "un retoque pequeño" al system prompt — ¿solo tocó lo que dijo?</li>
  <li><strong>Migrar entre familias de modelos.</strong> Adaptar un prompt de GPT a Claude suele ser cambios de redacción menores — haz diff después de reescribir para confirmar que la estructura quedó igual.</li>
</ul>

<h3>Lado a lado vs unificado</h3>
<ul>
  <li><strong>Lado a lado</strong> — A a la izquierda, B a la derecha. Bueno si las dos versiones tienen longitud similar y quieres escanear visualmente.</li>
  <li><strong>Unificado</strong> — una sola columna con marcadores + / −, como <code>git diff</code>. Mejor para compartir en Slack o cuando los cambios son escasos.</li>
</ul>

<h3>Errores comunes</h3>
<ul>
  <li><strong>Es diff a nivel de línea.</strong> Una sola palabra cambiada en medio de una línea larga marca toda la línea como añadida+eliminada. Para diff de frase, mejor una herramienta a nivel de palabra.</li>
  <li><strong>Espacios al final.</strong> Espacios ocultos al final de la línea la marcan como diferente — útil o ruido según el caso. Activa "Ignorar espacios finales" si solo importa el contenido visible.</li>
  <li><strong>Bloques reordenados se ven como borrar+añadir.</strong> Si moviste un párrafo de la posición 1 a la 3, el diff lo muestra como eliminado en 1 y añadido en 3. No hay detección de "movido".</li>
  <li><strong>Líneas, no tokens.</strong> El diff habla líneas, no tokens. Si ambos prompts tienen el mismo contenido con saltos de línea distintos, todas las líneas saldrán diferentes. Normaliza saltos de línea primero.</li>
  <li><strong>Privacidad.</strong> Todo se queda en tu pestaña. No pegues secretos en el placeholder de ejemplo — está hardcodeado, no conectado a tu input.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Le prompt engineering, c'est de l'itération : on écrit un prompt, on le teste, on ajuste une formulation, on retéste. Après une douzaine de tours, vous avez une « version 1 » et une « version 14 » et aucun enregistrement propre de ce qui a changé où. Cet outil vous donne cet enregistrement à la demande — collez deux prompts et voyez exactement quelles lignes ont été ajoutées, supprimées ou laissées intactes. Pas de git, pas de setup, pas d'upload.</p>

<h3>Quand l'utiliser</h3>
<ul>
  <li><strong>Auditer un changement déployé.</strong> Le marketing a ajusté le system prompt la semaine dernière — qu'est-ce qui a changé exactement ? Collez les deux versions et lisez le diff.</li>
  <li><strong>A/B testing de prompts.</strong> Deux candidats, un fait mieux sur les évals. Diff pour isoler ce qui pourrait faire la différence.</li>
  <li><strong>Annuler une régression.</strong> Le dernier prompt est pire que celui d'il y a deux itérations — quelle ligne avez-vous changée ?</li>
  <li><strong>Reviewer l'édition d'un collègue.</strong> Il vous a envoyé un « petit ajustement » du system prompt — n'a-t-il touché que ce qu'il a dit ?</li>
  <li><strong>Migrer entre familles de modèles.</strong> Adapter un prompt de GPT à Claude implique souvent des changements de formulation mineurs — diff après réécriture pour confirmer que la structure est restée.</li>
</ul>

<h3>Côte à côte vs unifié</h3>
<ul>
  <li><strong>Côte à côte</strong> — A à gauche, B à droite. Bon quand les deux versions ont une longueur similaire et que vous voulez scanner visuellement.</li>
  <li><strong>Unifié</strong> — une seule colonne avec des marqueurs + / −, comme la sortie de <code>git diff</code>. Mieux pour partager dans un Slack ou quand les changements sont rares.</li>
</ul>

<h3>Pièges courants</h3>
<ul>
  <li><strong>C'est un diff au niveau ligne.</strong> Un seul mot changé au milieu d'une longue ligne marque toute la ligne comme ajoutée+supprimée. Pour du diff de phrase, mieux vaut un outil au niveau mot.</li>
  <li><strong>Espaces de fin.</strong> Des espaces cachés en fin de ligne la marquent comme différente — utile ou bruit selon le cas. Activez « Ignorer les espaces de fin » si seul le contenu visible compte.</li>
  <li><strong>Blocs réordonnés ressemblent à suppression+ajout.</strong> Si vous avez déplacé un paragraphe de la position 1 à la 3, le diff le montre supprimé en 1 et ajouté en 3. Pas de détection « déplacé ».</li>
  <li><strong>Lignes, pas tokens.</strong> Le diff parle lignes. Si vos deux prompts ont le même contenu mais rebreaké différemment, chaque ligne paraîtra différente. Normalisez les retours à la ligne d'abord.</li>
  <li><strong>Confidentialité.</strong> Tout reste dans votre onglet. Ne collez pas de secrets dans le placeholder d'exemple — il est en dur, pas connecté à votre entrée.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Il prompt engineering è iterazione: scrivi un prompt, lo testi, modifichi una frase, ritesti. Dopo una decina di giri hai una "versione 1" e una "versione 14" e nessun registro pulito di cosa è cambiato dove. Questo strumento ti dà quel registro a richiesta — incolla due prompt e vedi esattamente quali righe sono state aggiunte, rimosse o lasciate uguali. Niente git, niente setup, niente upload.</p>

<h3>Quando usarlo</h3>
<ul>
  <li><strong>Audit di un cambio in produzione.</strong> Marketing ha ritoccato il system prompt la settimana scorsa — cosa è cambiato esattamente? Incolla entrambe e leggi il diff.</li>
  <li><strong>A/B test di prompt.</strong> Due candidati, uno fa meglio sulle eval. Diff per isolare cosa potrebbe star facendo la differenza.</li>
  <li><strong>Rollback di una regressione.</strong> L'ultimo prompt è peggiore di due iterazioni fa — quale riga hai cambiato?</li>
  <li><strong>Review dell'edit di un collega.</strong> Ti ha mandato "una piccola modifica" al system prompt — ha toccato solo quello che ha detto?</li>
  <li><strong>Migrazione tra famiglie di modelli.</strong> Adattare un prompt da GPT a Claude di solito significa cambi di parole minori — diff dopo la riscrittura per confermare che la struttura sia rimasta.</li>
</ul>

<h3>Affiancato vs unificato</h3>
<ul>
  <li><strong>Affiancato</strong> — A a sinistra, B a destra. Buono quando le due versioni hanno lunghezze simili e vuoi scansionare visivamente.</li>
  <li><strong>Unificato</strong> — singola colonna con marcatori + / −, come l'output di <code>git diff</code>. Migliore per condividere su Slack o quando i cambi sono pochi.</li>
</ul>

<h3>Trappole comuni</h3>
<ul>
  <li><strong>È un diff a livello riga.</strong> Una sola parola cambiata in mezzo a una riga lunga marca tutta la riga come aggiunta+rimossa. Per diff a livello frase, meglio uno strumento a livello parola.</li>
  <li><strong>Whitespace finale.</strong> Spazi nascosti a fine riga la marcano come diversa — utile o rumore a seconda. Attiva "Ignora whitespace finale" se conta solo il contenuto visibile.</li>
  <li><strong>Blocchi riordinati sembrano cancella+aggiungi.</strong> Se hai spostato un paragrafo da posizione 1 a 3, il diff lo mostra rimosso a 1 e aggiunto a 3. Nessuna rilevazione "spostato".</li>
  <li><strong>Righe, non token.</strong> Il diff parla righe. Se entrambi i prompt hanno lo stesso contenuto a-capo diversi, ogni riga sembrerà diversa. Normalizza prima i ritorni a capo.</li>
  <li><strong>Privacy.</strong> Tutto resta nella tua tab. Non incollare segreti nel placeholder di esempio — è hardcoded, non connesso al tuo input.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Prompt engineering é iteração: você escreve um prompt, testa, ajusta uma frase, testa de novo. Depois de uma dúzia de rodadas, você tem uma "versão 1" e uma "versão 14" e nenhum registro limpo do que mudou onde. Esta ferramenta te dá esse registro sob demanda — cole dois prompts e veja exatamente quais linhas foram adicionadas, removidas ou ficaram iguais. Sem git, sem setup, sem upload.</p>

<h3>Quando usar</h3>
<ul>
  <li><strong>Auditar uma mudança em produção.</strong> Marketing ajustou o system prompt na semana passada — o que mudou exatamente? Cole as duas versões e leia o diff.</li>
  <li><strong>A/B test de prompts.</strong> Dois candidatos, um vai melhor nas evals. Diff pra isolar o que pode estar fazendo a diferença.</li>
  <li><strong>Reverter uma regressão.</strong> O prompt mais recente é pior que o de duas iterações atrás — qual linha você mudou?</li>
  <li><strong>Revisar o edit de um colega.</strong> Te mandou um "ajustinho" no system prompt — ele mexeu só onde disse que ia mexer?</li>
  <li><strong>Migrar entre famílias de modelos.</strong> Adaptar um prompt do GPT pro Claude geralmente envolve mudanças pequenas de palavra — diff depois pra confirmar que a estrutura ficou.</li>
</ul>

<h3>Lado a lado vs unificado</h3>
<ul>
  <li><strong>Lado a lado</strong> — A à esquerda, B à direita. Bom quando as duas versões têm tamanho parecido e você quer escanear visualmente.</li>
  <li><strong>Unificado</strong> — coluna única com marcadores + / −, espelhando saída do <code>git diff</code>. Melhor pra compartilhar no Slack ou quando as mudanças são esparsas.</li>
</ul>

<h3>Pegadinhas comuns</h3>
<ul>
  <li><strong>É diff em nível de linha.</strong> Uma palavra trocada no meio de uma linha longa marca a linha inteira como adicionada+removida. Pra diff em nível de frase, melhor uma ferramenta de nível de palavra.</li>
  <li><strong>Whitespace no final.</strong> Espaços escondidos no fim da linha marcam ela como diferente — útil ou ruído conforme o caso. Liga "Ignorar whitespace final" se só importa o conteúdo visível.</li>
  <li><strong>Blocos reordenados parecem deletar+adicionar.</strong> Se moveu um parágrafo da posição 1 pra 3, o diff mostra removido em 1 e adicionado em 3. Não tem detecção de "movido".</li>
  <li><strong>Linhas, não tokens.</strong> O diff fala linhas. Se seus dois prompts têm o mesmo conteúdo com quebras diferentes, toda linha sai diferente. Normaliza quebras antes.</li>
  <li><strong>Privacidade.</strong> Tudo fica na sua aba. Não cole segredos no placeholder de exemplo — ele é hardcoded, não tá conectado ao seu input.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Prompt engineering to iteracja: piszesz prompt, testujesz, poprawiasz frazę, testujesz znowu. Po tuzinie rundek masz „wersję 1" i „wersję 14" i żadnego czystego zapisu, co się gdzie zmieniło. To narzędzie daje ci taki zapis na żądanie — wklej dwa prompty i zobacz dokładnie, które linie zostały dodane, usunięte albo zostawione w spokoju. Bez gita, bez setupu, bez uploadu.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li><strong>Audyt wdrożonej zmiany.</strong> Marketing podrasował system prompt w zeszłym tygodniu — co dokładnie się zmieniło? Wklej obie wersje, przeczytaj diff.</li>
  <li><strong>A/B testowanie promptów.</strong> Dwóch kandydatów, jeden bije na evalach. Diff, żeby wyizolować, co może robić różnicę.</li>
  <li><strong>Cofnięcie regresji.</strong> Najnowszy prompt jest gorszy od tego sprzed dwóch iteracji — którą linię zmieniłeś?</li>
  <li><strong>Review edycji kolegi.</strong> Wysłał ci „małą poprawkę" system promptu — czy ruszył tylko to, co powiedział?</li>
  <li><strong>Migracja między rodzinami modeli.</strong> Adaptacja promptu z GPT na Claude'a to zwykle drobne zmiany sformułowań — diff po przepisaniu, żeby potwierdzić, że struktura została.</li>
</ul>

<h3>Side-by-side vs unified</h3>
<ul>
  <li><strong>Side-by-side</strong> — A po lewej, B po prawej. Dobre, gdy obie wersje są podobnej długości i chcesz skanować wzrokowo.</li>
  <li><strong>Unified</strong> — jedna kolumna z markerami + / −, jak wyjście <code>git diff</code>. Lepsze do dzielenia się na Slacku albo przy rzadkich zmianach.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>To diff na poziomie linii.</strong> Jedno słowo zmienione w środku długiej linii oznacza całą linię jako dodaną+usuniętą. Do diffu na poziomie zdania lepsze narzędzie na poziomie słów.</li>
  <li><strong>Trailing whitespace.</strong> Ukryte spacje na końcu linii oznaczają ją jako różną — bywa przydatne, bywa szum. Włącz „Ignoruj trailing whitespace", jeśli liczy się tylko widoczna treść.</li>
  <li><strong>Przeniesione bloki wyglądają jak delete+add.</strong> Jeśli przeniosłeś akapit z pozycji 1 na 3, diff pokazuje usunięcie na 1 i dodanie na 3. Brak detekcji „moved".</li>
  <li><strong>Linie, nie tokeny.</strong> Diff mówi liniami. Jeśli dwa prompty mają tę samą treść inaczej przełamaną, każda linia będzie wyglądała inaczej. Najpierw znormalizuj łamania.</li>
  <li><strong>Prywatność.</strong> Wszystko zostaje w twojej karcie. Nie wklejaj sekretów w przykładowy placeholder — jest zahardkodowany, nie podpięty pod twój input.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>プロンプトエンジニアリングは反復作業です。書いて、試して、一文を調整して、また試す。十数回繰り返した頃には「バージョン 1」と「バージョン 14」が手元にあるのに、どこをどう変えたかの整理された記録はどこにもない、ということがよくあります。本ツールは必要なときにその記録を作ります。2 つのプロンプトを貼り付ければ、どの行が追加・削除・据え置きになったかが正確に見えます。Git も設定もアップロードも不要です。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li><strong>本番投入された変更の監査。</strong> 先週マーケが system prompt を調整した、具体的に何が変わった？ 両バージョンを貼って差分を読む。</li>
  <li><strong>プロンプトの A/B テスト。</strong> 候補が 2 つ、片方が eval で有利。何が差を生んでいる可能性が高いか、差分で切り分け。</li>
  <li><strong>リグレッション復元。</strong> 最新プロンプトが 2 反復前より劣化、どの行を変えた？</li>
  <li><strong>チームメイトの編集レビュー。</strong> 「ちょっと触っただけ」と言われた system prompt、本当にそこしか触っていない？</li>
  <li><strong>モデル系列間の移植。</strong> GPT 用プロンプトを Claude に移すと文言が細かく変わりがち。書き直しの後に diff を取って構造が保たれているか確認。</li>
</ul>

<h3>並列表示と統合表示</h3>
<ul>
  <li><strong>並列表示</strong> — 左に A、右に B。両バージョンが似た長さで視覚的に追いたいときに有効。</li>
  <li><strong>統合表示</strong> — 単一列に + / − マーカー。<code>git diff</code> のような表現で、Slack 共有や差分が少ない場面に向きます。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>これは行単位差分です。</strong> 長い行の中の単語 1 つを変えると、その行全体が削除＋追加として表示されます。文単位で見たい場合は語単位の差分ツールを使ってください。</li>
  <li><strong>末尾の空白。</strong> 行末の見えないスペースは差分として扱われます。場面によって有用にもノイズにもなるので、「末尾空白を無視」をオン／オフして使い分けます。</li>
  <li><strong>並べ替えは「削除＋追加」に見えます。</strong> 段落を位置 1 から位置 3 に移動すると、位置 1 に「削除」、位置 3 に「追加」が出ます。「移動」検出はありません。</li>
  <li><strong>トークンではなく行を扱います。</strong> 改行位置だけ違って中身は同じ 2 つのプロンプトは、全行違うように見えます。事前に改行を整えてください。</li>
  <li><strong>プライバシー。</strong> 入力はタブ内で完結します。プレースホルダー文はハードコードされており、入力とは連動しません。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Prompt engineering is iteratie: je schrijft een prompt, test 'm, tweakt één zin, test opnieuw. Na een dozijn ronden heb je een "versie 1" en een "versie 14" en geen schoon overzicht van wat er waar veranderd is. Deze tool geeft je dat overzicht op aanvraag — plak twee prompts en zie precies welke regels zijn toegevoegd, verwijderd of onaangetast bleven. Geen git, geen setup, geen upload.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li><strong>Auditen van een deployed change.</strong> Marketing heeft het system prompt vorige week getweaked — wat is er precies anders? Plak beide versies en lees de diff.</li>
  <li><strong>A/B testing van prompts.</strong> Twee kandidaten, eentje doet het beter op evals. Diff om te isoleren wat het verschil zou kunnen maken.</li>
  <li><strong>Terugdraaien van een regressie.</strong> De nieuwste prompt is slechter dan die van twee iteraties geleden — welke regel heb je veranderd?</li>
  <li><strong>Reviewen van een teamgenoot's edit.</strong> Ze stuurden je een "kleine tweak" van het system prompt — hebben ze alleen wat ze zeiden aangepast?</li>
  <li><strong>Migreren tussen modelfamilies.</strong> Een prompt van GPT naar Claude aanpassen betekent vaak kleine woordwijzigingen — diff na herschrijven om te bevestigen dat de structuur intact bleef.</li>
</ul>

<h3>Side-by-side vs unified</h3>
<ul>
  <li><strong>Side-by-side</strong> — A links, B rechts. Goed als beide versies vergelijkbare lengte hebben en je visueel wilt scannen.</li>
  <li><strong>Unified</strong> — enkele kolom met + / − markers, zoals <code>git diff</code>-output. Beter voor delen in een Slack-bericht of bij sparse changes.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Dit is een line-level diff.</strong> Eén woord veranderd midden in een lange regel markeert de hele regel als toegevoegd+verwijderd. Voor prose-level diff van een zin wil je misschien een word-level tool.</li>
  <li><strong>Trailing whitespace.</strong> Verborgen spaties aan het eind van een regel markeren 'm als anders — handig of ruizig afhankelijk van het geval. Gebruik de "Ignore trailing whitespace"-toggle als alleen zichtbare content telt.</li>
  <li><strong>Herordende blokken zien eruit als delete+add.</strong> Als je een paragraaf van positie 1 naar 3 verplaatste, toont de diff 'm verwijderd op 1 en toegevoegd op 3. Geen "moved" detectie.</li>
  <li><strong>Regels, geen tokens.</strong> Deze diff spreekt geen token; hij spreekt regels. Als je twee prompts dezelfde content hebben, maar anders gewrapped, lijkt elke regel anders. Normaliseer line breaks eerst.</li>
  <li><strong>Privacy.</strong> Alles blijft in je tab. Plak geen geheimen in de voorbeeld-placeholder van de tool — de placeholder-tekst is hardcoded, niet verbonden met je input.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Prompt mühendisliği yinelemedir: prompt yazarsın, test edersin, bir ifadeyi değiştirirsin, tekrar test edersin. Bir düzine turdan sonra elinde "sürüm 1" ve "sürüm 14" var, ama nerede ne değiştiğine dair temiz bir kayıt yok. Bu araç o kaydı isteğe bağlı verir — herhangi iki prompt'u yapıştır ve hangi satırların eklendiğini, kaldırıldığını veya dokunulmadan kaldığını tam olarak gör. Git yok, kurulum yok, upload yok.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li><strong>Bir deployment değişikliğini denetleme.</strong> Pazarlama geçen hafta system prompt'u ince ayarlamış — tam olarak ne farklı? İki sürümü de yapıştır ve diff'i oku.</li>
  <li><strong>Prompt A/B testi.</strong> İki aday, biri eval'de daha iyi. Farkı izole etmek için diff.</li>
  <li><strong>Regresyonu geri alma.</strong> En son prompt iki iterasyon öncekinden daha kötü — hangi satırı değiştirdin?</li>
  <li><strong>Bir takım arkadaşının edit'ini inceleme.</strong> "Küçük bir ayarlama" gönderdi system prompt'a — sadece söylediği yere mi dokundu?</li>
  <li><strong>Model aileleri arasında geçiş.</strong> Bir prompt'u GPT'den Claude'a uyarlamak genelde küçük kelime değişiklikleri demek — yeniden yazımdan sonra yapının korunduğunu doğrulamak için diff.</li>
</ul>

<h3>Yan yana vs birleşik</h3>
<ul>
  <li><strong>Yan yana</strong> — A solda, B sağda. İki sürüm benzer uzunlukta olduğunda ve görsel taramak istediğinde iyi.</li>
  <li><strong>Birleşik</strong> — + / − işaretçileriyle tek sütun, <code>git diff</code> çıktısını yansıtır. Slack mesajında paylaşmak veya seyrek değişiklikler için daha iyi.</li>
</ul>

<h3>Yaygın tuzaklar</h3>
<ul>
  <li><strong>Bu satır seviyesi bir diff.</strong> Uzun bir satırın ortasında değişen tek kelime tüm satırı ekleme+kaldırma olarak işaretler. Cümle seviyesi diff için kelime seviyesinde bir araç tercih edebilirsin.</li>
  <li><strong>Sondaki boşluk.</strong> Bir satırın sonundaki gizli boşluklar onu farklı olarak işaretler — duruma göre yararlı veya gürültü. Yalnızca görünür içerikle ilgileniyorsan "Sondaki boşluğu yok say" anahtarını kullan.</li>
  <li><strong>Yeniden sıralanmış bloklar silme+ekleme gibi görünür.</strong> Bir paragrafı 1. konumdan 3.'ye taşıdıysan, diff onu 1'de kaldırıldı ve 3'te eklendi olarak gösterir. "Taşındı" tespiti yok.</li>
  <li><strong>Satırlar, token'lar değil.</strong> Bu diff token konuşmaz; satır konuşur. İki prompt'un aynı içeriği farklı satır uzunluklarına sarılı haldeyse, her satır farklı görünür. Önce satır sonlarını normalize et.</li>
  <li><strong>Gizlilik.</strong> Her şey sekmeinde kalır. Aracın örnek yer tutucusuna sırlar yapıştırma — yer tutucu metni sabit kodlanmış, girişine bağlı değil.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Prompt engineering itu iterasi: kamu tulis prompt, tes, ubah satu frasa, tes lagi. Setelah selusin putaran, kamu punya "versi 1" dan "versi 14" tanpa catatan bersih tentang apa yang berubah di mana. Tool ini memberi catatan itu sesuai permintaan — tempel dua prompt apa pun dan lihat persis baris mana yang ditambah, dihapus, atau dibiarkan. Tanpa git, tanpa setup, tanpa upload.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li><strong>Mengaudit perubahan yang sudah ter-deploy.</strong> Marketing tweak system prompt minggu lalu — apa persisnya yang berbeda? Tempel kedua versi dan baca diff-nya.</li>
  <li><strong>A/B testing prompt.</strong> Dua kandidat, satu lebih baik di eval. Diff untuk mengisolasi apa yang mungkin membuat perbedaan.</li>
  <li><strong>Membalikkan regresi.</strong> Prompt terbaru lebih buruk dari dua iterasi lalu — baris mana yang kamu ubah?</li>
  <li><strong>Mereview edit teman tim.</strong> Mereka kirim "tweak kecil" ke system prompt — apa mereka hanya menyentuh apa yang dikatakan?</li>
  <li><strong>Migrasi antar keluarga model.</strong> Mengadaptasi prompt dari GPT ke Claude biasanya berarti perubahan kata kecil — diff setelah menulis ulang untuk konfirmasi struktur tetap sama.</li>
</ul>

<h3>Side-by-side vs unified</h3>
<ul>
  <li><strong>Side-by-side</strong> — A di kiri, B di kanan. Bagus saat kedua versi panjangnya mirip dan kamu ingin scan visual.</li>
  <li><strong>Unified</strong> — kolom tunggal dengan marker + / −, mencerminkan output <code>git diff</code>. Lebih baik untuk berbagi di Slack atau saat perubahan jarang.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Ini diff level baris.</strong> Satu kata berubah di tengah baris panjang menandai seluruh baris sebagai ditambah+dihapus. Untuk diff level kalimat, kamu mungkin lebih suka tool level kata.</li>
  <li><strong>Whitespace di akhir.</strong> Spasi tersembunyi di akhir baris menandainya sebagai berbeda — berguna atau noise tergantung kasus. Pakai toggle "Abaikan whitespace akhir" jika hanya peduli konten terlihat.</li>
  <li><strong>Blok yang diurutkan ulang terlihat seperti hapus+tambah.</strong> Kalau kamu memindahkan paragraf dari posisi 1 ke 3, diff menunjukkannya dihapus di 1 dan ditambah di 3. Tidak ada deteksi "dipindahkan".</li>
  <li><strong>Baris, bukan token.</strong> Diff ini bicara baris, bukan token. Kalau dua prompt-mu punya konten sama dengan line-break beda, tiap baris akan terlihat beda. Normalisasi line-break dulu.</li>
  <li><strong>Privasi.</strong> Semuanya tetap di tab-mu. Jangan tempel rahasia ke placeholder contoh tool — teks placeholder hardcoded, tidak terhubung ke input-mu.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Prompt engineering là việc lặp đi lặp lại: bạn viết prompt, test, chỉnh một câu, test lại. Sau cả chục vòng, bạn có "phiên bản 1" và "phiên bản 14" và không có ghi chép sạch sẽ nào về cái gì đã thay đổi ở đâu. Công cụ này cho bạn ghi chép đó theo yêu cầu — dán hai prompt bất kỳ và xem chính xác dòng nào đã được thêm, xóa, hoặc giữ nguyên. Không git, không setup, không upload.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li><strong>Audit một thay đổi đã deploy.</strong> Marketing đã chỉnh system prompt tuần trước — chính xác cái gì khác? Dán cả hai phiên bản và đọc diff.</li>
  <li><strong>A/B test prompt.</strong> Hai ứng cử viên, một cái chạy tốt hơn trên evals. Diff để cô lập cái gì có thể đang tạo ra khác biệt.</li>
  <li><strong>Revert một regression.</strong> Prompt mới nhất tệ hơn cái cách đây hai vòng lặp — bạn đã thay dòng nào?</li>
  <li><strong>Review edit của đồng đội.</strong> Họ gửi cho bạn một "chỉnh nhỏ" cho system prompt — họ có chỉ chạm vào phần đã nói không?</li>
  <li><strong>Chuyển giữa các họ model.</strong> Chuyển một prompt từ GPT sang Claude thường là những thay đổi từ ngữ nhỏ — diff sau khi viết lại để xác nhận cấu trúc vẫn giữ nguyên.</li>
</ul>

<h3>Cạnh nhau vs hợp nhất</h3>
<ul>
  <li><strong>Cạnh nhau</strong> — A bên trái, B bên phải. Tốt khi cả hai phiên bản có độ dài tương tự và bạn muốn quét bằng mắt.</li>
  <li><strong>Hợp nhất</strong> — một cột duy nhất với dấu + / −, phản chiếu output của <code>git diff</code>. Tốt hơn để chia sẻ trên Slack hoặc khi thay đổi rời rạc.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Đây là diff cấp dòng.</strong> Một từ thay đổi giữa dòng dài đánh dấu cả dòng là thêm+xóa. Để diff cấp câu, bạn có thể thích công cụ cấp từ hơn.</li>
  <li><strong>Whitespace cuối dòng.</strong> Khoảng trắng ẩn ở cuối dòng đánh dấu nó là khác — hữu ích hoặc nhiễu tùy trường hợp. Bật toggle "Bỏ qua whitespace cuối" nếu chỉ quan tâm đến nội dung nhìn thấy.</li>
  <li><strong>Khối được sắp xếp lại trông giống xóa+thêm.</strong> Nếu bạn di chuyển đoạn từ vị trí 1 sang 3, diff hiển thị nó bị xóa ở 1 và thêm ở 3. Không có phát hiện "moved".</li>
  <li><strong>Dòng, không phải token.</strong> Diff này nói dòng, không nói token. Nếu hai prompt có cùng nội dung nhưng wrap khác nhau, mỗi dòng sẽ trông khác. Chuẩn hóa ngắt dòng trước.</li>
  <li><strong>Riêng tư.</strong> Mọi thứ ở lại tab của bạn. Đừng dán bí mật vào placeholder ví dụ — văn bản placeholder là hard-coded, không kết nối với input của bạn.</li>
</ul>
""",
        "hi": """
<h2>यह किसके लिए है?</h2>
<p>Prompt engineering iteration है: आप एक prompt लिखते हैं, test करते हैं, एक phrase tweak करते हैं, फिर test करते हैं। एक दर्जन rounds के बाद, आपके पास एक "version 1" और एक "version 14" है और कोई clean record नहीं कि कहाँ क्या बदला। यह tool आपको वह record on-demand देता है — कोई भी दो prompts paste करें और देखें कि कौन सी lines जोड़ी गईं, हटाई गईं, या अकेली छोड़ी गईं। कोई git नहीं, कोई setup नहीं, कोई upload नहीं।</p>

<h3>कब इस्तेमाल करें</h3>
<ul>
  <li><strong>Deployed change का audit।</strong> Marketing ने पिछले हफ्ते system prompt tweak किया — वास्तव में क्या अलग है? दोनों versions paste करें और diff पढ़ें।</li>
  <li><strong>Prompts का A/B testing।</strong> दो candidate prompts, एक evals पर बेहतर चलता है। यह isolate करने के लिए diff करें कि क्या difference कर रहा है।</li>
  <li><strong>Regression को revert करना।</strong> Latest prompt दो iterations पहले से बदतर है — कौन सी line आपने बदली?</li>
  <li><strong>Teammate के edit की review।</strong> उन्होंने आपको system prompt में "एक छोटा tweak" भेजा — क्या उन्होंने केवल उस हिस्से को छुआ जो उन्होंने कहा?</li>
  <li><strong>Model families के बीच migration।</strong> GPT से Claude पर prompt को adapt करने का मतलब अक्सर शब्दों में छोटे बदलाव होता है — rewrite करने के बाद diff करें यह confirm करने के लिए कि structure same रहा।</li>
</ul>

<h3>Side-by-side vs unified</h3>
<ul>
  <li><strong>Side-by-side</strong> — A बाईं ओर, B दाईं ओर। तब अच्छा जब दोनों versions समान लंबाई के हों और आप दृश्य रूप से scan करना चाहें।</li>
  <li><strong>Unified</strong> — + / − markers के साथ single column, <code>git diff</code> output को mirror करता है। Slack message में share करने या sparse changes के लिए बेहतर।</li>
</ul>

<h3>आम गलतियाँ</h3>
<ul>
  <li><strong>यह line-level diff है।</strong> लंबी line के बीच में एक भी शब्द बदलने पर पूरी line को added+removed के रूप में चिन्हित किया जाता है। एक वाक्य के prose-level diff के लिए, आप word-level tool पसंद कर सकते हैं।</li>
  <li><strong>Trailing whitespace।</strong> एक line के अंत में छिपे spaces उसे अलग के रूप में मार्क करेंगे — case के अनुसार उपयोगी या noisy। यदि आप केवल दृश्य content की परवाह करते हैं तो "Trailing whitespace ignore करें" toggle का उपयोग करें।</li>
  <li><strong>Reordered blocks delete+add की तरह दिखते हैं।</strong> यदि आपने एक paragraph को position 1 से position 3 पर move किया, diff इसे position 1 पर removed और position 3 पर added दिखाता है। कोई "moved" detection नहीं है।</li>
  <li><strong>Lines, tokens नहीं।</strong> यह diff token नहीं बोलता; lines बोलता है। यदि आपके दो prompts में same content है अलग line lengths में rewrapped, हर line अलग दिखेगी। पहले line breaks normalise करें।</li>
  <li><strong>Privacy।</strong> सब कुछ आपके tab में रहता है। Tool के example placeholder में secrets paste न करें — placeholder text hard-coded है, आपके input से connected नहीं।</li>
</ul>
""",
        "sk": """
<h2>Načo to slúži?</h2>
<p>Prompt engineering je iterácia: napíšeš prompt, otestuješ, upravíš jednu frázu, otestuješ znova. Po tucte kôl máš „verziu 1" a „verziu 14" a žiadny čistý záznam toho, čo sa kde zmenilo. Tento nástroj dá ten záznam na vyžiadanie — vlož dva prompty a uvidíš presne, ktoré riadky boli pridané, odstránené alebo nechané tak. Žiadny git, žiadny setup, žiadny upload.</p>

<h3>Kedy to použiť</h3>
<ul>
  <li><strong>Audit nasadené zmeny.</strong> Marketing minulý týždeň upravil system prompt — čo presne je iné? Vlož obe verzie a prečítaj diff.</li>
  <li><strong>A/B test promptov.</strong> Dvaja kandidáti, jeden ide lepšie na evaloch. Diff na izolovanie toho, čo môže robiť rozdiel.</li>
  <li><strong>Rollback regresie.</strong> Najnovší prompt je horší ako ten spred dvoch iterácií — ktorý riadok si zmenil?</li>
  <li><strong>Review úprav kolegu.</strong> Poslal ti „malú úpravu" system promptu — naozaj sa dotkol len toho, čo povedal?</li>
  <li><strong>Migrácia medzi rodinami modelov.</strong> Prispôsobenie promptu z GPT na Claude zvyčajne znamená drobné zmeny slov — diff po prepise, aby si potvrdil zachovanie štruktúry.</li>
</ul>

<h3>Side-by-side vs unified</h3>
<ul>
  <li><strong>Side-by-side</strong> — A vľavo, B vpravo. Dobré, keď obe verzie majú podobnú dĺžku a chceš vizuálne skenovať.</li>
  <li><strong>Unified</strong> — jeden stĺpec s + / − značkami, ako výstup z <code>git diff</code>. Lepšie na zdieľanie v Slacku alebo pri riedkych zmenách.</li>
</ul>

<h3>Časté pasce</h3>
<ul>
  <li><strong>Toto je riadkový diff.</strong> Jedno zmenené slovo uprostred dlhého riadku označí celý riadok ako pridaný+odstránený. Pre vetnú úroveň radšej slovný diff.</li>
  <li><strong>Trailing whitespace.</strong> Skryté medzery na konci riadku ho označia ako odlišný — podľa prípadu užitočné alebo šum. Zapni „Ignorovať koncový whitespace", ak ti záleží iba na viditeľnom obsahu.</li>
  <li><strong>Premiestnené bloky vyzerajú ako odstránenie+pridanie.</strong> Ak si presunul odsek z pozície 1 na 3, diff to ukáže ako odstránené na 1 a pridané na 3. Žiadna detekcia „moved".</li>
  <li><strong>Riadky, nie tokeny.</strong> Diff hovorí riadkami. Ak dva prompty majú rovnaký obsah inak zalomený, každý riadok bude vyzerať inak. Najprv znormalizuj zalomenia.</li>
  <li><strong>Súkromie.</strong> Všetko zostáva v tvojej karte. Nevkladaj tajomstvá do ukážkového placeholderu — text placeholderu je natvrdo, nie je pripojený na tvoj vstup.</li>
</ul>
""",
        "cs": """
<h2>K čemu to slouží?</h2>
<p>Prompt engineering je iterace: napíšeš prompt, otestuješ, upravíš jednu frázi, otestuješ znova. Po tuctu kol máš „verzi 1" a „verzi 14" a žádný čistý záznam toho, co se kde změnilo. Tenhle nástroj dá ten záznam na vyžádání — vlož dva prompty a uvidíš přesně, které řádky byly přidány, odstraněny nebo nechány být. Žádný git, žádný setup, žádný upload.</p>

<h3>Kdy to použít</h3>
<ul>
  <li><strong>Audit nasazené změny.</strong> Marketing minulý týden upravil system prompt — co přesně je jiné? Vlož obě verze a přečti diff.</li>
  <li><strong>A/B test promptů.</strong> Dva kandidáti, jeden jede líp na evalech. Diff na izolaci toho, co může dělat rozdíl.</li>
  <li><strong>Rollback regrese.</strong> Nejnovější prompt je horší než ten před dvěma iteracemi — který řádek jsi změnil?</li>
  <li><strong>Review úprav kolegy.</strong> Poslal ti „malou úpravu" system promptu — opravdu se dotkl jen toho, co řekl?</li>
  <li><strong>Migrace mezi rodinami modelů.</strong> Adaptace promptu z GPT na Claude obvykle znamená drobné změny slov — diff po přepsání, abys potvrdil zachování struktury.</li>
</ul>

<h3>Side-by-side vs unified</h3>
<ul>
  <li><strong>Side-by-side</strong> — A vlevo, B vpravo. Dobré, když obě verze mají podobnou délku a chceš vizuálně skenovat.</li>
  <li><strong>Unified</strong> — jeden sloupec s + / − značkami, jako výstup z <code>git diff</code>. Lepší na sdílení v Slacku nebo při řídkých změnách.</li>
</ul>

<h3>Časté pasti</h3>
<ul>
  <li><strong>Tohle je řádkový diff.</strong> Jedno změněné slovo uprostřed dlouhého řádku označí celý řádek jako přidaný+odstraněný. Pro větnou úroveň radši slovní diff.</li>
  <li><strong>Trailing whitespace.</strong> Skryté mezery na konci řádku ho označí jako odlišný — podle případu užitečné nebo šum. Zapni „Ignorovat koncový whitespace", pokud ti záleží jen na viditelném obsahu.</li>
  <li><strong>Přemístěné bloky vypadají jako odstranění+přidání.</strong> Pokud jsi přesunul odstavec z pozice 1 na 3, diff to ukáže jako odstraněné na 1 a přidané na 3. Žádná detekce „moved".</li>
  <li><strong>Řádky, ne tokeny.</strong> Diff mluví řádky. Pokud dva prompty mají stejný obsah jinak zalomený, každý řádek bude vypadat jinak. Nejdřív znormalizuj zalomení.</li>
  <li><strong>Soukromí.</strong> Všechno zůstává v tvé kartě. Nevkládej tajemství do ukázkového placeholderu — text placeholderu je natvrdo, není připojen na tvůj vstup.</li>
</ul>
""",
    },
    "related": ["text-diff", "json-diff", "token-counter"],
    "howto": {"flow": "compare", "action": "compare", "noun": "text"},
}
