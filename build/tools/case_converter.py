TOOL = {
    "slug": "case-converter",
    "category": "text",
    "icon": "Aa",
    "tags": ["case", "convert", "camel", "snake", "kebab", "pascal", "title", "upper", "lower"],
    "i18n": {
        "en": {
            "name": "Case Converter",
            "tagline": "Convert text between UPPER, lower, Title, Sentence, camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE, and dot.case.",
            "description": "Free online case converter. Switch text between upper, lower, title, sentence, camel, pascal, snake, kebab, constant, and dot case in one click.",
        },
        "de": {"name": "Schreibweisen-Konverter", "tagline": "Wandle Text zwischen GROSS, klein, Titel, Satz, camelCase, PascalCase, snake_case, kebab-case, KONSTANTE und dot.case um.", "description": "Kostenloser Schreibweisen-Konverter für GROSS, klein, Titel, Satz, camel, pascal, snake, kebab, konstante und Punkt-Schreibweise."},
        "es": {"name": "Conversor de Mayúsculas", "tagline": "Convierte texto entre MAYÚSCULAS, minúsculas, Título, Oración, camelCase, PascalCase, snake_case, kebab-case, CONSTANTE y dot.case.", "description": "Conversor de mayúsculas/minúsculas gratuito. MAYÚS, minús, título, oración, camel, pascal, snake, kebab, constante y punto."},
        "fr": {"name": "Convertisseur de Casse", "tagline": "Convertissez du texte entre MAJUSCULES, minuscules, Titre, Phrase, camelCase, PascalCase, snake_case, kebab-case, CONSTANTE et dot.case.", "description": "Convertisseur de casse gratuit. MAJ, min, titre, phrase, camel, pascal, snake, kebab, constante et point."},
        "it": {"name": "Convertitore di Maiuscole/Minuscole", "tagline": "Converti testo tra MAIUSCOLO, minuscolo, Titolo, Frase, camelCase, PascalCase, snake_case, kebab-case, COSTANTE e dot.case.", "description": "Convertitore di maiuscole/minuscole gratuito. MAIUSC, minusc, titolo, frase, camel, pascal, snake, kebab, costante e punto."},
        "pt": {"name": "Conversor de Capitalização", "tagline": "Converta texto entre MAIÚSCULAS, minúsculas, Título, Frase, camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE e dot.case.", "description": "Conversor de capitalização online gratuito. Alterne texto entre maiúsculas, minúsculas, título, frase, camel, pascal, snake, kebab, constant e dot case com um clique."},
        "pl": {"name": "Konwerter Wielkości Liter", "tagline": "Konwertuj tekst między WIELKIMI, małymi, Tytułowymi, Zdaniowymi, camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE i dot.case.", "description": "Darmowy konwerter wielkości liter online. Zmień tekst między upper, lower, title, sentence, camel, pascal, snake, kebab, constant i dot case jednym kliknięciem."},
        "ja": {"name": "ケース変換ツール", "tagline": "テキストを大文字、小文字、タイトル、文、camelCase、PascalCase、snake_case、kebab-case、CONSTANT_CASE、dot.case の間で変換。", "description": "オンライン無料のケース変換ツール。upper、lower、title、sentence、camel、pascal、snake、kebab、constant、dot ケースをワンクリックで切り替えできます。"},
        "nl": {"name": "Case Converter", "tagline": "Converteer tekst tussen UPPER, lower, Title, Sentence, camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE en dot.case.", "description": "Gratis online case converter. Schakel tekst tussen upper, lower, title, sentence, camel, pascal, snake, kebab, constant en dot case in één klik."},
        "tr": {"name": "Case Converter", "tagline": "Metni UPPER, lower, Title, Sentence, camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE ve dot.case arasında dönüştür.", "description": "Ücretsiz online büyük/küçük harf dönüştürücü. Metni tek tıkla upper, lower, title, sentence, camel, pascal, snake, kebab, constant ve dot case arasında değiştir."},
        "id": {"name": "Pengubah Case", "tagline": "Ubah teks antara UPPER, lower, Title, Sentence, camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE, dan dot.case.", "description": "Pengubah case teks gratis. Konversi antara UPPER, lower, Title Case, Sentence case, camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE, dan dot.case. Sadar-Unicode dan cepat."},
        "vi": {"name": "Chuyển đổi Case", "tagline": "Chuyển văn bản giữa UPPER, lower, Title, Sentence, camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE và dot.case.", "description": "Công cụ chuyển đổi case văn bản miễn phí trực tuyến. Chuyển bất kỳ chuỗi nào sang UPPER, lower, Title, Sentence, camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE hoặc dot.case ngay lập tức."},
        "hi": {"name": "Case Converter", "tagline": "Text को UPPER, lower, Title, Sentence, camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE और dot.case के बीच बदलें।", "description": "मुफ़्त ऑनलाइन case converter। Text को एक click में upper, lower, title, sentence, camel, pascal, snake, kebab, constant और dot case के बीच switch करें।"},
        "sk": {"name": 'Konvertor veľkosti písmen', "tagline": 'Prevod textu medzi UPPER, lower, Title, Sentence, camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE a dot.case.', "description": 'Bezplatný online konvertor veľkosti písmen. Prevedie text medzi všetkými bežnými case formátmi — UPPER, lower, Title, camelCase, snake_case, kebab-case a ďalšie. Funguje v prehliadači.'},
        "cs": {"name": 'Konvertor velikosti písmen', "tagline": 'Převod textu mezi UPPER, lower, Title, Sentence, camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE a dot.case.', "description": 'Zdarma online konvertor velikosti písmen. Převede text mezi všemi běžnými case formáty — UPPER, lower, Title, camelCase, snake_case, kebab-case a další. Funguje v prohlížeči.'},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="cc-input" oninput="ccRun()" placeholder="Paste or type any text here" spellcheck="false">The Quick Brown Fox Jumps Over the Lazy Dog</textarea>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="case-grid" id="cc-out"></div>
</div>
""",
    "script": """
<style>
.case-grid{display:grid;gap:0.6rem}
.case-row{display:grid;grid-template-columns:140px 1fr auto;gap:0.6rem;align-items:center;padding:0.55rem 0.7rem;background:var(--bg-elev);border:1px solid var(--border);border-radius:8px}
.case-row .lbl{font-size:0.78rem;color:var(--text-muted);font-family:ui-monospace,monospace}
.case-row .val{font-family:ui-monospace,monospace;font-size:0.9rem;word-break:break-word;overflow-wrap:anywhere}
.case-row button{padding:0.3rem 0.65rem;font-size:0.78rem}
@media(max-width:600px){.case-row{grid-template-columns:1fr;gap:0.25rem}.case-row button{justify-self:start}}
</style>
<script>
function ccWords(s){
  return s
    .replace(/([a-z\\d])([A-Z])/g, '$1 $2')
    .replace(/([A-Z]+)([A-Z][a-z])/g, '$1 $2')
    .replace(/[_\\-\\.\\s/]+/g, ' ')
    .trim()
    .split(/\\s+/)
    .filter(Boolean);
}
const CC_FORMS = [
  ['UPPER',     w => w.map(x=>x.toUpperCase()).join(' ')],
  ['lower',     w => w.map(x=>x.toLowerCase()).join(' ')],
  ['Title',     w => w.map(x=>x[0].toUpperCase()+x.slice(1).toLowerCase()).join(' ')],
  ['Sentence',  w => w.length ? (w[0][0].toUpperCase()+w[0].slice(1).toLowerCase()+(w.length>1?' '+w.slice(1).map(x=>x.toLowerCase()).join(' '):'')) : ''],
  ['camelCase', w => w.map((x,i)=>i===0?x.toLowerCase():x[0].toUpperCase()+x.slice(1).toLowerCase()).join('')],
  ['PascalCase',w => w.map(x=>x[0].toUpperCase()+x.slice(1).toLowerCase()).join('')],
  ['snake_case',w => w.map(x=>x.toLowerCase()).join('_')],
  ['kebab-case',w => w.map(x=>x.toLowerCase()).join('-')],
  ['CONSTANT',  w => w.map(x=>x.toUpperCase()).join('_')],
  ['dot.case',  w => w.map(x=>x.toLowerCase()).join('.')],
  ['path/case', w => w.map(x=>x.toLowerCase()).join('/')],
  ['Train-Case',w => w.map(x=>x[0].toUpperCase()+x.slice(1).toLowerCase()).join('-')],
  ['inverse',   (w,raw) => raw.split('').map(c=>c===c.toLowerCase()?c.toUpperCase():c.toLowerCase()).join('')],
  ['aLtErNaTe', (w,raw) => raw.split('').map((c,i)=>i%2?c.toUpperCase():c.toLowerCase()).join('')],
];
function ccCopy(text, btn){
  navigator.clipboard.writeText(text);
  const old = btn.textContent;
  btn.textContent = '✓';
  setTimeout(()=>btn.textContent = old, 900);
}
function ccRun(){
  const raw = document.getElementById('cc-input').value;
  const words = ccWords(raw);
  const out = document.getElementById('cc-out');
  out.innerHTML = '';
  CC_FORMS.forEach(([label, fn]) => {
    const val = fn(words, raw);
    const row = document.createElement('div');
    row.className = 'case-row';
    const l = document.createElement('div'); l.className = 'lbl'; l.textContent = label;
    const v = document.createElement('div'); v.className = 'val'; v.textContent = val || '—';
    const b = document.createElement('button'); b.className = 'secondary'; b.textContent = '{LBL_COPY}';
    b.onclick = () => ccCopy(val, b);
    row.appendChild(l); row.appendChild(v); row.appendChild(b);
    out.appendChild(row);
  });
}
document.addEventListener('DOMContentLoaded', ccRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Every language and platform has its own conventions for naming things — JavaScript wants <code>camelCase</code>, Python wants <code>snake_case</code>, CSS wants <code>kebab-case</code>, environment variables want <code>CONSTANT_CASE</code>. Translating between them by hand is fiddly, especially with edge cases (acronyms, numbers, existing separators). This tool splits any input into words by detecting case transitions, separators (<code>_ - . /</code>), and whitespace, then re-joins them in 14 different styles.</p>

<h3>When to use it</h3>
<ul>
  <li>Renaming a field from API JSON (camelCase) to a Python ORM column (snake_case).</li>
  <li>Generating CSS class names from design-system token names that arrive in PascalCase.</li>
  <li>Converting a list of headings into kebab-case slugs, or environment-variable names into CONSTANT_CASE.</li>
  <li>Quickly converting "The Quick Brown Fox" into Title Case, Sentence case, or Train-Case for a headline / button label.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Acronyms are tricky.</strong> Should "XMLHttpRequest" become "XML_Http_Request" or "Xml_Http_Request"? This tool treats consecutive capitals as one word boundary (<code>xml http request</code>), then re-cases — which matches Java/JS conventions but not all style guides.</li>
  <li><strong>Numbers attach to the previous word.</strong> "Item2" becomes one word "item2", not two. Add a separator if you want them split.</li>
  <li><strong>"camelCase first letter"</strong> is always lowercase even if the input started with a capital. PascalCase preserves the capital.</li>
  <li><strong>Round-tripping isn't always lossless.</strong> Going camelCase → kebab-case → camelCase loses the original capitalisation hint at word boundaries; the case-detection heuristic does its best but can't recover what wasn't preserved.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Cada linguagem e plataforma tem suas próprias convenções para nomear coisas — JavaScript quer <code>camelCase</code>, Python quer <code>snake_case</code>, CSS quer <code>kebab-case</code>, variáveis de ambiente querem <code>CONSTANT_CASE</code>. Traduzir entre elas na mão é chato, especialmente com casos especiais (siglas, números, separadores já existentes). Esta ferramenta quebra qualquer entrada em palavras detectando transições de capitalização, separadores (<code>_ - . /</code>) e espaços em branco, e depois remonta em 14 estilos diferentes.</p>

<h3>Quando usar</h3>
<ul>
  <li>Renomear um campo de um JSON de API (camelCase) para uma coluna de ORM Python (snake_case).</li>
  <li>Gerar nomes de classes CSS a partir de nomes de tokens de design-system que chegam em PascalCase.</li>
  <li>Converter uma lista de títulos para slugs em kebab-case, ou nomes de variáveis de ambiente para CONSTANT_CASE.</li>
  <li>Converter rapidamente "The Quick Brown Fox" para Title Case, Sentence case ou Train-Case para um título / rótulo de botão.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Siglas são complicadas.</strong> "XMLHttpRequest" deve virar "XML_Http_Request" ou "Xml_Http_Request"? Esta ferramenta trata letras maiúsculas consecutivas como um único limite de palavra (<code>xml http request</code>) e depois recapitaliza — o que combina com convenções Java/JS, mas não com todos os style guides.</li>
  <li><strong>Números ficam grudados na palavra anterior.</strong> "Item2" vira uma palavra só "item2", não duas. Adicione um separador se quiser separar.</li>
  <li><strong>"Primeira letra do camelCase"</strong> é sempre minúscula mesmo se a entrada começou com maiúscula. PascalCase preserva a maiúscula.</li>
  <li><strong>Round-trip nem sempre é sem perdas.</strong> Ir de camelCase → kebab-case → camelCase perde a dica original de capitalização nos limites de palavra; a heurística de detecção faz o que pode, mas não consegue recuperar o que não foi preservado.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Każdy język i platforma ma swoje konwencje nazewnicze — JavaScript chce <code>camelCase</code>, Python chce <code>snake_case</code>, CSS chce <code>kebab-case</code>, zmienne środowiskowe chcą <code>CONSTANT_CASE</code>. Tłumaczenie między nimi ręcznie jest upierdliwe, zwłaszcza przy edge case'ach (akronimy, liczby, istniejące separatory). To narzędzie dzieli dowolne wejście na słowa, wykrywając zmiany wielkości liter, separatory (<code>_ - . /</code>) i białe znaki, a potem składa je z powrotem w 14 różnych stylach.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Zmiana nazwy pola z JSON-a API (camelCase) na kolumnę ORM-a w Pythonie (snake_case).</li>
  <li>Generowanie nazw klas CSS z nazw tokenów design systemu, które przychodzą w PascalCase.</li>
  <li>Konwersja listy nagłówków na slugi w kebab-case albo nazwy zmiennych środowiskowych na CONSTANT_CASE.</li>
  <li>Szybka konwersja "The Quick Brown Fox" na Title Case, Sentence case albo Train-Case do nagłówka / etykiety przycisku.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Akronimy są podchwytliwe.</strong> Czy "XMLHttpRequest" powinno stać się "XML_Http_Request" czy "Xml_Http_Request"? To narzędzie traktuje ciąg wielkich liter jako jeden punkt podziału (<code>xml http request</code>) i potem ustawia wielkość — co pasuje do konwencji Java/JS, ale nie do wszystkich style guide'ów.</li>
  <li><strong>Liczby przyklejają się do poprzedniego słowa.</strong> "Item2" staje się jednym słowem "item2", nie dwoma. Dodaj separator, jeśli chcesz je rozdzielić.</li>
  <li><strong>"Pierwsza litera camelCase"</strong> jest zawsze mała, nawet jeśli wejście zaczynało się od wielkiej. PascalCase zachowuje wielką.</li>
  <li><strong>Round-trip nie zawsze jest bezstratny.</strong> Przejście camelCase → kebab-case → camelCase gubi oryginalną informację o wielkości liter na granicach słów; heurystyka robi co może, ale nie odtworzy tego, czego nie zachowano.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>言語やプラットフォームごとに命名規則は異なります。JavaScript は <code>camelCase</code>、Python は <code>snake_case</code>、CSS は <code>kebab-case</code>、環境変数は <code>CONSTANT_CASE</code>。これらを手作業で変換するのは手間がかかり、特に頭字語、数字、既存の区切り記号があると面倒です。このツールは大文字・小文字の変化、区切り記号（<code>_ - . /</code>）、空白を検出して入力を単語に分割し、14 種類のスタイルで再構成します。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>API JSON のフィールド名（camelCase）を Python ORM のカラム名（snake_case）にリネームするとき。</li>
  <li>PascalCase で渡されるデザインシステムのトークン名から CSS クラス名を生成するとき。</li>
  <li>見出しのリストを kebab-case のスラグや、環境変数名を CONSTANT_CASE に変換するとき。</li>
  <li>"The Quick Brown Fox" を Title Case、Sentence case、Train-Case にサッと変換して見出しやボタンラベルを作りたいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>頭字語は厄介です。</strong> "XMLHttpRequest" は "XML_Http_Request" にすべきか、"Xml_Http_Request" にすべきか？ このツールは連続する大文字を 1 つの境界として扱い（<code>xml http request</code>）、再キャピタライズします。Java/JS の慣習には合いますが、すべてのスタイルガイドに合うわけではありません。</li>
  <li><strong>数字は前の単語にくっつきます。</strong> "Item2" は "item2" 1 単語になり、2 つには分かれません。分けたい場合は区切り記号を入れてください。</li>
  <li><strong>"camelCase の最初の文字"</strong> は、入力が大文字で始まっていても常に小文字になります。PascalCase は大文字を保持します。</li>
  <li><strong>ラウンドトリップは必ずしも無損失ではありません。</strong> camelCase → kebab-case → camelCase と変換すると、元の単語境界の大文字情報は失われます。検出ヒューリスティックは可能な限り頑張りますが、保持されていない情報は復元できません。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Elke taal en elk platform heeft eigen conventies voor het benoemen van dingen — JavaScript wil <code>camelCase</code>, Python wil <code>snake_case</code>, CSS wil <code>kebab-case</code>, environment variables willen <code>CONSTANT_CASE</code>. Daartussen vertalen met de hand is gepriegel, vooral bij edge cases (acroniemen, getallen, bestaande separators). Deze tool splitst elke input in woorden door case-overgangen, separators (<code>_ - . /</code>) en whitespace te detecteren, en plakt ze daarna in 14 verschillende stijlen terug aan elkaar.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een veld hernoemen van API-JSON (camelCase) naar een Python ORM-kolom (snake_case).</li>
  <li>CSS-classnames genereren uit design-system tokennamen die in PascalCase binnenkomen.</li>
  <li>Een lijst koppen converteren naar kebab-case slugs, of environment variable-namen naar CONSTANT_CASE.</li>
  <li>Snel "The Quick Brown Fox" omzetten naar Title Case, Sentence case of Train-Case voor een kop / button-label.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Acroniemen zijn lastig.</strong> Moet "XMLHttpRequest" worden tot "XML_Http_Request" of "Xml_Http_Request"? Deze tool behandelt opeenvolgende hoofdletters als één woordgrens (<code>xml http request</code>) en re-cased dan — wat overeenkomt met Java/JS-conventies maar niet met alle stijlgidsen.</li>
  <li><strong>Getallen plakken aan het vorige woord.</strong> "Item2" wordt één woord "item2", geen twee. Voeg een separator toe als je ze gesplitst wilt.</li>
  <li><strong>"camelCase eerste letter"</strong> is altijd kleine letter, ook als de input met een hoofdletter begon. PascalCase behoudt de hoofdletter.</li>
  <li><strong>Round-trippen is niet altijd lossless.</strong> camelCase → kebab-case → camelCase verliest de oorspronkelijke hoofdletterhint bij woordgrenzen; de case-detectie heuristiek doet zijn best maar kan niet terughalen wat niet bewaard is.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Her dilin ve platformun şeyleri adlandırma için kendi gelenekleri vardır — JavaScript <code>camelCase</code>, Python <code>snake_case</code>, CSS <code>kebab-case</code>, ortam değişkenleri <code>CONSTANT_CASE</code> ister. Aralarında elle çevirmek özellikle uç durumlarda (kısaltmalar, sayılar, mevcut ayraçlar) zahmetlidir. Bu araç herhangi bir girdiyi case geçişlerini, ayraçları (<code>_ - . /</code>) ve boşluğu tespit ederek kelimelere ayırır, sonra 14 farklı stilde yeniden birleştirir.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Bir API JSON'undan (camelCase) bir Python ORM sütununa (snake_case) alan adı değiştirme.</li>
  <li>PascalCase'de gelen tasarım sistemi token adlarından CSS sınıf adları üretme.</li>
  <li>Bir başlık listesini kebab-case slug'lara veya ortam değişkeni adlarını CONSTANT_CASE'e dönüştürme.</li>
  <li>"The Quick Brown Fox" ifadesini bir başlık / düğme etiketi için Title Case, Sentence case veya Train-Case'e hızlıca dönüştürme.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Kısaltmalar zordur.</strong> "XMLHttpRequest" "XML_Http_Request" mi yoksa "Xml_Http_Request" mi olmalı? Bu araç ardışık büyük harfleri tek kelime sınırı olarak ele alır (<code>xml http request</code>), sonra yeniden case'ler.</li>
  <li><strong>Sayılar önceki kelimeye yapışır.</strong> "Item2" tek kelime "item2" olur, iki değil. Ayrılmasını istiyorsan ayraç ekle.</li>
  <li><strong>"camelCase ilk harfi"</strong> giriş büyükle başlasa bile her zaman küçüktür. PascalCase büyük harfi korur.</li>
  <li><strong>Round-trip her zaman kayıpsız değildir.</strong> camelCase → kebab-case → camelCase, kelime sınırlarındaki orijinal büyük harf ipucunu kaybeder.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Setiap bahasa dan platform punya konvensi penamaan sendiri — JavaScript ingin <code>camelCase</code>, Python ingin <code>snake_case</code>, CSS ingin <code>kebab-case</code>, environment variable ingin <code>CONSTANT_CASE</code>. Menerjemahkan antar bentuk secara manual itu ribet, terutama untuk edge case (akronim, angka, separator yang sudah ada). Tool ini memecah input apa pun jadi kata-kata dengan mendeteksi transisi case, separator (<code>_ - . /</code>), dan whitespace, lalu menggabungkan kembali dalam 14 gaya berbeda.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Mengubah nama field dari JSON API (camelCase) ke kolom ORM Python (snake_case).</li>
  <li>Membuat nama class CSS dari nama token design-system yang datang dalam PascalCase.</li>
  <li>Mengkonversi daftar heading menjadi slug kebab-case, atau nama environment variable menjadi CONSTANT_CASE.</li>
  <li>Cepat mengubah "The Quick Brown Fox" menjadi Title Case, Sentence case, atau Train-Case untuk headline / label tombol.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Akronim itu tricky.</strong> Haruskah "XMLHttpRequest" jadi "XML_Http_Request" atau "Xml_Http_Request"? Tool ini memperlakukan huruf kapital berurutan sebagai satu batas kata (<code>xml http request</code>), lalu re-case — yang cocok dengan konvensi Java/JS tapi bukan semua style guide.</li>
  <li><strong>Angka menempel ke kata sebelumnya.</strong> "Item2" jadi satu kata "item2", bukan dua. Tambahkan separator jika kamu ingin memisahkannya.</li>
  <li><strong>"Huruf pertama camelCase"</strong> selalu lowercase meski input mulai dengan kapital. PascalCase mempertahankan kapital.</li>
  <li><strong>Round-tripping tidak selalu lossless.</strong> Beralih camelCase → kebab-case → camelCase kehilangan petunjuk kapitalisasi asli di batas kata.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Văn bản trong code và content thường cần được biểu diễn ở các "case" cụ thể: tên class trong PascalCase, biến trong camelCase, slug URL trong kebab-case, hằng số trong CONSTANT_CASE. Việc chuyển đổi thủ công thì dễ sai — đặc biệt với các từ viết tắt và dấu chấm câu. Công cụ này thực hiện việc chuyển đổi cho bạn với các quy tắc nhất quán cho mỗi case.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Đổi tên: chuyển <code>UserAccount</code> thành <code>user_account</code> cho Python hoặc <code>user-account</code> cho URL.</li>
  <li>Chuyển dữ liệu giữa API có quy ước đặt tên khác nhau.</li>
  <li>Làm sạch heading của tài liệu thành slug hoặc anchor.</li>
  <li>Tạo nhanh CONSTANT_CASE cho hằng số môi trường hoặc enum.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Viết tắt phá vỡ camelCase ngây thơ.</strong> <code>XMLHTTPRequest</code> hay <code>XmlHttpRequest</code>? Quy ước Google JavaScript thiên về cái sau; thư viện cũ dùng cái trước. Hãy nhất quán.</li>
  <li><strong>Title Case không phải là viết hoa từng từ.</strong> Title Case tiếng Anh chân chính giữ chữ thường cho mạo từ, giới từ ngắn và liên từ — nhưng các framework thường dùng "Capitalize Each Word" rồi gọi nó là title case.</li>
  <li><strong>Dấu câu trong slug.</strong> Một bộ tạo kebab-case tốt sẽ bỏ dấu câu, chuyển khoảng trắng thành dấu gạch ngang và viết thường mọi thứ — đừng để dấu nháy hay dấu chấm than rơi vào.</li>
  <li><strong>Không phải tất cả ngôn ngữ đều có case.</strong> Tiếng Trung, tiếng Nhật và tiếng Hàn không có khái niệm chữ hoa/chữ thường — chuyển đổi case của chúng là no-op.</li>
</ul>
""",
        "hi": """
<h2>यह किसके लिए है?</h2>
<p>हर language और platform की चीज़ों को नाम देने की अपनी conventions होती हैं — JavaScript को <code>camelCase</code> चाहिए, Python को <code>snake_case</code>, CSS को <code>kebab-case</code>, environment variables को <code>CONSTANT_CASE</code>। हाथ से इनके बीच translate करना झंझट है, खासकर edge cases (acronyms, numbers, मौजूदा separators) के साथ। यह tool किसी भी input को case transitions, separators (<code>_ - . /</code>) और whitespace detect करके words में split करता है, फिर उन्हें 14 अलग styles में फिर से जोड़ देता है।</p>

<h3>कब इस्तेमाल करें</h3>
<ul>
  <li>API JSON (camelCase) से किसी field का नाम Python ORM column (snake_case) के लिए बदलना।</li>
  <li>PascalCase में आने वाले design-system token names से CSS class names बनाना।</li>
  <li>Headings की list को kebab-case slugs में, या environment variable names को CONSTANT_CASE में बदलना।</li>
  <li>"The Quick Brown Fox" को जल्दी से किसी headline / button label के लिए Title Case, Sentence case, या Train-Case में बदलना।</li>
</ul>

<h3>आम गलतियाँ</h3>
<ul>
  <li><strong>Acronyms tricky हैं।</strong> क्या "XMLHttpRequest" "XML_Http_Request" बने या "Xml_Http_Request"? यह tool लगातार capitals को एक word boundary मानता है (<code>xml http request</code>), फिर re-case करता है — जो Java/JS conventions से मेल खाता है पर सभी style guides से नहीं।</li>
  <li><strong>Numbers पिछले word से जुड़ जाते हैं।</strong> "Item2" एक ही word "item2" बनता है, दो नहीं। अगर आप उन्हें split करना चाहते हैं तो separator जोड़ें।</li>
  <li><strong>"camelCase का पहला letter"</strong> हमेशा lowercase होता है, भले ही input capital से शुरू हुआ हो। PascalCase capital बनाए रखता है।</li>
  <li><strong>Round-tripping हमेशा lossless नहीं होती।</strong> camelCase → kebab-case → camelCase करने पर word boundaries पर original capitalisation hint खो जाती है; case-detection heuristic अपनी पूरी कोशिश करती है पर जो preserve नहीं हुआ उसे recover नहीं कर सकती।</li>
</ul>
""",
        "sk": """

<h2>Načo to slúži?</h2>
<p>Programátorský kód, JSON kľúče, CSS triedy a URL slugy používajú rôzne case konvencie — <code>camelCase</code>, <code>PascalCase</code>, <code>snake_case</code>, <code>kebab-case</code>, <code>CONSTANT_CASE</code>, <code>dot.case</code>. Tento nástroj zoberie akýkoľvek text a okamžite ho prepíše do ľubovoľného z nich.</p>

<h3>Kedy to použiť</h3>
<ul>
  <li>Konverzia API JSON keys z <code>snake_case</code> (Python) na <code>camelCase</code> (JavaScript).</li>
  <li>Generovanie CSS class mien z titulku komponentu.</li>
  <li>Príprava CONSTANT_CASE názvov pre environment variables.</li>
  <li>Rýchla normalizácia copy-paste textu pred vložením do dokumentu.</li>
</ul>

<h3>Časté chyby</h3>
<ul>
  <li><strong>Akronymy.</strong> <code>HTMLParser</code> v PascalCase je validný — keď to prevedieš na snake_case, môže to skončiť ako <code>h_t_m_l_parser</code> aj keď chceš <code>html_parser</code>. Dohodnúť konvenciu vopred.</li>
  <li><strong>Sentence case ≠ Title Case.</strong> Sentence: prvé slovo veľké; Title: každé slovo veľké okrem spojok.</li>
  <li><strong>Čísla.</strong> <code>foo2bar</code> sa pri konverzii môže rozdeliť ako <code>foo_2_bar</code> alebo <code>foo2_bar</code> — záleží na implementácii.</li>
  <li><strong>Diakritika.</strong> Slovenské znaky (š, č, ž…) zostávajú pri väčšine konverzií, ale nie sú validné v slug-formátoch.</li>
</ul>
""",
        "cs": """

<h2>K čemu to slouží?</h2>
<p>Programátorský kód, JSON klíče, CSS třídy a URL slugy používají různé case konvence — <code>camelCase</code>, <code>PascalCase</code>, <code>snake_case</code>, <code>kebab-case</code>, <code>CONSTANT_CASE</code>, <code>dot.case</code>. Tenhle nástroj vezme jakýkoli text a okamžitě ho přepíše do libovolného z nich.</p>

<h3>Kdy to použít</h3>
<ul>
  <li>Konverze API JSON keys z <code>snake_case</code> (Python) na <code>camelCase</code> (JavaScript).</li>
  <li>Generování CSS class jmen z titulku komponenty.</li>
  <li>Příprava CONSTANT_CASE názvů pro environment variables.</li>
  <li>Rychlá normalizace copy-paste textu před vložením do dokumentu.</li>
</ul>

<h3>Časté chyby</h3>
<ul>
  <li><strong>Akronymy.</strong> <code>HTMLParser</code> v PascalCase je validní — když to převedeš na snake_case, může to skončit jako <code>h_t_m_l_parser</code>, i když chceš <code>html_parser</code>. Domluvit konvenci předem.</li>
  <li><strong>Sentence case ≠ Title Case.</strong> Sentence: první slovo velké; Title: každé slovo velké kromě spojek.</li>
  <li><strong>Čísla.</strong> <code>foo2bar</code> se při konverzi může rozdělit jako <code>foo_2_bar</code> nebo <code>foo2_bar</code> — záleží na implementaci.</li>
  <li><strong>Diakritika.</strong> České znaky (š, č, ž…) zůstávají při většině konverzí, ale nejsou validní ve slug-formátech.</li>
</ul>
""",
    },
    "related": ["slug-generator", "word-counter", "text-diff"],
    "howto": {"flow": "transform", "action": "convert", "noun": "text"},
}
