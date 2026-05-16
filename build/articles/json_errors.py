"""Article: JSON — 5 common errors devs hit and how to fix them.

This is the first article in the /articles/ section. ARTICLES-INFRA / W01.
Dev/data vertical. ~1000 words, English only for this batch.
"""

ARTICLE = {
    "slug": "json-errors",
    "date": "2026-05-16",
    "author": "Toolhub Team",
    "category": "data",
    "tags": ["json", "debugging", "dev-tools", "parsing", "syntax"],
    "tool_refs": ["json-formatter", "json-diff", "json-path"],
    "title": {
        "en": "JSON: 5 common errors devs hit and how to fix them",
    },
    "subtitle": {
        "en": "Trailing commas, single quotes, comments — the five mistakes that account for most \"but it looks fine\" JSON failures, and the one-character fix for each.",
    },
    "summary": {
        "en": "Trailing commas, single quotes, unquoted keys, comments, and unescaped characters cause the majority of \"but it looks fine\" JSON failures. Five concrete fixes, with code samples and a short RFC 8259 reference.",
    },
    "body": {
        "en": r"""
<p>JSON looks simple — until your parser throws <code>SyntaxError: Unexpected token</code> at line 47 of a 200-line config file and you can't see what's wrong. The spec (RFC 8259) is barely sixteen pages, but small differences from JavaScript's looser object syntax catch out experienced developers all the time. The fix is usually one character.</p>

<p>Here are the five errors that account for the vast majority of "but it looks fine" JSON failures — what the parser sees, why it complains, and how to spot the same shape next time. If you want to throw a blob into a working tool while you read, our <a href="/json-formatter/">JSON formatter</a> will point at the exact offending column.</p>

<h2>1. Trailing commas</h2>

<p>JavaScript object literals tolerate them. JSON does not.</p>

<pre><code>{"name": "ada",}   ✗ trailing comma — invalid JSON
{"name": "ada"}    ✓ valid

[1, 2, 3,]         ✗ trailing comma — invalid
[1, 2, 3]          ✓ valid</code></pre>

<p>The grammar in RFC 8259 defines an object as <code>{ member, member, member }</code> — commas are <em>separators</em> between members, not terminators. The same rule applies to arrays.</p>

<p>This usually bites when you're hand-editing config files: you delete the last entry, forget the comma that was on the previous line, save, and the parser stops cooperating. Some tooling has trained us in the opposite direction — ESLint will helpfully <em>add</em> trailing commas to JS source so diffs are cleaner, and that habit carries over.</p>

<p>If your build chain includes a JSON5 or JSONC file (VS Code's <code>settings.json</code> is JSONC), trailing commas are allowed there — but they will fail the moment that file is read by a strict parser, like an HTTP client or a Go <code>encoding/json</code> call.</p>

<h2>2. Single vs double quotes</h2>

<p>JSON requires double quotes around every string. Single quotes are rejected, even though JavaScript treats <code>'foo'</code> and <code>"foo"</code> as equivalent.</p>

<pre><code>{'name': 'ada'}    ✗ single quotes — invalid
{"name": "ada"}    ✓ valid</code></pre>

<p>This goes for keys as well as values. The reason is that JSON is a strict subset of JavaScript object notation — the spec authors chose one quote style and one only to keep parsers simple and avoid the edge case of escaped quotes within mixed-quote strings.</p>

<p>If you're generating JSON from a templating language (Jinja, Mustache, Handlebars) and getting single quotes by mistake, check whether you're using raw string interpolation or Python's <code>repr()</code> — both prefer single quotes by default and will silently emit invalid JSON. Use <code>json.dumps()</code> in Python, <code>JSON.stringify()</code> in JavaScript, or the equivalent in your language to serialize properly.</p>

<h2>3. Unquoted keys</h2>

<p>JavaScript object literals let you write keys without quotes — <code>{name: "ada"}</code> — when the key is a valid identifier. JSON requires every key to be a quoted string, no exceptions.</p>

<pre><code>{name: "ada"}      ✗ unquoted key — invalid
{"name": "ada"}    ✓ valid</code></pre>

<p>You'll hit this when copy-pasting from JS source into a <code>.json</code> file or when a colleague writes documentation showing "the object" without actually meaning JSON. It's also a sign of confusion when a YAML or TOML user is writing JSON for the first time — both of those allow bare keys.</p>

<p>A related trap: numeric keys. JSON keys are <em>always</em> strings, even if the value looks like a number.</p>

<pre><code>{1: "first"}       ✗ unquoted, numeric — invalid
{"1": "first"}     ✓ valid</code></pre>

<p>If you're querying nested data and not sure how a parser will interpret your structure, <a href="/json-path/">JSON Path</a> lets you test selectors against a real JSON blob.</p>

<h2>4. Comments</h2>

<p>JSON has no comments. Not <code>//</code>, not <code>/* */</code>, not <code>#</code>. Douglas Crockford (the spec's designer) deliberately left them out — his reasoning was that comments encouraged people to embed parsing directives, defeating the point of a portable data format.</p>

<pre><code>{
  // user record   ✗ JSON has no comments
  "name": "ada"
}</code></pre>

<p>Most parsers will reject the entire document if they encounter a comment-shaped token. Some lenient parsers (jq, JSON5, JSONC) accept comments — but anything that hits a stricter parser downstream will fail.</p>

<p>The pragmatic workaround is to add a <code>"_comment"</code> field with the note as its value. Parsers that don't recognize it will ignore it, and humans editing the file get the context.</p>

<pre><code>{
  "_comment": "user record — see PR #423",
  "name": "ada"
}</code></pre>

<p>If you're copying JSON from JS or Python source that includes inline notes, strip them first.</p>

<h2>5. Special characters in strings</h2>

<p>Strings in JSON must escape four kinds of characters: the double quote (<code>\"</code>), the backslash (<code>\\</code>), control characters below U+0020 such as <code>\n</code> and <code>\t</code>, and the forward slash (<code>\/</code>) if you want — the last one is optional but useful in HTML contexts.</p>

<pre><code>{"path": "C:\Users\ada"}            ✗ backslash not escaped
{"path": "C:\\Users\\ada"}          ✓ valid

{"quote": "She said "hi""}          ✗ unescaped quote
{"quote": "She said \"hi\""}        ✓ valid

{"note": "line one
line two"}                          ✗ literal newline
{"note": "line one\nline two"}      ✓ valid</code></pre>

<p>For arbitrary Unicode, JSON strings support <code>\uXXXX</code> escapes — useful when you can't trust the encoding of the channel transporting the payload.</p>

<h2>From the spec</h2>

<blockquote>
  <p>"All Unicode characters may be placed within the quotation marks, except for the characters that MUST be escaped: quotation mark, reverse solidus, and the control characters (U+0000 through U+001F)."</p>
  <cite>— <a href="https://datatracker.ietf.org/doc/html/rfc8259#section-7" rel="noopener">RFC 8259 §7</a> (IETF, public domain)</cite>
</blockquote>

<p>That sentence is the entire rule for what counts as a valid JSON string. Memorize it and §5 (the trailing-comma rule) and you've covered the four most common parse failures.</p>

<p>It's also the reason pasting JSON between systems with mismatched line endings (Windows CRLF vs. Unix LF) sometimes breaks silently. If you need to compare two payloads that <em>should</em> be equivalent but one parser rejects, <a href="/json-diff/">JSON diff</a> will show you the exact byte that differs.</p>

<h2>The Toolhub workflow</h2>

<p>Three browser-side tools cover most JSON-debugging cases:</p>

<ul>
  <li><a href="/json-formatter/">JSON formatter</a> — pretty-print, validate, and pinpoint the column of a syntax error.</li>
  <li><a href="/json-diff/">JSON diff</a> — compare two payloads structurally, not line by line.</li>
  <li><a href="/json-path/">JSON Path</a> — query nested data with <code>$.users[0].name</code> selectors.</li>
</ul>

<p>Everything runs locally — your JSON never leaves the tab. Bookmark whichever fits the way you debug.</p>
""".strip(),
    },
}
