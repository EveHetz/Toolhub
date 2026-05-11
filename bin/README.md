# bin/ — Toolhub lifecycle scripts

Single source of truth for adding and removing tools. Either script
keeps every dependent artefact (manifest, rendered pages, sitemap,
home-page TOOLS array, cross-references in other tools' `related`
arrays) in sync — there's no separate manifest-edit + sitemap-edit
+ cross-link-audit dance.

Both scripts are:

- **idempotent** — re-running with the same arguments is a no-op
- **dry-run-able** — `--dry-run` prints the plan and changes nothing
- **stdlib-only** — no extra Python dependencies

Run from the repo root.

---

## `bin/addtool`

```
bin/addtool <slug> --cat <category> [--icon <emoji>] [--from <existing-slug>] [--dry-run]
```

- `<slug>` must be kebab-case, 3–40 chars, matching `^[a-z][a-z0-9-]*[a-z0-9]$`
- `--cat` must be one of the categories already in use across
  `build/tools/*.py` (run any existing tool through `grep '"category"'`
  to see the list)
- `--icon` defaults to `🛠`
- `--from <existing-slug>` clones that tool's manifest as a starting
  template (useful for variants — `bin/addtool color-blender --cat design --from color-converter`).
  The cloned `name`/`tagline`/`description` are explicitly TODO-marked so
  the operator can't accidentally ship under the wrong name.

What it does:

1. Validates slug + category
2. Writes `build/tools/<slug_underscored>.py` with placeholder i18n entries
   for every language (each marked `TODO`), an empty `body`, an empty
   `script`, and a 3-section placeholder `help` block
3. Runs `python3 build/build.py` to render the per-language pages
4. Runs `python3 build/build.py --update-index` to refresh the home-page
   `TOOLS` array

If the manifest already exists, addtool exits 0 without touching anything.

### Examples

```
bin/addtool json-sorter --cat data
bin/addtool color-blender --cat design --icon 🎨 --from color-converter
bin/addtool json-sorter --cat data --dry-run
```

---

## `bin/removetool`

```
bin/removetool <slug> [--dry-run]
```

What it does:

1. Lists every artefact it would touch:
   - `build/tools/<slug_underscored>.py`
   - `/<slug>/` and `/<lang>/<slug>/` rendered directories
   - `<url>` blocks in `sitemap.xml` whose `<loc>` ends with `/<slug>/`
   - Other manifests whose `related` array mentions this slug
2. With `--dry-run`, stops there
3. Otherwise removes everything in the list and re-runs
   `python3 build/build.py --update-index` so the home-page TOOLS array
   no longer references the removed tool

If nothing matches, removetool exits 0 without touching anything.

### Examples

```
bin/removetool json-sorter --dry-run
bin/removetool json-sorter
```

---

## When to use which

- Adding a new tool? Use `bin/addtool` rather than hand-creating files —
  it guarantees you don't miss the home-page TOOLS array or skip a
  language in i18n.
- Decommissioning a tool? Use `bin/removetool` rather than hand-deleting
  directories — it cleans up sitemap entries and related-array
  cross-references too.
- One-off edits to an existing tool's content live in the manifest;
  these scripts are only for the create/destroy lifecycle.
