TOOL = {
    "slug": "mortgage-affordability-calculator",
    "category": "math",
    "icon": "🏡",
    "tags": ["mortgage", "affordability", "home", "house", "calculator", "income", "dti", "down payment"],
    "i18n": {
        "en": {
            "name": "Mortgage Affordability Calculator",
            "tagline": "How much house can I afford? Income + monthly debts + down payment + interest rate → max purchase price under the 28/36 DTI rule.",
            "description": "Free in-browser mortgage affordability calculator. Enter gross annual income, recurring monthly debts, available down payment, mortgage interest rate, and term. Get back the max home price you can afford under the classic 28/36 debt-to-income (DTI) rule, the matching monthly PITI payment, and the implied principal you'd be borrowing. Pairs with our loan-calculator for the actual amortization schedule once you've picked a price.",
        },
        "de": {"name": "Hypothekenleistbarkeits-Rechner", "tagline": "Wie viel Haus kann ich mir leisten? Einkommen + monatliche Schulden + Anzahlung + Zins → maximaler Kaufpreis nach der 28/36-DTI-Regel.", "description": "Kostenloser Hypothekenleistbarkeits-Rechner im Browser. Gib Bruttojahreseinkommen, monatliche Schulden, Anzahlung, Hypothekenzins und Laufzeit ein. Erhalte den maximal leistbaren Kaufpreis nach der klassischen 28/36-DTI-Regel, die zugehörige monatliche PITI-Rate und die Kreditsumme."},
        "es": {"name": "Calculadora de Capacidad Hipotecaria", "tagline": "¿Cuánto puedo gastar en casa? Ingresos + deudas mensuales + entrada + tipo de interés → precio máximo bajo la regla 28/36 DTI.", "description": "Calculadora gratuita de capacidad hipotecaria en el navegador. Introduce ingresos brutos anuales, deudas mensuales, entrada, tipo de interés y plazo. Obtén el precio máximo bajo la regla 28/36 DTI, la cuota PITI mensual asociada y el principal a financiar."},
        "fr": {"name": "Calculatrice de Capacité d'Emprunt", "tagline": "Quel prix de maison puis-je me permettre ? Revenus + dettes mensuelles + apport + taux → prix max selon la règle 28/36 DTI.", "description": "Calculatrice gratuite de capacité d'emprunt immobilier en navigateur. Saisissez revenus bruts annuels, dettes mensuelles, apport, taux d'intérêt et durée. Obtenez le prix max selon la règle 28/36 DTI, la mensualité PITI et le principal à emprunter."},
        "it": {"name": "Calcolatore Capacità di Mutuo", "tagline": "Quanto posso permettermi di casa? Reddito + debiti mensili + acconto + tasso → prezzo max sotto la regola 28/36 DTI.", "description": "Calcolatore gratuito di capacità di mutuo nel browser. Inserisci reddito lordo annuo, debiti mensili, acconto, tasso d'interesse e durata. Ottieni il prezzo massimo sotto la regola 28/36 DTI, la rata PITI mensile e il capitale da finanziare."},
        "pt": {"name": "Calculadora de Capacidade de Financiamento", "tagline": "Quanto de casa posso pagar? Renda + dívidas mensais + entrada + taxa de juros → preço máximo pela regra 28/36 DTI.", "description": "Calculadora gratuita de capacidade de financiamento no navegador. Informe renda bruta anual, dívidas mensais recorrentes, valor de entrada, taxa de juros do financiamento e prazo. Obtenha o preço máximo de casa pela clássica regra 28/36 DTI, a parcela PITI mensal correspondente e o principal a financiar. Combina com a nossa loan-calculator para a tabela de amortização real depois que você escolher um preço."},
        "pl": {"name": "Kalkulator Zdolności Kredytowej", "tagline": "Ile domu mnie stać? Dochód + miesięczne zobowiązania + wkład własny + oprocentowanie → maks. cena wg reguły 28/36 DTI.", "description": "Darmowy kalkulator zdolności kredytowej hipotecznej w przeglądarce. Wpisz roczny dochód brutto, miesięczne zobowiązania, wkład własny, oprocentowanie kredytu i okres. Dostań maks. cenę domu wg klasycznej reguły 28/36 DTI, odpowiadającą miesięczną ratę PITI i kwotę kredytu do zaciągnięcia. Łączy się z naszym loan-calculator dla pełnego harmonogramu spłaty po wyborze ceny."},
        "ja": {"name": "住宅ローン支払能力計算機", "tagline": "いくらの家を買えるか？ 収入 + 月々の負債 + 頭金 + 金利 → 28/36 DTI ルールに基づく最大購入額。", "description": "ブラウザ完結の無料住宅ローン支払能力計算ツール。年間税前収入、月々の負債、頭金、住宅ローン金利、返済期間を入力すると、伝統的な 28/36 債務収入比（DTI）ルールに基づく最大購入可能額、対応する月額 PITI 支払、借入元本を表示します。価格を決めた後はローン計算機で実際の償却スケジュールも参照できます。"},
        "nl": {"name": "Hypotheekafsluitbaarheid-Calculator", "tagline": "Hoeveel huis kan ik betalen? Inkomen + maandelijkse schulden + aanbetaling + rente → max aankoopprijs onder de 28/36 DTI-regel.", "description": "Gratis in-browser hypotheekafsluitbaarheid-calculator. Voer bruto jaarinkomen, terugkerende maandelijkse schulden, aanbetaling, hypotheekrente en looptijd in. Krijg de max huisprijs onder de klassieke 28/36 debt-to-income (DTI)-regel, de bijbehorende maandelijkse PITI-betaling en het implied principal dat je zou lenen."},
        "tr": {"name": "Mortgage Karşılanabilirlik Hesaplayıcı", "tagline": "Ne kadar ev alabilirim? Gelir + aylık borçlar + peşinat + faiz oranı → 28/36 DTI kuralına göre maksimum fiyat.", "description": "Tarayıcıda ücretsiz mortgage karşılanabilirlik hesaplayıcı. Brüt yıllık gelir, aylık tekrarlayan borçlar, mevcut peşinat, mortgage faiz oranı ve vade gir. Klasik 28/36 borç-gelir (DTI) kuralı altında karşılayabileceğin maksimum ev fiyatını, eşleşen aylık PITI ödemesini ve borçlanacağın anaparayı al."},
        "id": {"name": "Kalkulator Kemampuan KPR", "tagline": "Berapa rumah yang sanggup saya beli? Pendapatan + utang bulanan + DP + bunga → harga maks dengan aturan 28/36 DTI.", "description": "Kalkulator kemampuan KPR gratis di browser. Masukkan pendapatan bruto tahunan, utang bulanan, DP, suku bunga KPR, dan tenor. Dapatkan harga rumah maksimum berdasarkan aturan klasik 28/36 DTI, cicilan PITI bulanan yang sesuai, dan principal yang akan kamu pinjam. Cocok dipasangkan dengan loan-calculator kami untuk tabel amortisasi setelah memilih harga."},
        "vi": {"name": "Máy tính Khả năng Vay Mua Nhà", "tagline": "Tôi mua được nhà bao nhiêu? Thu nhập + nợ hàng tháng + đặt cọc + lãi suất → giá tối đa theo quy tắc 28/36 DTI.", "description": "Máy tính khả năng vay mua nhà miễn phí trên trình duyệt. Nhập thu nhập gộp hàng năm, nợ hàng tháng, tiền đặt cọc, lãi suất vay và kỳ hạn. Nhận giá nhà tối đa theo quy tắc 28/36 nợ-thu nhập (DTI), khoản trả PITI hàng tháng tương ứng và principal cần vay."},
        "hi": {"name": "Mortgage Affordability Calculator", "tagline": "मैं कितना घर खरीद सकता हूँ? Income + मासिक debts + down payment + interest rate → 28/36 DTI rule के तहत अधिकतम कीमत।", "description": "मुफ़्त in-browser mortgage affordability calculator। gross annual income, recurring मासिक debts, available down payment, mortgage interest rate, और term डालें। classic 28/36 debt-to-income (DTI) rule के तहत अधिकतम घर की कीमत, मिलान मासिक PITI payment, और implied principal प्राप्त करें। कीमत चुनने के बाद वास्तविक amortization schedule के लिए हमारे loan-calculator के साथ pairs।"},
        "sk": {"name": "Kalkulačka dostupnosti hypotéky", "tagline": "Aký drahý dom si môžem dovoliť? Príjem + mesačné dlhy + akontácia + úrok → maximálna cena podľa pravidla 28/36 DTI.", "description": "Bezplatná kalkulačka dostupnosti hypotéky priamo v prehliadači. Zadaj hrubý ročný príjem, mesačné dlhy, akontáciu, úrokovú sadzbu a dobu splácania. Dostaneš maximálnu cenu domu podľa klasického pravidla 28/36 DTI, zodpovedajúcu mesačnú splátku PITI a výšku úveru."},
        "cs": {"name": "Kalkulačka dostupnosti hypotéky", "tagline": "Jak drahý dům si můžu dovolit? Příjem + měsíční dluhy + akontace + úrok → maximální cena podle pravidla 28/36 DTI.", "description": "Bezplatná kalkulačka dostupnosti hypotéky přímo v prohlížeči. Zadej hrubý roční příjem, měsíční dluhy, akontaci, úrokovou sazbu a dobu splácení. Dostaneš maximální cenu domu podle klasického pravidla 28/36 DTI, odpovídající měsíční splátku PITI a výši úvěru."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Gross annual income</label>
      <input type="number" id="ma-income" step="any" min="0" value="80000" oninput="maRun()">
    </div>
    <div>
      <label>Monthly recurring debts (car, cards, student loans)</label>
      <input type="number" id="ma-debts" step="any" min="0" value="400" oninput="maRun()">
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Down payment</label>
      <input type="number" id="ma-down" step="any" min="0" value="40000" oninput="maRun()">
    </div>
    <div>
      <label>Interest rate (annual %)</label>
      <input type="number" id="ma-rate" step="0.01" min="0" value="6.5" oninput="maRun()">
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Term (years)</label>
      <input type="number" id="ma-term" step="1" min="1" max="40" value="30" oninput="maRun()">
    </div>
    <div>
      <label>Property tax + insurance (% of home price / year)</label>
      <input type="number" id="ma-ti" step="0.05" min="0" value="1.5" oninput="maRun()">
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>DTI rule</label>
      <select id="ma-rule" onchange="maRun()">
        <option value="28">28% front-end (housing only) — conservative</option>
        <option value="36" selected>36% back-end (housing + all debt) — standard</option>
        <option value="43">43% — qualified mortgage maximum (US)</option>
      </select>
    </div>
    <div>
      <label>Currency symbol</label>
      <input type="text" id="ma-cur" maxlength="4" value="$" oninput="maRun()">
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="ma-out" class="output"></div>
</div>
""",
    "script": """
<style>
.ma-hero{background:var(--accent);color:#fff;padding:1rem 1.2rem;border-radius:8px;text-align:center;margin-bottom:0.8rem}
.ma-hero .ma-big{font-family:ui-monospace,monospace;font-size:1.8rem;font-weight:700;line-height:1.1}
.ma-hero .ma-sub{font-size:0.82rem;opacity:0.9;margin-top:0.25rem}
.ma-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:0.6rem}
.ma-stat{background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;padding:0.7rem 0.85rem}
.ma-stat .ma-num{font-family:ui-monospace,monospace;font-size:1.15rem;font-weight:600;color:var(--accent)}
.ma-stat .ma-lbl{font-size:0.76rem;color:var(--text-muted);margin-top:0.15rem}
.ma-note{margin-top:0.7rem;color:var(--text-muted);font-size:0.8rem;line-height:1.45}
.ma-pill{display:inline-block;background:var(--bg-elev);border:1px solid var(--border);border-radius:999px;padding:0.15rem 0.5rem;font-size:0.7rem;margin-left:0.3rem;color:var(--text-muted)}
</style>
<script>
function maFmt(n, cur){
  if(!isFinite(n) || n < 0) return '—';
  return cur + Math.round(n).toLocaleString('en-US');
}
function maRun(){
  const income = parseFloat(document.getElementById('ma-income').value) || 0;
  const debts  = parseFloat(document.getElementById('ma-debts').value)  || 0;
  const down   = parseFloat(document.getElementById('ma-down').value)   || 0;
  const rate   = parseFloat(document.getElementById('ma-rate').value)   || 0;
  const years  = Math.max(1, parseFloat(document.getElementById('ma-term').value) || 30);
  const tiPct  = parseFloat(document.getElementById('ma-ti').value)     || 0;
  const rule   = parseFloat(document.getElementById('ma-rule').value);
  const cur    = document.getElementById('ma-cur').value || '';
  const out    = document.getElementById('ma-out');
  if(income <= 0){ out.textContent = '{LBL_NO_INPUT}'; return; }
  const monthlyIncome = income / 12;
  // Back-end (housing + other debt) <= rule% of monthly income.
  // Front-end variant just uses housing only.
  const maxTotalRatio = monthlyIncome * (rule / 100);
  const otherDebt = (rule === 28) ? 0 : debts;
  const maxHousingPayment = Math.max(0, maxTotalRatio - otherDebt);
  // Housing payment = P&I + (tiPct/100/12)*homePrice.
  // Loan amount = homePrice - down.
  // Monthly rate
  const r = (rate / 100) / 12;
  const n = years * 12;
  // For a given homePrice H:
  //   PI = (H - down) * r * (1+r)^n / ((1+r)^n - 1)
  //   TI = H * (tiPct/100/12)
  //   total = PI + TI <= maxHousingPayment
  // Solve for H.
  let piFactor;
  if(r === 0){ piFactor = 1 / n; }
  else {
    const pow = Math.pow(1+r, n);
    piFactor = (r * pow) / (pow - 1);
  }
  const tiFactor = (tiPct / 100) / 12;
  // maxHousingPayment = (H - down) * piFactor + H * tiFactor
  //                   = H * (piFactor + tiFactor) - down * piFactor
  // H = (maxHousingPayment + down * piFactor) / (piFactor + tiFactor)
  const denom = piFactor + tiFactor;
  let maxHome = 0;
  if(denom > 0){
    maxHome = (maxHousingPayment + down * piFactor) / denom;
  }
  if(maxHome < down) maxHome = down;
  const principal = Math.max(0, maxHome - down);
  const monthlyPI = principal * piFactor;
  const monthlyTI = maxHome * tiFactor;
  const monthlyTotal = monthlyPI + monthlyTI;
  const backEndDTI = monthlyIncome > 0 ? ((monthlyTotal + debts) / monthlyIncome) * 100 : 0;
  const frontEndDTI = monthlyIncome > 0 ? (monthlyTotal / monthlyIncome) * 100 : 0;
  const ltv = maxHome > 0 ? (principal / maxHome) * 100 : 0;
  out.innerHTML = `
    <div class="ma-hero">
      <div class="ma-big">${maFmt(maxHome, cur)}</div>
      <div class="ma-sub">Max home price under ${rule}% ${rule===28?'front-end':'back-end'} DTI</div>
    </div>
    <div class="ma-grid">
      <div class="ma-stat"><div class="ma-num">${maFmt(monthlyTotal, cur)}</div><div class="ma-lbl">Monthly PITI</div></div>
      <div class="ma-stat"><div class="ma-num">${maFmt(monthlyPI, cur)}</div><div class="ma-lbl">P&amp;I portion</div></div>
      <div class="ma-stat"><div class="ma-num">${maFmt(monthlyTI, cur)}</div><div class="ma-lbl">Tax + insurance</div></div>
      <div class="ma-stat"><div class="ma-num">${maFmt(principal, cur)}</div><div class="ma-lbl">Loan principal</div></div>
      <div class="ma-stat"><div class="ma-num">${ltv.toFixed(1)}%</div><div class="ma-lbl">Loan-to-value</div></div>
      <div class="ma-stat"><div class="ma-num">${backEndDTI.toFixed(1)}%</div><div class="ma-lbl">Back-end DTI<span class="ma-pill">housing + debt</span></div></div>
    </div>
    <div class="ma-note">
      The ${rule}% rule limits ${rule===28?'housing payment alone':'housing payment plus all other recurring debt'} to ${rule}% of your gross monthly income (${maFmt(monthlyIncome, cur)}). Front-end DTI here is ${frontEndDTI.toFixed(1)}%. Lenders look at PMI, HOA fees and credit score on top of this — treat the figure as a ceiling, not a target.
    </div>
  `;
}
document.addEventListener('DOMContentLoaded', maRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Before you fall in love with a listing, it's worth knowing the ceiling. This calculator answers "how much house can my income support?" by inverting the standard mortgage math: instead of asking what a $400,000 home costs per month, it asks what home price corresponds to the maximum monthly payment your debt-to-income ratio allows. The result is the price at which a lender stops underwriting — useful for setting a budget, shortlisting neighbourhoods, or sanity-checking what your agent says you "qualify for".</p>

<h3>How it works</h3>
<ul>
  <li><strong>Monthly income</strong> is your gross annual divided by 12 — that's what lenders use.</li>
  <li><strong>The DTI rule</strong> caps your housing-related spending at a percentage of that monthly income. 28% front-end means PITI alone; 36% back-end means PITI + car loans + student loans + minimum credit-card payments. 43% is the legal ceiling for a "qualified mortgage" in the US after Dodd-Frank.</li>
  <li><strong>PITI</strong> stands for principal, interest, taxes, insurance. Your principal &amp; interest payment is solved from the standard amortization formula (P&amp;I = L × r(1+r)<sup>n</sup> / ((1+r)<sup>n</sup>−1) where L is loan amount, r is monthly rate, n is months). T&amp;I is approximated as a percentage of home value per year — typically 1.0–2.5% in the US depending on state, much lower in most of Europe.</li>
  <li><strong>We solve the home price algebraically</strong>: maxPITI = (H − down) × piFactor + H × tiFactor, then re-arrange for H. Loan principal is then maxHome − down payment.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>PMI is not included.</strong> If your down payment is under 20%, expect 0.3–1.5% of the loan amount per year in private mortgage insurance. This calculator does not account for it — assume your real max is 5–10% lower than the figure shown when LTV &gt; 80%.</li>
  <li><strong>HOA / condo fees aren't modelled.</strong> A condo with $400/month HOA effectively reduces the housing budget by $400 — subtract it from your income inputs by adding $400 to monthly debts, or just mentally adjust.</li>
  <li><strong>Tax/insurance varies wildly by location.</strong> 1.5% is a US average. Texas and New Jersey are 2.5%+; California is around 1.1%; most of Europe is well under 1%. Look up your area before relying on this number.</li>
  <li><strong>DTI is a ceiling, not a recommendation.</strong> Living right at 36% DTI leaves no buffer for car repairs, kids, or a roof. Many financial planners suggest 25–30% housing including taxes as a comfortable target.</li>
  <li><strong>Lenders also look at credit score, employment history, and reserves.</strong> A DTI calculator tells you the maximum a lender would underwrite assuming everything else is fine — it doesn't guarantee approval.</li>
  <li><strong>Variable-rate mortgages need a stress test.</strong> If your rate could rise 2 percentage points, recompute at the higher rate and make sure that's still livable.</li>
</ul>

<h3>Pairs with</h3>
<ul>
  <li><strong>loan-calculator</strong> — once you pick a target price, switch over to see the full month-by-month amortization, total interest, and "what if I pay extra" scenarios.</li>
  <li><strong>percentage-calculator</strong> — for quick sanity checks on down-payment percentages, fee splits, etc.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Antes de se apaixonar por um anúncio, vale conhecer o teto. Esta calculadora responde "quanto de casa minha renda sustenta?" invertendo a matemática hipotecária padrão: em vez de perguntar quanto custa por mês um imóvel de R$ 400.000, ela pergunta qual preço corresponde ao máximo pagamento mensal que sua relação dívida/renda permite. O resultado é o preço a partir do qual o banco para de aprovar — útil para definir orçamento, escolher bairros, ou bater o pé com o corretor sobre o que você "se qualifica".</p>

<h3>Como funciona</h3>
<ul>
  <li><strong>Renda mensal</strong> é sua renda bruta anual dividida por 12 — é o que os bancos usam.</li>
  <li><strong>A regra DTI</strong> limita seu gasto com moradia a um percentual dessa renda mensal. 28% front-end é só PITI; 36% back-end é PITI + financiamento de carro + estudantil + mínimo do cartão. 43% é o teto legal para uma "qualified mortgage" nos EUA pós-Dodd-Frank.</li>
  <li><strong>PITI</strong> significa principal, juros, impostos (IPTU), seguro. O P&amp;I é resolvido pela fórmula padrão de amortização. T&amp;I é aproximado como percentual do valor do imóvel por ano — tipicamente 1,0–2,5% nos EUA, bem menor no Brasil (IPTU costuma ser 0,3–1,5% + seguro residencial).</li>
  <li><strong>Resolvemos algebricamente</strong>: maxPITI = (H − entrada) × piFactor + H × tiFactor, depois isolamos H. Principal = preço máximo − entrada.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Não inclui PMI ou seguros adicionais.</strong> Se a entrada é abaixo de 20% nos EUA, espere 0,3–1,5% do empréstimo/ano em PMI. No Brasil, MIP e DFI já vêm embutidos na parcela e podem adicionar 0,02–0,04%/mês.</li>
  <li><strong>Condomínio não modelado.</strong> Um apto com R$ 800/mês de condomínio reduz o orçamento habitacional em R$ 800 — adicione esse valor às dívidas mensais ou ajuste mentalmente.</li>
  <li><strong>Imposto/seguro varia muito por local.</strong> 1,5% é média EUA. Texas e New Jersey passam de 2,5%; Califórnia ~1,1%; Brasil bem abaixo. Consulte sua região antes de confiar no número.</li>
  <li><strong>DTI é teto, não recomendação.</strong> Viver com DTI cravado em 36% não deixa folga para conserto de carro, filhos, ou um telhado novo. Planejadores recomendam 25–30% com moradia incluindo impostos.</li>
  <li><strong>Bancos olham também score, histórico de emprego e reservas.</strong> O DTI te diz o máximo que um banco aprovaria se o resto estiver ok — não garante aprovação.</li>
  <li><strong>Hipoteca com taxa variável precisa de teste de estresse.</strong> Se a taxa puder subir 2 pontos percentuais, recalcule no valor maior e confira se ainda cabe no orçamento.</li>
</ul>

<h3>Combina com</h3>
<ul>
  <li><strong>loan-calculator</strong> — depois de escolher um preço-alvo, veja a amortização mês a mês completa, total de juros, e cenários "e se eu pagar a mais".</li>
  <li><strong>percentage-calculator</strong> — para checagens rápidas em percentuais de entrada, divisão de taxas, etc.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Bevor du dich in eine Anzeige verliebst, lohnt es sich, die Decke zu kennen. Dieser Rechner beantwortet "wie viel Haus kann mein Einkommen tragen?", indem er die Standard-Hypotheken-Mathematik umkehrt: Statt zu fragen, was ein 400.000-€-Haus pro Monat kostet, fragt er, welcher Kaufpreis der maximalen Monatsrate entspricht, die deine Schuldenquote (DTI) erlaubt.</p>
<h3>Wie es funktioniert</h3>
<ul>
<li><strong>Monatseinkommen</strong> = Brutto-Jahreseinkommen / 12.</li>
<li><strong>DTI-Regel</strong> begrenzt Wohnkosten auf einen Anteil davon. 28% front-end = nur PITI; 36% back-end = PITI + alle wiederkehrenden Schulden.</li>
<li><strong>PITI</strong> = Tilgung, Zinsen, Steuern, Versicherung. T+I als Prozent des Hauspreises/Jahr (1,0–2,5% US, viel niedriger in DE).</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>PMI / Hypothekenversicherung nicht enthalten.</strong> Bei &lt;20% Anzahlung in den USA üblich.</li>
<li><strong>Hausgeld / WEG-Beiträge nicht modelliert.</strong> Bei einer Wohnung manuell zu Schulden hinzufügen.</li>
<li><strong>Variabler Zins benötigt Stresstest.</strong> Bei +2 Prozentpunkten neu rechnen.</li>
</ul>
<h3>Kombiniert mit</h3>
<ul>
<li><strong>loan-calculator</strong> — Tilgungsplan und Mehrzahlungs-Szenarien.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Antes de enamorarte de un anuncio, conviene saber el techo. Esta calculadora responde "¿cuánto piso/casa soporta mi sueldo?" invirtiendo la matemática hipotecaria: pregunta qué precio corresponde a la cuota máxima que tu ratio deuda/ingreso permite.</p>
<h3>Cómo funciona</h3>
<ul>
<li><strong>Ingresos mensuales</strong> = ingresos brutos anuales / 12.</li>
<li><strong>Regla DTI</strong> limita el gasto en vivienda a un porcentaje. 28% front-end = solo PITI; 36% back-end = PITI + todas las deudas.</li>
<li><strong>PITI</strong> = capital, intereses, impuestos (IBI), seguros. T+I como % anual del valor de la vivienda.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>PMI no incluido</strong> si entrada &lt;20% (típico US, no UK/ES).</li>
<li><strong>Comunidad de propietarios no modelada</strong>: súmala a las deudas mensuales.</li>
<li><strong>Tipo variable necesita stress test</strong>: recalcula con +2 puntos.</li>
</ul>
<h3>Se combina con</h3>
<ul>
<li><strong>loan-calculator</strong> — cuadro de amortización completo.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Avant de tomber amoureux d'une annonce, mieux vaut connaître son plafond. Cette calculatrice répond à « combien de maison mon revenu peut-il porter ? » en inversant le calcul hypothécaire standard : elle demande quel prix d'achat correspond à la mensualité maximale autorisée par votre ratio dette/revenu.</p>
<h3>Comment ça marche</h3>
<ul>
<li><strong>Revenu mensuel</strong> = revenu brut annuel / 12.</li>
<li><strong>Règle DTI</strong> limite la part logement. 28% front-end = PITI seul ; 36% back-end = PITI + autres dettes (en France le taux d'endettement maxi est ~35%).</li>
<li><strong>PITI</strong> = capital, intérêts, taxes (foncière), assurance.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>PMI absent</strong> — pertinent US, pas FR.</li>
<li><strong>Charges de copro non modélisées</strong> : ajoutez-les aux dettes mensuelles.</li>
<li><strong>Taux variable</strong> : recalculez avec +2 points.</li>
</ul>
<h3>Se combine avec</h3>
<ul>
<li><strong>loan-calculator</strong> — tableau d'amortissement complet.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Prima di innamorarti di un annuncio, conviene conoscere il tetto. Questa calcolatrice risponde "quanta casa può sostenere il mio reddito?" invertendo la matematica del mutuo: chiede quale prezzo corrisponde alla rata massima consentita dal tuo rapporto debito/reddito.</p>
<h3>Come funziona</h3>
<ul>
<li><strong>Reddito mensile</strong> = reddito lordo annuo / 12.</li>
<li><strong>Regola DTI</strong> limita la spesa abitativa. 28% front-end = solo PITI; 36% back-end = PITI + tutti i debiti (in Italia di norma rata &lt;= 1/3 del reddito).</li>
<li><strong>PITI</strong> = capitale, interessi, tasse (IMU), assicurazione.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>PMI non incluso</strong> — rilevante US, non IT.</li>
<li><strong>Spese condominiali non modellate</strong>: aggiungile ai debiti mensili.</li>
<li><strong>Tasso variabile</strong>: ricalcola con +2 punti.</li>
</ul>
<h3>Si combina con</h3>
<ul>
<li><strong>loan-calculator</strong> — piano di ammortamento completo.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Zanim zakochasz się w ofercie, warto poznać sufit. Ten kalkulator odpowiada "ile mieszkania/domu uniesie mój dochód?", odwracając standardową matematykę hipoteczną: pyta, jaka cena odpowiada maksymalnej miesięcznej racie dopuszczalnej przez twój wskaźnik dług/dochód.</p>
<h3>Jak to działa</h3>
<ul>
<li><strong>Dochód miesięczny</strong> = roczny brutto / 12.</li>
<li><strong>Reguła DTI</strong> ogranicza wydatki mieszkaniowe. 28% front-end = tylko PITI; 36% back-end = PITI + wszystkie zobowiązania. W Polsce KNF zaleca DStI &lt;= 40–50% w zależności od dochodu.</li>
<li><strong>PITI</strong> = kapitał, odsetki, podatki (od nieruchomości), ubezpieczenie.</li>
</ul>
<h3>Częste pułapki</h3>
<ul>
<li><strong>Brak PMI</strong> — dotyczy głównie US.</li>
<li><strong>Czynsz administracyjny</strong> nie jest modelowany — dodaj do miesięcznych zobowiązań.</li>
<li><strong>Stopa zmienna wymaga stress testu</strong> — przelicz z +2 punktami.</li>
<li><strong>WIBOR/WIRON</strong> kontra stała stopa to oddzielna decyzja — tu zakładamy stałą stopę.</li>
</ul>
<h3>Łączy się z</h3>
<ul>
<li><strong>loan-calculator</strong> — pełen harmonogram spłat.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>物件に恋する前に、上限を知っておく価値があります。本ツールは「自分の収入で買える家はいくらか」という問いに、住宅ローンの標準計算を逆向きに解くことで答えます。400,000 ドルの家の月々の支払額を尋ねる代わりに、債務収入比（DTI）が許す最大月支払額に対応する物件価格を計算します。</p>
<h3>仕組み</h3>
<ul>
<li><strong>月収</strong>＝年税前収入 ÷ 12。</li>
<li><strong>DTI ルール</strong>は住宅関連支出を月収の一定割合に制限します。28% フロントエンド＝ PITI のみ／36% バックエンド＝ PITI ＋全リカリング負債。日本では返済比率 25〜30% が一般的なライン。</li>
<li><strong>PITI</strong>＝元金、利息、税金（固定資産税）、保険。年率に対する月利は r / 12。</li>
</ul>
<h3>よくある注意点</h3>
<ul>
<li><strong>PMI（民間住宅ローン保険）は含まれません。</strong> 米国の話で、頭金 20% 未満の場合に必要です。</li>
<li><strong>管理費・修繕積立金は未考慮。</strong> マンションの場合、月々の負債に加えてください。</li>
<li><strong>変動金利はストレステストを。</strong> +2 ポイントで再計算し、依然として無理なく払えるか確認してください。</li>
</ul>
<h3>組み合わせ</h3>
<ul>
<li><strong>loan-calculator</strong> ── 価格を決めた後の月次償却表と繰上返済シナリオ。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Voordat je verliefd wordt op een listing, is het waard om het plafond te kennen. Deze calculator beantwoordt "hoeveel huis kan mijn inkomen dragen?" door de standaard-hypotheek-mathematica om te draaien: wat is de huisprijs die correspondeert met de maximale maandlast die je debt-to-income ratio toelaat?</p>
<h3>Hoe het werkt</h3>
<ul>
<li><strong>Maandinkomen</strong> = bruto-jaarinkomen / 12.</li>
<li><strong>DTI-regel</strong> limiteert woonlasten als percentage van dat maandinkomen. 28% front-end = alleen PITI; 36% back-end = PITI + autoleningen + studieleningen + creditcard-minima.</li>
<li><strong>PITI</strong> = principal, interest, taxes, insurance. In NL ~1% OZB + opstal- en inboedelverzekering.</li>
</ul>
<h3>Veelvoorkomende valkuilen</h3>
<ul>
<li><strong>NHG en hypotheekrenteaftrek niet gemodelleerd</strong> — die zijn NL-specifiek en verlagen de effectieve maandlast.</li>
<li><strong>VvE-bijdrage niet meegenomen</strong>: tel die op bij maandelijkse schulden.</li>
<li><strong>Variabele rente vraagt stresstest</strong> — herreken bij +2 procentpunten.</li>
</ul>
<h3>Combineert met</h3>
<ul>
<li><strong>loan-calculator</strong> — volledige aflossingsschema.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Bir ilana aşık olmadan önce, tavanı bilmeye değer. Bu hesaplayıcı standart mortgage matematiğini tersine çevirerek "gelirim ne kadar evi taşır?" sorusuna cevap verir: borç-gelir oranının izin verdiği maksimum aylık ödemeye karşılık gelen ev fiyatını sorar.</p>
<h3>Nasıl çalışır</h3>
<ul>
<li><strong>Aylık gelir</strong> = brüt yıllık / 12.</li>
<li><strong>DTI kuralı</strong> konut harcamasını sınırlar. 28% front-end = sadece PITI; 36% back-end = PITI + tüm borçlar. Türkiye'de kredi notu ve gelir belgesine göre bankalar farklı eşikler uygular.</li>
<li><strong>PITI</strong> = anapara, faiz, vergi (emlak), sigorta.</li>
</ul>
<h3>Sık yapılan hatalar</h3>
<ul>
<li><strong>PMI dahil değil</strong> — US'ye özgü.</li>
<li><strong>Aidat dahil değil</strong>: aylık borçlara ekle.</li>
<li><strong>Değişken faiz</strong>: +2 puanla yeniden hesapla.</li>
<li><strong>TÜFE-endeksli kredi</strong> ayrı bir hesap gerektirir; burada sabit faiz varsayılır.</li>
</ul>
<h3>Eşleşir</h3>
<ul>
<li><strong>loan-calculator</strong> — tam amortisman tablosu.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Sebelum jatuh cinta sama listing, ada baiknya tahu plafon. Kalkulator ini menjawab "berapa rumah yang bisa ditopang pendapatan saya?" dengan membalik matematika KPR standar: berapa harga rumah yang sesuai dengan cicilan maksimum yang diizinkan rasio utang-pendapatan.</p>
<h3>Cara kerja</h3>
<ul>
<li><strong>Pendapatan bulanan</strong> = bruto tahunan / 12.</li>
<li><strong>Aturan DTI</strong> membatasi pengeluaran perumahan. 28% front-end = hanya PITI; 36% back-end = PITI + semua utang. Di Indonesia bank umumnya pakai 30–40% sebagai batas DBR.</li>
<li><strong>PITI</strong> = pokok, bunga, pajak (PBB), asuransi.</li>
</ul>
<h3>Kesalahan umum</h3>
<ul>
<li><strong>PMI tidak termasuk</strong> — itu US, di Indonesia ada premi asuransi jiwa kredit yang sering sudah dipotong dari plafon.</li>
<li><strong>IPL / service charge apartemen</strong> tidak dimodelkan; tambahkan ke utang bulanan.</li>
<li><strong>Bunga floating</strong>: re-test dengan +2 poin di atas suku bunga sekarang.</li>
</ul>
<h3>Pasangan</h3>
<ul>
<li><strong>loan-calculator</strong> — tabel amortisasi lengkap.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Trước khi yêu một listing nhà, đáng để biết trần ngân sách. Máy tính này trả lời "thu nhập của tôi gánh nổi nhà bao nhiêu?" bằng cách đảo ngược toán vay mua nhà chuẩn: nó hỏi giá nhà nào ứng với khoản trả hàng tháng tối đa mà tỷ lệ nợ-thu nhập (DTI) cho phép.</p>
<h3>Cách hoạt động</h3>
<ul>
<li><strong>Thu nhập tháng</strong> = thu nhập gộp năm / 12.</li>
<li><strong>Quy tắc DTI</strong> giới hạn chi phí nhà ở. 28% front-end = chỉ PITI; 36% back-end = PITI + tất cả nợ định kỳ.</li>
<li><strong>PITI</strong> = gốc, lãi, thuế (nhà đất), bảo hiểm.</li>
</ul>
<h3>Lưu ý thường gặp</h3>
<ul>
<li><strong>PMI không tính</strong> — chỉ áp dụng US.</li>
<li><strong>Phí quản lý chung cư</strong> không mô hình hóa; cộng vào nợ hàng tháng.</li>
<li><strong>Lãi thả nổi cần stress test</strong> — tính lại với +2 điểm.</li>
</ul>
<h3>Đi cùng</h3>
<ul>
<li><strong>loan-calculator</strong> — bảng khấu trừ đầy đủ.</li>
</ul>
""",
        "hi": """
<h2>यह किसके लिए है?</h2>
<p>एक listing से प्यार हो जाने से पहले, ceiling जानना worth है। यह calculator answer करता है कि "मेरी income कितना घर support कर सकती है?" standard mortgage math को invert करके: यह पूछता है कि कौन सी घर की कीमत आपके debt-to-income ratio द्वारा allowed maximum monthly payment से correspond करती है।</p>
<h3>यह कैसे काम करता है</h3>
<ul>
<li><strong>Monthly income</strong> = gross annual / 12।</li>
<li><strong>DTI rule</strong> housing-related खर्च को उस monthly income के percentage पर cap करता है। 28% front-end means केवल PITI; 36% back-end means PITI + car loans + student loans + minimum credit-card payments।</li>
<li><strong>PITI</strong> stands for principal, interest, taxes, insurance। P&amp;I को standard amortization formula से solve किया जाता है।</li>
</ul>
<h3>आम गलतियाँ</h3>
<ul>
<li><strong>PMI included नहीं है।</strong> यदि down payment 20% से कम है, तो 0.3–1.5% loan amount/year की private mortgage insurance expect करें।</li>
<li><strong>Society maintenance modeled नहीं।</strong> Apartment के लिए, monthly debts में जोड़ें या mentally adjust करें।</li>
<li><strong>Variable-rate mortgages को stress test चाहिए।</strong> यदि आपकी rate 2 percentage points बढ़ सकती है, तो higher rate पर recompute करें।</li>
</ul>
<h3>साथ pairs</h3>
<ul>
<li><strong>loan-calculator</strong> — पूरी month-by-month amortization।</li>
</ul>
""",
        "sk": """
<h2>Načo to slúži?</h2>
<p>Než sa zaľúbiš do inzerátu, oplatí sa poznať strop. Táto kalkulačka odpovedá na otázku "akú drahú nehnuteľnosť unesie môj príjem?" obrátením štandardnej hypotekárnej matematiky: pýta sa, akej cene domu zodpovedá maximálna mesačná splátka, ktorú dovoľuje pomer dlh/príjem.</p>
<h3>Ako to funguje</h3>
<ul>
<li><strong>Mesačný príjem</strong> = ročný brutto / 12.</li>
<li><strong>Pravidlo DTI</strong> obmedzuje výdavky na bývanie na percento z mesačného príjmu. 28% front-end = len PITI; 36% back-end = PITI + všetky pravidelné dlhy. V SK NBS odporúča DTI &lt;= 8× ročný príjem a DSTI &lt;= 60%.</li>
<li><strong>PITI</strong> = istina, úroky, daň (z nehnuteľnosti), poistenie.</li>
</ul>
<h3>Časté chyby</h3>
<ul>
<li><strong>Bez PMI</strong> — americká vec.</li>
<li><strong>Bez fondu opráv</strong> v bytovke; pripočítaj k mesačným dlhom.</li>
<li><strong>Variabilný úrok</strong>: prepočítaj s +2 b. b.</li>
</ul>
<h3>Spolu s</h3>
<ul>
<li><strong>loan-calculator</strong> — splátkový kalendár.</li>
</ul>
""",
        "cs": """
<h2>K čemu to slouží?</h2>
<p>Než se zamiluješ do inzerátu, vyplatí se znát strop. Tahle kalkulačka odpovídá na otázku "jak drahou nemovitost unese můj příjem?" obrácením standardní hypoteční matematiky: ptá se, jaké ceně domu odpovídá maximální měsíční splátka, kterou dovoluje poměr dluh/příjem.</p>
<h3>Jak to funguje</h3>
<ul>
<li><strong>Měsíční příjem</strong> = roční brutto / 12.</li>
<li><strong>Pravidlo DTI</strong> omezuje výdaje na bydlení na procento z měsíčního příjmu. 28% front-end = pouze PITI; 36% back-end = PITI + všechny pravidelné dluhy. V ČR ČNB doporučuje DTI &lt;= 8× roční příjem a DSTI &lt;= 45%.</li>
<li><strong>PITI</strong> = jistina, úroky, daň (z nemovitostí), pojištění.</li>
</ul>
<h3>Časté chyby</h3>
<ul>
<li><strong>Bez PMI</strong> — americká věc.</li>
<li><strong>Bez fondu oprav</strong> u bytu; přičti k měsíčním dluhům.</li>
<li><strong>Variabilní úrok</strong>: přepočítej s +2 b. b.</li>
</ul>
<h3>Spolu s</h3>
<ul>
<li><strong>loan-calculator</strong> — splátkový kalendář.</li>
</ul>
""",
    },
    "related": ["loan-calculator", "percentage-calculator", "currency-converter"],
    "howto": {"flow": "calculate", "action": "format", "noun": "affordability"},
}
