"""Article: Token counting for LLM cost management.

W03 article. AI vertical. ~1000 words, English only.
"""

ARTICLE = {
    "slug": "token-counting-cost-mgmt",
    "date": "2026-05-19",
    "author": "Toolhub Team",
    "category": "ai",
    "tags": ["llm", "tokens", "cost", "anthropic", "openai", "ai-engineering"],
    "tool_refs": ["token-counter", "prompt-diff", "json-schema-to-pydantic"],
    "title": {
        "en": "Token counting for LLM cost management",
    },
    "subtitle": {
        "en": "Why your LLM bill keeps surprising you, where the expensive tokens are actually hiding, and the trade-offs worth thinking about before you ship a feature that hits the API on every page view.",
    },
    "summary": {
        "en": "Most LLM cost surprises come from one mistake: assuming a token is roughly a word. It isn't. System prompts on every request, JSON whitespace, tool-use schemas, and vision tokens add up faster than developers expect. Five places where the bill actually lives, with real numbers.",
    },
    "body": {
        "en": r"""
<p>Most LLM cost surprises come from one mistake: assuming a token is roughly a word. It isn't. A 500-word English email is around 625 tokens. A 500-character base64-encoded image fragment is also around 625 tokens. A 500-word JSON blob with whitespace and repeated field names? Closer to 1,200. Same wall-clock typing time. Very different bills at the end of the month.</p>

<p>If your feature hits an LLM on every page view and you haven't actually counted what each call costs in tokens, you don't have a cost forecast — you have a budget that explodes when traffic shows up. Here are the five places where token counts surprise developers, what the numbers look like at scale, and what to do about each before it bites.</p>

<h2>1. Tokens aren't words. They're not characters either.</h2>

<p>Tokenizers split text into sub-word units, and the rules depend on the model. The string <code>"GPT-4"</code> is 4 tokens in OpenAI's tokenizer (<code>"G", "PT", "-", "4"</code>) and 3 in Anthropic's. The string <code>"supercalifragilisticexpialidocious"</code> is 9 tokens in cl100k (OpenAI) and 11 in Claude's tokenizer. Same characters, different costs.</p>

<p>What this means in practice:</p>

<ul>
<li>You cannot reliably estimate cost by character or word count. The ratio shifts per model and per content type.</li>
<li>The same prompt may cost meaningfully more on one model than another even at the same per-token price.</li>
<li>Code, JSON, and non-English content all tokenize less efficiently than plain English — sometimes 2-3x worse.</li>
</ul>

<p>Run your actual prompts through the actual tokenizer for the actual model you're using before you ship. The <a href="/token-counter/">token counter</a> handles the major models. Anthropic also publishes their tokenizer behaviour in their <a href="https://docs.claude.com/en/docs/about-claude/models" target="_blank" rel="noopener">model documentation</a>.</p>

<h2>2. System prompts are paid for on every single request</h2>

<p>This is the one that catches everyone. You write a beautiful 2,000-token system prompt with examples, edge cases, and tone guidance. You ship the feature. It works. Then someone in finance asks why the API bill is €4,200 this month.</p>

<p>Math: 2,000 tokens × 50,000 requests/day × 30 days = 3 billion input tokens/month. At Claude Sonnet 4.6 pricing of $3/million input tokens, that's $9,000/month — just for the system prompt. The user's actual question is the cheap part.</p>

<p>Three things to do, in order of effort:</p>

<ul>
<li><strong>Enable prompt caching.</strong> Anthropic's prompt caching has a 5-minute TTL and a 90% discount on cached portions. If your system prompt is stable, mark it as <code>cache_control: { "type": "ephemeral" }</code> and most requests hit cache. Same example collapses from $9,000 to ~$900/month.</li>
<li><strong>Tighten the system prompt.</strong> Most are 2-3x longer than they need to be. Cut examples that aren't proving their worth, drop "be helpful and accurate" boilerplate the model already knows.</li>
<li><strong>Pre-process where you can.</strong> If your prompt has long instructions about output format, consider switching to a constrained output schema instead.</li>
</ul>

<h2>3. JSON in / JSON out has hidden whitespace cost</h2>

<p>If you're round-tripping JSON through the API — sending structured input, asking for structured output — whitespace and indentation get billed at full token rates.</p>

<pre><code>{
  "user_id": 12345,
  "preferences": {
    "language": "en",
    "timezone": "UTC"
  }
}     ← pretty-printed, ~30 tokens

{"user_id":12345,"preferences":{"language":"en","timezone":"UTC"}}
       ← minified, ~22 tokens (-27%)</code></pre>

<p>27% might not sound much, but compound it across a million calls. Worse: field names repeat. If you have an array of 500 objects each with the same eight keys, those eight key strings get tokenized 500 times. Abbreviated field names cost less. <code>"timezone"</code> is 2 tokens; <code>"tz"</code> is 1.</p>

<p>If you're using tool-use mode (function calling), the schema you provide also counts. Trim descriptions to what's necessary for the model to use the tool correctly, not what would help a human read it. For converting between schema formats, <a href="/json-schema-to-pydantic/">the JSON Schema to Pydantic converter</a> handles a common pattern.</p>

<h2>4. Vision tokens are not free</h2>

<p>Multimodal calls add a per-image cost most teams forget to model. Anthropic's vision pricing charges roughly 1,568 tokens for a 1092×1092 image — same as ~1,500 tokens of prose. OpenAI's scales by detail level. Both are billed at input rates.</p>

<p>If you've built a "user uploads photo of receipt, we extract line items" feature:</p>

<ul>
<li>1 image = ~1,500 input tokens for vision processing</li>
<li>+ your system prompt for the task</li>
<li>+ the JSON output</li>
<li>= ~3,000 tokens per receipt, easy</li>
</ul>

<p>10,000 receipts/day × 3,000 tokens × Claude Sonnet rates = ~$900/day in API costs alone. Compare that to your per-user revenue from the feature. The economics often demand caching, batching, or fallback to a cheaper OCR pipeline before LLM only on hard cases.</p>

<h2>5. Conversations bloat fast</h2>

<p>In a chat-style application, every turn includes the entire prior conversation as input. Turn 10 sends the previous 9 turns plus the new question. Cost grows roughly quadratically with conversation length.</p>

<p>Mitigations:</p>

<ul>
<li><strong>Summarize old turns.</strong> After turn N, replace turns 1 to N-5 with a compressed summary. The model loses some context detail; your bill gets bounded.</li>
<li><strong>Cap conversation length.</strong> Force a new conversation after 20 turns or 50K tokens of history.</li>
<li><strong>Use prompt caching for the system prompt portion</strong> so at least the stable preamble doesn't repay full cost every turn.</li>
</ul>

<p>If you're A/B testing different prompts to see which one your costs prefer, <a href="/prompt-diff/">prompt diff</a> shows what actually changed and where.</p>

<h2>The discipline</h2>

<p>Token counting isn't an optimization concern that you address after you've shipped. It's a planning concern that goes in before you write the first prompt. Three habits that pay back the time spent learning them:</p>

<ol>
<li><strong>Always know your per-request token count before shipping.</strong> Run a real example through a tokenizer, write the number in your design doc, multiply by expected traffic.</li>
<li><strong>Log token counts per request</strong> alongside latency and error rate. Anthropic and OpenAI both return <code>usage</code> fields. Push them into your metrics like any other operational signal.</li>
<li><strong>Set a hard monthly budget</strong> in your provider's dashboard. The "I'll watch it" approach has put a lot of indie devs into surprise five-figure bills.</li>
</ol>

<p>The tooling we ship at Toolhub is browser-only, no LLM in the loop — but if your team is shipping LLM-backed features, the <a href="/token-counter/">token counter</a> is the first stop. Get the cost picture before the bill picture.</p>
"""
    },
}
