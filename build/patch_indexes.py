#!/usr/bin/env python3
"""
Batch F: in-place polish of all 5 index.html files.

Changes:
  - Filter buttons rendered from JS using actual category counts (so
    'validation' / 'design' / 'datetime' / 'math' tools no longer fall
    through the filter)
  - Hero subtitle uses live tool count from TOOLS array
  - Theme toggle init fixed (default-dark now shows the right icon)
  - `/` keyboard shortcut to focus search
  - Empty 'no-results' string set by JS using i18n
  - Lang select reflects the current language
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

LANG_DATA = {
    "en": {
        "all": "All",
        "no_results": "No tools found. Try a different search.",
        "hero_sub_post": "tools — fast, private, no signup. Just use them.",
        "search_hint": "Search tools…  (press / to focus)",
        "cats": {
            "developer": "Developer", "text": "Text", "encoding": "Encoding",
            "data": "Data", "security": "Security", "media": "Media",
            "validation": "Validation", "design": "Design",
            "datetime": "Date &amp; Time", "math": "Math",
        },
    },
    "de": {
        "all": "Alle",
        "no_results": "Keine Tools gefunden. Versuche eine andere Suche.",
        "hero_sub_post": "Tools — schnell, privat, ohne Anmeldung.",
        "search_hint": "Tools suchen…  (Taste / drücken)",
        "cats": {
            "developer": "Entwickler", "text": "Text", "encoding": "Kodierung",
            "data": "Daten", "security": "Sicherheit", "media": "Medien",
            "validation": "Validierung", "design": "Design",
            "datetime": "Datum &amp; Zeit", "math": "Mathe",
        },
    },
    "es": {
        "all": "Todas",
        "no_results": "No se encontraron herramientas. Prueba con otra búsqueda.",
        "hero_sub_post": "herramientas — rápidas, privadas, sin registro.",
        "search_hint": "Buscar herramientas…  (pulsa /)",
        "cats": {
            "developer": "Desarrollo", "text": "Texto", "encoding": "Codificación",
            "data": "Datos", "security": "Seguridad", "media": "Medios",
            "validation": "Validación", "design": "Diseño",
            "datetime": "Fecha y Hora", "math": "Matemáticas",
        },
    },
    "fr": {
        "all": "Tous",
        "no_results": "Aucun outil trouvé. Essayez une autre recherche.",
        "hero_sub_post": "outils — rapides, privés, sans inscription.",
        "search_hint": "Rechercher des outils…  (appuyez sur /)",
        "cats": {
            "developer": "Développeur", "text": "Texte", "encoding": "Encodage",
            "data": "Données", "security": "Sécurité", "media": "Média",
            "validation": "Validation", "design": "Design",
            "datetime": "Date &amp; Heure", "math": "Maths",
        },
    },
    "it": {
        "all": "Tutti",
        "no_results": "Nessuno strumento trovato. Prova un'altra ricerca.",
        "hero_sub_post": "strumenti — veloci, privati, senza registrazione.",
        "search_hint": "Cerca strumenti…  (premi /)",
        "cats": {
            "developer": "Sviluppatore", "text": "Testo", "encoding": "Codifica",
            "data": "Dati", "security": "Sicurezza", "media": "Media",
            "validation": "Validazione", "design": "Design",
            "datetime": "Data &amp; Ora", "math": "Matematica",
        },
    },
}


def patch_one(path: Path, lang: str) -> None:
    data = LANG_DATA[lang]
    text = path.read_text()

    # 1. Replace the static filters block with an empty container (JS will populate)
    text = re.sub(
        r'<div class="filters" id="filters">[\s\S]*?</div>',
        '<div class="filters" id="filters"></div>',
        text, count=1,
    )

    # 2. Replace the hero subtitle <p> with one that gets filled from JS
    text = re.sub(
        r'(<section class="hero">\s*<h1>[^<]+</h1>\s*<p)[^>]*>[^<]+</p>',
        r'\1 id="hero-sub"></p>',
        text, count=1,
    )

    # 3. Replace search placeholder with localised "press / to focus" hint
    text = re.sub(
        r'(<input type="text" id="search" placeholder=)"[^"]+"',
        rf'\1"{data["search_hint"]}"',
        text, count=1,
    )

    # 4. Replace 'no-results' div content
    text = re.sub(
        r'(<div class="no-results" id="no-results">)[^<]+(</div>)',
        rf'\1{data["no_results"]}\2',
        text, count=1,
    )

    # 5. Mark the current language in the lang-select
    if lang == "en":
        sel_pattern = r'<option value="">'
        sel_replace = '<option value="" selected="selected">'
    else:
        sel_pattern = rf'<option value="{lang}">'
        sel_replace = f'<option value="{lang}" selected="selected">'
    text = re.sub(sel_pattern, sel_replace, text, count=1)

    # 6. Inject the data block + dynamic init script just before the closing TOOLS render
    cat_json = (
        "{"
        + ", ".join(f'"{k}": "{v}"' for k, v in data["cats"].items())
        + "}"
    )
    init_block = f"""
    const LBL_ALL = "{data['all']}";
    const HERO_SUB_POST = "{data['hero_sub_post']}";
    const CAT_LABELS = {cat_json};

    function renderFilters() {{
      const counts = {{}};
      for (const t of TOOLS) counts[t.cat] = (counts[t.cat] || 0) + 1;
      const cats = Object.keys(counts).sort((a, b) => counts[b] - counts[a]);
      const wrap = document.getElementById('filters');
      let html = `<button class="filter-btn active" data-cat="all">${{LBL_ALL}} <span class="cnt">${{TOOLS.length}}</span></button>`;
      for (const c of cats) {{
        const label = CAT_LABELS[c] || c.charAt(0).toUpperCase() + c.slice(1);
        html += `<button class="filter-btn" data-cat="${{c}}">${{label}} <span class="cnt">${{counts[c]}}</span></button>`;
      }}
      wrap.innerHTML = html;
    }}

    function renderHero() {{
      document.getElementById('hero-sub').textContent = `${{TOOLS.length}} ${{HERO_SUB_POST}}`;
    }}
"""

    # Insert init_block right after the TOOLS = [ ... ]; line
    text = re.sub(
        r'(const TOOLS\s*=\s*\[[\s\S]*?\];)',
        r'\1\n' + init_block,
        text, count=1,
    )

    # 7. Theme toggle init: also flip icon when default-dark
    text = re.sub(
        r"const saved = localStorage\.getItem\('theme'\) \|\| 'dark';[\s\S]*?render\(TOOLS\);",
        """const saved = localStorage.getItem('theme') || 'dark';
    if (saved === 'light') {
      document.documentElement.setAttribute('data-theme', 'light');
      document.querySelector('.theme-toggle').textContent = '🌙';
    } else {
      document.querySelector('.theme-toggle').textContent = '☀️';
    }
    renderFilters();
    renderHero();
    render(TOOLS);

    // `/` keyboard shortcut to focus search
    document.addEventListener('keydown', e => {
      if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
        e.preventDefault();
        document.getElementById('search').focus();
      }
    });""",
        text, count=1, flags=re.DOTALL,
    )

    # 8. Add a tiny .cnt CSS rule for filter button counts (idempotent insert)
    if ".filter-btn .cnt" not in text:
        text = text.replace(
            ".filter-btn:hover, .filter-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); }",
            ".filter-btn:hover, .filter-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); }\n    .filter-btn .cnt { display: inline-block; margin-left: 0.3rem; padding: 0 0.35rem; border-radius: 8px; background: rgba(255,255,255,0.12); font-size: 0.72rem; font-weight: 600; }\n    .filter-btn:not(.active) .cnt { background: var(--bg); color: var(--text-muted); }",
        )

    path.write_text(text)
    print(f"  ✓ patched {path.relative_to(ROOT)}")


def main():
    print("Batch F — index.html polish")
    patch_one(ROOT / "index.html", "en")
    for lang in ("de", "es", "fr", "it"):
        patch_one(ROOT / lang / "index.html", lang)
    print("Done.")


if __name__ == "__main__":
    main()
