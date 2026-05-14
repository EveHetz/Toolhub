TOOL = {
    "slug": "damage-calculator",
    "category": "gaming",
    "icon": "⚔️",
    "tags": ["damage", "calculator", "combat", "rpg", "formula", "crit", "game-dev", "balance"],
    "i18n": {
        "en": {
            "name": "Damage Calculator",
            "tagline": "Combat damage formula tester for RPGs. Attack vs defense, crit chance, resistances, multipliers, armor pen. See expected damage range + crit-adjusted average + damage-per-second. For game balance tuning.",
            "description": "Free in-browser damage calculator for RPG combat design. Plug in attacker stats (ATK, weapon damage, crit %, crit multiplier, armor pen) and defender stats (DEF, resistance %, armor). Pick a formula: subtractive (DMG - DEF), divisive (DMG × DEF/(DEF+k)), percent-resist, or custom. Get expected damage, min/max range, crit-adjusted average, and DPS at given attack speed. Pure JS, no upload.",
        },
        "de": {
            "name": "Schaden-Rechner",
            "tagline": "Combat-Schadensformel-Tester für RPGs. Angriff vs. Verteidigung, Crit-Chance, Resistenzen, Multiplikatoren, Rüstungsdurchschlag. Erwarteter Schaden + Crit-Schnitt + DPS. Fürs Balance-Tuning.",
            "description": "Kostenloser In-Browser-Schadensrechner fürs RPG-Combat-Design. Angreifer-Werte (ATK, Waffenschaden, Crit %, Crit-Multiplikator, Rüstungsdurchschlag) und Verteidiger-Werte (DEF, Resistenz %, Rüstung) eintragen. Formel wählen: subtraktiv (DMG - DEF), divisiv (DMG × DEF/(DEF+k)), Prozent-Resistenz oder Custom. Erhalte erwarteten Schaden, Min/Max-Range, crit-bereinigten Schnitt und DPS bei Angriffsgeschwindigkeit. Pures JS, kein Upload.",
        },
        "es": {
            "name": "Calculadora de daño",
            "tagline": "Probador de fórmulas de daño en combate para RPGs. Ataque vs defensa, % crit, resistencias, multiplicadores, penetración de armadura. Rango esperado + media con crit + DPS. Para tuning de balance.",
            "description": "Calculadora gratuita de daño en navegador para diseño de combate RPG. Mete stats de atacante (ATK, daño de arma, crit %, multiplicador de crit, penetración) y defensor (DEF, resistencia %, armadura plana). Elige fórmula: sustractiva (DMG - DEF), divisiva (DMG × DEF/(DEF+k)), porcentaje-resistencia o expresión custom. Daño esperado, rango min/máx, media ajustada por crit y DPS a la velocidad de ataque dada. JS puro, sin upload.",
        },
        "fr": {
            "name": "Calculateur de dégâts",
            "tagline": "Testeur de formules de dégâts pour RPG. Attaque vs défense, % crit, résistances, multiplicateurs, pénétration. Plage attendue + moyenne avec crit + DPS. Pour le tuning d'équilibrage.",
            "description": "Calculateur de dégâts gratuit dans le navigateur pour le design de combat RPG. Saisis les stats de l'attaquant (ATK, dégâts d'arme, crit %, multiplicateur de crit, pénétration d'armure) et du défenseur (DEF, résistance %, armure plate). Choisis une formule : soustractive (DMG - DEF), divisive (DMG × DEF/(DEF+k)), résistance en pourcentage ou expression personnalisée. Dégâts attendus, plage min/max, moyenne ajustée au crit et DPS à la vitesse d'attaque donnée. JS pur, aucun upload.",
        },
        "it": {
            "name": "Calcolatore di danno",
            "tagline": "Tester di formule di danno in combattimento per RPG. Attacco vs difesa, % crit, resistenze, moltiplicatori, penetrazione. Range atteso + media con crit + DPS. Per il tuning del bilanciamento.",
            "description": "Calcolatore di danno gratuito nel browser per il design del combattimento RPG. Inserisci le statistiche dell'attaccante (ATK, danno arma, crit %, moltiplicatore crit, penetrazione armatura) e del difensore (DEF, resistenza %, armatura piatta). Scegli una formula: sottrattiva (DMG - DEF), divisiva (DMG × DEF/(DEF+k)), percentuale-resistenza o espressione personalizzata. Danno atteso, range min/max, media corretta per crit e DPS alla velocità di attacco data. JS puro, nessun upload.",
        },
        "pt": {
            "name": "Calculadora de dano",
            "tagline": "Testador de fórmulas de dano em combate pra RPG. Ataque vs defesa, % crit, resistências, multiplicadores, penetração de armadura. Range esperado + média ajustada com crit + DPS. Pra tuning de balance.",
            "description": "Calculadora de dano gratuita no browser pra design de combate em RPG. Coloque stats do atacante (ATK, dano da arma, crit %, multiplicador de crit, penetração) e do defensor (DEF, resistência %, armadura). Escolha uma fórmula: subtrativa (DMG - DEF), divisiva (DMG × DEF/(DEF+k)), porcentagem-resistência ou expressão custom. Dano esperado, range min/máx, média ajustada com crit e DPS na velocidade de ataque dada. JS puro, sem upload.",
        },
        "pl": {
            "name": "Kalkulator obrażeń",
            "tagline": "Tester formuł obrażeń w walce dla RPG. Atak vs obrona, % crit, oporności, mnożniki, penetracja pancerza. Oczekiwany zakres + średnia z critami + DPS. Do tuningu balansu.",
            "description": "Darmowy kalkulator obrażeń w przeglądarce do designu walki w RPG. Wpisz staty atakującego (ATK, dmg broni, crit %, mnożnik crit, penetracja pancerza) i obrońcy (DEF, oporność %, płaski pancerz). Wybierz formułę: subtrakcyjna (DMG - DEF), dywizyjna (DMG × DEF/(DEF+k)), procent oporności albo własne wyrażenie. Dostaniesz oczekiwane obrażenia, zakres min/max, średnią z uwzględnieniem critów i DPS przy zadanej szybkości ataku. Czysty JS, bez uploadu.",
        },
        "ja": {
            "name": "ダメージ計算機",
            "tagline": "RPG 戦闘ダメージ式テスター。攻撃 vs 防御、クリ率、耐性、倍率、防御貫通。期待ダメージ範囲＋クリ込み平均＋DPS。バランス調整向け。",
            "description": "RPG の戦闘デザイン向けの無料ブラウザ内ダメージ計算機。攻撃側（ATK、武器ダメ、クリ率、クリ倍率、防御貫通）と防御側（DEF、耐性 %、固定アーマー）の値を入れて、式を選択：減算式（DMG - DEF）、除算式（DMG × DEF/(DEF+k)）、％耐性、カスタム式。期待ダメージ、最小／最大レンジ、クリ込み平均、攻撃速度に応じた DPS を表示します。純粋な JS でアップロードなし。",
        },
        "nl": {
            "name": "Schade-calculator",
            "tagline": "Combat damage formule-tester voor RPGs. Aanval vs verdediging, crit %, resistenties, multipliers, armor pen. Verwacht range + crit-adjusted gemiddelde + DPS. Voor balance-tuning.",
            "description": "Gratis in-browser schade-calculator voor RPG combat-design. Vul attacker-stats in (ATK, wapenschade, crit %, crit-multiplier, armor pen) en defender-stats (DEF, resistentie %, vaste armor). Kies een formule: subtractief (DMG - DEF), divisief (DMG × DEF/(DEF+k)), percent-resist of custom expressie. Krijg verwachte schade, min/max range, crit-adjusted gemiddelde en DPS bij gegeven attack speed. Pure JS, geen upload.",
        },
        "tr": {
            "name": "Hasar Hesaplayıcı",
            "tagline": "RPG'ler için savaş hasarı formül test edici. Saldırı vs savunma, krit %, dirençler, çarpanlar, armor pen. Beklenen hasar aralığı + krit-ortalama + DPS. Denge ayarı için.",
            "description": "RPG savaş tasarımı için ücretsiz tarayıcı içi hasar hesaplayıcı. Saldıran istatistiklerini (ATK, silah hasarı, krit %, krit çarpanı, zırh delme) ve savunan istatistiklerini (DEF, direnç %, sabit zırh) gir. Bir formül seç: çıkarmalı (DMG - DEF), bölmeli (DMG × DEF/(DEF+k)), yüzde-direnç veya özel ifade. Beklenen hasar, min/maks aralığı, krit-düzeltilmiş ortalama ve verilen saldırı hızında DPS al. Saf JS, yükleme yok.",
        },
        "id": {
            "name": "Kalkulator damage",
            "tagline": "Tester formula damage combat untuk RPG. Attack vs defense, crit %, resistance, multiplier, armor pen. Range damage harapan + rata-rata dengan crit + DPS. Untuk tuning balance.",
            "description": "Kalkulator damage in-browser gratis untuk desain combat RPG. Masukkan stat attacker (ATK, damage senjata, crit %, crit multiplier, armor pen) dan defender (DEF, resistance %, flat armor). Pilih formula: subtraktif (DMG - DEF), divisif (DMG × DEF/(DEF+k)), persen-resist, atau ekspresi custom. Dapatkan damage harapan, range min/maks, rata-rata yang disesuaikan dengan crit, dan DPS pada attack speed yang diberikan. Pure JS, tanpa upload.",
        },
        "vi": {
            "name": "Máy tính sát thương",
            "tagline": "Bộ thử công thức sát thương combat cho RPG. Tấn công vs phòng thủ, % crit, kháng, hệ số, xuyên giáp. Khoảng sát thương kỳ vọng + trung bình có crit + DPS. Dùng để tinh chỉnh cân bằng.",
            "description": "Máy tính sát thương trong trình duyệt miễn phí cho thiết kế combat RPG. Nhập chỉ số người tấn công (ATK, dmg vũ khí, crit %, hệ số crit, xuyên giáp) và người phòng thủ (DEF, kháng %, giáp phẳng). Chọn công thức: trừ (DMG - DEF), chia (DMG × DEF/(DEF+k)), phần-trăm-kháng hoặc biểu thức tùy chỉnh. Nhận sát thương kỳ vọng, khoảng min/max, trung bình có crit và DPS theo tốc độ tấn công cho trước. JS thuần, không upload.",
        },
        "hi": {
            "name": "Damage Calculator",
            "tagline": "RPG के लिए combat damage formula tester। Attack vs defense, crit %, resistances, multipliers, armor pen। Expected damage range + crit-adjusted average + DPS। Game balance tuning के लिए।",
            "description": "RPG combat design के लिए मुफ़्त in-browser damage calculator। Attacker stats (ATK, weapon damage, crit %, crit multiplier, armor pen) और defender stats (DEF, resistance %, flat armor) डालें। एक formula चुनें: subtractive (DMG - DEF), divisive (DMG × DEF/(DEF+k)), percent-resist, या custom expression। Expected damage, min/max range, crit-adjusted average, और दिए गए attack speed पर DPS पाएँ। Pure JS, कोई upload नहीं।",
        },
        "sk": {
            "name": "Kalkulačka damage",
            "tagline": "Tester combat damage formuly pre RPG. Útok vs obrana, crit %, resistencie, multiplikátory, armor pen. Očakávaný damage range + crit-adjusted priemer + DPS. Na balance tuning.",
            "description": "Bezplatná in-browser kalkulačka damage pre RPG combat dizajn. Zadaj staty útočníka (ATK, weapon damage, crit %, crit multiplier, armor pen) a obrancu (DEF, resistance %, flat armor). Vyber formulu: subtraktívna (DMG - DEF), divizívna (DMG × DEF/(DEF+k)), percent-resist alebo custom výraz. Dostaneš očakávaný damage, min/max range, crit-adjusted priemer a DPS pri zadanej rýchlosti útoku. Čisté JS, žiadny upload.",
        },
        "cs": {
            "name": "Kalkulačka damage",
            "tagline": "Tester combat damage formule pro RPG. Útok vs obrana, crit %, resistance, multiplikátory, armor pen. Očekávaný damage range + crit-adjusted průměr + DPS. Pro balance tuning.",
            "description": "Bezplatná in-browser kalkulačka damage pro RPG combat design. Zadej staty útočníka (ATK, weapon damage, crit %, crit multiplier, armor pen) a obránce (DEF, resistance %, flat armor). Vyber formuli: subtraktivní (DMG - DEF), divizivní (DMG × DEF/(DEF+k)), percent-resist nebo custom výraz. Dostaneš očekávaný damage, min/max range, crit-adjusted průměr a DPS při zadané rychlosti útoku. Čisté JS, žádný upload.",
        },
    },
    "body": """
<div class="tool-card">
  <label>Formula</label>
  <select id="dmg-formula" onchange="dmgRun()">
    <option value="sub">Subtractive: DMG − DEF (clamp ≥ 1)</option>
    <option value="div" selected>Divisive: DMG × 100/(100+DEF)</option>
    <option value="pct">Percent resist: DMG × (1 − resist%)</option>
    <option value="custom">Custom JS expression</option>
  </select>
  <div id="dmg-custom-row" style="display:none;margin-top:0.6rem">
    <label>Custom expression <span class="meta" style="font-weight:normal">(vars: atk, wpn, def, res, pen, armor)</span></label>
    <input type="text" id="dmg-custom" value="(atk + wpn) * 100 / (100 + Math.max(0, def - pen))" oninput="dmgRun()" style="font-family:ui-monospace,monospace">
  </div>
</div>

<div class="tool-card">
  <label style="color:#f85149">⚔️ Attacker</label>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:0.8rem">
    <div><label style="font-weight:normal">ATK stat</label><input type="number" id="dmg-atk" value="50" step="any" oninput="dmgRun()"></div>
    <div><label style="font-weight:normal">Weapon damage</label><input type="number" id="dmg-wpn" value="40" step="any" oninput="dmgRun()"></div>
    <div><label style="font-weight:normal">Variance %</label><input type="number" id="dmg-var" value="15" step="any" min="0" max="100" oninput="dmgRun()"></div>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:0.8rem;margin-top:0.6rem">
    <div><label style="font-weight:normal">Crit chance %</label><input type="number" id="dmg-crit" value="20" step="any" min="0" max="100" oninput="dmgRun()"></div>
    <div><label style="font-weight:normal">Crit multiplier</label><input type="number" id="dmg-critmult" value="2" step="any" min="1" oninput="dmgRun()"></div>
    <div><label style="font-weight:normal">Armor pen (flat)</label><input type="number" id="dmg-pen" value="0" step="any" oninput="dmgRun()"></div>
  </div>
</div>

<div class="tool-card">
  <label style="color:#3fb950">🛡 Defender</label>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:0.8rem">
    <div><label style="font-weight:normal">DEF stat</label><input type="number" id="dmg-def" value="30" step="any" oninput="dmgRun()"></div>
    <div><label style="font-weight:normal">Resistance %</label><input type="number" id="dmg-res" value="0" step="any" min="0" max="100" oninput="dmgRun()"></div>
    <div><label style="font-weight:normal">Flat armor</label><input type="number" id="dmg-armor" value="0" step="any" oninput="dmgRun()"></div>
  </div>
</div>

<div class="tool-card">
  <label>Combat speed</label>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.8rem">
    <div><label style="font-weight:normal">Attacks per second</label><input type="number" id="dmg-aps" value="1.2" step="any" min="0.01" oninput="dmgRun()"></div>
    <div style="display:flex;align-items:end"><label style="font-weight:normal"><input type="checkbox" id="dmg-compare" onchange="dmgToggleCompare()" style="margin-right:0.4rem">Compare with config B</label></div>
  </div>
</div>

<div id="dmg-config-b" style="display:none">
  <div class="tool-card" style="border:1px dashed var(--accent)">
    <label>Config B (attacker)</label>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:0.8rem">
      <div><label style="font-weight:normal">ATK</label><input type="number" id="dmgb-atk" value="50" step="any" oninput="dmgRun()"></div>
      <div><label style="font-weight:normal">Weapon</label><input type="number" id="dmgb-wpn" value="60" step="any" oninput="dmgRun()"></div>
      <div><label style="font-weight:normal">Crit %</label><input type="number" id="dmgb-crit" value="50" step="any" min="0" max="100" oninput="dmgRun()"></div>
    </div>
  </div>
</div>

<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="dmg-out" class="dmg-out"></div>
</div>
""",
    "script": """
<style>
.dmg-out{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:0.7rem}
.dmg-card{background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;padding:0.7rem 0.85rem}
.dmg-card.b{border-color:var(--accent)}
.dmg-card h4{margin:0 0 0.4rem 0;font-size:0.78rem;color:var(--text-muted);font-weight:600;text-transform:uppercase;letter-spacing:0.05em}
.dmg-big{font-family:ui-monospace,monospace;font-size:1.5rem;font-weight:700;color:var(--accent)}
.dmg-sub{font-family:ui-monospace,monospace;font-size:0.82rem;color:var(--text-muted);margin-top:0.2rem}
.dmg-diff{font-family:ui-monospace,monospace;font-size:0.85rem;font-weight:600;margin-top:0.3rem}
.dmg-diff.up{color:#3fb950}
.dmg-diff.down{color:#f85149}
.dmg-err{color:#f85149;font-family:ui-monospace,monospace;font-size:0.85rem}
</style>
<script>
function dmgFmt(n){
  if(!isFinite(n)) return '∞';
  if(Math.abs(n) >= 1000) return Math.round(n).toLocaleString('en-US');
  if(Math.abs(n) >= 10) return n.toFixed(1);
  return n.toFixed(2);
}
function dmgToggleCompare(){
  const on = document.getElementById('dmg-compare').checked;
  document.getElementById('dmg-config-b').style.display = on ? '' : 'none';
  dmgRun();
}
function dmgToggleCustom(){
  const f = document.getElementById('dmg-formula').value;
  document.getElementById('dmg-custom-row').style.display = f === 'custom' ? '' : 'none';
}
let dmgLastErr = null;
function dmgApply(formula, atk, wpn, def, res, pen, armor, customSrc){
  const effDef = Math.max(0, def + armor - pen);
  const base = atk + wpn;
  switch(formula){
    case 'sub': return Math.max(1, base - effDef);
    case 'div': return base * 100 / (100 + effDef);
    case 'pct': return base * (1 - Math.min(1, Math.max(0, res / 100)));
    case 'custom': {
      try{
        // Lexical scope only; no `this`, no globals beyond Math
        const fn = new Function('atk','wpn','def','res','pen','armor','Math','return (' + customSrc + ');');
        const v = fn(atk, wpn, effDef, res, pen, armor, Math);
        if(typeof v !== 'number' || isNaN(v)) throw new Error('Expression did not return a number');
        return v;
      } catch(e){
        dmgLastErr = e.message;
        return NaN;
      }
    }
  }
  return 0;
}
function dmgCompute(suffix){
  const get = (id) => parseFloat(document.getElementById(id).value) || 0;
  const atk = get('dmg-atk' + (suffix || ''));
  const wpn = get('dmg-wpn' + (suffix || ''));
  const variance = get('dmg-var');
  const crit = get('dmg-crit' + (suffix || ''));
  const critMult = get('dmg-critmult');
  const pen = get('dmg-pen');
  const def = get('dmg-def');
  const res = get('dmg-res');
  const armor = get('dmg-armor');
  const aps = get('dmg-aps');
  const formula = document.getElementById('dmg-formula').value;
  const custom = document.getElementById('dmg-custom').value;
  dmgLastErr = null;
  const mid = dmgApply(formula, atk, wpn, def, res, pen, armor, custom);
  const lo = dmgApply(formula, atk, wpn * (1 - variance / 100), def, res, pen, armor, custom);
  const hi = dmgApply(formula, atk, wpn * (1 + variance / 100), def, res, pen, armor, custom);
  const critChance = Math.min(1, Math.max(0, crit / 100));
  const avg = mid * (1 + critChance * (critMult - 1));
  const dps = avg * aps;
  return { mid, lo, hi, avg, dps, critChance, critMult, aps, err: dmgLastErr };
}
function dmgCard(title, r, cls){
  if(r.err) return `<div class="dmg-card ${cls||''}"><h4>${title}</h4><div class="dmg-err">⚠ ${r.err}</div></div>`;
  return `<div class="dmg-card ${cls||''}">
    <h4>${title}</h4>
    <div class="dmg-big">${dmgFmt(r.mid)}</div>
    <div class="dmg-sub">Range: ${dmgFmt(r.lo)} – ${dmgFmt(r.hi)}</div>
    <div class="dmg-sub">Crit-adjusted avg: <strong>${dmgFmt(r.avg)}</strong> (${(r.critChance*100).toFixed(0)}% × ${r.critMult.toFixed(2)})</div>
    <div class="dmg-sub">DPS @ ${r.aps.toFixed(2)} aps: <strong>${dmgFmt(r.dps)}</strong></div>
  </div>`;
}
function dmgDiff(a, b){
  if(a.err || b.err) return '';
  const dDps = b.dps - a.dps;
  const pct = a.dps === 0 ? 0 : (dDps / a.dps) * 100;
  const dir = dDps >= 0 ? 'up' : 'down';
  const sign = dDps >= 0 ? '+' : '−';
  return `<div class="dmg-card"><h4>Δ (B vs A)</h4>
    <div class="dmg-diff ${dir}">${sign}${dmgFmt(Math.abs(dDps))} DPS</div>
    <div class="dmg-sub">${sign}${Math.abs(pct).toFixed(1)}% vs A</div>
    <div class="dmg-sub">Avg per hit: ${sign}${dmgFmt(Math.abs(b.avg - a.avg))}</div>
  </div>`;
}
function dmgRun(){
  dmgToggleCustom();
  const compare = document.getElementById('dmg-compare').checked;
  const a = dmgCompute('');
  let html = dmgCard(compare ? 'Config A' : 'Result', a, compare ? 'a' : '');
  if(compare){
    const b = dmgCompute('b');
    html += dmgCard('Config B', b, 'b');
    html += dmgDiff(a, b);
  }
  document.getElementById('dmg-out').innerHTML = html;
}
document.addEventListener('DOMContentLoaded', dmgRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Combat in an RPG is a formula that takes attacker stats and defender stats and produces a number — but which formula? Subtractive, divisive, percent-resist, and custom hybrids all behave differently as numbers scale. A formula that feels fine at level 1 with ATK 10 vs DEF 5 can produce one-shot kills at level 50 with ATK 500 vs DEF 50. This tool lets you plug in the formula and the stats and immediately see expected damage, min/max range, the crit-adjusted average, and DPS at a given attack speed — so you can sanity-check that your level-50 fight isn't accidentally a one-shot.</p>

<h3>The formulas</h3>
<ul>
  <li><strong>Subtractive</strong> (<code>DMG − DEF</code>, clamped to ≥ 1) — the simplest. Used in classic Dragon Quest / Final Fantasy. Problem: at high DEF the damage hits the clamp and combat becomes binary (you either can damage or you can't). Easy to break with armor scaling.</li>
  <li><strong>Divisive</strong> (<code>DMG × 100 / (100 + DEF)</code>) — the default in modern action RPGs (League of Legends, Path of Exile uses a variant). Damage smoothly decreases as DEF rises, never reaches zero, scales predictably. DEF = 100 means 50% damage taken; DEF = 200 means 33%.</li>
  <li><strong>Percent resist</strong> (<code>DMG × (1 − resist%)</code>) — common for elemental damage. Resist 30% = take 70% damage. Cap resist at 75% or 80% to avoid invincibility.</li>
  <li><strong>Custom JS expression</strong> — for game-specific formulas. Variables in scope: <code>atk</code>, <code>wpn</code>, <code>def</code> (effective, post-pen), <code>res</code>, <code>pen</code>, <code>armor</code>, plus <code>Math</code>. Expression is evaluated with <code>new Function</code>, sandboxed to those names.</li>
</ul>

<h3>What the numbers mean</h3>
<ul>
  <li><strong>Expected damage</strong> — the formula output at neutral variance. The single-number summary.</li>
  <li><strong>Range</strong> — applies the variance % to weapon damage. ±15% is a common default.</li>
  <li><strong>Crit-adjusted average</strong> — expected damage × (1 + critChance × (critMult − 1)). The number that matters for sustained DPS, not just a single hit.</li>
  <li><strong>DPS</strong> — crit-adjusted average × attacks per second. Compare two builds at this number to decide which is "stronger" on paper.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Variance is on weapon damage only.</strong> ATK and DEF don't roll. This matches most games — weapon damage is the "physical roll", stats are the static modifiers.</li>
  <li><strong>Armor pen reduces effective DEF, not damage.</strong> The order is: effective DEF = max(0, DEF + flat armor − pen), then the formula. This is the standard ordering — applying pen after the formula breaks most balance.</li>
  <li><strong>Resistance is multiplicative.</strong> Two 30% resists on the same damage type don't stack to 60%; they stack to (1 − 0.7×0.7) = 51%. For the tool, enter your total effective resist, not the sum of sources.</li>
  <li><strong>Crit multiplier is total, not bonus.</strong> A 2× crit means 200% of normal damage, not 100% + 100%. If your game uses bonus stacking, convert before entering.</li>
  <li><strong>DPS is a paper number.</strong> Real combat has cooldowns, dodges, positioning, animation lock, and resource costs. DPS is a starting point for balance, not the destination.</li>
  <li><strong>Custom expressions evaluate live.</strong> Don't reference DOM, globals, or storage. The sandbox is just <code>Math</code> + the named variables. Errors show inline.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Combat in einem RPG ist eine Formel, die Angreifer- und Verteidiger-Werte zu einer Zahl macht — aber welche Formel? Subtraktiv, divisiv, Prozent-Resistenz und hybride Custom-Varianten verhalten sich beim Skalieren unterschiedlich. Eine Formel, die auf Level 1 gut wirkt, kann auf Level 50 zum One-Shot werden. Dieses Tool lässt dich Formel und Werte eintragen und zeigt erwarteten Schaden, Min/Max-Range, crit-bereinigten Schnitt und DPS — so erkennst du Skalierungsbrüche früh.</p>

<h3>Formeln</h3>
<ul>
  <li><strong>Subtraktiv</strong> — klassisch (Dragon Quest). Bricht bei hoher DEF.</li>
  <li><strong>Divisiv</strong> — Default in modernen Action-RPGs. Sanfter Abfall.</li>
  <li><strong>Prozent-Resistenz</strong> — typisch für Elementarschaden. Caps bei 75–80%.</li>
  <li><strong>Custom</strong> — JS-Ausdruck, sandboxed auf <code>atk</code>, <code>wpn</code>, <code>def</code>, <code>res</code>, <code>pen</code>, <code>armor</code>, <code>Math</code>.</li>
</ul>

<h3>Stolperfallen</h3>
<ul>
  <li><strong>Resistenzen sind multiplikativ.</strong> 30% + 30% = 51%, nicht 60%.</li>
  <li><strong>Crit-Multiplikator ist total.</strong> 2× = 200% normaler Schaden.</li>
  <li><strong>DPS ist eine Papierzahl.</strong> Cooldowns, Dodges, Animations-Lock zählen real, nicht hier.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>El combate en un RPG es una fórmula que toma stats de atacante y defensor y produce un número — pero, ¿qué fórmula? Sustractiva, divisiva, porcentaje-resistencia e híbridas se comportan distinto al escalar. Esta herramienta deja meter fórmula y stats y muestra al instante daño esperado, rango min/máx, media ajustada por crit y DPS — para que detectes roturas de escala antes de enviarlas al juego.</p>

<h3>Fórmulas</h3>
<ul>
  <li><strong>Sustractiva</strong> — clásica (Dragon Quest). Se rompe con DEF alta.</li>
  <li><strong>Divisiva</strong> — default en action-RPGs modernos. Caída suave.</li>
  <li><strong>Porcentaje-resistencia</strong> — típica para daño elemental. Capa al 75–80%.</li>
  <li><strong>Custom</strong> — expresión JS, sandboxed a <code>atk</code>, <code>wpn</code>, <code>def</code>, <code>res</code>, <code>pen</code>, <code>armor</code>, <code>Math</code>.</li>
</ul>

<h3>Cuidados comunes</h3>
<ul>
  <li><strong>Las resistencias son multiplicativas.</strong> 30% + 30% = 51%, no 60%.</li>
  <li><strong>El multiplicador de crit es total.</strong> 2× = 200% del daño normal.</li>
  <li><strong>DPS es un número de papel.</strong> Cooldowns, esquives, animation lock importan en juego real, no aquí.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Le combat dans un RPG est une formule qui prend les stats d'attaquant et de défenseur et produit un nombre — mais quelle formule ? Soustractive, divisive, résistance en pourcentage et hybrides custom se comportent différemment quand les nombres montent. Cet outil te laisse renseigner formule et stats et montre instantanément les dégâts attendus, la plage min/max, la moyenne ajustée au crit et le DPS — pour repérer les ruptures d'échelle avant qu'elles arrivent au joueur.</p>

<h3>Formules</h3>
<ul>
  <li><strong>Soustractive</strong> — classique (Dragon Quest). Casse à DEF élevée.</li>
  <li><strong>Divisive</strong> — défaut des action-RPGs modernes. Décroissance douce.</li>
  <li><strong>Résistance en %</strong> — typique pour les dégâts élémentaires. Cap à 75–80%.</li>
  <li><strong>Custom</strong> — expression JS, sandboxée à <code>atk</code>, <code>wpn</code>, <code>def</code>, <code>res</code>, <code>pen</code>, <code>armor</code>, <code>Math</code>.</li>
</ul>

<h3>Pièges courants</h3>
<ul>
  <li><strong>Les résistances sont multiplicatives.</strong> 30% + 30% = 51%, pas 60%.</li>
  <li><strong>Le multiplicateur de crit est total.</strong> 2× = 200% des dégâts normaux.</li>
  <li><strong>Le DPS est un nombre théorique.</strong> Cooldowns, esquives, animation lock comptent en vrai, pas ici.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Il combattimento in un RPG è una formula che prende le stat di attaccante e difensore e produce un numero — ma quale formula? Sottrattiva, divisiva, percentuale-resistenza e ibridi custom si comportano in modo diverso quando i numeri crescono. Questo strumento ti fa inserire formula e stat e mostra all'istante danno atteso, range min/max, media corretta per crit e DPS — così individui rotture di scala prima che arrivino al giocatore.</p>

<h3>Formule</h3>
<ul>
  <li><strong>Sottrattiva</strong> — classica (Dragon Quest). Si rompe con DEF alta.</li>
  <li><strong>Divisiva</strong> — default negli action-RPG moderni. Decrescita morbida.</li>
  <li><strong>Percentuale-resistenza</strong> — tipica per il danno elementale. Cappata al 75–80%.</li>
  <li><strong>Custom</strong> — espressione JS, sandboxata a <code>atk</code>, <code>wpn</code>, <code>def</code>, <code>res</code>, <code>pen</code>, <code>armor</code>, <code>Math</code>.</li>
</ul>

<h3>Errori comuni</h3>
<ul>
  <li><strong>Le resistenze sono moltiplicative.</strong> 30% + 30% = 51%, non 60%.</li>
  <li><strong>Il moltiplicatore di crit è totale.</strong> 2× = 200% del danno normale.</li>
  <li><strong>Il DPS è un numero su carta.</strong> Cooldown, schivate, animation lock contano nel gioco reale, non qui.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Combate em RPG é uma fórmula que pega stats do atacante e do defensor e produz um número — mas qual fórmula? Subtrativa, divisiva, porcentagem-resistência e híbridas se comportam diferente quando os números sobem. Esta ferramenta deixa você plugar fórmula e stats e mostra na hora dano esperado, range min/máx, média ajustada com crit e DPS — pra você pegar quebra de escala antes de mandar pro jogo.</p>

<h3>Fórmulas</h3>
<ul>
  <li><strong>Subtrativa</strong> — clássica (Dragon Quest). Quebra com DEF alta.</li>
  <li><strong>Divisiva</strong> — padrão em action-RPGs modernos. Queda suave.</li>
  <li><strong>Porcentagem-resistência</strong> — típica pra dano elemental. Capa em 75–80%.</li>
  <li><strong>Custom</strong> — expressão JS, sandbox em <code>atk</code>, <code>wpn</code>, <code>def</code>, <code>res</code>, <code>pen</code>, <code>armor</code>, <code>Math</code>.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Resistências são multiplicativas.</strong> 30% + 30% = 51%, não 60%.</li>
  <li><strong>Multiplicador de crit é total.</strong> 2× = 200% do dano normal.</li>
  <li><strong>DPS é número de papel.</strong> Cooldowns, esquivas, animation lock contam no jogo real, não aqui.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Walka w RPG to formuła, która bierze staty atakującego i obrońcy i daje liczbę — ale jaka formuła? Subtrakcyjna, dywizyjna, procent-oporu i hybrydy custom zachowują się różnie przy skalowaniu liczb. To narzędzie pozwala wpisać formułę i staty i od razu pokazuje oczekiwane obrażenia, zakres min/max, średnią z critami i DPS — żebyś łapał załamania skali zanim trafią do gracza.</p>

<h3>Formuły</h3>
<ul>
  <li><strong>Subtrakcyjna</strong> — klasyk (Dragon Quest). Pęka przy wysokim DEF.</li>
  <li><strong>Dywizyjna</strong> — default w nowoczesnych action-RPG. Łagodny spadek.</li>
  <li><strong>Procent-oporu</strong> — typowe dla obrażeń żywiołowych. Cap na 75–80%.</li>
  <li><strong>Custom</strong> — wyrażenie JS, sandbox z <code>atk</code>, <code>wpn</code>, <code>def</code>, <code>res</code>, <code>pen</code>, <code>armor</code>, <code>Math</code>.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Oporności są multiplikatywne.</strong> 30% + 30% = 51%, nie 60%.</li>
  <li><strong>Mnożnik crita to total.</strong> 2× = 200% normalnych obrażeń.</li>
  <li><strong>DPS to liczba na papierze.</strong> Cooldowny, uniki, animation lock liczą się w realnej walce, nie tutaj.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>RPG の戦闘は、攻撃側と防御側のステータスを受け取って数を出す「式」です。減算、除算、％耐性、ハイブリッドのカスタムなど、式によってスケール時の挙動はまったく異なります。Lv.1 で違和感のない式が、Lv.50 では一撃必殺になることもあります。本ツールは式と数値を入れるだけで、期待ダメージ、最小／最大レンジ、クリ込み平均、攻撃速度に応じた DPS を即時表示します。プレイヤーに届く前にスケール破綻を発見できます。</p>

<h3>式の種類</h3>
<ul>
  <li><strong>減算式</strong> — 古典的（ドラクエ等）。DEF が上がると破綻しやすい。</li>
  <li><strong>除算式</strong> — モダンなアクション RPG のデフォルト。なだらかに減衰。</li>
  <li><strong>％耐性</strong> — 属性ダメージ向け。75–80% でキャップ推奨。</li>
  <li><strong>カスタム</strong> — JS 式。サンドボックス：<code>atk</code>、<code>wpn</code>、<code>def</code>、<code>res</code>、<code>pen</code>、<code>armor</code>、<code>Math</code>。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>耐性は乗算で合成。</strong> 30% + 30% = 51% であって 60% ではない。</li>
  <li><strong>クリ倍率は総量。</strong> 2× は通常の 200%。+100% ではない。</li>
  <li><strong>DPS は紙の数。</strong> 実戦ではクールダウン、回避、アニメーションロックも効きます。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Combat in een RPG is een formule die attacker- en defender-stats neemt en een nummer produceert — maar welke formule? Subtractief, divisief, percent-resist en custom hybrids gedragen zich anders bij schalen. Deze tool laat je formule en stats invullen en toont direct verwachte schade, min/max range, crit-adjusted gemiddelde en DPS — zodat je scale-breaks vangt voor ze bij de speler aankomen.</p>

<h3>Formules</h3>
<ul>
  <li><strong>Subtractief</strong> — klassiek (Dragon Quest). Breekt bij hoge DEF.</li>
  <li><strong>Divisief</strong> — default in moderne action-RPGs. Zachte afname.</li>
  <li><strong>Percent-resist</strong> — typisch voor elemental damage. Cap op 75–80%.</li>
  <li><strong>Custom</strong> — JS-expressie, sandboxed naar <code>atk</code>, <code>wpn</code>, <code>def</code>, <code>res</code>, <code>pen</code>, <code>armor</code>, <code>Math</code>.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Resists zijn multiplicatief.</strong> 30% + 30% = 51%, geen 60%.</li>
  <li><strong>Crit-multiplier is totaal.</strong> 2× = 200% van normale schade.</li>
  <li><strong>DPS is een papier-nummer.</strong> Cooldowns, dodges, animation lock tellen in echt gevecht, niet hier.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>RPG'de savaş, saldıran ve savunan istatistiklerini alıp bir sayı üreten bir formüldür — ama hangi formül? Çıkarmalı, bölmeli, yüzde-direnç ve özel hibritler ölçekte farklı davranır. Bu araç formül ve istatistikleri girince anında beklenen hasarı, min/maks aralığı, krit-düzeltilmiş ortalamayı ve DPS'yi gösterir — ölçek kırılmalarını oyuncuya ulaşmadan yakalarsın.</p>

<h3>Formüller</h3>
<ul>
  <li><strong>Çıkarmalı</strong> — klasik (Dragon Quest). Yüksek DEF'te kırılır.</li>
  <li><strong>Bölmeli</strong> — modern action-RPG'lerin varsayılanı. Yumuşak azalış.</li>
  <li><strong>Yüzde-direnç</strong> — elementel hasar için tipik. %75–80'de cap.</li>
  <li><strong>Özel</strong> — JS ifadesi, sandbox: <code>atk</code>, <code>wpn</code>, <code>def</code>, <code>res</code>, <code>pen</code>, <code>armor</code>, <code>Math</code>.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Dirençler çarpımsaldır.</strong> %30 + %30 = %51, %60 değil.</li>
  <li><strong>Krit çarpanı toplamdır.</strong> 2× = normal hasarın %200'ü.</li>
  <li><strong>DPS kağıt üzerinde bir sayıdır.</strong> Cooldown, dodge, animation lock gerçek savaşta sayar, burada değil.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Combat di RPG adalah formula yang menerima stat attacker dan defender lalu menghasilkan angka — tapi formula yang mana? Subtraktif, divisif, persen-resist, dan hybrid custom berperilaku berbeda saat angka membesar. Tool ini membiarkanmu memasukkan formula dan stat lalu menampilkan langsung damage harapan, range min/maks, rata-rata yang disesuaikan crit, dan DPS — supaya kamu tangkap pecahnya skala sebelum sampai ke pemain.</p>

<h3>Formula</h3>
<ul>
  <li><strong>Subtraktif</strong> — klasik (Dragon Quest). Pecah saat DEF tinggi.</li>
  <li><strong>Divisif</strong> — default di action-RPG modern. Penurunan halus.</li>
  <li><strong>Persen-resist</strong> — umum untuk damage elemental. Cap di 75–80%.</li>
  <li><strong>Custom</strong> — ekspresi JS, sandbox: <code>atk</code>, <code>wpn</code>, <code>def</code>, <code>res</code>, <code>pen</code>, <code>armor</code>, <code>Math</code>.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Resistance bersifat multiplikatif.</strong> 30% + 30% = 51%, bukan 60%.</li>
  <li><strong>Crit multiplier itu total.</strong> 2× = 200% damage normal.</li>
  <li><strong>DPS itu angka di atas kertas.</strong> Cooldown, dodge, animation lock berlaku di combat asli, bukan di sini.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Combat trong RPG là một công thức nhận chỉ số tấn công và phòng thủ rồi cho ra một con số — nhưng công thức nào? Trừ, chia, phần-trăm-kháng và các biến thể custom hành xử rất khác khi số liệu mở rộng. Tool này cho bạn cắm công thức và chỉ số rồi ngay lập tức hiển thị sát thương kỳ vọng, khoảng min/max, trung bình có crit và DPS — để bạn bắt lỗi tỉ lệ trước khi đến tay người chơi.</p>

<h3>Các công thức</h3>
<ul>
  <li><strong>Trừ</strong> — cổ điển (Dragon Quest). Vỡ khi DEF cao.</li>
  <li><strong>Chia</strong> — mặc định ở action-RPG hiện đại. Giảm mượt.</li>
  <li><strong>Phần-trăm-kháng</strong> — phổ biến cho sát thương hệ. Cap ở 75–80%.</li>
  <li><strong>Custom</strong> — biểu thức JS, sandbox: <code>atk</code>, <code>wpn</code>, <code>def</code>, <code>res</code>, <code>pen</code>, <code>armor</code>, <code>Math</code>.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Kháng là nhân.</strong> 30% + 30% = 51%, không phải 60%.</li>
  <li><strong>Hệ số crit là tổng.</strong> 2× = 200% sát thương thường.</li>
  <li><strong>DPS là số trên giấy.</strong> Cooldown, né, animation lock đóng vai trò trong combat thật, không phải ở đây.</li>
</ul>
""",
        "hi": """
<h2>यह किसके लिए है?</h2>
<p>RPG में combat एक formula है जो attacker stats और defender stats लेकर एक number देता है — लेकिन कौन सा formula? Subtractive, divisive, percent-resist, और custom hybrids सभी numbers बढ़ने पर अलग व्यवहार करते हैं। यह tool आपको formula और stats डालने देता है और तुरंत expected damage, min/max range, crit-adjusted average, और DPS दिखाता है — ताकि आप scale ब्रेक को player तक पहुंचने से पहले पकड़ सकें।</p>

<h3>Formulas</h3>
<ul>
  <li><strong>Subtractive</strong> — classical (Dragon Quest)। High DEF पर टूटता है।</li>
  <li><strong>Divisive</strong> — modern action-RPGs का default। Smooth decline।</li>
  <li><strong>Percent resist</strong> — elemental damage के लिए typical। 75–80% पर cap।</li>
  <li><strong>Custom</strong> — JS expression, sandbox: <code>atk</code>, <code>wpn</code>, <code>def</code>, <code>res</code>, <code>pen</code>, <code>armor</code>, <code>Math</code>।</li>
</ul>

<h3>आम गलतियाँ</h3>
<ul>
  <li><strong>Resistances multiplicative हैं।</strong> 30% + 30% = 51% होते हैं, 60% नहीं।</li>
  <li><strong>Crit multiplier total है।</strong> 2× का मतलब normal damage का 200% है।</li>
  <li><strong>DPS एक paper number है।</strong> Cooldowns, dodges, animation lock real combat में मायने रखते हैं, यहाँ नहीं।</li>
</ul>
""",
        "sk": """
<h2>Načo to slúži?</h2>
<p>Combat v RPG je formula, ktorá berie staty útočníka a obrancu a vyrobí číslo — ale ktorá formula? Subtraktívna, divizívna, percent-resist a custom hybridy sa správajú inak pri škálovaní. Tento nástroj ti dovolí zadať formulu a staty a okamžite ukáže očakávaný damage, min/max range, crit-adjusted priemer a DPS — aby si zachytil rozbité škálovanie skôr, než sa dostane k hráčovi.</p>

<h3>Formuly</h3>
<ul>
  <li><strong>Subtraktívna</strong> — klasika (Dragon Quest). Rozbije sa pri vysokej DEF.</li>
  <li><strong>Divizívna</strong> — default v moderných action RPG. Plynulý pokles.</li>
  <li><strong>Percent resist</strong> — typické pre elementálny damage. Cap na 75–80 %.</li>
  <li><strong>Custom</strong> — JS výraz, sandbox: <code>atk</code>, <code>wpn</code>, <code>def</code>, <code>res</code>, <code>pen</code>, <code>armor</code>, <code>Math</code>.</li>
</ul>

<h3>Časté chyby</h3>
<ul>
  <li><strong>Resistencie sú multiplikatívne.</strong> 30 % + 30 % = 51 %, nie 60 %.</li>
  <li><strong>Crit multiplikátor je totál.</strong> 2× = 200 % normálneho damage.</li>
  <li><strong>DPS je papierové číslo.</strong> Cooldowny, úhyby, animation lock platia v reálnom boji, nie tu.</li>
</ul>
""",
        "cs": """
<h2>K čemu to slouží?</h2>
<p>Combat v RPG je formule, která bere staty útočníka a obránce a vyrobí číslo — ale která formule? Subtraktivní, divizivní, percent-resist a custom hybridy se chovají jinak při škálování. Tenhle nástroj ti dovolí zadat formuli a staty a okamžitě ukáže očekávaný damage, min/max range, crit-adjusted průměr a DPS — abys zachytil rozbité škálování dřív, než se dostane k hráči.</p>

<h3>Formule</h3>
<ul>
  <li><strong>Subtraktivní</strong> — klasika (Dragon Quest). Rozbije se při vysoké DEF.</li>
  <li><strong>Divizivní</strong> — default v moderních action RPG. Plynulý pokles.</li>
  <li><strong>Percent resist</strong> — typické pro elementální damage. Cap na 75–80 %.</li>
  <li><strong>Custom</strong> — JS výraz, sandbox: <code>atk</code>, <code>wpn</code>, <code>def</code>, <code>res</code>, <code>pen</code>, <code>armor</code>, <code>Math</code>.</li>
</ul>

<h3>Časté chyby</h3>
<ul>
  <li><strong>Resistance jsou multiplikativní.</strong> 30 % + 30 % = 51 %, ne 60 %.</li>
  <li><strong>Crit multiplikátor je totál.</strong> 2× = 200 % normálního damage.</li>
  <li><strong>DPS je papírové číslo.</strong> Cooldowny, úhyby, animation lock platí v reálném boji, ne tady.</li>
</ul>
""",
    },
    "related": ["xp-curve-calculator", "dice-roller", "color-blind-sim"],
    "howto": {"flow": "calculate", "action": "format", "noun": "damage"},
}
