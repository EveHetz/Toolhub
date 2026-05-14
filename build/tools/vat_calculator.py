import json
from pathlib import Path

_DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "vat_rates.json"
_VAT_DATA = json.loads(_DATA_PATH.read_text(encoding="utf-8"))
_VAT_DATA_JS = json.dumps(_VAT_DATA, ensure_ascii=False, separators=(",", ":"))

TOOL = {
    "slug": "vat-calculator",
    "category": "math",
    "icon": "🧾",
    "tags": ["vat", "tax", "calculator", "eu", "uk", "small-business", "freelancer", "invoice", "iva", "tva", "mwst"],
    "i18n": {
        "en": {
            "name": "VAT Calculator",
            "tagline": "Calculate VAT for any EU country, UK, Switzerland, and more — with current 2025 rates including post-reform updates many tools miss. Standard, reduced, and zero rates supported.",
            "description": "Free online VAT calculator with up-to-date rates for 30+ countries. Pick a country, pick a category (standard, reduced, zero), enter net or gross — get the breakdown. Includes recent rate changes (Slovakia 20%→23% in 2025, Estonia 22%→24%, etc.) and per-category reduced rates. No upload, no tracking, no signup.",
        },
        "de": {
            "name": "MwSt.-Rechner",
            "tagline": "Mehrwertsteuer für jedes EU-Land, UK, die Schweiz und mehr berechnen — mit aktuellen 2025-Sätzen inkl. Reformen, die viele Tools übersehen. Regel-, ermäßigte und Null-Sätze.",
            "description": "Kostenloser MwSt.-Rechner mit aktuellen Sätzen für 30+ Länder. Land wählen, Kategorie (Standard, ermäßigt, null) wählen, Netto oder Brutto eingeben — die Aufteilung erscheint. Berücksichtigt jüngste Reformen (Slowakei 20 %→23 % in 2025, Estland 22 %→24 % u. a.) und länderspezifische ermäßigte Sätze. Kein Upload, kein Tracking, keine Anmeldung.",
        },
        "es": {
            "name": "Calculadora de IVA",
            "tagline": "Calcula el IVA para cualquier país de la UE, Reino Unido, Suiza y más — con tipos actuales de 2025, incluidas reformas que muchas calculadoras no recogen. Tipos general, reducido y cero.",
            "description": "Calculadora de IVA gratuita con tipos actualizados para 30+ países. Elige país, elige categoría (general, reducido, cero), introduce neto o bruto — verás el desglose. Incluye cambios recientes (Eslovaquia 20%→23% en 2025, Estonia 22%→24%, etc.) y tipos reducidos por categoría. Sin subida, sin tracking, sin registro.",
        },
        "fr": {
            "name": "Calculateur de TVA",
            "tagline": "Calculez la TVA pour tout pays de l'UE, le Royaume-Uni, la Suisse et plus — taux 2025 à jour, y compris les réformes que beaucoup d'outils oublient. Taux normal, réduit et zéro.",
            "description": "Calculateur de TVA gratuit avec des taux à jour pour 30+ pays. Choisissez le pays, la catégorie (normal, réduit, zéro), saisissez HT ou TTC — vous voyez la ventilation. Inclut les changements récents (Slovaquie 20%→23% en 2025, Estonie 22%→24%, etc.) et les taux réduits par catégorie. Aucun envoi, aucun tracking, sans inscription.",
        },
        "it": {
            "name": "Calcolatore IVA",
            "tagline": "Calcola l'IVA per qualsiasi paese UE, Regno Unito, Svizzera e altri — con le aliquote 2025 aggiornate, incluse riforme che molti tool dimenticano. Ordinaria, ridotta e zero.",
            "description": "Calcolatore IVA gratuito con aliquote aggiornate per 30+ paesi. Scegli il paese, la categoria (ordinaria, ridotta, zero), inserisci netto o lordo — vedi lo split. Include cambi recenti (Slovacchia 20%→23% nel 2025, Estonia 22%→24%, ecc.) e aliquote ridotte per categoria. Nessun upload, nessun tracking, nessuna registrazione.",
        },
        "pt": {
            "name": "Calculadora de IVA",
            "tagline": "Calcule o IVA para qualquer país da UE, Reino Unido, Suíça e mais — com taxas atuais de 2025, incluindo reformas que muitas calculadoras omitem. Normal, reduzida e zero.",
            "description": "Calculadora de IVA gratuita com taxas atualizadas para 30+ países. Escolha o país, a categoria (normal, reduzida, zero), digite líquido ou bruto — veja o detalhamento. Inclui mudanças recentes (Eslováquia 20%→23% em 2025, Estônia 22%→24%, etc.) e taxas reduzidas por categoria. Sem upload, sem rastreamento, sem cadastro.",
        },
        "pl": {
            "name": "Kalkulator VAT",
            "tagline": "Policz VAT dla każdego kraju UE, UK, Szwajcarii i nie tylko — z aktualnymi stawkami 2025, w tym reformami, których wiele kalkulatorów nie ma. Stawka podstawowa, obniżone i zerowa.",
            "description": "Darmowy kalkulator VAT z aktualnymi stawkami dla 30+ krajów. Wybierz kraj, kategorię (podstawowa, obniżona, zerowa), wpisz netto lub brutto — zobaczysz rozbicie. Uwzględnia ostatnie zmiany (Słowacja 20%→23% w 2025, Estonia 22%→24% itd.) i stawki obniżone wg kategorii. Bez wgrywania, bez śledzenia, bez rejestracji.",
        },
        "ja": {
            "name": "付加価値税 (VAT) 計算機",
            "tagline": "EU 各国、英国、スイスなどの VAT を 2025 年の最新税率で計算 — 多くのツールが反映していない改正済みの税率に対応。標準・軽減・ゼロ税率対応。",
            "description": "無料の VAT 計算機。30 か国以上の最新税率を内蔵。国を選び、カテゴリ（標準、軽減、ゼロ）を選び、税抜または税込で金額を入力すると内訳を表示します。直近の改正（スロバキア 20%→23%、エストニア 22%→24% など）と国別の軽減税率に対応。アップロードなし、追跡なし、登録不要。",
        },
        "nl": {
            "name": "BTW-calculator",
            "tagline": "Bereken BTW voor elk EU-land, het VK, Zwitserland en meer — met actuele 2025-tarieven inclusief hervormingen die veel tools missen. Standaard, verlaagd en nul.",
            "description": "Gratis BTW-calculator met up-to-date tarieven voor 30+ landen. Kies een land, kies een categorie (standaard, verlaagd, nul), voer netto of bruto in — zie de uitsplitsing. Met recente wijzigingen (Slowakije 20%→23% in 2025, Estland 22%→24%, enz.) en verlaagde tarieven per categorie. Geen upload, geen tracking, geen registratie.",
        },
        "tr": {
            "name": "KDV Hesaplayıcı",
            "tagline": "Tüm AB ülkeleri, Birleşik Krallık, İsviçre ve daha fazlası için KDV hesapla — 2025'in güncel oranlarıyla, çoğu aracın atladığı reform sonrası güncellemeler dahil. Standart, indirimli ve sıfır.",
            "description": "30+ ülke için güncel oranlarla ücretsiz KDV hesaplayıcı. Ülke seç, kategori seç (standart, indirimli, sıfır), net veya brüt gir — dökümü gör. Son değişiklikleri (Slovakya 20%→23% 2025'te, Estonya 22%→24% vb.) ve kategori bazlı indirimli oranları içerir. Yükleme yok, takip yok, kayıt yok.",
        },
        "id": {
            "name": "Kalkulator PPN (VAT)",
            "tagline": "Hitung PPN untuk negara UE mana pun, UK, Swiss, dan lainnya — dengan tarif 2025 terbaru termasuk pembaruan pasca-reformasi yang sering terlewat tool lain. Standar, dikurangi, dan nol.",
            "description": "Kalkulator PPN gratis dengan tarif terkini untuk 30+ negara. Pilih negara, pilih kategori (standar, dikurangi, nol), masukkan netto atau bruto — lihat rinciannya. Termasuk perubahan terbaru (Slovakia 20%→23% di 2025, Estonia 22%→24%, dll.) dan tarif dikurangi per kategori. Tanpa upload, tanpa tracking, tanpa daftar.",
        },
        "vi": {
            "name": "Máy tính VAT",
            "tagline": "Tính VAT cho mọi nước EU, Anh, Thụy Sĩ và hơn nữa — với mức thuế 2025 hiện hành, bao gồm cải cách mà nhiều công cụ bỏ sót. Mức chuẩn, giảm, và bằng 0.",
            "description": "Máy tính VAT miễn phí với mức thuế cập nhật cho hơn 30 quốc gia. Chọn nước, chọn loại (chuẩn, giảm, 0), nhập net hoặc gross — xem phân tích. Bao gồm thay đổi gần đây (Slovakia 20%→23% trong 2025, Estonia 22%→24%, v.v.) và mức giảm theo loại. Không upload, không tracking, không đăng ký.",
        },
        "hi": {
            "name": "VAT Calculator",
            "tagline": "किसी भी EU देश, UK, Switzerland और अधिक के लिए VAT calculate करें — 2025 की ताज़ा rates के साथ जो कई tools नहीं रखते। Standard, reduced और zero rates।",
            "description": "मुफ़्त ऑनलाइन VAT calculator जिसमें 30+ देशों की up-to-date rates हैं। देश चुनें, category (standard, reduced, zero) चुनें, net या gross डालें — breakdown देखें। हाल के बदलाव शामिल हैं (Slovakia 20%→23% 2025 में, Estonia 22%→24% आदि) और category-wise reduced rates। कोई upload नहीं, कोई tracking नहीं, signup नहीं।",
        },
        "sk": {
            "name": "Kalkulačka DPH",
            "tagline": "Vyrátaj DPH pre ľubovoľnú krajinu EÚ, Veľkú Britániu, Švajčiarsko a ďalšie — s aktuálnymi sadzbami pre rok 2025 vrátane zmien po reforme, ktoré mnohé online kalkulačky stále nemajú. Slovensko zvýšilo základnú sadzbu z 20 % na 23 % od 1. 1. 2025.",
            "description": "Bezplatná online kalkulačka DPH s aktuálnymi sadzbami pre 30+ krajín. Vyber si krajinu, vyber kategóriu (základná, znížená, nulová), zadaj netto alebo brutto — uvidíš rozpis. Zahŕňa najnovšie zmeny — Slovensko z 20 % na 23 % od 1. 1. 2025, znížené sadzby 19 % a 5 %, Česko zjednotené 12 %, Estónsko 22 % → 24 % od 1. 7. 2025, Fínsko 24 % → 25,5 %, Švajčiarsko 7,7 % → 8,1 % a ďalšie. Žiadne nahrávanie, žiadne sledovanie, žiadna registrácia.",
        },
        "cs": {
            "name": "Kalkulačka DPH",
            "tagline": "Spočítej DPH pro jakoukoli zemi EU, Spojené království, Švýcarsko a další — s aktuálními sazbami pro rok 2025, včetně reforem, které mnoho online kalkulaček stále nemá. Česko sjednotilo sníženou sazbu z 15 % + 10 % na 12 % od 1. 1. 2024.",
            "description": "Zdarma online kalkulačka DPH s aktuálními sazbami pro 30+ zemí. Vyber si zemi, vyber kategorii (základní, snížená, nulová), zadej netto nebo brutto — uvidíš rozpis. Zahrnuje nejnovější změny — Česko sjednocená snížená sazba 12 % od 1. 1. 2024, Slovensko z 20 % na 23 % od 1. 1. 2025, Estonsko 22 % → 24 % od 1. 7. 2025, Finsko 24 % → 25,5 %, Švýcarsko 7,7 % → 8,1 % a další. Žádné nahrávání, žádné sledování, žádná registrace.",
        },
    },
    "body": """
<div class="tool-card">
  <label for="vat-country">Country</label>
  <select id="vat-country" onchange="vatPopulate()" style="font-size:1rem;padding:0.6rem"></select>
</div>
<div class="tool-card">
  <label for="vat-rate">Rate category</label>
  <select id="vat-rate" onchange="vatRun()" style="font-size:1rem;padding:0.6rem"></select>
  <div class="meta" id="vat-rate-notes" style="margin-top:0.4rem;color:var(--text-muted);font-size:0.85rem"></div>
</div>
<div class="tool-card">
  <label for="vat-amount">Amount</label>
  <input type="number" id="vat-amount" step="0.01" min="0" value="100" oninput="vatRun()" style="font-size:1.1rem;padding:0.6rem">
  <div style="margin-top:0.7rem;display:flex;gap:1rem;flex-wrap:wrap">
    <label style="display:inline-flex;gap:0.4rem;align-items:center"><input type="radio" name="vat-mode" value="net" onchange="vatRun()" style="width:auto"> {LBL_NET}</label>
    <label style="display:inline-flex;gap:0.4rem;align-items:center"><input type="radio" name="vat-mode" value="gross" checked onchange="vatRun()" style="width:auto"> {LBL_GROSS}</label>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="vat-out" class="output"></div>
</div>
<div class="meta" id="vat-meta" style="text-align:center;color:var(--text-muted);font-size:0.8rem;margin-top:0.8rem"></div>
""",
    "script": """
<style>
.vat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:0.6rem;margin-bottom:0.4rem}
.vat-stat{background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;padding:0.7rem 0.85rem}
.vat-stat .vat-num{font-family:ui-monospace,monospace;font-size:1.25rem;font-weight:600;color:var(--accent)}
.vat-stat .vat-lbl{font-size:0.78rem;color:var(--text-muted);margin-top:0.15rem}
.vat-stat.vat-vat{border-color:var(--accent)}
</style>
<script>
const VAT_DATA = __VAT_DATA__;
function vatFmt(n, currency){
  if(!isFinite(n)) return '—';
  return currency + ' ' + n.toFixed(2);
}
function vatInit(){
  const c = document.getElementById('vat-country');
  const codes = Object.keys(VAT_DATA.countries).sort(function(a,b){
    return VAT_DATA.countries[a].name.localeCompare(VAT_DATA.countries[b].name);
  });
  codes.forEach(function(code){
    const info = VAT_DATA.countries[code];
    const opt = document.createElement('option');
    opt.value = code;
    opt.textContent = info.name + ' (' + code + ')';
    if(code === 'SK') opt.selected = true;
    c.appendChild(opt);
  });
  vatPopulate();
}
function vatPopulate(){
  const code = document.getElementById('vat-country').value;
  const r = document.getElementById('vat-rate');
  r.innerHTML = '';
  VAT_DATA.countries[code].rates.forEach(function(rate, i){
    const opt = document.createElement('option');
    opt.value = i;
    opt.textContent = rate.label + ' — ' + rate.rate + '%';
    r.appendChild(opt);
  });
  vatRun();
}
function vatRun(){
  const code = document.getElementById('vat-country').value;
  const idx = parseInt(document.getElementById('vat-rate').value, 10) || 0;
  const country = VAT_DATA.countries[code];
  const rate = country.rates[idx];
  const amount = parseFloat(document.getElementById('vat-amount').value);
  const modeEl = document.querySelector('input[name="vat-mode"]:checked');
  const mode = modeEl ? modeEl.value : 'gross';
  const currency = country.currency;
  const out = document.getElementById('vat-out');
  if(!isFinite(amount) || amount < 0){
    out.textContent = '{LBL_NO_INPUT}';
  } else {
    const r = rate.rate / 100;
    let net, vat, gross;
    if(mode === 'net'){
      net = amount; vat = amount * r; gross = amount + vat;
    } else {
      gross = amount; net = (1 + r) === 0 ? amount : amount / (1 + r); vat = gross - net;
    }
    out.innerHTML =
      '<div class="vat-grid">' +
      '<div class="vat-stat"><div class="vat-num">' + vatFmt(net, currency) + '</div><div class="vat-lbl">{LBL_NET}</div></div>' +
      '<div class="vat-stat vat-vat"><div class="vat-num">' + vatFmt(vat, currency) + '</div><div class="vat-lbl">VAT @ ' + rate.rate + '%</div></div>' +
      '<div class="vat-stat"><div class="vat-num">' + vatFmt(gross, currency) + '</div><div class="vat-lbl">{LBL_GROSS}</div></div>' +
      '</div>';
  }
  document.getElementById('vat-rate-notes').textContent = rate.notes || '';
  document.getElementById('vat-meta').textContent =
    'Rates as of ' + VAT_DATA._meta.last_updated + '. ' + VAT_DATA._meta.disclaimer;
}
document.addEventListener('DOMContentLoaded', vatInit);
</script>
""".replace("__VAT_DATA__", _VAT_DATA_JS),
    "help": {
        "en": """
<h2>What is VAT and how does it work?</h2>
<p>Value-Added Tax (VAT) is a consumption tax applied at each step of the supply chain on the <em>value added</em> at that step. Businesses charge VAT on sales (output VAT), reclaim VAT on purchases (input VAT), and remit the difference to the tax authority. To the end consumer it looks like a sales tax built into the price; to a business it's effectively a flow-through unless they make exempt supplies.</p>

<p>Two numbers matter for any line on an invoice:</p>
<ul>
  <li><strong>Net</strong> — the price before VAT (what the business books as revenue).</li>
  <li><strong>Gross</strong> — the price including VAT (what the customer actually pays).</li>
</ul>
<p>If your input is the gross figure (a price tag, a card receipt), the calculator backs out the VAT: <code>net = gross / (1 + rate)</code>. If your input is the net figure (a B2B quote), it adds the VAT on top: <code>vat = net × rate</code>.</p>

<h2>When to use this vs. your accounting software</h2>
<p>This is a quick-check calculator, not bookkeeping. Use it to:</p>
<ul>
  <li>Sanity-check an invoice line before sending it.</li>
  <li>Convert a customer-facing price into a net figure for margin maths.</li>
  <li>Compare prices across countries with different rates.</li>
  <li>Confirm what a recent rate change actually does to your typical sale.</li>
</ul>
<p>Don't use it for:</p>
<ul>
  <li>Filing a return — your accounting software handles cumulative input/output VAT, partial exemption, MOSS/OSS, and bad-debt relief.</li>
  <li>Legal advice — categorisation (which rate applies to your specific service) is the part that gets businesses fined, and that's a question for your accountant or the local tax authority's published guidance.</li>
</ul>

<h2>About the rate dataset</h2>
<p>The rates in this calculator are hand-curated as of the date shown beneath the result, drawn from each country's tax authority. The differentiator vs. the bulk of online VAT calculators is that this dataset reflects post-reform 2025 rates — for example:</p>
<ul>
  <li><strong>Slovakia</strong>: standard rate raised from 20% to 23% on 2025-01-01.</li>
  <li><strong>Czech Republic</strong>: previous 15% and 10% reduced tiers consolidated to a single 12% rate on 2024-01-01.</li>
  <li><strong>Estonia</strong>: standard rate raised to 24% on 2025-07-01.</li>
  <li><strong>Finland</strong>: standard rate raised from 24% to 25.5% on 2024-09-01.</li>
  <li><strong>Switzerland</strong>: standard rate raised from 7.7% to 8.1% on 2024-01-01.</li>
  <li><strong>Singapore</strong>: GST raised from 8% to 9% on 2024-01-01.</li>
</ul>
<p>Reduced categories vary widely — there is no EU-wide list of "what counts as a book" or "what counts as a restaurant service". The notes under each rate are a hint, not a ruling. Always check your tax authority's guidance for your specific supply.</p>

<h2>Common gotchas</h2>
<ul>
  <li><strong>Net + VAT ≠ gross when you start from gross.</strong> Subtracting a percentage from a gross figure gives a different number than dividing by (1 + rate). 100 with 23% VAT included = 81.30 net, not 77.00.</li>
  <li><strong>Reverse-charge invoices.</strong> Cross-border B2B supplies inside the EU often shift the VAT to the buyer. Your invoice shows 0% VAT but the supply isn't zero-rated — the buyer self-accounts.</li>
  <li><strong>Distance-sale thresholds.</strong> Selling B2C across EU borders triggers the OSS scheme above €10k/year — you charge the buyer's country's rate, not yours.</li>
  <li><strong>VAT-registered ≠ VAT-charging.</strong> Many small freelancers in Slovakia, Czech Republic and elsewhere fall under the registration threshold and don't charge VAT at all.</li>
  <li><strong>Rounding rules differ.</strong> Most authorities accept either per-line or per-invoice rounding to the nearest cent, but consistency matters. Don't mix the two on one invoice.</li>
</ul>
""",
        "de": """
<h2>Was ist die Mehrwertsteuer und wie funktioniert sie?</h2>
<p>Die Mehrwertsteuer (MwSt., Umsatzsteuer) ist eine Verbrauchssteuer, die auf jeder Stufe der Lieferkette auf den <em>Mehrwert</em> erhoben wird. Unternehmen erheben MwSt. auf Verkäufe (Ausgangs-USt.), ziehen die MwSt. aus Eingangsrechnungen ab (Vorsteuer) und zahlen die Differenz ans Finanzamt.</p>

<p>Zwei Zahlen pro Rechnungszeile zählen:</p>
<ul>
  <li><strong>Netto</strong> — Preis vor MwSt. (Umsatz).</li>
  <li><strong>Brutto</strong> — Preis inkl. MwSt. (Kundenpreis).</li>
</ul>
<p>Bei Brutto-Eingabe wird die MwSt. herausgerechnet: <code>netto = brutto / (1 + Satz)</code>. Bei Netto-Eingabe wird sie aufgeschlagen: <code>mwst = netto × Satz</code>.</p>

<h2>Wann dieses Tool — und wann das Buchhaltungssystem?</h2>
<p>Schnellprüfung statt Buchhaltung. Geeignet für:</p>
<ul>
  <li>Plausibilitätskontrolle einer Rechnungszeile vor dem Versand.</li>
  <li>Umrechnung eines Endkundenpreises in den Nettowert für Margenrechnungen.</li>
  <li>Preisvergleich über Länder mit unterschiedlichen Sätzen hinweg.</li>
  <li>Prüfen, wie sich eine aktuelle Reform tatsächlich auf den eigenen Standardumsatz auswirkt.</li>
</ul>
<p>Nicht geeignet für: USt.-Voranmeldungen, OSS/MOSS, anteiligen Vorsteuerabzug oder rechtliche Einordnung der korrekten Kategorie — das gehört in die Buchhaltungssoftware bzw. zum Steuerberater.</p>

<h2>Zur Datenbasis</h2>
<p>Die Sätze stammen aus den offiziellen Veröffentlichungen der jeweiligen Steuerbehörden, Stand wie unter dem Ergebnis angezeigt. Anders als die meisten Online-Rechner berücksichtigt das Tool auch Reformen aus 2024 / 2025:</p>
<ul>
  <li><strong>Slowakei</strong>: Regelsatz von 20 % auf 23 % zum 1. 1. 2025.</li>
  <li><strong>Tschechien</strong>: ermäßigte Sätze 15 % und 10 % auf einheitlich 12 % zum 1. 1. 2024 zusammengelegt.</li>
  <li><strong>Estland</strong>: Regelsatz auf 24 % zum 1. 7. 2025.</li>
  <li><strong>Finnland</strong>: Regelsatz von 24 % auf 25,5 % zum 1. 9. 2024.</li>
  <li><strong>Schweiz</strong>: Regelsatz von 7,7 % auf 8,1 % zum 1. 1. 2024.</li>
</ul>
<p>Ob eine konkrete Leistung in einen ermäßigten Satz fällt, regelt das nationale Recht — die Notizen sind ein Hinweis, keine Auskunft.</p>

<h2>Häufige Stolperfallen</h2>
<ul>
  <li><strong>Brutto minus % ≠ Netto.</strong> 100 brutto mit 23 % MwSt. ergibt 81,30 netto, nicht 77,00.</li>
  <li><strong>Reverse-Charge</strong> verschiebt die Steuerschuld bei B2B-EU-Leistungen oft auf den Empfänger.</li>
  <li><strong>OSS-Schwelle (10 000 € p. a.)</strong> für B2C-Lieferungen ins EU-Ausland — danach gilt der Satz des Bestimmungslandes.</li>
  <li><strong>Kleinunternehmer</strong> liegen unter der Registrierungsgrenze und weisen keine MwSt. aus.</li>
  <li><strong>Rundungsregeln</strong> unterscheiden zwischen Posten- und Belegrundung — innerhalb einer Rechnung konsistent bleiben.</li>
</ul>
""",
        "es": """
<h2>¿Qué es el IVA y cómo funciona?</h2>
<p>El IVA (Impuesto sobre el Valor Añadido) es un impuesto al consumo que grava cada eslabón de la cadena de suministro sobre el <em>valor añadido</em>. Las empresas repercuten IVA en sus ventas, deducen el IVA soportado en sus compras y liquidan la diferencia con Hacienda.</p>

<p>Dos cifras por cada línea de factura:</p>
<ul>
  <li><strong>Neto</strong> — precio antes de IVA.</li>
  <li><strong>Bruto</strong> — precio con IVA (lo que paga el cliente).</li>
</ul>
<p>Si tu importe es bruto, la calculadora desagrega el IVA: <code>neto = bruto / (1 + tipo)</code>. Si es neto, lo añade: <code>iva = neto × tipo</code>.</p>

<h2>Cuándo usar esto vs. tu software contable</h2>
<p>Es una calculadora de comprobación rápida, no contabilidad. Útil para:</p>
<ul>
  <li>Verificar una línea de factura antes de enviarla.</li>
  <li>Convertir un precio de venta a neto para hacer cuentas de margen.</li>
  <li>Comparar precios entre países con tipos distintos.</li>
  <li>Calcular el impacto real de una reforma reciente sobre tu venta típica.</li>
</ul>
<p>No sirve para: declaraciones, OSS/MOSS, prorrata o calificación legal de la operación. Eso es asesoría fiscal.</p>

<h2>Sobre los tipos</h2>
<p>Los tipos están curados a mano según la fecha indicada bajo el resultado, basados en publicaciones oficiales. Incluye reformas 2024 / 2025 que muchas calculadoras online no han incorporado:</p>
<ul>
  <li><strong>Eslovaquia</strong>: tipo general de 20% a 23% el 2025-01-01.</li>
  <li><strong>Chequia</strong>: tipos reducidos 15% y 10% consolidados a 12% el 2024-01-01.</li>
  <li><strong>Estonia</strong>: tipo general a 24% el 2025-07-01.</li>
  <li><strong>Finlandia</strong>: tipo general a 25,5% el 2024-09-01.</li>
  <li><strong>Suiza</strong>: tipo general a 8,1% el 2024-01-01.</li>
</ul>
<p>Las categorías reducidas varían: las notas son una pista, no un dictamen.</p>

<h2>Errores frecuentes</h2>
<ul>
  <li><strong>Restar % al bruto ≠ neto.</strong> 100 bruto con 21% sale 82,64 neto, no 79,00.</li>
  <li><strong>Inversión del sujeto pasivo</strong>: en B2B intracomunitario el destinatario suele autorrepercutirse el IVA.</li>
  <li><strong>Umbral OSS</strong> de 10 000 € anuales en B2C transfronterizo dentro de la UE.</li>
  <li><strong>Estar dado de alta no significa repercutir IVA.</strong> Hay regímenes especiales y exenciones.</li>
  <li><strong>Redondeo por línea vs. por factura</strong>: mantener la consistencia dentro del documento.</li>
</ul>
""",
        "fr": """
<h2>Qu'est-ce que la TVA et comment ça marche ?</h2>
<p>La TVA (Taxe sur la Valeur Ajoutée) est un impôt sur la consommation appliqué à chaque étape de la chaîne d'approvisionnement sur la <em>valeur ajoutée</em>. Les entreprises facturent la TVA sur leurs ventes, déduisent la TVA sur leurs achats et reversent la différence au Trésor.</p>

<p>Deux chiffres par ligne de facture :</p>
<ul>
  <li><strong>HT</strong> — prix hors taxes.</li>
  <li><strong>TTC</strong> — prix toutes taxes comprises (ce que paie le client).</li>
</ul>
<p>Si vous saisissez le TTC, la calculatrice extrait la TVA : <code>HT = TTC / (1 + taux)</code>. Si vous saisissez le HT, elle l'ajoute : <code>TVA = HT × taux</code>.</p>

<h2>Quand l'utiliser plutôt que votre logiciel comptable</h2>
<p>Vérification rapide, pas comptabilité. Bon pour :</p>
<ul>
  <li>Contrôler une ligne de facture avant envoi.</li>
  <li>Convertir un prix client en HT pour le calcul de marge.</li>
  <li>Comparer des prix entre pays à taux différents.</li>
  <li>Vérifier l'impact d'une réforme récente sur votre vente courante.</li>
</ul>
<p>Pas adapté pour : déclaration CA3, OSS/MOSS, prorata, ou qualification juridique de l'opération. C'est le rôle de l'expert-comptable.</p>

<h2>À propos des taux</h2>
<p>Taux compilés à la main d'après les publications officielles, à la date affichée sous le résultat. Inclut les réformes 2024 / 2025 que beaucoup d'outils en ligne n'ont pas encore intégrées :</p>
<ul>
  <li><strong>Slovaquie</strong> : taux normal de 20 % à 23 % au 1.1.2025.</li>
  <li><strong>République tchèque</strong> : taux réduits 15 % et 10 % fusionnés en 12 % au 1.1.2024.</li>
  <li><strong>Estonie</strong> : taux normal à 24 % au 1.7.2025.</li>
  <li><strong>Finlande</strong> : taux normal à 25,5 % au 1.9.2024.</li>
  <li><strong>Suisse</strong> : taux normal à 8,1 % au 1.1.2024.</li>
</ul>
<p>L'éligibilité aux taux réduits varie par pays — les notes sont indicatives.</p>

<h2>Pièges courants</h2>
<ul>
  <li><strong>Soustraire un % du TTC ≠ HT.</strong> 100 TTC avec TVA 20 % donne 83,33 HT, pas 80,00.</li>
  <li><strong>Autoliquidation</strong> sur les opérations B2B intra-UE.</li>
  <li><strong>Seuil OSS</strong> à 10 000 € / an pour le B2C transfrontalier dans l'UE.</li>
  <li><strong>Franchise en base de TVA</strong> : sous le seuil, la TVA n'est ni facturée ni déduite.</li>
  <li><strong>Arrondi par ligne / par facture</strong> : rester cohérent dans le même document.</li>
</ul>
""",
        "it": """
<h2>Cos'è l'IVA e come funziona?</h2>
<p>L'IVA è un'imposta sui consumi applicata a ogni passaggio della catena di fornitura sul <em>valore aggiunto</em>. Le imprese addebitano IVA sulle vendite (IVA a debito), detraggono l'IVA sugli acquisti (IVA a credito) e versano la differenza all'erario.</p>

<p>Due numeri per ogni riga di fattura:</p>
<ul>
  <li><strong>Imponibile (netto)</strong> — prezzo prima dell'IVA.</li>
  <li><strong>Totale (lordo)</strong> — prezzo IVA inclusa.</li>
</ul>
<p>Se inserisci il lordo, il calcolatore scorpora l'IVA: <code>netto = lordo / (1 + aliquota)</code>. Se inserisci il netto, la aggiunge: <code>iva = netto × aliquota</code>.</p>

<h2>Quando usarlo vs. il gestionale</h2>
<p>Verifica rapida, non contabilità. Utile per:</p>
<ul>
  <li>Controllare una riga di fattura prima dell'invio.</li>
  <li>Convertire un prezzo al pubblico in imponibile per i conti di margine.</li>
  <li>Confrontare prezzi tra paesi con aliquote diverse.</li>
  <li>Capire l'effetto reale di una riforma recente su una vendita tipica.</li>
</ul>
<p>Non sostituisce la dichiarazione, l'OSS/MOSS, il pro-rata o l'inquadramento dell'operazione: per quelli serve il commercialista.</p>

<h2>Sui dati</h2>
<p>Aliquote compilate a mano dalle pubblicazioni ufficiali alla data indicata sotto il risultato. Sono incluse riforme 2024 / 2025 che molti calcolatori online non hanno ancora aggiornato:</p>
<ul>
  <li><strong>Slovacchia</strong>: ordinaria da 20% a 23% dal 1° gennaio 2025.</li>
  <li><strong>Repubblica Ceca</strong>: ridotte 15% e 10% unificate al 12% dal 1° gennaio 2024.</li>
  <li><strong>Estonia</strong>: ordinaria al 24% dal 1° luglio 2025.</li>
  <li><strong>Finlandia</strong>: ordinaria al 25,5% dal 1° settembre 2024.</li>
  <li><strong>Svizzera</strong>: ordinaria all'8,1% dal 1° gennaio 2024.</li>
</ul>
<p>Le aliquote ridotte applicabili variano per paese — le note sono indicative.</p>

<h2>Trappole frequenti</h2>
<ul>
  <li><strong>Sottrarre la % al lordo ≠ netto.</strong> 100 lordi al 22% danno 81,97 netti, non 78.</li>
  <li><strong>Reverse charge</strong> nelle operazioni B2B intra-UE.</li>
  <li><strong>Soglia OSS</strong> a 10 000 € annui per le vendite B2C transfrontaliere intra-UE.</li>
  <li><strong>Regime forfettario</strong>: sotto soglia non si addebita IVA.</li>
  <li><strong>Arrotondamento per riga / per fattura</strong>: coerenza all'interno dello stesso documento.</li>
</ul>
""",
        "pt": """
<h2>O que é IVA e como funciona?</h2>
<p>O IVA (Imposto sobre o Valor Acrescentado) é um imposto sobre o consumo aplicado em cada etapa da cadeia de fornecimento sobre o <em>valor acrescentado</em>. As empresas cobram IVA nas vendas (IVA liquidado), deduzem o IVA das compras (IVA dedutível) e entregam a diferença à autoridade fiscal.</p>

<p>Duas cifras por linha de fatura:</p>
<ul>
  <li><strong>Líquido (sem IVA)</strong> — preço antes do IVA.</li>
  <li><strong>Bruto (com IVA)</strong> — preço que o cliente paga.</li>
</ul>
<p>Se inserir o valor bruto, a calculadora extrai o IVA: <code>líquido = bruto / (1 + taxa)</code>. Se inserir o líquido, soma o IVA: <code>iva = líquido × taxa</code>.</p>

<h2>Quando usar isto vs. o software de contabilidade</h2>
<p>Verificação rápida, não contabilidade. Útil para:</p>
<ul>
  <li>Conferir uma linha de fatura antes de enviar.</li>
  <li>Converter um preço ao público em valor líquido para cálculos de margem.</li>
  <li>Comparar preços entre países com taxas diferentes.</li>
  <li>Ver o impacto real de uma reforma recente sobre a sua venda típica.</li>
</ul>
<p>Não substitui a declaração periódica, OSS/MOSS, pro-rata ou enquadramento legal da operação — isso é trabalho do contabilista.</p>

<h2>Sobre os dados</h2>
<p>Taxas compiladas à mão a partir de publicações oficiais, na data indicada sob o resultado. Inclui reformas 2024 / 2025 que muitas calculadoras online ainda não refletem:</p>
<ul>
  <li><strong>Eslováquia</strong>: taxa normal de 20% para 23% em 2025-01-01.</li>
  <li><strong>República Checa</strong>: taxas reduzidas 15% e 10% unificadas em 12% em 2024-01-01.</li>
  <li><strong>Estónia</strong>: taxa normal para 24% em 2025-07-01.</li>
  <li><strong>Finlândia</strong>: taxa normal para 25,5% em 2024-09-01.</li>
  <li><strong>Suíça</strong>: taxa normal para 8,1% em 2024-01-01.</li>
</ul>
<p>A elegibilidade de taxas reduzidas varia por país — as notas são indicativas.</p>

<h2>Erros frequentes</h2>
<ul>
  <li><strong>Subtrair % ao bruto ≠ líquido.</strong> 100 com IVA 23% inclui dá 81,30 líquido, não 77,00.</li>
  <li><strong>Reverse-charge</strong> em B2B intra-UE.</li>
  <li><strong>Limiar OSS</strong> de €10 000 anuais para vendas B2C transfronteiriças na UE.</li>
  <li><strong>Estar registado em IVA</strong> ≠ liquidar IVA: há regimes especiais.</li>
  <li><strong>Arredondamento por linha / por fatura</strong>: manter coerência no mesmo documento.</li>
</ul>
""",
        "pl": """
<h2>Co to jest VAT i jak działa?</h2>
<p>VAT (podatek od wartości dodanej) to podatek konsumpcyjny naliczany na każdym etapie łańcucha dostaw od <em>wartości dodanej</em>. Firmy doliczają VAT do sprzedaży (VAT należny), odliczają VAT z zakupów (VAT naliczony) i wpłacają różnicę do US.</p>

<p>Dwie liczby na linię faktury:</p>
<ul>
  <li><strong>Netto</strong> — cena bez VAT.</li>
  <li><strong>Brutto</strong> — cena z VAT (to, co płaci klient).</li>
</ul>
<p>Jeśli wpisujesz brutto, kalkulator wylicza VAT: <code>netto = brutto / (1 + stawka)</code>. Jeśli netto — dodaje VAT: <code>vat = netto × stawka</code>.</p>

<h2>Kiedy używać tego, a kiedy księgowości</h2>
<p>To szybki check, nie księgowość. Dobre do:</p>
<ul>
  <li>Sprawdzenia pozycji faktury przed wysłaniem.</li>
  <li>Przeliczenia ceny detalicznej na netto do marży.</li>
  <li>Porównania cen między krajami z różnymi stawkami.</li>
  <li>Sprawdzenia, jak ostatnia reforma wpływa na typową sprzedaż.</li>
</ul>
<p>Nie nadaje się do: JPK / deklaracji, OSS/MOSS, struktury sprzedaży zwolnionej, ani kwalifikacji prawnej operacji — to robota dla księgowej / księgowego.</p>

<h2>O danych</h2>
<p>Stawki ręcznie zebrane z publikacji urzędów skarbowych, na datę pokazaną pod wynikiem. Uwzględnia reformy 2024 / 2025, których wiele kalkulatorów online jeszcze nie ma:</p>
<ul>
  <li><strong>Słowacja</strong>: stawka podstawowa z 20% na 23% od 2025-01-01.</li>
  <li><strong>Czechy</strong>: obniżone 15% i 10% zjednoczone w 12% od 2024-01-01.</li>
  <li><strong>Estonia</strong>: podstawowa do 24% od 2025-07-01.</li>
  <li><strong>Finlandia</strong>: podstawowa do 25,5% od 2024-09-01.</li>
  <li><strong>Szwajcaria</strong>: podstawowa do 8,1% od 2024-01-01.</li>
</ul>
<p>Stawki obniżone różnią się — notatki są wskazówką, nie interpretacją.</p>

<h2>Częste pułapki</h2>
<ul>
  <li><strong>Odjąć % od brutto ≠ netto.</strong> 100 brutto z VAT 23% to 81,30 netto, nie 77,00.</li>
  <li><strong>Odwrotne obciążenie</strong> przy B2B wewnątrz UE.</li>
  <li><strong>Próg OSS</strong> 10 000 € rocznie dla sprzedaży B2C między krajami UE.</li>
  <li><strong>Zwolnienie podmiotowe</strong> w PL: poniżej 200 000 zł obrotu w roku można nie być vat-owcem.</li>
  <li><strong>Zaokrąglanie linii vs. faktury</strong> — zachować spójność w jednym dokumencie.</li>
</ul>
""",
        "ja": """
<h2>VAT（付加価値税）とは</h2>
<p>VAT は流通の各段階で「付加された価値」に対して課される消費課税です。事業者は売上に VAT を上乗せして請求（仮受 VAT）、仕入の VAT を控除（仮払 VAT）し、その差額を税務当局に納付します。エンドユーザーから見ると価格に含まれる消費税のように見え、事業者にとっては実質的にパススルー（免税取引がなければ）です。</p>

<p>請求書 1 行につき重要な数字は 2 つ：</p>
<ul>
  <li><strong>税抜（Net）</strong> — VAT 前の価格（事業者の売上として計上）。</li>
  <li><strong>税込（Gross）</strong> — VAT を含む価格（顧客が支払う額）。</li>
</ul>
<p>税込から税抜を逆算する場合：<code>net = gross / (1 + 税率)</code>。税抜に VAT を上乗せする場合：<code>vat = net × 税率</code>。</p>

<h2>会計ソフトとの使い分け</h2>
<p>本ツールは確認用の電卓であって、帳簿付けではありません。次のような用途に向いています：</p>
<ul>
  <li>請求書 1 行の送信前のサニティチェック。</li>
  <li>顧客向け価格から粗利計算のための税抜価格への変換。</li>
  <li>税率が異なる国同士の価格比較。</li>
  <li>直近の税率改正が自社の代表的な取引に与える影響の確認。</li>
</ul>
<p>申告、OSS/MOSS、按分、適用税率の最終判断は会計ソフトと税理士の領域です。</p>

<h2>税率データについて</h2>
<p>各国の税務当局の公式情報を元に、結果欄に示された日付で手作業で整備しています。多くのオンライン計算機が未反映の 2024 / 2025 年の改正にも対応：</p>
<ul>
  <li><strong>スロバキア</strong>：標準税率を 20% → 23% に引き上げ（2025-01-01）。</li>
  <li><strong>チェコ</strong>：軽減税率 15% と 10% を 12% に統合（2024-01-01）。</li>
  <li><strong>エストニア</strong>：標準税率を 24% に引き上げ（2025-07-01）。</li>
  <li><strong>フィンランド</strong>：標準税率を 24% → 25.5% に引き上げ（2024-09-01）。</li>
  <li><strong>スイス</strong>：標準税率を 7.7% → 8.1% に引き上げ（2024-01-01）。</li>
</ul>
<p>軽減税率の対象は国ごとに異なります。注記は目安であり、最終的な判定は当局のガイダンスに従ってください。</p>

<h2>よくある落とし穴</h2>
<ul>
  <li><strong>税込から税率を単純に引くと税抜にならない。</strong> 100 税込（23%）は 81.30 税抜であって 77 ではありません。</li>
  <li><strong>リバースチャージ</strong> 国境を越える EU 域内 B2B では買い手側に納税義務が移ることがあります。</li>
  <li><strong>OSS の年 1 万ユーロ閾値</strong> を超えると、B2C 越境販売には買い手国の税率が適用されます。</li>
  <li><strong>VAT 登録 ≠ 必ず VAT を課す。</strong> 登録閾値以下の事業者は課税しない場合があります。</li>
  <li><strong>丸めのルール</strong> 行単位／請求書単位どちらかに統一して、同一請求書内では混在させないこと。</li>
</ul>
""",
        "nl": """
<h2>Wat is BTW en hoe werkt het?</h2>
<p>BTW (Belasting Toegevoegde Waarde) is een verbruiksbelasting die op elke schakel van de keten wordt geheven over de <em>toegevoegde waarde</em>. Bedrijven rekenen BTW op verkoop (af te dragen), trekken BTW op inkoop af (voorbelasting) en dragen het verschil af aan de Belastingdienst.</p>

<p>Twee getallen per factuurregel:</p>
<ul>
  <li><strong>Netto</strong> — prijs exclusief BTW.</li>
  <li><strong>Bruto</strong> — prijs inclusief BTW (wat de klant betaalt).</li>
</ul>
<p>Vul je bruto in, dan rekent de calculator BTW eruit: <code>netto = bruto / (1 + tarief)</code>. Vul je netto in, dan komt BTW erbij: <code>btw = netto × tarief</code>.</p>

<h2>Wanneer dit gebruiken vs. je boekhoudpakket</h2>
<p>Snelle controle, geen boekhouding. Geschikt voor:</p>
<ul>
  <li>Een regel op een factuur checken voor je verstuurt.</li>
  <li>Een consumentenprijs naar netto rekenen voor marge.</li>
  <li>Prijzen vergelijken tussen landen met verschillende tarieven.</li>
  <li>De werkelijke impact van een recente tarief-wijziging op je standaardomzet zien.</li>
</ul>
<p>Niet voor aangiftes, OSS/MOSS, pro rata of de juridische kwalificatie van de prestatie — dat is werk voor je accountant.</p>

<h2>Over de tarieven</h2>
<p>Handmatig samengesteld uit officiële publicaties, op de datum onder het resultaat. Bevat hervormingen 2024 / 2025 die veel online tools nog niet hebben:</p>
<ul>
  <li><strong>Slowakije</strong>: standaardtarief van 20% naar 23% op 2025-01-01.</li>
  <li><strong>Tsjechië</strong>: verlaagde 15% en 10% samengevoegd tot 12% op 2024-01-01.</li>
  <li><strong>Estland</strong>: standaardtarief naar 24% op 2025-07-01.</li>
  <li><strong>Finland</strong>: standaardtarief naar 25,5% op 2024-09-01.</li>
  <li><strong>Zwitserland</strong>: standaardtarief naar 8,1% op 2024-01-01.</li>
</ul>
<p>Wat onder een verlaagd tarief valt verschilt per land — de notities zijn een hint, geen oordeel.</p>

<h2>Veelvoorkomende valkuilen</h2>
<ul>
  <li><strong>% aftrekken van bruto ≠ netto.</strong> 100 bruto met 21% BTW geeft 82,64 netto, niet 79.</li>
  <li><strong>Verleggingsregeling</strong> bij grensoverschrijdende B2B binnen de EU.</li>
  <li><strong>OSS-drempel</strong> €10.000 per jaar voor grensoverschrijdende B2C-verkoop binnen de EU.</li>
  <li><strong>Kleine ondernemersregeling (KOR)</strong>: onder de drempel reken je geen BTW.</li>
  <li><strong>Afronding per regel / per factuur</strong>: consistent blijven binnen één document.</li>
</ul>
""",
        "tr": """
<h2>KDV nedir ve nasıl çalışır?</h2>
<p>KDV (Katma Değer Vergisi), tedarik zincirinin her aşamasında <em>katma değer</em> üzerinden alınan bir tüketim vergisidir. İşletmeler satıştan KDV tahsil eder (hesaplanan KDV), alımlardaki KDV'yi indirir (indirilecek KDV) ve farkı vergi idaresine öder.</p>

<p>Bir fatura satırı için iki sayı önemlidir:</p>
<ul>
  <li><strong>Net (KDV hariç)</strong> — KDV öncesi fiyat.</li>
  <li><strong>Brüt (KDV dahil)</strong> — müşterinin ödediği fiyat.</li>
</ul>
<p>Brüt girersen, hesaplayıcı KDV'yi ayrıştırır: <code>net = brüt / (1 + oran)</code>. Net girersen, KDV'yi ekler: <code>kdv = net × oran</code>.</p>

<h2>Bunu mu, muhasebe yazılımını mı?</h2>
<p>Bu hızlı kontrol içindir, defter tutmak için değil. Şunlara iyi gelir:</p>
<ul>
  <li>Bir fatura satırını göndermeden önce mantık kontrolü.</li>
  <li>Müşteri fiyatını marj hesabı için net'e çevirmek.</li>
  <li>Farklı oranlı ülkeler arası fiyat kıyaslaması.</li>
  <li>Yakın bir reformun tipik satışına gerçek etkisini görmek.</li>
</ul>
<p>KDV beyannamesi, OSS/MOSS, kısmi istisna veya işlemin hukuki nitelendirmesi için değil — bunlar mali müşavir işidir.</p>

<h2>Oran verisi hakkında</h2>
<p>Resmi yayınlardan, sonuç altındaki tarihte elle derlenmiştir. Çoğu online aracın atladığı 2024 / 2025 reformlarını içerir:</p>
<ul>
  <li><strong>Slovakya</strong>: standart oran 20% → 23%, 2025-01-01.</li>
  <li><strong>Çek Cumhuriyeti</strong>: indirimli 15% ve 10% birleşip 12%, 2024-01-01.</li>
  <li><strong>Estonya</strong>: standart oran 24%, 2025-07-01.</li>
  <li><strong>Finlandiya</strong>: standart oran 25,5%, 2024-09-01.</li>
  <li><strong>İsviçre</strong>: standart oran 8,1%, 2024-01-01.</li>
</ul>
<p>İndirimli oran kapsamı ülkeye göre değişir — notlar yalnızca ipucudur.</p>

<h2>Sık karşılaşılan tuzaklar</h2>
<ul>
  <li><strong>Brüt'ten % çıkarmak net vermez.</strong> 100 brüt (%20 KDV dahil) net 83,33'tür, 80 değil.</li>
  <li><strong>Tersine yükümlülük (reverse-charge)</strong> AB içi sınır ötesi B2B'de.</li>
  <li><strong>OSS eşiği</strong> AB içi sınır ötesi B2C için yıllık 10 000 €.</li>
  <li><strong>KDV mükellefi olmak ≠ KDV hesaplamak</strong>: özel rejimler ve istisnalar olabilir.</li>
  <li><strong>Satır bazında ya da fatura bazında yuvarlama</strong>: aynı belgede tutarlı kal.</li>
</ul>
""",
        "id": """
<h2>Apa itu PPN/VAT dan bagaimana cara kerjanya?</h2>
<p>PPN (Pajak Pertambahan Nilai) adalah pajak konsumsi yang dikenakan di setiap rantai pasok atas <em>nilai tambah</em>. Pelaku usaha memungut PPN saat menjual (PPN keluaran), mengkreditkan PPN saat membeli (PPN masukan), dan menyetor selisihnya ke otoritas pajak.</p>

<p>Dua angka penting per baris faktur:</p>
<ul>
  <li><strong>Netto</strong> — harga sebelum PPN.</li>
  <li><strong>Bruto</strong> — harga sudah termasuk PPN (yang dibayar pelanggan).</li>
</ul>
<p>Kalau input-mu bruto, kalkulator akan mengeluarkan PPN: <code>netto = bruto / (1 + tarif)</code>. Kalau input-mu netto, akan ditambahkan PPN: <code>ppn = netto × tarif</code>.</p>

<h2>Kapan pakai ini vs. software akuntansi</h2>
<p>Ini kalkulator cek cepat, bukan pembukuan. Berguna untuk:</p>
<ul>
  <li>Memastikan satu baris faktur sebelum dikirim.</li>
  <li>Konversi harga jual ke netto untuk hitung margin.</li>
  <li>Membandingkan harga antar negara dengan tarif beda.</li>
  <li>Melihat dampak nyata reformasi tarif terbaru pada penjualan rutinmu.</li>
</ul>
<p>Bukan untuk SPT, OSS/MOSS, prorata, atau penentuan klasifikasi hukum transaksi — itu ranah konsultan pajak.</p>

<h2>Tentang data tarif</h2>
<p>Tarif dirakit manual dari publikasi otoritas pajak, per tanggal yang muncul di bawah hasil. Mencakup reformasi 2024 / 2025 yang banyak kalkulator online belum perbarui:</p>
<ul>
  <li><strong>Slovakia</strong>: standar dari 20% ke 23% pada 2025-01-01.</li>
  <li><strong>Republik Ceko</strong>: tarif kurang 15% dan 10% disatukan jadi 12% pada 2024-01-01.</li>
  <li><strong>Estonia</strong>: standar ke 24% pada 2025-07-01.</li>
  <li><strong>Finlandia</strong>: standar ke 25,5% pada 2024-09-01.</li>
  <li><strong>Swiss</strong>: standar ke 8,1% pada 2024-01-01.</li>
</ul>
<p>Kategori tarif dikurangi berbeda-beda — catatan hanya petunjuk.</p>

<h2>Kesalahan umum</h2>
<ul>
  <li><strong>Mengurangi % dari bruto ≠ netto.</strong> 100 bruto dengan PPN 11% = 90,09 netto, bukan 89.</li>
  <li><strong>Reverse-charge</strong> di B2B lintas batas Uni Eropa.</li>
  <li><strong>Ambang OSS</strong> €10.000 per tahun untuk B2C lintas batas dalam UE.</li>
  <li><strong>PKP ≠ wajib pungut semua transaksi</strong>: ada regime khusus dan pembebasan.</li>
  <li><strong>Pembulatan per baris atau per faktur</strong>: konsisten dalam satu dokumen.</li>
</ul>
""",
        "vi": """
<h2>VAT là gì và hoạt động như thế nào?</h2>
<p>VAT (Thuế Giá Trị Gia Tăng) là một loại thuế tiêu dùng được áp ở mỗi khâu của chuỗi cung ứng dựa trên <em>giá trị gia tăng</em>. Doanh nghiệp tính VAT khi bán hàng (VAT đầu ra), khấu trừ VAT khi mua (VAT đầu vào), và nộp phần chênh lệch cho cơ quan thuế.</p>

<p>Hai con số trên mỗi dòng hóa đơn:</p>
<ul>
  <li><strong>Net</strong> — giá trước thuế.</li>
  <li><strong>Gross</strong> — giá đã bao gồm VAT (khách hàng trả).</li>
</ul>
<p>Nếu nhập gross, máy tính sẽ tách VAT ra: <code>net = gross / (1 + tỷ lệ)</code>. Nếu nhập net, sẽ cộng VAT vào: <code>vat = net × tỷ lệ</code>.</p>

<h2>Khi nào dùng cái này thay vì phần mềm kế toán</h2>
<p>Đây là máy tính kiểm tra nhanh, không phải sổ sách. Phù hợp để:</p>
<ul>
  <li>Kiểm tra một dòng hóa đơn trước khi gửi.</li>
  <li>Chuyển giá bán cho khách sang giá net để tính margin.</li>
  <li>So sánh giá giữa các nước có tỷ lệ khác nhau.</li>
  <li>Xem một thay đổi tỷ lệ gần đây tác động thực sự ra sao tới đơn hàng tiêu chuẩn của bạn.</li>
</ul>
<p>Không dùng cho tờ khai, OSS/MOSS, phân bổ, hay xác định pháp lý loại giao dịch — đó là việc của kế toán/tư vấn thuế.</p>

<h2>Về dữ liệu tỷ lệ</h2>
<p>Tỷ lệ được sưu tầm thủ công từ thông báo của các cơ quan thuế, theo ngày hiển thị dưới kết quả. Bao gồm cải cách 2024 / 2025 mà nhiều công cụ online chưa cập nhật:</p>
<ul>
  <li><strong>Slovakia</strong>: chuẩn từ 20% lên 23%, 2025-01-01.</li>
  <li><strong>Cộng hòa Séc</strong>: giảm 15% và 10% gộp thành 12%, 2024-01-01.</li>
  <li><strong>Estonia</strong>: chuẩn lên 24%, 2025-07-01.</li>
  <li><strong>Phần Lan</strong>: chuẩn lên 25,5%, 2024-09-01.</li>
  <li><strong>Thụy Sĩ</strong>: chuẩn lên 8,1%, 2024-01-01.</li>
</ul>
<p>Phạm vi tỷ lệ giảm thay đổi theo quốc gia — phần ghi chú chỉ là gợi ý.</p>

<h2>Cạm bẫy hay gặp</h2>
<ul>
  <li><strong>Trừ % từ gross ≠ net.</strong> 100 gross với VAT 10% là 90,91 net, không phải 90.</li>
  <li><strong>Cơ chế reverse-charge</strong> trong B2B nội bộ EU.</li>
  <li><strong>Ngưỡng OSS</strong> 10 000 € mỗi năm cho B2C xuyên biên giới trong EU.</li>
  <li><strong>Đăng ký VAT ≠ luôn xuất VAT</strong>: có cơ chế đặc biệt và miễn trừ.</li>
  <li><strong>Làm tròn theo dòng hay theo hóa đơn</strong>: giữ nhất quán trong cùng một chứng từ.</li>
</ul>
""",
        "hi": """
<h2>VAT क्या है और कैसे काम करता है?</h2>
<p>VAT (Value-Added Tax) एक consumption tax है जो supply chain के हर step पर <em>added value</em> पर लगाया जाता है। Businesses sales पर VAT charge करते हैं (output VAT), purchases पर VAT recover करते हैं (input VAT), और अंतर tax authority को देते हैं।</p>

<p>हर invoice line पर दो numbers मायने रखते हैं:</p>
<ul>
  <li><strong>Net</strong> — VAT से पहले की कीमत।</li>
  <li><strong>Gross</strong> — VAT समेत कीमत (जो customer pay करता है)।</li>
</ul>
<p>अगर आप gross डालते हैं, calculator VAT निकालता है: <code>net = gross / (1 + rate)</code>। अगर net डालते हैं, ऊपर से VAT जोड़ता है: <code>vat = net × rate</code>।</p>

<h2>इसे कब उपयोग करें vs. accounting software</h2>
<p>यह quick-check calculator है, bookkeeping नहीं। उपयोगी इसके लिए:</p>
<ul>
  <li>भेजने से पहले invoice line की sanity check।</li>
  <li>Margin calculation के लिए customer price को net में बदलना।</li>
  <li>अलग rates वाले देशों के बीच price compare करना।</li>
  <li>हाल की rate change का असली असर देखना अपने typical sale पर।</li>
</ul>
<p>इसका उपयोग नहीं: filing return, OSS/MOSS, partial exemption, या categorization decisions के लिए — वो accountant या tax authority का काम है।</p>

<h2>Rate dataset के बारे में</h2>
<p>Rates result के नीचे दिखाई तारीख के अनुसार, हर country की tax authority के publications से हाथ से curate की गई हैं। बाकी VAT calculators से अंतर यह है कि यह dataset 2024/2025 के post-reform rates को दर्शाता है:</p>
<ul>
  <li><strong>Slovakia</strong>: standard rate 20% से 23% पर, 2025-01-01।</li>
  <li><strong>Czech Republic</strong>: 15% और 10% reduced tiers को 12% में consolidate, 2024-01-01।</li>
  <li><strong>Estonia</strong>: standard rate 24%, 2025-07-01।</li>
  <li><strong>Finland</strong>: standard rate 25.5%, 2024-09-01।</li>
  <li><strong>Switzerland</strong>: standard rate 8.1%, 2024-01-01।</li>
</ul>
<p>Reduced categories देश-दर-देश अलग हैं — notes संकेत हैं, ruling नहीं।</p>

<h2>आम गलतियाँ</h2>
<ul>
  <li><strong>Gross से % घटाना ≠ net।</strong> 23% VAT included के साथ 100 gross = 81.30 net, 77.00 नहीं।</li>
  <li><strong>Reverse-charge invoices</strong>: cross-border B2B EU supplies में VAT अक्सर buyer पर shift होता है।</li>
  <li><strong>Distance-sale thresholds</strong>: EU में cross-border B2C €10k/year से ऊपर OSS scheme लागू होती है।</li>
  <li><strong>VAT-registered ≠ VAT-charging</strong>: कई छोटे freelancers threshold से नीचे रहते हैं।</li>
  <li><strong>Rounding rules</strong>: per-line या per-invoice — एक ही invoice में mix न करें।</li>
</ul>
""",
        "sk": """
<h2>Čo je DPH a ako funguje?</h2>
<p>DPH (Daň z pridanej hodnoty) je spotrebná daň. Vyberá sa v každom kroku dodávateľského reťazca z <em>pridanej hodnoty</em>. Podnikatelia účtujú DPH na výstupe pri predaji, odpočítavajú si DPH na vstupe z nákupov, a rozdiel odvádzajú daňovému úradu. Pre koncového zákazníka to vyzerá ako daň zahrnutá v cene; pre platcu DPH je to v podstate prietokový režim (okrem oslobodených plnení).</p>

<p>Dôležité sú dve čísla na riadok faktúry:</p>
<ul>
  <li><strong>Netto (bez DPH)</strong> — cena pred DPH, ktorú si firma účtuje ako výnos.</li>
  <li><strong>Brutto (s DPH)</strong> — cena vrátane DPH, ktorú reálne platí zákazník.</li>
</ul>
<p>Ak vstup zadávaš brutto (cenovka, terminálový blok), kalkulačka DPH oddelí: <code>netto = brutto / (1 + sadzba)</code>. Ak je vstup netto (B2B ponuka), DPH pripočíta: <code>DPH = netto × sadzba</code>.</p>

<h2>Slovenská poznámka — prečo to teraz</h2>
<p>Slovenská sadzba DPH sa od 1. januára 2025 zmenila — základná sadzba stúpla z 20 % na <strong>23 %</strong>. Veľa online kalkulačiek ešte stále počíta s 20 %. Tento nástroj má aktuálne čísla vrátane znížených sadzieb:</p>
<ul>
  <li><strong>23 %</strong> — základná sadzba (od 1. 1. 2025).</li>
  <li><strong>19 %</strong> — znížená sadzba pre reštauračné a stravovacie služby, vstupy do fitness, nealkoholické nápoje.</li>
  <li><strong>5 %</strong> — základné potraviny, knihy (vrátane elektronických), lieky, ubytovanie, sociálne bývanie.</li>
  <li><strong>0 %</strong> — vývoz mimo EÚ, intrakomunitárne dodanie tovaru.</li>
</ul>

<h2>Kedy použiť kalkulačku a kedy účtovný softvér</h2>
<p>Tento nástroj je rýchla kontrola, nie účtovníctvo. Hodí sa na:</p>
<ul>
  <li>Overenie riadku faktúry pred odoslaním.</li>
  <li>Prepočet ceny pre zákazníka na netto kvôli marži.</li>
  <li>Porovnanie ceny medzi krajinami s rôznymi sadzbami.</li>
  <li>Zistenie, ako sa nová sadzba prejaví na vašom typickom predaji.</li>
</ul>
<p>Na podanie DPH priznania, OSS/MOSS, pomer odpočtu alebo právne zaradenie konkrétneho plnenia použite účtovný softvér a daňového poradcu — chybná kategorizácia (zlá znížená sadzba) je presne to, na čom firmy dostanú pokutu.</p>

<h2>O dátach</h2>
<p>Sadzby ručne overené podľa oficiálnych zdrojov k dátumu uvedenému pod výsledkom. Zahŕňa reformy 2024 / 2025, ktoré veľa online kalkulačiek nemá:</p>
<ul>
  <li><strong>Slovensko</strong>: základná sadzba z 20 % na 23 %, 1. 1. 2025.</li>
  <li><strong>Česko</strong>: znížené sadzby 15 % a 10 % zlúčené na 12 % od 1. 1. 2024.</li>
  <li><strong>Estónsko</strong>: základná sadzba na 24 % od 1. 7. 2025.</li>
  <li><strong>Fínsko</strong>: základná sadzba na 25,5 % od 1. 9. 2024.</li>
  <li><strong>Švajčiarsko</strong>: základná sadzba na 8,1 % od 1. 1. 2024.</li>
</ul>

<h2>Časté chyby</h2>
<ul>
  <li><strong>Odpočítať % od brutto neznamená netto.</strong> 100 € brutto s DPH 23 % je 81,30 € netto, nie 77 €.</li>
  <li><strong>Tuzemský prenos daňovej povinnosti</strong> a cezhraničné reverse-charge — DPH prechádza na odberateľa, faktúra má 0 %, ale plnenie nie je oslobodené.</li>
  <li><strong>OSS prah 10 000 € ročne</strong> pri B2C predaji do iných štátov EÚ — nad ním sa účtuje sadzba krajiny zákazníka.</li>
  <li><strong>Neplatiteľ DPH</strong> — malé živnosti pod registračným prahom DPH neúčtujú vôbec.</li>
  <li><strong>Zaokrúhľovanie po riadku vs. po faktúre</strong> — v jednom doklade buďte konzistentní.</li>
</ul>
""",
        "cs": """
<h2>Co je DPH a jak funguje?</h2>
<p>DPH (Daň z přidané hodnoty) je spotřební daň. Vybírá se v každém kroku dodavatelského řetězce z <em>přidané hodnoty</em>. Podnikatelé účtují DPH na výstupu při prodeji, odpočítávají si DPH na vstupu z nákupů, a rozdíl odvádějí finančnímu úřadu. Pro koncového zákazníka to vypadá jako daň zahrnutá v ceně; pro plátce DPH je to v podstatě průtokový režim (kromě osvobozených plnění).</p>

<p>Důležitá jsou dvě čísla na řádek faktury:</p>
<ul>
  <li><strong>Netto (bez DPH)</strong> — cena před DPH, kterou si firma účtuje jako výnos.</li>
  <li><strong>Brutto (s DPH)</strong> — cena včetně DPH, kterou reálně platí zákazník.</li>
</ul>
<p>Pokud zadáváš brutto (cenovka, blok z terminálu), kalkulačka DPH oddělí: <code>netto = brutto / (1 + sazba)</code>. Pokud je vstup netto (B2B nabídka), DPH se připočte: <code>DPH = netto × sazba</code>.</p>

<h2>Česká poznámka — proč zrovna teď</h2>
<p>České sazby DPH se výrazně proměnily — od 1. ledna 2024 byly dvě snížené sazby <strong>15 % a 10 % sloučeny do jediné 12% sazby</strong>. Hodně online kalkulaček (a kalkulaček ve starých šablonách faktur) tuhle změnu ještě nemá. Tento nástroj má aktuální stav:</p>
<ul>
  <li><strong>21 %</strong> — základní sazba.</li>
  <li><strong>12 %</strong> — sjednocená snížená sazba (potraviny, knihy, léky, ubytování, stavební práce a další — od 1. 1. 2024).</li>
  <li><strong>0 %</strong> — vývoz mimo EU, intrakomunitární dodání zboží.</li>
</ul>

<h2>Kdy použít kalkulačku a kdy účetní software</h2>
<p>Tento nástroj je rychlá kontrola, ne účetnictví. Hodí se na:</p>
<ul>
  <li>Ověření řádku faktury před odesláním.</li>
  <li>Přepočet zákaznické ceny na netto kvůli marži.</li>
  <li>Porovnání cen mezi zeměmi s různými sazbami.</li>
  <li>Zjištění, jak se nová sazba projeví na vašem typickém prodeji.</li>
</ul>
<p>Pro podání DPH přiznání, OSS/MOSS, krácený odpočet nebo právní zařazení konkrétního plnění použijte účetní software a daňového poradce — špatná kategorizace (špatná snížená sazba) je přesně to, na čem firmy dostávají pokutu.</p>

<h2>O datech</h2>
<p>Sazby ručně ověřené podle oficiálních zdrojů k datu pod výsledkem. Zahrnuje reformy 2024 / 2025, které mnoho online kalkulaček nemá:</p>
<ul>
  <li><strong>Česko</strong>: snížené 15 % a 10 % sjednoceny na 12 % od 1. 1. 2024.</li>
  <li><strong>Slovensko</strong>: základní sazba z 20 % na 23 %, 1. 1. 2025.</li>
  <li><strong>Estonsko</strong>: základní sazba na 24 % od 1. 7. 2025.</li>
  <li><strong>Finsko</strong>: základní sazba na 25,5 % od 1. 9. 2024.</li>
  <li><strong>Švýcarsko</strong>: základní sazba na 8,1 % od 1. 1. 2024.</li>
</ul>

<h2>Časté chyby</h2>
<ul>
  <li><strong>Odečíst % od brutto neznamená netto.</strong> 100 Kč brutto s DPH 21 % je 82,64 Kč netto, ne 79 Kč.</li>
  <li><strong>Tuzemský přenos daňové povinnosti</strong> a přeshraniční reverse-charge — DPH přechází na odběratele, faktura má 0 %, ale plnění není osvobozené.</li>
  <li><strong>OSS práh 10 000 € ročně</strong> u B2C prodeje do jiných států EU — nad ním se účtuje sazba země zákazníka.</li>
  <li><strong>Neplátce DPH</strong> — malí živnostníci pod registračním prahem DPH neúčtují vůbec.</li>
  <li><strong>Zaokrouhlování po řádku vs. po faktuře</strong> — v jednom dokladu buďte konzistentní.</li>
</ul>
""",
    },
    "related": ["percentage-calculator", "tip-split-calculator", "unit-converter"],
    "howto": {"flow": "calculate", "action": "format", "noun": {
        "en": "VAT", "de": "MwSt.", "es": "IVA", "fr": "TVA", "it": "IVA",
        "pt": "IVA", "pl": "VAT", "ja": "VAT", "nl": "BTW", "tr": "KDV",
        "id": "PPN", "vi": "VAT", "hi": "VAT", "sk": "DPH", "cs": "DPH",
    }},
}
