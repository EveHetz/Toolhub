TOOL = {
    "slug": "loan-calculator",
    "category": "math",
    "icon": "🏦",
    "tags": ["loan", "mortgage", "calculator", "interest", "amortization", "monthly", "payment"],
    "i18n": {
        "en": {
            "name": "Loan Calculator",
            "tagline": "Compute monthly payment, total interest, and full amortization schedule for any loan. Fixed-rate, simple-interest, principal+interest. Browser-only.",
            "description": "Free loan / mortgage calculator. Enter principal, annual interest rate, term in years (or months), get back: monthly payment, total interest paid over the loan's life, total amount paid, and a full month-by-month amortization schedule (principal portion + interest portion + remaining balance for every month). Useful for mortgage shopping, car loans, personal loans. Pure JS — no upload, no broker referrals.",
        },
        "de": {"name": "Kreditrechner", "tagline": "Monatsrate, Gesamtzinsen und kompletten Tilgungsplan für jeden Kredit berechnen. Festzinssatz, Annuitätenkredit. Nur Browser.", "description": "Kostenloser Kredit-/Hypothekenrechner. Gib Kreditsumme, Jahreszins und Laufzeit in Jahren (oder Monaten) ein und erhalte: Monatsrate, gesamte Zinskosten über die Laufzeit, Gesamtsumme und vollständigen Tilgungsplan (Tilgungs- und Zinsanteil + Restschuld pro Monat). Nützlich für Hypothekenvergleich, Autokredite, Privatkredite. Reines JavaScript — kein Upload, keine Vermittler."},
        "es": {"name": "Calculadora de Préstamos", "tagline": "Calcula cuota mensual, intereses totales y cuadro de amortización completo. Tipo fijo, sistema francés. Solo en navegador.", "description": "Calculadora gratuita de préstamos e hipotecas. Introduce capital, tipo de interés anual y plazo en años (o meses): obtén cuota mensual, intereses totales pagados durante la vida del préstamo, importe total y cuadro de amortización mes a mes (capital + intereses + saldo pendiente cada mes). Útil para comparar hipotecas, créditos coche, préstamos personales."},
        "fr": {"name": "Calculatrice de Prêt", "tagline": "Calculez la mensualité, le total d'intérêts et le tableau d'amortissement complet. Taux fixe, amortissement constant. Navigateur seul.", "description": "Calculatrice gratuite de prêt / crédit immobilier. Saisissez capital, taux d'intérêt annuel et durée en années (ou mois) : obtenez mensualité, total d'intérêts payés sur la vie du prêt, montant total et tableau d'amortissement mois par mois (capital + intérêts + capital restant dû). Utile pour comparer prêts immo, crédits auto, prêts perso."},
        "it": {"name": "Calcolatore di Prestiti", "tagline": "Calcola rata mensile, interessi totali e piano di ammortamento completo. Tasso fisso, francese. Solo browser.", "description": "Calcolatore gratuito di prestiti / mutui. Inserisci capitale, tasso d'interesse annuo e durata in anni (o mesi): ottieni rata mensile, interessi totali pagati nella vita del prestito, importo totale e piano di ammortamento mese per mese (quota capitale + quota interessi + debito residuo per ogni mese). Utile per confrontare mutui, prestiti auto, prestiti personali."},
        "pt": {"name": "Calculadora de Empréstimo", "tagline": "Calcule a parcela mensal, juros totais e a tabela de amortização completa de qualquer empréstimo. Taxa fixa, sistema Price. Só no navegador.", "description": "Calculadora gratuita de empréstimo / financiamento. Informe principal, taxa de juros anual e prazo em anos (ou meses) e veja: parcela mensal, total de juros pagos durante a vida do empréstimo, valor total pago, e a tabela de amortização mês a mês completa (parcela de principal + parcela de juros + saldo devedor de cada mês). Útil para comparar financiamento imobiliário, financiamento de carro, empréstimo pessoal. Puro JS — sem upload, sem indicações de corretor."},
        "pl": {"name": "Kalkulator Kredytu", "tagline": "Policz miesięczną ratę, łączne odsetki i pełny harmonogram spłat dla dowolnego kredytu. Stała stopa, raty równe. Tylko przeglądarka.", "description": "Darmowy kalkulator kredytu / hipoteki. Wpisz kwotę, oprocentowanie roczne i okres w latach (lub miesiącach), żeby dostać: miesięczną ratę, łączne odsetki zapłacone w ciągu kredytu, łączną kwotę spłaty i pełny harmonogram spłat miesiąc po miesiącu (część kapitałowa + część odsetkowa + saldo pozostałe do spłaty na każdy miesiąc). Przydatne do porównywania hipotek, kredytów samochodowych, gotówkowych. Czysty JS — bez uploadu, bez pośredników."},
        "ja": {"name": "ローン計算機", "tagline": "任意のローンの月々返済額、総利息、完全な償却スケジュールを計算。固定金利、元利均等。ブラウザのみ。", "description": "無料のローン／住宅ローン計算ツール。元本、年利、返済期間（年または月）を入力すると、月々返済額、ローン期間全体での総利息、総支払額、月ごとの完全な償却スケジュール（元金部分＋利息部分＋残高）が得られます。住宅ローン比較、自動車ローン、個人ローンに便利。サーバーへ何も送信しない純粋な JavaScript。"},
        "nl": {"name": "Lening-calculator", "tagline": "Bereken maandlast, totale rente en volledig aflossingsschema voor elke lening. Vaste rente, annuïteit. Alleen browser.", "description": "Gratis lening- / hypotheek-calculator. Voer hoofdsom, jaarrente en looptijd in jaren (of maanden) in, krijg terug: maandbedrag, totaal aan rente over de looptijd, totaal betaald bedrag, en een volledig maandelijks aflossingsschema (aflossings-deel + rente-deel + resterend saldo per maand). Nuttig voor hypotheekvergelijken, autoleningen, persoonlijke leningen."},
        "tr": {"name": "Kredi Hesaplayıcı", "tagline": "Herhangi bir kredi için aylık ödeme, toplam faiz ve tam amortisman tablosu hesapla. Sabit oran, eşit taksit. Sadece tarayıcı.", "description": "Ücretsiz kredi / mortgage hesaplayıcı. Anapara, yıllık faiz oranı ve vade (yıl ya da ay) gir, geri al: aylık ödeme, kredi ömrü boyunca ödenen toplam faiz, ödenen toplam tutar ve aydan aya tam amortisman tablosu (her ay için anapara payı + faiz payı + kalan bakiye). Konut kredisi, taşıt kredisi, ihtiyaç kredisi karşılaştırması için faydalı."},
        "id": {"name": "Kalkulator Pinjaman", "tagline": "Hitung cicilan bulanan, total bunga, dan tabel amortisasi lengkap untuk pinjaman apa pun. Bunga tetap, anuitas. Hanya browser.", "description": "Kalkulator pinjaman / KPR gratis. Masukkan pokok, bunga tahunan, dan tenor dalam tahun (atau bulan): dapatkan cicilan bulanan, total bunga selama umur pinjaman, total dibayar, dan tabel amortisasi bulan demi bulan lengkap (porsi pokok + porsi bunga + saldo tersisa setiap bulan). Berguna untuk membandingkan KPR, kredit mobil, KTA."},
        "vi": {"name": "Máy tính Khoản vay", "tagline": "Tính khoản trả hàng tháng, tổng lãi và lịch khấu trừ đầy đủ cho bất kỳ khoản vay nào. Lãi suất cố định, gốc+lãi. Chỉ trình duyệt.", "description": "Máy tính khoản vay / vay mua nhà miễn phí. Nhập principal, lãi suất hàng năm, kỳ hạn theo năm (hoặc tháng), nhận lại: khoản trả hàng tháng, tổng lãi đã trả qua đời khoản vay, tổng số tiền đã trả, và bảng amortization đầy đủ theo tháng (phần gốc + phần lãi + số dư còn lại cho mỗi tháng). Hữu ích cho mua sắm vay mua nhà, vay mua xe, vay cá nhân."},
        "hi": {"name": "Loan Calculator", "tagline": "किसी भी loan के लिए monthly payment, total interest, और पूरा amortization schedule compute करें। Fixed-rate, simple-interest, principal+interest। Browser-only।", "description": "मुफ़्त loan / mortgage calculator। principal, annual interest rate, term in years (या months) डालें, वापस पाएं: monthly payment, loan के जीवन भर का total interest, total amount paid, और पूरा month-by-month amortization schedule (principal portion + interest portion + remaining balance हर month के लिए)। Mortgage shopping, car loans, personal loans के लिए useful। Pure JS — कोई upload नहीं, कोई broker referrals नहीं।"},
        "sk": {"name": "Kalkulačka pôžičky", "tagline": "Vypočíta mesačnú splátku, celkové úroky a kompletný splátkový kalendár pre akúkoľvek pôžičku. Fixná sadzba, anuitné splácanie. Iba v prehliadači.", "description": "Bezplatná kalkulačka pôžičky / hypotéky. Zadaj istinu, ročnú úrokovú sadzbu a dobu splácania v rokoch (alebo mesiacoch): dostaneš mesačnú splátku, celkové úroky za dobu pôžičky, celkovú zaplatenú sumu a kompletný splátkový kalendár mesiac po mesiaci (časť istiny + časť úroku + zostatok dlhu pre každý mesiac). Užitočné pri porovnávaní hypoték, autopôžičiek, spotrebných úverov."},
        "cs": {"name": "Kalkulačka úvěru", "tagline": "Vypočítá měsíční splátku, celkové úroky a kompletní splátkový kalendář pro jakýkoli úvěr. Fixní sazba, anuitní splácení. Pouze v prohlížeči.", "description": "Bezplatná kalkulačka úvěru / hypotéky. Zadej jistinu, roční úrokovou sazbu a dobu splácení v letech (nebo měsících): dostaneš měsíční splátku, celkové úroky za dobu úvěru, celkovou zaplacenou sumu a kompletní splátkový kalendář měsíc po měsíci (část jistiny + část úroku + zůstatek dluhu pro každý měsíc). Užitečné při porovnávání hypoték, autoúvěrů, spotřebitelských úvěrů."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Principal (loan amount)</label>
      <input type="number" id="ln-principal" step="any" min="0" value="250000" oninput="lnRun()">
    </div>
    <div>
      <label>Interest rate (annual %)</label>
      <input type="number" id="ln-rate" step="0.01" min="0" value="6.5" oninput="lnRun()">
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Term</label>
      <input type="number" id="ln-term" step="1" min="1" value="30" oninput="lnRun()">
    </div>
    <div>
      <label>Term unit</label>
      <select id="ln-unit" onchange="lnRun()">
        <option value="years" selected>Years</option>
        <option value="months">Months</option>
      </select>
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Extra payment per month (optional)</label>
      <input type="number" id="ln-extra" step="any" min="0" value="0" oninput="lnRun()">
    </div>
    <div>
      <label>Currency symbol</label>
      <input type="text" id="ln-cur" maxlength="4" value="$" oninput="lnRun()">
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="ln-out" class="output"></div>
</div>
""",
    "script": """
<style>
.ln-hero{background:var(--accent);color:#fff;padding:1rem 1.2rem;border-radius:8px;text-align:center;margin-bottom:0.8rem}
.ln-hero .ln-big{font-family:ui-monospace,monospace;font-size:1.8rem;font-weight:700;line-height:1.1}
.ln-hero .ln-sub{font-size:0.82rem;opacity:0.9;margin-top:0.25rem}
.ln-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:0.6rem;margin-bottom:0.8rem}
.ln-stat{background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;padding:0.7rem 0.85rem}
.ln-stat .ln-num{font-family:ui-monospace,monospace;font-size:1.05rem;font-weight:600;color:var(--accent);word-break:break-all}
.ln-stat .ln-lbl{font-size:0.74rem;color:var(--text-muted);margin-top:0.15rem}
.ln-chart{height:60px;background:var(--bg-elev);border:1px solid var(--border);border-radius:6px;overflow:hidden;display:flex;margin-bottom:0.5rem}
.ln-chart-p{background:var(--accent)}
.ln-chart-i{background:#c97a4a}
.ln-legend{font-size:0.75rem;color:var(--text-muted);display:flex;gap:1rem;margin-bottom:0.7rem}
.ln-legend span::before{content:'';display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:0.4rem;vertical-align:middle}
.ln-legend .ln-l-p::before{background:var(--accent)}
.ln-legend .ln-l-i::before{background:#c97a4a}
.ln-tab{width:100%;border-collapse:collapse;font-family:ui-monospace,monospace;font-size:0.78rem}
.ln-tab th,.ln-tab td{padding:0.3rem 0.4rem;border-bottom:1px solid var(--border);text-align:right}
.ln-tab th{color:var(--text-muted);font-weight:600;text-align:right;background:var(--bg-elev);position:sticky;top:0}
.ln-tab th:first-child,.ln-tab td:first-child{text-align:left;color:var(--text-muted)}
.ln-tab-wrap{max-height:340px;overflow:auto;border:1px solid var(--border);border-radius:6px}
.ln-extra-note{background:var(--bg-elev);border-left:3px solid var(--accent);padding:0.6rem 0.85rem;border-radius:0 6px 6px 0;font-size:0.85rem;margin:0.6rem 0;color:var(--text)}
.ln-page{display:flex;gap:0.5rem;align-items:center;justify-content:flex-end;margin-top:0.5rem;font-size:0.78rem;color:var(--text-muted)}
.ln-page button{padding:0.3rem 0.6rem;font-size:0.78rem}
</style>
<script>
const LN_STATE = { rows: [], extraRows: [], page: 0, pageSize: 60 };
function lnFmt(n, cur){
  if(!isFinite(n)) return '—';
  const r = Math.round(n*100)/100;
  return cur + r.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
}
function lnAmortize(principal, monthlyRate, months, extra){
  const rows = [];
  let bal = principal;
  let basePayment;
  if(monthlyRate === 0){
    basePayment = principal / months;
  } else {
    const pow = Math.pow(1+monthlyRate, months);
    basePayment = principal * (monthlyRate * pow) / (pow - 1);
  }
  let totalInterest = 0;
  let m = 0;
  while(bal > 0.005 && m < months + 600){
    m++;
    const interest = bal * monthlyRate;
    let principalPart = basePayment - interest + extra;
    if(principalPart > bal) principalPart = bal;
    const payment = principalPart + interest;
    bal -= principalPart;
    if(bal < 0.005) bal = 0;
    totalInterest += interest;
    rows.push({month: m, payment, principal: principalPart, interest, balance: bal});
    if(extra <= 0 && m >= months) break;
  }
  return { rows, totalInterest, basePayment, payments: rows.length };
}
function lnRun(){
  const principal = parseFloat(document.getElementById('ln-principal').value) || 0;
  const annualRate = parseFloat(document.getElementById('ln-rate').value) || 0;
  const term = parseFloat(document.getElementById('ln-term').value) || 0;
  const unit = document.getElementById('ln-unit').value;
  const extra = parseFloat(document.getElementById('ln-extra').value) || 0;
  const cur = document.getElementById('ln-cur').value || '';
  const out = document.getElementById('ln-out');
  if(principal <= 0 || term <= 0){ out.textContent = '{LBL_NO_INPUT}'; return; }
  const months = Math.round(unit === 'years' ? term * 12 : term);
  const monthlyRate = (annualRate/100) / 12;
  const base = lnAmortize(principal, monthlyRate, months, 0);
  const withExtra = extra > 0 ? lnAmortize(principal, monthlyRate, months, extra) : null;
  LN_STATE.rows = (withExtra ? withExtra.rows : base.rows);
  LN_STATE.page = 0;
  const monthlyPayment = base.basePayment;
  const totalPaid = monthlyPayment * months;
  const totalInterest = base.totalInterest;
  let extraBlock = '';
  if(withExtra){
    const monthsSaved = months - withExtra.payments;
    const interestSaved = base.totalInterest - withExtra.totalInterest;
    const yearsSavedTxt = monthsSaved >= 12
      ? Math.floor(monthsSaved/12) + 'y ' + (monthsSaved%12) + 'mo'
      : monthsSaved + ' month' + (monthsSaved===1?'':'s');
    extraBlock = `<div class="ln-extra-note"><strong>Extra ${lnFmt(extra, cur)}/month saves ${yearsSavedTxt}</strong> and ${lnFmt(interestSaved, cur)} in interest. Payoff in ${withExtra.payments} months instead of ${months}.</div>`;
  }
  const pPct = totalPaid > 0 ? (principal / totalPaid * 100) : 0;
  const iPct = 100 - pPct;
  out.innerHTML = `
    <div class="ln-hero">
      <div class="ln-big">${lnFmt(monthlyPayment, cur)}</div>
      <div class="ln-sub">Monthly payment over ${months} months${withExtra ? ' (base, before extra)' : ''}</div>
    </div>
    <div class="ln-grid">
      <div class="ln-stat"><div class="ln-num">${lnFmt(principal, cur)}</div><div class="ln-lbl">Principal</div></div>
      <div class="ln-stat"><div class="ln-num">${lnFmt(totalInterest, cur)}</div><div class="ln-lbl">Total interest (base)</div></div>
      <div class="ln-stat"><div class="ln-num">${lnFmt(totalPaid, cur)}</div><div class="ln-lbl">Total paid (base)</div></div>
      <div class="ln-stat"><div class="ln-num">${(annualRate).toFixed(2)}%</div><div class="ln-lbl">Annual rate</div></div>
    </div>
    <div class="ln-chart"><div class="ln-chart-p" style="width:${pPct.toFixed(2)}%"></div><div class="ln-chart-i" style="width:${iPct.toFixed(2)}%"></div></div>
    <div class="ln-legend"><span class="ln-l-p">Principal ${pPct.toFixed(1)}%</span><span class="ln-l-i">Interest ${iPct.toFixed(1)}%</span></div>
    ${extraBlock}
    <div><strong>Amortization schedule${withExtra ? ' (with extra payments)' : ''}</strong></div>
    <div id="ln-tab-host" style="margin-top:0.4rem"></div>
    <div class="ln-page">
      <button type="button" class="secondary" onclick="lnPagePrev()">‹ Prev</button>
      <span id="ln-page-info"></span>
      <button type="button" class="secondary" onclick="lnPageNext()">Next ›</button>
    </div>
  `;
  lnRenderTable(cur);
}
function lnRenderTable(cur){
  cur = cur || document.getElementById('ln-cur').value || '';
  const host = document.getElementById('ln-tab-host');
  if(!host) return;
  const rows = LN_STATE.rows;
  const total = rows.length;
  const pages = Math.max(1, Math.ceil(total / LN_STATE.pageSize));
  if(LN_STATE.page >= pages) LN_STATE.page = pages - 1;
  if(LN_STATE.page < 0) LN_STATE.page = 0;
  const start = LN_STATE.page * LN_STATE.pageSize;
  const slice = rows.slice(start, start + LN_STATE.pageSize);
  const body = slice.map(r => `<tr><td>${r.month}</td><td>${lnFmt(r.payment, cur)}</td><td>${lnFmt(r.principal, cur)}</td><td>${lnFmt(r.interest, cur)}</td><td>${lnFmt(r.balance, cur)}</td></tr>`).join('');
  host.innerHTML = `
    <div class="ln-tab-wrap">
      <table class="ln-tab">
        <thead><tr><th>Month</th><th>Payment</th><th>Principal</th><th>Interest</th><th>Balance</th></tr></thead>
        <tbody>${body}</tbody>
      </table>
    </div>
  `;
  const info = document.getElementById('ln-page-info');
  if(info) info.textContent = `Page ${LN_STATE.page + 1} of ${pages} · ${total} payments`;
}
function lnPagePrev(){ LN_STATE.page = Math.max(0, LN_STATE.page - 1); lnRenderTable(); }
function lnPageNext(){
  const pages = Math.max(1, Math.ceil(LN_STATE.rows.length / LN_STATE.pageSize));
  LN_STATE.page = Math.min(pages - 1, LN_STATE.page + 1);
  lnRenderTable();
}
document.addEventListener('DOMContentLoaded', lnRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>For any fixed-rate loan — mortgage, car, personal — the monthly payment, total interest, and balance trajectory are fully determined by three numbers: principal, rate, and term. This tool computes all of them and renders the month-by-month amortization schedule so you can see exactly where each payment goes. The extra-payment slider lets you check the impact of paying a little above the required amount, which on a mortgage often shortens the loan by years.</p>

<h3>The amortization formula</h3>
<p>For a loan of principal <code>L</code> at monthly rate <code>r</code> over <code>n</code> months, the fixed monthly payment <code>P</code> that exactly pays it off is:</p>
<pre>P = L × r(1+r)^n / ((1+r)^n − 1)</pre>
<p>Each month the interest accrued is <code>balance × r</code>; the rest of the payment chips away at principal. Early in the loan, most of the payment is interest; late in the loan, most is principal. That's why paying extra <em>early</em> saves disproportionately more interest than paying extra late.</p>

<h3>When to use it</h3>
<ul>
  <li><strong>Mortgage shopping.</strong> Compare 15-year vs 30-year terms or two different rates side by side.</li>
  <li><strong>Car loans.</strong> See the real cost of a "0% APR" vs a rebate-and-finance offer.</li>
  <li><strong>Personal loans / debt consolidation.</strong> Decide whether a lower rate over a longer term saves money or just spreads pain.</li>
  <li><strong>Extra-payment planning.</strong> Test "$200/month extra" or "lump sum once a year" scenarios.</li>
  <li><strong>Refinance check.</strong> Compute remaining interest at the current rate, then re-enter the smaller balance at the new rate and term.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>APR ≠ note rate.</strong> The annual percentage rate (APR) in disclosures includes fees and points; the "note rate" here is the bare interest rate. APR is the better number for comparing loans, but the note rate is what computes your payment.</li>
  <li><strong>Compounding convention.</strong> US mortgages compound monthly: monthly rate = annual / 12. Canadian mortgages compound semi-annually by law (so monthly rate is slightly different). This calculator uses simple monthly compounding — adjust if you're modelling a Canadian or unusual product.</li>
  <li><strong>Escrow / impounds aren't shown.</strong> Your mortgage servicer usually adds property tax and insurance to your monthly payment and pays them on your behalf. That's not included here — see mortgage-affordability-calculator for PITI.</li>
  <li><strong>Variable-rate loans.</strong> ARM, tracker, or variable-rate mortgages re-calculate after each rate change. This tool assumes a single fixed rate for the full term — useful as a "if rate stayed flat" baseline, not a forecast.</li>
  <li><strong>Prepayment penalties.</strong> Some loans (esp. US auto and short-term mortgages from before 2010) charge a fee for paying extra. Read your terms before relying on the "extra payment saves Y interest" figure.</li>
  <li><strong>Rounding.</strong> Banks round each monthly payment to cents and absorb the final cent or two in the last payment. Our schedule does the same — the last row's balance is forced to zero.</li>
</ul>

<h3>Pairs with</h3>
<ul>
  <li><strong>mortgage-affordability-calculator</strong> — work backwards from your income to a max price, then use this tool to see the schedule.</li>
  <li><strong>percentage-calculator</strong> — quick check on rate changes (e.g. what's 6.5% × 1.1?).</li>
  <li><strong>currency-converter</strong> — if you're modelling a loan in a foreign currency.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Para qualquer empréstimo de taxa fixa — imobiliário, carro, pessoal — a parcela mensal, o total de juros e a trajetória do saldo são totalmente determinados por três números: principal, taxa e prazo. Esta ferramenta calcula todos eles e renderiza a tabela de amortização mês a mês para você ver exatamente para onde vai cada parcela. O slider de pagamento extra deixa você testar o impacto de pagar acima do mínimo — em um financiamento imobiliário isso muitas vezes encurta o prazo em anos.</p>

<h3>A fórmula de amortização</h3>
<p>Para um empréstimo de principal <code>L</code> a taxa mensal <code>r</code> em <code>n</code> meses, a parcela mensal fixa <code>P</code> que zera o saldo é:</p>
<pre>P = L × r(1+r)^n / ((1+r)^n − 1)</pre>
<p>Em cada mês os juros acumulados são <code>saldo × r</code>; o resto da parcela amortiza o principal. No início do contrato, a maior parte é juros; no fim, é amortização. Por isso pagar a mais <em>cedo</em> economiza desproporcionalmente mais juros do que pagar a mais tarde.</p>

<h3>Quando usar</h3>
<ul>
  <li><strong>Comparar financiamentos.</strong> Prazo de 240 meses vs 360 meses, duas taxas diferentes, dois bancos.</li>
  <li><strong>Financiamento de carro.</strong> Veja o custo real de um "0% taxa" vs desconto-à-vista + financiamento.</li>
  <li><strong>Crédito pessoal / consolidação.</strong> Decida se uma taxa menor em prazo maior economiza ou só espalha a dor.</li>
  <li><strong>Planejamento de pagamento extra.</strong> Teste cenários "R$ 500/mês extra" ou "13º salário no fim do ano".</li>
  <li><strong>Refinanciamento.</strong> Calcule juros restantes na taxa atual, depois entre o saldo na nova taxa.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>CET ≠ taxa nominal.</strong> O Custo Efetivo Total (CET) inclui taxas e seguros; a "taxa nominal" aqui é só o juro. CET compara melhor entre bancos, mas a taxa nominal calcula sua parcela.</li>
  <li><strong>Tabela Price vs SAC.</strong> Esta calculadora usa Price (parcelas iguais). No SAC, brasileiro, a amortização é constante e a parcela diminui ao longo do tempo. Para modelar SAC, recalcule manualmente ou veja outra ferramenta.</li>
  <li><strong>Seguros e taxa administrativa não incluídos.</strong> MIP, DFI, taxa de administração aparecem na parcela real mas não aqui — adicione manualmente.</li>
  <li><strong>Empréstimos com taxa variável.</strong> Sistemas indexados a TR, IPCA ou Selic recalculam após cada ajuste. Esta ferramenta assume uma única taxa fixa por todo o prazo — útil como baseline "se a taxa não mudasse".</li>
  <li><strong>Multa por pagamento antecipado.</strong> No Brasil, lei do consumidor garante quitação antecipada com desconto proporcional dos juros — mas vale conferir o contrato.</li>
</ul>

<h3>Combina com</h3>
<ul>
  <li><strong>mortgage-affordability-calculator</strong> — trabalhe ao contrário, da sua renda para o preço máximo, depois use esta ferramenta para ver a tabela.</li>
  <li><strong>percentage-calculator</strong> — verificação rápida de mudanças de taxa.</li>
  <li><strong>currency-converter</strong> — se você está modelando empréstimo em moeda estrangeira.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Für jeden Festzinskredit — Hypothek, Auto, Privat — sind Monatsrate, Gesamtzinsen und Restschuldverlauf vollständig durch drei Zahlen bestimmt: Kreditsumme, Zinssatz, Laufzeit. Dieses Tool berechnet alles und zeigt den Tilgungsplan Monat für Monat. Der Sonderzahlungs-Slider zeigt, wie viel eine kleine Mehrzahlung pro Monat spart.</p>
<h3>Die Annuitäten-Formel</h3>
<pre>P = L × r(1+r)^n / ((1+r)^n − 1)</pre>
<p>Pro Monat sind die Zinsen <code>Saldo × r</code>, der Rest ist Tilgung. Anfangs überwiegen Zinsen, am Ende Tilgung — deshalb spart frühe Sondertilgung überproportional viel.</p>
<h3>Wann verwenden</h3>
<ul>
<li>Hypotheken vergleichen (15 vs 30 Jahre, zwei Zinssätze).</li>
<li>Autokredit-Angebote prüfen.</li>
<li>Sondertilgungs-Szenarien.</li>
<li>Anschlussfinanzierung modellieren.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Effektiver Jahreszins ≠ Nominalzins.</strong> Vergleich nur über den effektiven Zins.</li>
<li><strong>Zinsbindung in DE meist 5/10/15 Jahre.</strong> Diese Berechnung nimmt eine Festrate über die volle Laufzeit an — bei Anschlussfinanzierung neu rechnen.</li>
<li><strong>Sondertilgungsrecht prüfen.</strong> Manche Verträge erlauben nur 5% p.a.</li>
</ul>
<h3>Kombiniert mit</h3>
<ul>
<li><strong>mortgage-affordability-calculator</strong> — Maximalpreis aus Einkommen.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Para cualquier préstamo de tipo fijo — hipoteca, coche, personal — la cuota mensual, los intereses totales y la trayectoria del saldo están totalmente determinados por tres números: capital, tipo, plazo. Esta herramienta calcula todo y muestra el cuadro de amortización mes a mes.</p>
<h3>La fórmula del sistema francés</h3>
<pre>P = L × r(1+r)^n / ((1+r)^n − 1)</pre>
<p>Cada mes los intereses son <code>saldo × r</code>; el resto amortiza capital. Al principio domina la cuota de intereses; al final la amortización.</p>
<h3>Cuándo usarla</h3>
<ul>
<li>Comparar hipotecas (15 vs 30 años, distintos tipos).</li>
<li>Crédito coche, préstamo personal.</li>
<li>Amortización anticipada.</li>
<li>Subrogación o refinanciación.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>TAE ≠ TIN.</strong> Compara siempre por TAE.</li>
<li><strong>Hipoteca variable</strong>: tipo + euríbor. Aquí se asume tipo fijo.</li>
<li><strong>Comisión por amortización.</strong> Revisa antes de confiar en el ahorro mostrado.</li>
</ul>
<h3>Se combina con</h3>
<ul>
<li><strong>mortgage-affordability-calculator</strong>.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Pour tout prêt à taux fixe — immobilier, auto, perso — la mensualité, le total d'intérêts et la trajectoire du capital restant dû sont entièrement déterminés par trois chiffres : capital, taux, durée. Cet outil calcule tout et affiche le tableau d'amortissement mois par mois.</p>
<h3>La formule</h3>
<pre>P = L × r(1+r)^n / ((1+r)^n − 1)</pre>
<p>Chaque mois, les intérêts valent <code>capital restant × r</code> ; le reste amortit. En début de prêt, les intérêts dominent ; en fin, l'amortissement.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Comparer prêts immo (15 vs 25 ans).</li>
<li>Crédit auto, perso.</li>
<li>Remboursement anticipé.</li>
<li>Renégociation, rachat de crédit.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>TAEG ≠ taux nominal.</strong> Le TAEG inclut frais et assurance ; pour comparer, utiliser le TAEG.</li>
<li><strong>Assurance emprunteur</strong> souvent obligatoire — non incluse ici.</li>
<li><strong>Indemnités de remboursement anticipé (IRA)</strong> : vérifier le contrat.</li>
</ul>
<h3>Se combine avec</h3>
<ul>
<li><strong>mortgage-affordability-calculator</strong>.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Per qualsiasi prestito a tasso fisso — mutuo, auto, personale — rata mensile, interessi totali e andamento del debito residuo sono completamente determinati da tre numeri: capitale, tasso, durata. Questo strumento calcola tutto e mostra il piano di ammortamento mese per mese.</p>
<h3>La formula (alla francese)</h3>
<pre>P = L × r(1+r)^n / ((1+r)^n − 1)</pre>
<p>Ogni mese gli interessi sono <code>debito residuo × r</code>; il resto è quota capitale. All'inizio dominano gli interessi, alla fine la quota capitale.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Confronto mutui (15 vs 30 anni).</li>
<li>Prestito auto, personale.</li>
<li>Estinzione anticipata.</li>
<li>Surroga / rinegoziazione.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>TAEG ≠ TAN.</strong> Confronta sempre con il TAEG (include spese).</li>
<li><strong>Mutuo variabile</strong>: tasso BCE + spread. Qui si assume tasso fisso.</li>
<li><strong>Penali estinzione anticipata</strong>: per i mutui prima casa in Italia sono vietate, ma per altri prodotti vanno verificate.</li>
</ul>
<h3>Si combina con</h3>
<ul>
<li><strong>mortgage-affordability-calculator</strong>.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Dla każdego kredytu o stałej stopie — hipotecznego, samochodowego, gotówkowego — miesięczna rata, łączne odsetki i przebieg salda są w pełni określone przez trzy liczby: kwota, stopa, okres. To narzędzie liczy wszystko i pokazuje harmonogram spłat miesiąc po miesiącu.</p>
<h3>Formuła raty równej</h3>
<pre>P = L × r(1+r)^n / ((1+r)^n − 1)</pre>
<p>W każdym miesiącu odsetki to <code>saldo × r</code>; reszta to kapitał. Na początku przeważają odsetki, pod koniec kapitał.</p>
<h3>Kiedy tego użyć</h3>
<ul>
<li>Porównanie hipotek (20 vs 30 lat).</li>
<li>Kredyt samochodowy, gotówkowy.</li>
<li>Nadpłata kredytu.</li>
<li>Refinansowanie / przeniesienie do innego banku.</li>
</ul>
<h3>Częste pułapki</h3>
<ul>
<li><strong>RRSO ≠ oprocentowanie nominalne.</strong> Zawsze porównuj po RRSO (zawiera prowizje i ubezpieczenia).</li>
<li><strong>Kredyt zmiennoprocentowy</strong> ze stawką WIBOR/WIRON się przelicza po każdej zmianie. Tu zakładamy stałą stopę przez cały okres.</li>
<li><strong>Prowizja za wcześniejszą spłatę.</strong> Dla kredytów hipotecznych w PL dozwolona do 3 lat po podpisaniu, dla konsumenckich limitowana ustawą — sprawdź umowę.</li>
</ul>
<h3>Łączy się z</h3>
<ul>
<li><strong>mortgage-affordability-calculator</strong>.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>固定金利のあらゆるローン（住宅、自動車、個人）について、月々の支払額、総利息、残高の推移は元本・金利・期間の 3 つで完全に決まります。本ツールはすべてを計算し、月ごとの償却表を表示します。繰上返済スライダーで、毎月少し多めに払った場合の効果も確認できます。</p>
<h3>元利均等返済の式</h3>
<pre>P = L × r(1+r)^n / ((1+r)^n − 1)</pre>
<p>毎月の利息は <code>残高 × r</code>、残りが元金返済です。序盤は利息が大半を占め、終盤は元金が大半に。だから早い段階の繰上返済ほど節約効果が大きいわけです。</p>
<h3>使うべきタイミング</h3>
<ul>
<li>住宅ローン比較（15 年 vs 35 年、固定 vs 固定）。</li>
<li>自動車ローン、個人ローン。</li>
<li>繰上返済シミュレーション。</li>
<li>借換え試算。</li>
</ul>
<h3>よくある注意点</h3>
<ul>
<li><strong>表面金利と実質年率は別物。</strong> 比較は実質年率で。</li>
<li><strong>変動金利は再計算が前提</strong>。本ツールは「金利が変わらなければ」の基準線を出します。</li>
<li><strong>団信、保証料、手数料は別途。</strong> 月々の支払いには加算されない場合もあります。</li>
<li><strong>繰上返済手数料</strong>を確認してください。</li>
</ul>
<h3>組み合わせ</h3>
<ul>
<li><strong>mortgage-affordability-calculator</strong>。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Voor elke vaste-rente-lening — hypotheek, auto, persoonlijk — zijn de maandlast, totale rente en saldo-traject volledig bepaald door drie getallen: hoofdsom, rente, looptijd. Deze tool berekent alles en toont het aflossingsschema maand voor maand.</p>
<h3>De annuïteit-formule</h3>
<pre>P = L × r(1+r)^n / ((1+r)^n − 1)</pre>
<p>Elke maand is de rente <code>saldo × r</code>; de rest is aflossing. In het begin overheerst rente, aan het eind aflossing.</p>
<h3>Wanneer gebruiken</h3>
<ul>
<li>Hypotheken vergelijken (20 vs 30 jaar).</li>
<li>Autolening, persoonlijke lening.</li>
<li>Extra aflossingen plannen.</li>
<li>Oversluit-check.</li>
</ul>
<h3>Veelvoorkomende valkuilen</h3>
<ul>
<li><strong>NHG / hypotheekrenteaftrek</strong> niet meegerekend — NL-specifiek.</li>
<li><strong>Annuïteit vs lineair</strong>: deze tool berekent annuïteit; lineair lost gelijk af en heeft dalende termijnen.</li>
<li><strong>Boeterente bij oversluiten</strong>: check de voorwaarden.</li>
</ul>
<h3>Combineert met</h3>
<ul>
<li><strong>mortgage-affordability-calculator</strong>.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Herhangi bir sabit faizli kredi için — mortgage, taşıt, ihtiyaç — aylık ödeme, toplam faiz ve bakiye gidişatı üç sayıyla tamamen belirlenir: anapara, faiz, vade. Bu araç hepsini hesaplar ve aydan aya amortisman tablosunu gösterir.</p>
<h3>Eşit taksit formülü</h3>
<pre>P = L × r(1+r)^n / ((1+r)^n − 1)</pre>
<p>Her ay faiz <code>bakiye × r</code>; geri kalan anaparayı azaltır. Başta faiz baskındır, sonda anapara.</p>
<h3>Ne zaman kullanılır</h3>
<ul>
<li>Konut kredisi karşılaştırma (10 vs 20 yıl).</li>
<li>Taşıt kredisi, ihtiyaç kredisi.</li>
<li>Erken kapama senaryoları.</li>
<li>Yeniden yapılandırma kontrolü.</li>
</ul>
<h3>Sık yapılan hatalar</h3>
<ul>
<li><strong>Yıllık maliyet oranı ≠ akdi faiz oranı.</strong> Karşılaştırmada toplam maliyeti kullan.</li>
<li><strong>BSMV ve KKDF</strong> dahil değil — TR'de gerçek aylık ödemeye eklenir.</li>
<li><strong>Erken kapama cezası</strong> — sözleşmeyi kontrol et.</li>
</ul>
<h3>Eşleşir</h3>
<ul>
<li><strong>mortgage-affordability-calculator</strong>.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Untuk pinjaman bunga tetap apa pun — KPR, mobil, KTA — cicilan bulanan, total bunga, dan jalur saldo sepenuhnya ditentukan oleh tiga angka: pokok, bunga, tenor. Tool ini menghitung semuanya dan menampilkan tabel amortisasi bulan demi bulan.</p>
<h3>Formula anuitas</h3>
<pre>P = L × r(1+r)^n / ((1+r)^n − 1)</pre>
<p>Setiap bulan bunga adalah <code>saldo × r</code>; sisanya mengurangi pokok. Di awal bunga mendominasi, di akhir pokok.</p>
<h3>Kapan digunakan</h3>
<ul>
<li>Banding KPR (15 vs 30 tahun).</li>
<li>Kredit mobil, KTA.</li>
<li>Pelunasan dipercepat.</li>
<li>Refinancing.</li>
</ul>
<h3>Kesalahan umum</h3>
<ul>
<li><strong>Efektif vs flat.</strong> Bunga flat dan bunga efektif beda jauh — bank Indonesia umumnya pakai efektif untuk KPR, flat untuk KTA pendek.</li>
<li><strong>Asuransi jiwa kredit</strong> tidak termasuk — biasanya dipotong di muka dari plafon.</li>
<li><strong>Penalti pelunasan dipercepat</strong> — cek kontrak.</li>
<li><strong>Bunga floating</strong> direkalkulasi tiap penyesuaian; tool ini asumsikan tetap.</li>
</ul>
<h3>Pasangan</h3>
<ul>
<li><strong>mortgage-affordability-calculator</strong>.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Đối với bất kỳ khoản vay lãi suất cố định nào — vay mua nhà, ô tô, cá nhân — khoản trả hàng tháng, tổng lãi và quỹ đạo số dư hoàn toàn được xác định bởi ba con số: principal, lãi suất, kỳ hạn. Công cụ này tính toán tất cả và hiển thị lịch khấu trừ theo tháng.</p>
<h3>Công thức trả góp đều</h3>
<pre>P = L × r(1+r)^n / ((1+r)^n − 1)</pre>
<p>Mỗi tháng tiền lãi là <code>số dư × r</code>; phần còn lại trả gốc. Đầu kỳ tiền lãi chiếm phần lớn, cuối kỳ tiền gốc.</p>
<h3>Khi nào nên dùng</h3>
<ul>
<li>So sánh vay mua nhà (15 vs 25 năm).</li>
<li>Vay mua ô tô, vay cá nhân.</li>
<li>Trả nợ trước hạn.</li>
<li>Tái cấu trúc / chuyển ngân hàng.</li>
</ul>
<h3>Lưu ý thường gặp</h3>
<ul>
<li><strong>Lãi dư nợ giảm dần vs lãi gốc cố định.</strong> Hai kiểu tính khác nhau ở Việt Nam — tool này dùng dư nợ giảm dần.</li>
<li><strong>Phí bảo hiểm khoản vay</strong> không tính ở đây.</li>
<li><strong>Phí trả trước hạn</strong> — đọc hợp đồng.</li>
<li><strong>Lãi thả nổi</strong> được tính lại sau mỗi điều chỉnh; tool này giả định cố định.</li>
</ul>
<h3>Đi cùng</h3>
<ul>
<li><strong>mortgage-affordability-calculator</strong>.</li>
</ul>
""",
        "hi": """
<h2>यह किसके लिए है?</h2>
<p>किसी भी fixed-rate loan के लिए — mortgage, car, personal — monthly payment, total interest, और balance trajectory तीन numbers द्वारा पूरी तरह determined हैं: principal, rate, और term। यह tool इन सभी को compute करता है और month-by-month amortization schedule render करता है ताकि आप देख सकें कि हर payment कहाँ जाती है।</p>
<h3>Amortization formula</h3>
<pre>P = L × r(1+r)^n / ((1+r)^n − 1)</pre>
<p>हर month accrued interest <code>balance × r</code> है; payment का बाकी हिस्सा principal कम करता है। Loan की शुरुआत में, payment का अधिकांश हिस्सा interest होता है; अंत में, principal।</p>
<h3>कब इस्तेमाल करें</h3>
<ul>
<li><strong>Mortgage shopping.</strong> 15-year vs 30-year terms की तुलना।</li>
<li><strong>Car loans.</strong> असली cost देखें।</li>
<li><strong>Personal loans / debt consolidation.</strong></li>
<li><strong>Extra-payment planning.</strong> "₹5000/month extra" scenarios test करें।</li>
</ul>
<h3>आम गलतियाँ</h3>
<ul>
<li><strong>APR ≠ note rate.</strong> APR fees और points include करती है; comparison के लिए APR बेहतर है।</li>
<li><strong>Floating rate loans</strong> rate change के बाद recalculate होते हैं। यह tool fixed rate assume करता है।</li>
<li><strong>Processing fee, GST, insurance</strong> India में payment में अलग से जुड़ सकते हैं।</li>
<li><strong>Prepayment penalty</strong> — RBI के नियमों के बावजूद कुछ products charge करते हैं।</li>
</ul>
<h3>साथ pairs</h3>
<ul>
<li><strong>mortgage-affordability-calculator</strong>।</li>
</ul>
""",
        "sk": """
<h2>Načo to slúži?</h2>
<p>Pre akúkoľvek pôžičku s fixnou sadzbou — hypotéku, autoúver, spotrebný úver — sú mesačná splátka, celkové úroky a priebeh zostatku úplne určené tromi číslami: istina, sadzba, doba. Tento nástroj všetko vypočíta a zobrazí splátkový kalendár mesiac po mesiaci.</p>
<h3>Anuitná formula</h3>
<pre>P = L × r(1+r)^n / ((1+r)^n − 1)</pre>
<p>Každý mesiac úrok je <code>zostatok × r</code>; zvyšok znižuje istinu. Na začiatku prevažuje úrok, na konci istina.</p>
<h3>Kedy to použiť</h3>
<ul>
<li>Porovnanie hypoték (20 vs 30 rokov).</li>
<li>Autoúver, spotrebný úver.</li>
<li>Mimoriadna splátka.</li>
<li>Refinancovanie do iného banky.</li>
</ul>
<h3>Časté chyby</h3>
<ul>
<li><strong>RPMN ≠ úroková sadzba.</strong> RPMN obsahuje poplatky.</li>
<li><strong>Fixácia v SK</strong> typicky 1/3/5/10 rokov — táto kalkulačka predpokladá fixnú sadzbu na celú dobu.</li>
<li><strong>Poplatok za predčasné splatenie</strong> pri zmene fixácie môže byť 0; mimo fixácie max 1%.</li>
</ul>
<h3>Spolu s</h3>
<ul>
<li><strong>mortgage-affordability-calculator</strong>.</li>
</ul>
""",
        "cs": """
<h2>K čemu to slouží?</h2>
<p>Pro jakýkoli úvěr s fixní sazbou — hypotéku, autoúvěr, spotřebitelský úvěr — jsou měsíční splátka, celkové úroky a průběh zůstatku zcela určeny třemi čísly: jistina, sazba, doba. Tento nástroj vše vypočítá a zobrazí splátkový kalendář měsíc po měsíci.</p>
<h3>Anuitní formule</h3>
<pre>P = L × r(1+r)^n / ((1+r)^n − 1)</pre>
<p>Každý měsíc úrok je <code>zůstatek × r</code>; zbytek snižuje jistinu. Na začátku převažuje úrok, na konci jistina.</p>
<h3>Kdy to použít</h3>
<ul>
<li>Porovnání hypoték (20 vs 30 let).</li>
<li>Autoúvěr, spotřebitelský úvěr.</li>
<li>Mimořádná splátka.</li>
<li>Refinancování k jiné bance.</li>
</ul>
<h3>Časté chyby</h3>
<ul>
<li><strong>RPSN ≠ úroková sazba.</strong> RPSN obsahuje poplatky.</li>
<li><strong>Fixace v ČR</strong> typicky 1/3/5/10 let — tato kalkulačka předpokládá fixní sazbu po celou dobu.</li>
<li><strong>Poplatek za předčasné splacení</strong> při změně fixace může být 0; mimo fixaci max 1%.</li>
</ul>
<h3>Spolu s</h3>
<ul>
<li><strong>mortgage-affordability-calculator</strong>.</li>
</ul>
""",
    },
    "related": ["mortgage-affordability-calculator", "percentage-calculator", "currency-converter"],
    "howto": {"flow": "calculate", "action": "format", "noun": "loan"},
}
