"""Article renderer — generates /articles/<slug>/index.html and /articles/index.html.

Loads every build/articles/*.py module (each exporting an ARTICLE dict) and
emits one page per article plus an index listing page. English-only at first;
the rendering already handles per-lang lookups so translations can drop in
later without code changes.

Run as part of build.py (preferred) or standalone:
    python3 build/articles.py
"""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
ARTICLES_DIR = BUILD / "articles"
PAGE_TEMPLATE = (BUILD / "page_template.html").read_text()

# Reuse i18n
spec = importlib.util.spec_from_file_location("i18n", BUILD / "i18n.py")
i18n_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(i18n_mod)
UI = i18n_mod.UI
LANGS = i18n_mod.LANGS

# Reuse tool manifests so the "Related Toolhub tools" block can pick up
# names/taglines instead of bare slugs.
TOOLS = []
for tool_file in sorted((BUILD / "tools").glob("*.py")):
    if tool_file.name.startswith("_"):
        continue
    sp = importlib.util.spec_from_file_location(tool_file.stem, tool_file)
    mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(mod)
    if hasattr(mod, "TOOL"):
        TOOLS.append(mod.TOOL)
TOOLS_BY_SLUG = {t["slug"]: t for t in TOOLS}

OG_LOCALES = {
    "en": "en_GB", "de": "de_DE", "es": "es_ES", "fr": "fr_FR", "it": "it_IT",
    "pt": "pt_BR", "pl": "pl_PL", "ja": "ja_JP", "nl": "nl_NL", "tr": "tr_TR",
    "id": "id_ID", "vi": "vi_VN", "hi": "hi_IN", "sk": "sk_SK", "cs": "cs_CZ",
}


ARTICLE_CSS = """
<style>
.article-meta { color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.5rem; display: flex; gap: 1.25rem; flex-wrap: wrap; }
.article-meta strong { color: var(--text); font-weight: 600; }
.article-subtitle { color: var(--text-muted); font-size: 1.1rem; line-height: 1.5; margin-bottom: 1.5rem; font-style: italic; }
.article-body { max-width: 70ch; margin: 0 auto; line-height: 1.65; }
.article-body p { color: var(--text-muted); font-size: 1rem; }
.article-body h2 { margin-top: 2rem; font-size: 1.3rem; }
.article-body pre { background: var(--code-bg); border: 1px solid var(--border); border-radius: 8px; padding: 0.9rem 1rem; overflow-x: auto; font-size: 0.88rem; line-height: 1.5; margin: 1rem 0; }
.article-body pre code { background: none; padding: 0; font-size: inherit; color: var(--text); display: block; white-space: pre; }
.article-body blockquote { border-left: 3px solid var(--accent); background: var(--surface); margin: 1.5rem 0; padding: 0.9rem 1.1rem; border-radius: 0 8px 8px 0; }
.article-body blockquote p { margin-bottom: 0.4rem; color: var(--text); font-style: italic; }
.article-body blockquote cite { font-size: 0.88rem; color: var(--text-muted); font-style: normal; display: block; }
.article-related { border-top: 1px solid var(--border); margin-top: 2.5rem; padding-top: 1.5rem; }
.article-related h2 { font-size: 1.1rem; margin-bottom: 0.6rem; margin-top: 0; }
.article-related ul { padding-left: 1.25rem; }
.article-related li { color: var(--text-muted); }
.article-back { display: inline-block; margin: 2rem 0 0.5rem; font-size: 0.95rem; }
.articles-list { list-style: none; padding: 0; margin: 1.5rem 0 0; }
.articles-list li { border-bottom: 1px solid var(--border); padding: 1.25rem 0; }
.articles-list li:last-child { border-bottom: 0; }
.articles-list h3 { font-size: 1.15rem; margin: 0 0 0.4rem; }
.articles-list h3 a { color: var(--text); text-decoration: none; }
.articles-list h3 a:hover { color: var(--accent); text-decoration: underline; }
.articles-list .date { color: var(--text-muted); font-size: 0.85rem; }
.articles-list .summary { color: var(--text-muted); font-size: 0.95rem; margin: 0.35rem 0 0; line-height: 1.55; }
</style>
""".strip()


def load_articles():
    """Load every build/articles/*.py manifest, sorted newest-first by date."""
    articles = []
    if not ARTICLES_DIR.is_dir():
        return articles
    for f in sorted(ARTICLES_DIR.glob("*.py")):
        if f.name.startswith("_"):
            continue
        sp = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(sp)
        sp.loader.exec_module(mod)
        if hasattr(mod, "ARTICLE"):
            articles.append(mod.ARTICLE)
    articles.sort(key=lambda a: a["date"], reverse=True)
    return articles


def _t(article, key, lang):
    """Per-lang lookup with English fallback."""
    return article[key].get(lang) or article[key]["en"]


def _has_lang(article, lang):
    """An article is considered translated for a lang if its body field has
    a non-empty entry for that lang. English is always assumed present."""
    if lang == "en":
        return True
    return bool(article.get("body", {}).get(lang))


def article_path(lang, slug):
    return f"/articles/{slug}/" if lang == "en" else f"/{lang}/articles/{slug}/"


def articles_index_path(lang):
    return "/articles/" if lang == "en" else f"/{lang}/articles/"


def article_output_path(lang, slug):
    return (ROOT / "articles" / slug / "index.html") if lang == "en" \
        else (ROOT / lang / "articles" / slug / "index.html")


def articles_index_output_path(lang):
    return (ROOT / "articles" / "index.html") if lang == "en" \
        else (ROOT / lang / "articles" / "index.html")


def _fill(text, mapping):
    for _ in range(3):
        for k, v in mapping.items():
            text = text.replace("{{" + k + "}}", str(v))
    return text


def _common_placeholders(lang, slug_with_articles, title, description):
    """Placeholders shared between page_template.html for static pages.
    slug_with_articles is e.g. "articles/json-errors" or "articles".
    """
    ui = UI[lang]
    sel = {l: ('selected="selected"' if l == lang else "") for l in LANGS}
    path = f"/{slug_with_articles}/" if lang == "en" else f"/{lang}/{slug_with_articles}/"

    def lp(seg):
        return f"/{seg}/" if lang == "en" else f"/{lang}/{seg}/"

    return {
        "LANG": lang,
        "TITLE": title,
        "H1": title,
        "DESCRIPTION": description,
        "PATH": path,
        "HOME": "/" if lang == "en" else f"/{lang}/",
        "PRIVACY": lp("privacy"),
        "PRIVACY_LBL": ui["privacy"],
        "ABOUT": lp("about"),
        "ABOUT_LBL": ui["about"],
        "CONTACT": lp("contact"),
        "CONTACT_LBL": ui["contact"],
        "FOR_SCHOOLS": lp("for-schools"),
        "FOR_SCHOOLS_LBL": ui["for_schools"],
        "DATA_HANDLING": lp("how-we-handle-your-data"),
        "DATA_HANDLING_LBL": ui["data_handling"],
        "AFFILIATE_DISCLOSURE": lp("affiliate-disclosure"),
        "AFFILIATE_DISCLOSURE_LBL": ui["affiliate_disclosure"],
        "COMPANION_TOOLS": lp("companion-tools"),
        "COMPANION_TOOLS_LBL": ui["companion_tools"],
        "ARTICLES": articles_index_path(lang),
        "NAV_ARTICLES_LBL": ui["nav_articles"],
        "ALL_TOOLS": ui["all_tools"],
        "THEME_TIP": ui["theme_tip"],
        "LANGUAGE": ui["language"],
        "SLUG": slug_with_articles,
        "SEL_EN": sel["en"], "SEL_DE": sel["de"], "SEL_ES": sel["es"],
        "SEL_FR": sel["fr"], "SEL_IT": sel["it"], "SEL_PT": sel["pt"],
        "SEL_PL": sel["pl"], "SEL_JA": sel["ja"], "SEL_NL": sel["nl"],
        "SEL_TR": sel["tr"], "SEL_ID": sel["id"], "SEL_VI": sel["vi"],
        "SEL_HI": sel["hi"], "SEL_SK": sel["sk"], "SEL_CS": sel["cs"],
        "OG_LOCALE": OG_LOCALES.get(lang, "en_GB"),
        "INLANG": lang,
        "OG_IMAGE_URL": "https://toolhub.software/og-image.png",
        "BREADCRUMB_LBL": ui["breadcrumb"],
    }


def _alternate_links_for_set(slug_with_articles, available_langs):
    """Emit hreflang links for the langs actually rendered for this URL.
    x-default always points to the EN variant."""
    out = []
    for L in available_langs:
        path = f"/{slug_with_articles}/" if L == "en" else f"/{L}/{slug_with_articles}/"
        out.append(f'<link rel="alternate" hreflang="{L}" href="https://toolhub.software{path}">')
    out.append(f'<link rel="alternate" hreflang="x-default" href="https://toolhub.software/{slug_with_articles}/">')
    return "\n  ".join(out)


def render_article(article, lang):
    """Render one article page."""
    ui = UI[lang]
    slug = article["slug"]
    title = _t(article, "title", lang)
    subtitle = _t(article, "subtitle", lang)
    summary = _t(article, "summary", lang)
    body = _t(article, "body", lang)

    # Build the related-tools block (only when refs resolve to real tools).
    refs = article.get("tool_refs", [])
    related_items = []
    for ref in refs:
        t = TOOLS_BY_SLUG.get(ref)
        href = f"/{ref}/" if lang == "en" else f"/{lang}/{ref}/"
        if t:
            name = t["i18n"].get(lang, t["i18n"]["en"])["name"]
            tagline = t["i18n"].get(lang, t["i18n"]["en"])["tagline"]
            related_items.append(f'<li><a href="{href}">{name}</a> — {tagline}</li>')
        else:
            related_items.append(f'<li><a href="{href}">/{ref}/</a></li>')

    related_html = ""
    if related_items:
        related_html = (
            f'<aside class="article-related">'
            f'<h2>{ui["article_related_tools"]}</h2>'
            f'<ul>{"".join(related_items)}</ul>'
            f'</aside>'
        )

    back_html = (
        f'<a class="article-back" href="{articles_index_path(lang)}">'
        f'{ui["article_back_to_index"]}</a>'
    )

    meta_html = (
        f'<p class="article-meta">'
        f'<span><strong>{ui["article_published"]}:</strong> {article["date"]}</span>'
        f'<span><strong>{ui["article_by"]}:</strong> {article["author"]}</span>'
        f'</p>'
    )

    body_html = (
        ARTICLE_CSS
        + f'<article class="article-body">'
        + f'<p class="article-subtitle">{subtitle}</p>'
        + meta_html
        + body
        + related_html
        + back_html
        + '</article>'
    )

    placeholders = _common_placeholders(lang, f"articles/{slug}", title, summary)
    placeholders.update({
        "BODY": body_html,
        "SCHEMA_TYPE": "Article",
        "ALTERNATE_LINKS": _alternate_links_for_set(
            f"articles/{slug}",
            [L for L in LANGS if _has_lang(article, L)],
        ),
    })

    # page_template.html lang-select expects {{SLUG}} placement at /{lang}/{SLUG}/.
    return _fill(PAGE_TEMPLATE, placeholders)


def render_index(articles, lang):
    """Render the /articles/ listing page for a given lang."""
    ui = UI[lang]
    title = ui["articles_index_title"]
    subtitle = ui["articles_index_subtitle"]

    items = []
    for a in articles:
        if not _has_lang(a, lang):
            continue
        href = article_path(lang, a["slug"])
        items.append(
            f'<li>'
            f'<h3><a href="{href}">{_t(a, "title", lang)}</a></h3>'
            f'<p class="date">{a["date"]}</p>'
            f'<p class="summary">{_t(a, "summary", lang)}</p>'
            f'</li>'
        )

    listing_html = (
        ARTICLE_CSS
        + f'<p class="article-subtitle">{subtitle}</p>'
        + (f'<ul class="articles-list">{"".join(items)}</ul>' if items
           else '<p>—</p>')
    )

    placeholders = _common_placeholders(lang, "articles", title, subtitle)
    placeholders.update({
        "BODY": listing_html,
        "SCHEMA_TYPE": "CollectionPage",
        # Index is currently EN-only; emit just en + x-default.
        "ALTERNATE_LINKS": _alternate_links_for_set("articles", ["en"]),
    })
    return _fill(PAGE_TEMPLATE, placeholders)


def write_articles():
    articles = load_articles()
    if not articles:
        print("  ! No articles found in build/articles/")
        return 0

    written = 0
    # Per-article pages — only for langs that have body content.
    for a in articles:
        for L in LANGS:
            if not _has_lang(a, L):
                continue
            out = article_output_path(L, a["slug"])
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(render_article(a, L))
            written += 1

    # Index page — EN only for now (no translated index variants).
    idx_out = articles_index_output_path("en")
    idx_out.parent.mkdir(parents=True, exist_ok=True)
    idx_out.write_text(render_index(articles, "en"))
    written += 1

    print(f"  ✓ Rendered {written} article files ({len(articles)} article(s) + 1 index)")
    return written


if __name__ == "__main__":
    print("Article renderer")
    write_articles()
    print("Done.")
