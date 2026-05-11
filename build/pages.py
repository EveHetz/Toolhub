# Static content pages — about, contact, for-schools.
# Each page has:
#   slug    — URL segment (e.g. "about" => /about/ for EN, /<lang>/about/ for others)
#   schema  — schema.org @type for the JSON-LD WebPage variant (AboutPage, ContactPage, WebPage)
#   i18n[lang] = { title, h1, description, body (HTML) }
#
# Pages are pure static content. No body/script/help like tools — rendered via
# build/page_template.html, NOT build/template.html.

REPO_URL = "https://github.com/JXXR1/Toolhub"
REPO_ISSUES = "https://github.com/JXXR1/Toolhub/issues"
CONTACT_EMAIL = "JXXR1@users.noreply.github.com"


def _about_body(intro_what, intro_why, intro_who, intro_how, intro_oss, intro_no_ai,
                h_what, h_why, h_who, h_how, h_oss, h_no_ai):
    return f"""
<h2>{h_what}</h2>
<p>{intro_what}</p>

<h2>{h_why}</h2>
<p>{intro_why}</p>

<h2>{h_who}</h2>
<p>{intro_who}</p>

<h2>{h_how}</h2>
<p>{intro_how}</p>

<h2>{h_oss}</h2>
<p>{intro_oss}</p>

<h2>{h_no_ai}</h2>
<p>{intro_no_ai}</p>
""".strip()


PAGES = {
    "about": {
        "slug": "about",
        "schema": "AboutPage",
        "i18n": {
            "en": {
                "title": "About Toolhub",
                "h1": "About Toolhub",
                "description": "Toolhub is a small no-tracking utility site built by one person. Free developer tools that run entirely in your browser, no signup, no data collection.",
                "body": _about_body(
                    intro_what="Toolhub is a collection of free developer and everyday utility tools that run entirely in your browser. No signup, no account, no tracking, no server-side processing. Paste your data in, get the result, close the tab — nothing is stored or transmitted.",
                    intro_why="Most online utility sites are ad-laden parking pages or shovel your data through fourteen third-party trackers before you even click anything. Toolhub is the alternative: one page, one tool, runs locally, leaves you alone.",
                    intro_who=f'JXXR1, indie maintainer. No company, no funding round, no investors. Toolhub started as a side project to scratch a personal itch — a single page that did one tool well — and grew from there. Reachable via <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="The site is static HTML hosted on GitHub Pages. Every tool runs as JavaScript in your browser — no API calls, no server-side compute, no data leaves your device unless explicitly noted (for example the YouTube Thumbnail tool fetches an image from YouTube's CDN; everything else is purely local).",
                    intro_oss=f'The full source is at <a href="{REPO_URL}">{REPO_URL}</a>. Contributions, bug reports, and tool ideas are welcome via GitHub Issues.',
                    intro_no_ai="Tool help blocks and translations are human-reviewed within reason, not pasted from an LLM. If you spot a translation that sounds robotic or wrong, open an issue — it's an easy fix and the kind of contribution that makes the site better for everyone.",
                    h_what="What Toolhub is",
                    h_why="Why",
                    h_who="Who",
                    h_how="How it works",
                    h_oss="Open source",
                    h_no_ai="No AI slop",
                ),
            },
            "de": {
                "title": "Über Toolhub",
                "h1": "Über Toolhub",
                "description": "Toolhub ist eine kleine, tracking-freie Utility-Seite, gebaut von einer Person. Kostenlose Entwickler-Tools, die komplett im Browser laufen — ohne Anmeldung, ohne Datensammlung.",
                "body": _about_body(
                    intro_what="Toolhub ist eine Sammlung kostenloser Entwickler- und Alltags-Tools, die komplett in deinem Browser laufen. Keine Anmeldung, kein Konto, kein Tracking, keine serverseitige Verarbeitung. Daten einfügen, Ergebnis bekommen, Tab schließen — nichts wird gespeichert oder übertragen.",
                    intro_why="Die meisten Utility-Seiten im Netz sind entweder mit Werbung vollgepflasterte Parking-Pages oder schicken deine Daten durch vierzehn Drittanbieter-Tracker, bevor du überhaupt klickst. Toolhub ist die Alternative: eine Seite, ein Tool, läuft lokal, lässt dich in Ruhe.",
                    intro_who=f'JXXR1, unabhängiger Maintainer. Keine Firma, keine Finanzierungsrunde, keine Investoren. Toolhub fing als Nebenprojekt an — eine einzige Seite, die ein Tool gut macht — und ist von dort gewachsen. Erreichbar über <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="Die Seite ist statisches HTML, gehostet auf GitHub Pages. Jedes Tool läuft als JavaScript in deinem Browser — keine API-Aufrufe, keine serverseitige Berechnung, keine Daten verlassen dein Gerät, außer es ist explizit angemerkt (zum Beispiel lädt das YouTube-Thumbnail-Tool ein Bild von YouTubes CDN; alles andere ist rein lokal).",
                    intro_oss=f'Der komplette Quellcode liegt auf <a href="{REPO_URL}">{REPO_URL}</a>. Beiträge, Bug-Reports und Tool-Ideen sind über GitHub Issues willkommen.',
                    intro_no_ai="Hilfetexte und Übersetzungen sind nach Möglichkeit von Menschen geprüft, nicht aus einem LLM kopiert. Wenn dir eine Übersetzung robotisch oder falsch vorkommt, öffne ein Issue — das ist eine schnelle Korrektur und macht die Seite für alle besser.",
                    h_what="Was Toolhub ist",
                    h_why="Warum",
                    h_who="Wer",
                    h_how="Wie es funktioniert",
                    h_oss="Open Source",
                    h_no_ai="Kein KI-Schrott",
                ),
            },
            "es": {
                "title": "Acerca de Toolhub",
                "h1": "Acerca de Toolhub",
                "description": "Toolhub es un pequeño sitio de utilidades sin tracking, hecho por una sola persona. Herramientas gratis para desarrolladores que se ejecutan enteramente en tu navegador, sin registro y sin recolectar datos.",
                "body": _about_body(
                    intro_what="Toolhub es una colección de herramientas gratis para desarrolladores y uso diario que se ejecutan enteramente en tu navegador. Sin registro, sin cuenta, sin tracking, sin procesamiento en servidor. Pegas los datos, obtienes el resultado, cierras la pestaña — nada se almacena ni se transmite.",
                    intro_why="La mayoría de sitios de utilidades online son páginas llenas de anuncios o pasan tus datos por catorce trackers de terceros antes de que hagas un solo clic. Toolhub es la alternativa: una página, una herramienta, funciona en local, te deja en paz.",
                    intro_who=f'JXXR1, mantenedor independiente. Sin empresa, sin ronda de financiación, sin inversores. Toolhub empezó como un proyecto paralelo para resolver una necesidad personal — una sola página que hiciera bien una herramienta — y creció desde ahí. Contactable vía <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="El sitio es HTML estático alojado en GitHub Pages. Cada herramienta funciona como JavaScript en tu navegador — sin llamadas a APIs, sin cómputo en servidor, ningún dato sale de tu dispositivo a menos que se indique explícitamente (por ejemplo, la herramienta de YouTube Thumbnail descarga una imagen desde la CDN de YouTube; todo lo demás es puramente local).",
                    intro_oss=f'El código fuente completo está en <a href="{REPO_URL}">{REPO_URL}</a>. Contribuciones, reportes de bugs e ideas de herramientas son bienvenidas vía GitHub Issues.',
                    intro_no_ai="Los textos de ayuda y traducciones están revisados por personas dentro de lo razonable, no pegados de un LLM. Si ves una traducción que suena robótica o incorrecta, abre un issue — es un cambio fácil y de los que hacen mejor el sitio para todos.",
                    h_what="Qué es Toolhub",
                    h_why="Por qué",
                    h_who="Quién",
                    h_how="Cómo funciona",
                    h_oss="Open source",
                    h_no_ai="Nada de basura generada por IA",
                ),
            },
            "fr": {
                "title": "À propos de Toolhub",
                "h1": "À propos de Toolhub",
                "description": "Toolhub est un petit site d'utilitaires sans tracking, fait par une seule personne. Des outils dev gratuits qui tournent entièrement dans ton navigateur, sans inscription ni collecte de données.",
                "body": _about_body(
                    intro_what="Toolhub est une collection d'outils gratuits pour développeurs et usage quotidien qui tournent entièrement dans ton navigateur. Pas d'inscription, pas de compte, pas de tracking, pas de traitement côté serveur. Tu colles tes données, tu obtiens le résultat, tu fermes l'onglet — rien n'est stocké ni transmis.",
                    intro_why="La plupart des sites d'utilitaires en ligne sont des pages couvertes de pubs ou refilent tes données à quatorze trackers tiers avant même que tu cliques. Toolhub est l'alternative : une page, un outil, tourne en local, te laisse tranquille.",
                    intro_who=f'JXXR1, mainteneur indépendant. Pas de société, pas de levée de fonds, pas d\'investisseurs. Toolhub a commencé comme un side project pour résoudre un besoin perso — une seule page qui fait bien un outil — et a grandi à partir de là. Joignable via <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="Le site est du HTML statique hébergé sur GitHub Pages. Chaque outil tourne en JavaScript dans ton navigateur — pas d'appels API, pas de calcul serveur, aucune donnée ne quitte ton appareil sauf mention explicite (par exemple l'outil YouTube Thumbnail récupère une image depuis le CDN de YouTube ; tout le reste est purement local).",
                    intro_oss=f'Le code source complet est sur <a href="{REPO_URL}">{REPO_URL}</a>. Les contributions, rapports de bugs et idées d\'outils sont les bienvenus via GitHub Issues.',
                    intro_no_ai="Les textes d'aide et les traductions sont relus par des humains dans la mesure du raisonnable, pas collés depuis un LLM. Si tu vois une traduction qui sonne robotique ou fausse, ouvre une issue — c'est une correction facile et le genre de contribution qui rend le site meilleur pour tout le monde.",
                    h_what="Ce qu'est Toolhub",
                    h_why="Pourquoi",
                    h_who="Qui",
                    h_how="Comment ça marche",
                    h_oss="Open source",
                    h_no_ai="Pas de contenu IA bâclé",
                ),
            },
            "it": {
                "title": "Chi siamo — Toolhub",
                "h1": "Chi siamo",
                "description": "Toolhub è un piccolo sito di utility senza tracking, costruito da una sola persona. Strumenti per sviluppatori gratuiti che girano interamente nel tuo browser, senza registrazione e senza raccolta dati.",
                "body": _about_body(
                    intro_what="Toolhub è una raccolta di strumenti gratuiti per sviluppatori e uso quotidiano che girano interamente nel tuo browser. Niente registrazione, niente account, niente tracking, niente elaborazione server-side. Incolli i dati, ottieni il risultato, chiudi la tab — nulla viene salvato o trasmesso.",
                    intro_why="La maggior parte dei siti di utility online sono parking page piene di pubblicità o passano i tuoi dati attraverso quattordici tracker di terze parti prima ancora che tu clicchi qualcosa. Toolhub è l'alternativa: una pagina, uno strumento, gira in locale, ti lascia in pace.",
                    intro_who=f'JXXR1, maintainer indipendente. Niente azienda, niente round di finanziamento, niente investitori. Toolhub è nato come progetto secondario per risolvere una necessità personale — una singola pagina che facesse bene uno strumento — ed è cresciuto da lì. Contattabile via <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="Il sito è HTML statico ospitato su GitHub Pages. Ogni strumento gira come JavaScript nel tuo browser — niente chiamate API, niente calcoli server-side, nessun dato lascia il tuo dispositivo salvo dove esplicitamente indicato (per esempio lo strumento YouTube Thumbnail scarica un'immagine dalla CDN di YouTube; tutto il resto è puramente locale).",
                    intro_oss=f'Il codice sorgente completo è su <a href="{REPO_URL}">{REPO_URL}</a>. Contributi, segnalazioni di bug e idee per strumenti sono i benvenuti via GitHub Issues.',
                    intro_no_ai="I testi di aiuto e le traduzioni sono rivisti da persone per quanto possibile, non incollati da un LLM. Se vedi una traduzione che suona robotica o sbagliata, apri una issue — è una correzione facile e il tipo di contributo che rende il sito migliore per tutti.",
                    h_what="Cos'è Toolhub",
                    h_why="Perché",
                    h_who="Chi",
                    h_how="Come funziona",
                    h_oss="Open source",
                    h_no_ai="Niente robaccia da IA",
                ),
            },
            "pt": {
                "title": "Sobre o Toolhub",
                "h1": "Sobre o Toolhub",
                "description": "Toolhub é um site pequeno de utilitários sem tracking, feito por uma pessoa só. Ferramentas grátis para devs que rodam inteiramente no seu navegador, sem cadastro e sem coletar dados.",
                "body": _about_body(
                    intro_what="Toolhub é uma coleção de ferramentas grátis para devs e uso cotidiano que rodam inteiramente no seu navegador. Sem cadastro, sem conta, sem tracking, sem processamento no servidor. Você cola os dados, pega o resultado, fecha a aba — nada é guardado nem transmitido.",
                    intro_why="A maioria dos sites de utilitários online são páginas lotadas de anúncios ou passam seus dados por quatorze trackers de terceiros antes de você clicar em qualquer coisa. O Toolhub é a alternativa: uma página, uma ferramenta, roda local, deixa você em paz.",
                    intro_who=f'JXXR1, mantenedor independente. Sem empresa, sem rodada de investimento, sem investidores. O Toolhub começou como um side project para resolver uma necessidade pessoal — uma página só que fizesse bem uma ferramenta — e cresceu a partir daí. Pode falar comigo pelo <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="O site é HTML estático hospedado no GitHub Pages. Cada ferramenta roda como JavaScript no seu navegador — sem chamadas a API, sem cálculo no servidor, nenhum dado sai do seu dispositivo a não ser quando explicitamente indicado (por exemplo, a ferramenta YouTube Thumbnail baixa uma imagem da CDN do YouTube; o resto é puramente local).",
                    intro_oss=f'O código-fonte completo está em <a href="{REPO_URL}">{REPO_URL}</a>. Contribuições, relatos de bug e ideias de ferramentas são bem-vindos via GitHub Issues.',
                    intro_no_ai="Os textos de ajuda e as traduções são revisados por pessoas dentro do razoável, não colados de um LLM. Se você ver uma tradução que soa robótica ou errada, abra uma issue — é uma correção fácil e do tipo que melhora o site pra todo mundo.",
                    h_what="O que é o Toolhub",
                    h_why="Por quê",
                    h_who="Quem",
                    h_how="Como funciona",
                    h_oss="Open source",
                    h_no_ai="Nada de lixo gerado por IA",
                ),
            },
            "pl": {
                "title": "O Toolhub",
                "h1": "O Toolhub",
                "description": "Toolhub to mała strona z narzędziami bez trackingu, zbudowana przez jedną osobę. Darmowe narzędzia dla devów, które działają w całości w przeglądarce — bez rejestracji, bez zbierania danych.",
                "body": _about_body(
                    intro_what="Toolhub to zbiór darmowych narzędzi dla devów i codziennego użytku, które działają w całości w twojej przeglądarce. Bez rejestracji, bez konta, bez trackingu, bez przetwarzania po stronie serwera. Wklejasz dane, dostajesz wynik, zamykasz kartę — nic się nie zapisuje ani nie wysyła.",
                    intro_why="Większość stron z narzędziami online to albo parking pages oblepione reklamami, albo przepuszczają twoje dane przez czternaście trackerów stron trzecich, zanim w ogóle coś klikniesz. Toolhub to alternatywa: jedna strona, jedno narzędzie, działa lokalnie, zostawia cię w spokoju.",
                    intro_who=f'JXXR1, niezależny maintainer. Bez firmy, bez rundy finansowania, bez inwestorów. Toolhub zaczął się jako side project, żeby zaspokoić własną potrzebę — jedna strona, która porządnie robi jedno narzędzie — i rozrósł się od tego. Można się dobić przez <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="Strona to statyczny HTML hostowany na GitHub Pages. Każde narzędzie działa jako JavaScript w twojej przeglądarce — bez wywołań API, bez obliczeń po stronie serwera, żadne dane nie opuszczają twojego urządzenia, chyba że jest to wyraźnie zaznaczone (na przykład narzędzie YouTube Thumbnail pobiera obraz z CDN YouTube'a; cała reszta jest czysto lokalna).",
                    intro_oss=f'Cały kod źródłowy jest na <a href="{REPO_URL}">{REPO_URL}</a>. Wkład, zgłoszenia bugów i pomysły na narzędzia są mile widziane przez GitHub Issues.',
                    intro_no_ai="Teksty pomocy i tłumaczenia są w miarę możliwości weryfikowane przez ludzi, nie wklejone z LLM-a. Jeśli widzisz tłumaczenie, które brzmi robotycznie albo źle — otwórz issue. To prosta poprawka i taki wkład, który robi stronę lepszą dla wszystkich.",
                    h_what="Czym jest Toolhub",
                    h_why="Dlaczego",
                    h_who="Kto",
                    h_how="Jak to działa",
                    h_oss="Open source",
                    h_no_ai="Bez AI-owej sieczki",
                ),
            },
            "ja": {
                "title": "Toolhub について",
                "h1": "Toolhub について",
                "description": "Toolhub は一人の開発者が作っている、トラッキングなしの小さなユーティリティサイトです。すべてブラウザ内で動く無料の開発者向けツール — 登録不要、データ収集なし。",
                "body": _about_body(
                    intro_what="Toolhub は、すべてブラウザ内で動作する無料の開発者向け・日常用ユーティリティツール集です。登録不要、アカウント不要、トラッキングなし、サーバー側処理もありません。データを貼り付けて、結果を取得して、タブを閉じる — 何も保存されず、送信もされません。",
                    intro_why="オンラインのユーティリティサイトの多くは広告だらけのパーキングページか、クリックする前にあなたのデータを十数個のサードパーティトラッカーに流しています。Toolhub はその代わりになるものです — 1ページ、1ツール、ローカルで動き、あなたをそっとしておきます。",
                    intro_who=f'JXXR1、独立した個人メンテナーです。会社も、資金調達ラウンドも、投資家もいません。Toolhub は個人的な必要を満たすためのサイドプロジェクトとして始まり — 1つのツールをきちんとこなす1ページのサイトとして — そこから育ってきました。連絡は <a href="{REPO_URL}">GitHub</a> からどうぞ。',
                    intro_how="サイトは GitHub Pages にホストされた静的 HTML です。各ツールはブラウザ内の JavaScript として動作します — API 呼び出しもサーバー側の計算もありません。明示的に注記されている場合を除き、データがあなたの端末を離れることはありません（例えば YouTube Thumbnail ツールは YouTube の CDN から画像を取得しますが、それ以外はすべて純粋にローカルで動作します）。",
                    intro_oss=f'ソースコード全体は <a href="{REPO_URL}">{REPO_URL}</a> にあります。コントリビューション、バグ報告、ツールのアイデアは GitHub Issues からどうぞ。',
                    intro_no_ai="ヘルプ文章や翻訳は、できる範囲で人の手でレビューしています。LLM から貼り付けただけのものではありません。ロボットっぽい、あるいは間違っている翻訳を見つけたら、Issue を開いてください — 簡単に直せますし、こうした貢献がサイトを皆にとって良いものにします。",
                    h_what="Toolhub とは",
                    h_why="なぜ作っているのか",
                    h_who="誰が作っているのか",
                    h_how="仕組み",
                    h_oss="オープンソース",
                    h_no_ai="AI のいい加減な出力は使いません",
                ),
            },
            "nl": {
                "title": "Over Toolhub",
                "h1": "Over Toolhub",
                "description": "Toolhub is een kleine tracking-vrije utility-site, gebouwd door één persoon. Gratis developer tools die volledig in je browser draaien, zonder account en zonder data-verzameling.",
                "body": _about_body(
                    intro_what="Toolhub is een verzameling gratis developer- en alledaagse tools die volledig in je browser draaien. Geen account, geen registratie, geen tracking, geen verwerking op de server. Je plakt je data, krijgt het resultaat, sluit het tabblad — niets wordt opgeslagen of verstuurd.",
                    intro_why="De meeste utility-sites online zijn parking pages volgeplakt met reclame, of duwen je data door veertien third-party trackers nog voor je iets aanklikt. Toolhub is het alternatief: één pagina, één tool, draait lokaal, laat je met rust.",
                    intro_who=f'JXXR1, onafhankelijke maintainer. Geen bedrijf, geen funding round, geen investeerders. Toolhub begon als een side project om een eigen behoefte op te lossen — één pagina die één tool goed deed — en is van daaruit gegroeid. Te bereiken via <a href="{REPO_URL}">GitHub</a>.',
                    intro_how="De site is statische HTML gehost op GitHub Pages. Elke tool draait als JavaScript in je browser — geen API calls, geen server-side compute, geen data verlaat je apparaat tenzij expliciet aangegeven (bijvoorbeeld de YouTube Thumbnail tool haalt een afbeelding op van YouTube's CDN; al het andere is puur lokaal).",
                    intro_oss=f'De volledige source staat op <a href="{REPO_URL}">{REPO_URL}</a>. Bijdragen, bug reports en tool-ideeën zijn welkom via GitHub Issues.',
                    intro_no_ai="Hulpteksten en vertalingen zijn binnen redelijke grenzen door mensen nagekeken, niet uit een LLM geplakt. Zie je een vertaling die robotachtig of fout klinkt, open een issue — het is een snelle fix en het soort bijdrage dat de site voor iedereen beter maakt.",
                    h_what="Wat Toolhub is",
                    h_why="Waarom",
                    h_who="Wie",
                    h_how="Hoe het werkt",
                    h_oss="Open source",
                    h_no_ai="Geen AI-rommel",
                ),
            },
        },
    },

    "contact": {
        "slug": "contact",
        "schema": "ContactPage",
        "i18n": {
            "en": {
                "title": "Contact",
                "h1": "Contact",
                "description": "Reach the Toolhub maintainer via GitHub Issues for bug reports, feature requests and tool ideas, or by email for everything else.",
                "body": f"""
<p>Toolhub is a one-person side project. Best-effort response times, not commercial. There is no contact form — this site has no backend, by design.</p>

<h2>GitHub Issues</h2>
<p>For bug reports, feature requests, translation fixes, and new tool ideas, please open an issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues is preferred because it gives the discussion a permanent URL other people with the same question can find later.</p>

<h2>Email</h2>
<p>For things that don't fit GitHub Issues — press, partnership, security disclosure, takedown requests — email <code>{CONTACT_EMAIL}</code>.</p>

<h2>Response times</h2>
<p>I aim to read everything within a week, but Toolhub is built and maintained in spare time alongside a day job. If something is urgent (e.g. security), say so in the subject line.</p>
""".strip(),
            },
            "de": {
                "title": "Kontakt",
                "h1": "Kontakt",
                "description": "Den Toolhub-Maintainer erreichst du über GitHub Issues für Bug-Reports, Feature-Wünsche und Tool-Ideen, oder per E-Mail für alles andere.",
                "body": f"""
<p>Toolhub ist ein Ein-Personen-Nebenprojekt. Best-Effort-Antwortzeiten, nichts Kommerzielles. Es gibt kein Kontaktformular — die Seite hat bewusst kein Backend.</p>

<h2>GitHub Issues</h2>
<p>Für Bug-Reports, Feature-Wünsche, Übersetzungs-Korrekturen und Ideen für neue Tools öffne bitte ein Issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues sind bevorzugt, weil sie der Diskussion eine permanente URL geben, die andere Leute mit derselben Frage später finden können.</p>

<h2>E-Mail</h2>
<p>Für Themen, die nicht in GitHub Issues passen — Presse, Kooperationen, Security-Disclosure, Takedown-Anfragen — schreibe an <code>{CONTACT_EMAIL}</code>.</p>

<h2>Antwortzeiten</h2>
<p>Ich versuche, alles innerhalb einer Woche zu lesen, aber Toolhub wird in der Freizeit neben einem Brotjob gebaut und gewartet. Wenn etwas dringend ist (z. B. Security), schreibe das in den Betreff.</p>
""".strip(),
            },
            "es": {
                "title": "Contacto",
                "h1": "Contacto",
                "description": "Contacta con el mantenedor de Toolhub vía GitHub Issues para reportes de bugs, peticiones de funcionalidades e ideas de herramientas, o por email para todo lo demás.",
                "body": f"""
<p>Toolhub es un proyecto paralelo de una sola persona. Tiempos de respuesta best-effort, no comerciales. No hay formulario de contacto — este sitio no tiene backend, por diseño.</p>

<h2>GitHub Issues</h2>
<p>Para reportes de bugs, peticiones de funcionalidades, correcciones de traducción e ideas de nuevas herramientas, por favor abre una issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues es la vía preferida porque le da a la discusión una URL permanente que otras personas con la misma pregunta pueden encontrar después.</p>

<h2>Email</h2>
<p>Para cosas que no encajan en GitHub Issues — prensa, partnerships, divulgación de seguridad, peticiones de retirada — escribe a <code>{CONTACT_EMAIL}</code>.</p>

<h2>Tiempos de respuesta</h2>
<p>Intento leer todo en una semana, pero Toolhub se construye y mantiene en tiempo libre, además de un trabajo principal. Si algo es urgente (por ejemplo, seguridad), indícalo en el asunto.</p>
""".strip(),
            },
            "fr": {
                "title": "Contact",
                "h1": "Contact",
                "description": "Contacte le mainteneur de Toolhub via GitHub Issues pour les bugs, demandes de fonctionnalités et idées d'outils, ou par email pour le reste.",
                "body": f"""
<p>Toolhub est un side project d'une seule personne. Délais de réponse en best-effort, rien de commercial. Il n'y a pas de formulaire de contact — ce site n'a pas de backend, c'est voulu.</p>

<h2>GitHub Issues</h2>
<p>Pour les rapports de bugs, demandes de fonctionnalités, corrections de traduction et idées de nouveaux outils, ouvre une issue :</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues est préféré parce que ça donne à la discussion une URL permanente que d'autres personnes avec la même question pourront retrouver plus tard.</p>

<h2>Email</h2>
<p>Pour les choses qui ne rentrent pas dans GitHub Issues — presse, partenariats, divulgation de sécurité, demandes de retrait — écris à <code>{CONTACT_EMAIL}</code>.</p>

<h2>Délais de réponse</h2>
<p>J'essaie de tout lire dans la semaine, mais Toolhub est construit et maintenu sur du temps libre, à côté d'un boulot principal. Si quelque chose est urgent (par exemple sécurité), mentionne-le dans le sujet.</p>
""".strip(),
            },
            "it": {
                "title": "Contatti",
                "h1": "Contatti",
                "description": "Contatta il maintainer di Toolhub via GitHub Issues per segnalazioni di bug, richieste di funzionalità e idee per strumenti, o via email per tutto il resto.",
                "body": f"""
<p>Toolhub è un side project di una sola persona. Tempi di risposta best-effort, non commerciali. Non c'è un form di contatto — il sito non ha backend, di proposito.</p>

<h2>GitHub Issues</h2>
<p>Per segnalazioni di bug, richieste di funzionalità, correzioni di traduzione e idee per nuovi strumenti, apri una issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues è preferito perché dà alla discussione un URL permanente che altre persone con la stessa domanda potranno trovare in futuro.</p>

<h2>Email</h2>
<p>Per cose che non rientrano in GitHub Issues — stampa, partnership, segnalazioni di sicurezza, richieste di rimozione — scrivi a <code>{CONTACT_EMAIL}</code>.</p>

<h2>Tempi di risposta</h2>
<p>Cerco di leggere tutto entro una settimana, ma Toolhub viene costruito e mantenuto nel tempo libero, oltre a un lavoro principale. Se qualcosa è urgente (es. sicurezza), scrivilo nell'oggetto.</p>
""".strip(),
            },
            "pt": {
                "title": "Contato",
                "h1": "Contato",
                "description": "Fala com o mantenedor do Toolhub via GitHub Issues para bugs, pedidos de funcionalidade e ideias de ferramentas, ou por e-mail pro resto.",
                "body": f"""
<p>Toolhub é um side project de uma pessoa só. Tempos de resposta best-effort, não comerciais. Não tem formulário de contato — o site não tem backend, de propósito.</p>

<h2>GitHub Issues</h2>
<p>Para relatos de bug, pedidos de funcionalidade, correções de tradução e ideias de novas ferramentas, abra uma issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>O GitHub Issues é preferido porque dá pra discussão uma URL permanente que outras pessoas com a mesma dúvida vão poder achar depois.</p>

<h2>E-mail</h2>
<p>Pra coisas que não cabem em GitHub Issues — imprensa, parceria, disclosure de segurança, pedidos de takedown — mande um e-mail pra <code>{CONTACT_EMAIL}</code>.</p>

<h2>Tempos de resposta</h2>
<p>Eu tento ler tudo dentro de uma semana, mas o Toolhub é construído e mantido no tempo livre, junto com um trabalho principal. Se for urgente (ex.: segurança), coloca isso no assunto.</p>
""".strip(),
            },
            "pl": {
                "title": "Kontakt",
                "h1": "Kontakt",
                "description": "Skontaktuj się z maintainerem Toolhub przez GitHub Issues w sprawie bugów, propozycji funkcji i pomysłów na narzędzia, albo mailem do reszty spraw.",
                "body": f"""
<p>Toolhub to jednoosobowy side project. Czasy odpowiedzi best-effort, nie komercyjne. Nie ma formularza kontaktowego — strona z założenia nie ma backendu.</p>

<h2>GitHub Issues</h2>
<p>W sprawie zgłoszeń bugów, propozycji funkcji, poprawek tłumaczeń i pomysłów na nowe narzędzia — otwórz issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues są preferowane, bo dają dyskusji stały URL, który inni ludzie z tym samym pytaniem znajdą później.</p>

<h2>Mail</h2>
<p>W sprawach, które nie pasują do GitHub Issues — prasa, współpraca, zgłoszenia bezpieczeństwa, takedown — pisz na <code>{CONTACT_EMAIL}</code>.</p>

<h2>Czasy odpowiedzi</h2>
<p>Staram się czytać wszystko w ciągu tygodnia, ale Toolhub jest budowany i utrzymywany po godzinach, obok głównej pracy. Jeśli coś jest pilne (np. bezpieczeństwo), napisz to w temacie.</p>
""".strip(),
            },
            "ja": {
                "title": "お問い合わせ",
                "h1": "お問い合わせ",
                "description": "バグ報告・機能リクエスト・新ツールのアイデアは GitHub Issues、それ以外はメールで Toolhub のメンテナーへご連絡ください。",
                "body": f"""
<p>Toolhub は個人で運営するサイドプロジェクトです。返信はベストエフォートで、商用サポートではありません。お問い合わせフォームは用意していません — このサイトはあえてバックエンドを持たない設計です。</p>

<h2>GitHub Issues</h2>
<p>バグ報告、機能リクエスト、翻訳の修正、新しいツールのアイデアは Issue を立ててください：</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues を優先しているのは、同じ疑問を持つ他の方が後から見つけられる、恒久的な URL がやりとりに残るためです。</p>

<h2>メール</h2>
<p>GitHub Issues に向かない用件 — プレス、提携、セキュリティ脆弱性の通報、削除要請など — は <code>{CONTACT_EMAIL}</code> 宛にメールしてください。</p>

<h2>返信までの時間</h2>
<p>すべてに 1 週間以内に目を通すよう心がけていますが、Toolhub は本業の傍ら、空き時間で開発・運用しています。急ぎの場合（セキュリティなど）は、件名にその旨をご記入ください。</p>
""".strip(),
            },
            "nl": {
                "title": "Contact",
                "h1": "Contact",
                "description": "Bereik de Toolhub-maintainer via GitHub Issues voor bug reports, feature requests en tool-ideeën, of per e-mail voor de rest.",
                "body": f"""
<p>Toolhub is een eenmans-side project. Best-effort responsetijden, niet commercieel. Er is geen contactformulier — deze site heeft bewust geen backend.</p>

<h2>GitHub Issues</h2>
<p>Voor bug reports, feature requests, vertaalcorrecties en ideeën voor nieuwe tools — open een issue:</p>
<p><a href="{REPO_ISSUES}">{REPO_ISSUES}</a></p>
<p>GitHub Issues heeft de voorkeur omdat het de discussie een permanente URL geeft die andere mensen met dezelfde vraag later kunnen vinden.</p>

<h2>E-mail</h2>
<p>Voor zaken die niet bij GitHub Issues passen — pers, samenwerking, security disclosure, takedown-verzoeken — mail naar <code>{CONTACT_EMAIL}</code>.</p>

<h2>Responsetijden</h2>
<p>Ik probeer alles binnen een week te lezen, maar Toolhub wordt in vrije tijd naast een dagbaan gebouwd en onderhouden. Als iets urgent is (bijvoorbeeld security), zet dat dan in de subject line.</p>
""".strip(),
            },
        },
    },

    "for-schools": {
        "slug": "for-schools",
        "schema": "WebPage",
        "i18n": {
            "en": {
                "title": "Toolhub for Schools",
                "h1": "Toolhub for Schools",
                "description": "Privacy-first developer and utility tools for classrooms. No signup, no tracking, multilingual, self-hostable. Filter-friendly and safe to share with students.",
                "body": f"""
<h2>Toolhub for classrooms</h2>
<p>Toolhub is a set of small in-browser tools that students can use without creating an account, without being tracked, and without being redirected to ads or affiliate funnels. Every tool runs entirely in the browser, which means student input never leaves the school network — there is no backend to call.</p>
<p>If you teach in a primary, secondary or tertiary setting and need a quick utility (a regex tester, a colour converter, a Base64 encoder, a password generator for a security lesson), Toolhub is built to be safe to put on the projector and safe to send to a class.</p>

<h2>Curriculum tie-ins</h2>
<ul>
<li><strong>Computer science:</strong> the <a href="/regex-tester/">regex tester</a> for pattern matching, the <a href="/base64-encoder/">Base64 encoder</a> for data lessons, the <a href="/hash-generator/">hash generator</a> for talking about integrity, the <a href="/cidr-calculator/">CIDR calculator</a> for networking units.</li>
<li><strong>Design and digital media:</strong> the <a href="/color-converter/">colour converter</a> and <a href="/color-picker/">colour picker</a> for talking about colour models, the <a href="/wcag-contrast/">WCAG contrast checker</a> for accessibility.</li>
<li><strong>Security awareness:</strong> the <a href="/password-generator/">password generator</a> for talking about entropy and password strength, the <a href="/jwt-decoder/">JWT decoder</a> for showing what's actually inside a token.</li>
<li><strong>Maths and health:</strong> the <a href="/percentage-calculator/">percentage calculator</a>, <a href="/unit-converter/">unit converter</a>, and <a href="/bmi-calculator/">BMI calculator</a> (the BMI page carries its own "not medical advice" notice).</li>
</ul>

<h2>Languages supported</h2>
<p>Every tool is translated into nine languages so students can work in their first language:</p>
<ul>
<li>English</li>
<li>Deutsch (German)</li>
<li>Español (Spanish)</li>
<li>Français (French)</li>
<li>Italiano (Italian)</li>
<li>Português (Portuguese)</li>
<li>Polski (Polish)</li>
<li>日本語 (Japanese)</li>
<li>Nederlands (Dutch)</li>
</ul>

<h2>Self-hosted option</h2>
<p>If your school network blocks external sites or you'd rather have full control, the entire site is around 5 MB and works offline as a Progressive Web App. You can mirror it on a school intranet — it's a static folder of HTML, CSS and JavaScript with no build step required to serve, just put the files behind any web server.</p>
<p>The full source is at <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Filter-friendly</h2>
<p>Toolhub is designed to play nicely with school web filters:</p>
<ul>
<li>No embedded social media widgets.</li>
<li>No chat widgets or live-chat overlays.</li>
<li>No auto-redirects to other sites.</li>
<li>No video or audio that auto-plays.</li>
<li>SafeSearch-friendly content — no adult tools, no gambling, no crypto-bro affiliate placements.</li>
</ul>

<h2>Contact for educators</h2>
<p>If you're using Toolhub in a classroom and want to tell me about it, suggest a tool for your subject, or contribute a translation for a language we don't yet cover well, please get in touch via <a href="/contact/">the contact page</a>. Bulk-translation contributions from native speakers — especially for less-served languages — are very welcome.</p>
""".strip(),
            },
            "de": {
                "title": "Toolhub für Schulen",
                "h1": "Toolhub für Schulen",
                "description": "Datenschutzfreundliche Entwickler- und Utility-Tools für den Unterricht. Ohne Anmeldung, ohne Tracking, mehrsprachig, selbst hostbar. Filter-freundlich und sicher zum Teilen mit Schülern.",
                "body": f"""
<h2>Toolhub im Klassenzimmer</h2>
<p>Toolhub ist eine Sammlung kleiner Browser-Tools, die Schülerinnen und Schüler nutzen können, ohne ein Konto anzulegen, ohne getrackt zu werden und ohne auf Werbung oder Affiliate-Trichter umgeleitet zu werden. Jedes Tool läuft komplett im Browser, was heißt: Schüler-Eingaben verlassen das Schulnetz nie — es gibt kein Backend, das aufgerufen würde.</p>
<p>Wenn Sie in einer Grund-, Sekundar- oder Hochschule unterrichten und schnell ein Utility brauchen (einen Regex-Tester, einen Farbkonverter, einen Base64-Encoder, einen Passwortgenerator für eine Security-Stunde), ist Toolhub so gebaut, dass es sicher auf den Beamer kann und sicher an eine Klasse weitergegeben werden kann.</p>

<h2>Anknüpfung an den Lehrplan</h2>
<ul>
<li><strong>Informatik:</strong> der <a href="/regex-tester/">Regex-Tester</a> für Pattern Matching, der <a href="/base64-encoder/">Base64-Encoder</a> für Datenlektionen, der <a href="/hash-generator/">Hash-Generator</a> als Aufhänger zum Thema Integrität, der <a href="/cidr-calculator/">CIDR-Rechner</a> für Netzwerk-Einheiten.</li>
<li><strong>Gestaltung und digitale Medien:</strong> der <a href="/color-converter/">Farbkonverter</a> und der <a href="/color-picker/">Farbwähler</a> für Farbmodelle, der <a href="/wcag-contrast/">WCAG-Kontrast-Checker</a> für Barrierefreiheit.</li>
<li><strong>Security-Awareness:</strong> der <a href="/password-generator/">Passwortgenerator</a> zur Erklärung von Entropie und Passwortstärke, der <a href="/jwt-decoder/">JWT-Decoder</a>, um zu zeigen, was wirklich in einem Token steht.</li>
<li><strong>Mathe und Gesundheit:</strong> der <a href="/percentage-calculator/">Prozentrechner</a>, <a href="/unit-converter/">Einheitenkonverter</a> und <a href="/bmi-calculator/">BMI-Rechner</a> (die BMI-Seite trägt ihren eigenen Hinweis „keine medizinische Beratung").</li>
</ul>

<h2>Unterstützte Sprachen</h2>
<p>Jedes Tool ist in neun Sprachen übersetzt, damit Schülerinnen und Schüler in ihrer Erstsprache arbeiten können:</p>
<ul>
<li>English</li>
<li>Deutsch</li>
<li>Español (Spanisch)</li>
<li>Français (Französisch)</li>
<li>Italiano (Italienisch)</li>
<li>Português (Portugiesisch)</li>
<li>Polski (Polnisch)</li>
<li>日本語 (Japanisch)</li>
<li>Nederlands (Niederländisch)</li>
</ul>

<h2>Self-Hosting-Option</h2>
<p>Wenn Ihr Schulnetzwerk externe Seiten blockiert oder Sie volle Kontrolle haben möchten: Die ganze Seite ist etwa 5 MB groß und funktioniert offline als Progressive Web App. Sie können sie in einem Schul-Intranet spiegeln — es ist ein statischer Ordner aus HTML, CSS und JavaScript, ohne Build-Schritt zum Ausliefern. Einfach die Dateien hinter einen beliebigen Webserver legen.</p>
<p>Der komplette Quellcode liegt auf <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Filter-freundlich</h2>
<p>Toolhub ist so gebaut, dass es gut mit Schul-Webfiltern zusammenarbeitet:</p>
<ul>
<li>Keine eingebetteten Social-Media-Widgets.</li>
<li>Keine Chat-Widgets oder Live-Chat-Overlays.</li>
<li>Keine automatischen Weiterleitungen auf andere Seiten.</li>
<li>Kein Video oder Audio, das von selbst startet.</li>
<li>SafeSearch-freundliche Inhalte — keine Adult-Tools, kein Glücksspiel, keine Krypto-Affiliate-Platzierungen.</li>
</ul>

<h2>Kontakt für Lehrkräfte</h2>
<p>Wenn Sie Toolhub im Unterricht einsetzen und davon erzählen, ein Tool für Ihr Fach vorschlagen oder eine Übersetzung für eine bisher schlecht abgedeckte Sprache beisteuern möchten, melden Sie sich über die <a href="/contact/">Kontaktseite</a>. Größere Übersetzungs-Beiträge von Muttersprachlern — besonders für weniger versorgte Sprachen — sind ausdrücklich willkommen.</p>
""".strip(),
            },
            "es": {
                "title": "Toolhub para escuelas",
                "h1": "Toolhub para escuelas",
                "description": "Herramientas para desarrolladores y utilidades, centradas en la privacidad, pensadas para el aula. Sin registro, sin tracking, multilingüe y autoalojable. Compatible con filtros web y seguro para compartir con estudiantes.",
                "body": f"""
<h2>Toolhub en el aula</h2>
<p>Toolhub es un conjunto de pequeñas herramientas que funcionan en el navegador y que los estudiantes pueden usar sin crear una cuenta, sin ser rastreados y sin que se les redirija a anuncios o embudos de afiliados. Cada herramienta corre enteramente en el navegador, lo que significa que lo que el estudiante escribe nunca sale de la red del centro — no hay backend al que llamar.</p>
<p>Si imparte clases en primaria, secundaria o universidad y necesita una utilidad rápida (un probador de regex, un convertidor de color, un codificador Base64, un generador de contraseñas para una clase de seguridad), Toolhub está pensado para ser seguro de proyectar y seguro de compartir con un grupo.</p>

<h2>Conexión con el currículo</h2>
<ul>
<li><strong>Informática:</strong> el <a href="/regex-tester/">probador de regex</a> para coincidencia de patrones, el <a href="/base64-encoder/">codificador Base64</a> para clases sobre datos, el <a href="/hash-generator/">generador de hash</a> para hablar de integridad, la <a href="/cidr-calculator/">calculadora CIDR</a> para temas de redes.</li>
<li><strong>Diseño y medios digitales:</strong> el <a href="/color-converter/">convertidor de color</a> y el <a href="/color-picker/">selector de color</a> para hablar de modelos de color, el <a href="/wcag-contrast/">comprobador de contraste WCAG</a> para accesibilidad.</li>
<li><strong>Concienciación en seguridad:</strong> el <a href="/password-generator/">generador de contraseñas</a> para hablar de entropía y robustez de contraseñas, el <a href="/jwt-decoder/">decodificador JWT</a> para enseñar qué hay realmente dentro de un token.</li>
<li><strong>Matemáticas y salud:</strong> la <a href="/percentage-calculator/">calculadora de porcentajes</a>, el <a href="/unit-converter/">convertidor de unidades</a> y la <a href="/bmi-calculator/">calculadora de IMC</a> (la página de IMC lleva su propio aviso de "no es consejo médico").</li>
</ul>

<h2>Idiomas disponibles</h2>
<p>Cada herramienta está traducida a nueve idiomas para que los estudiantes puedan trabajar en su lengua materna:</p>
<ul>
<li>English (inglés)</li>
<li>Deutsch (alemán)</li>
<li>Español</li>
<li>Français (francés)</li>
<li>Italiano</li>
<li>Português</li>
<li>Polski (polaco)</li>
<li>日本語 (japonés)</li>
<li>Nederlands (neerlandés)</li>
</ul>

<h2>Opción de alojamiento propio</h2>
<p>Si la red del centro bloquea sitios externos o si prefiere tener control total, el sitio entero pesa unos 5 MB y funciona sin conexión como Progressive Web App. Puede replicarlo en una intranet escolar — es una carpeta estática de HTML, CSS y JavaScript sin paso de build para servir; basta con poner los ficheros detrás de cualquier servidor web.</p>
<p>El código fuente completo está en <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Compatible con filtros web</h2>
<p>Toolhub está diseñado para llevarse bien con los filtros web escolares:</p>
<ul>
<li>Sin widgets de redes sociales incrustados.</li>
<li>Sin widgets de chat ni overlays de chat en vivo.</li>
<li>Sin redirecciones automáticas a otros sitios.</li>
<li>Sin vídeo o audio que se reproduzca solo.</li>
<li>Contenido compatible con SafeSearch — sin herramientas para adultos, sin apuestas, sin colocaciones de afiliados cripto.</li>
</ul>

<h2>Contacto para educadores</h2>
<p>Si usa Toolhub en el aula y quiere contármelo, sugerir una herramienta para su asignatura o aportar una traducción para un idioma que aún cubrimos mal, contacte a través de la <a href="/contact/">página de contacto</a>. Las contribuciones de traducción de hablantes nativos — sobre todo para idiomas menos cubiertos — son muy bienvenidas.</p>
""".strip(),
            },
            "fr": {
                "title": "Toolhub pour les écoles",
                "h1": "Toolhub pour les écoles",
                "description": "Outils dev et utilitaires axés sur la confidentialité pour la classe. Sans inscription, sans tracking, multilingue, auto-hébergeable. Compatible avec les filtres et sûr à partager avec des élèves.",
                "body": f"""
<h2>Toolhub en classe</h2>
<p>Toolhub est un ensemble de petits outils dans le navigateur que les élèves peuvent utiliser sans créer de compte, sans être pistés, et sans être redirigés vers des pubs ou des tunnels d'affiliation. Chaque outil tourne entièrement dans le navigateur, ce qui veut dire que ce que tape un élève ne sort jamais du réseau de l'établissement — il n'y a pas de backend à appeler.</p>
<p>Si vous enseignez en primaire, secondaire ou supérieur et qu'il vous faut un utilitaire rapide (un testeur de regex, un convertisseur de couleur, un encodeur Base64, un générateur de mots de passe pour une séance de sécurité), Toolhub est conçu pour être sans risque à projeter et sans risque à partager avec une classe.</p>

<h2>Liens avec le programme</h2>
<ul>
<li><strong>Informatique :</strong> le <a href="/regex-tester/">testeur de regex</a> pour la correspondance de motifs, l'<a href="/base64-encoder/">encodeur Base64</a> pour les cours sur les données, le <a href="/hash-generator/">générateur de hash</a> pour parler d'intégrité, la <a href="/cidr-calculator/">calculatrice CIDR</a> pour les unités réseau.</li>
<li><strong>Design et médias numériques :</strong> le <a href="/color-converter/">convertisseur de couleurs</a> et le <a href="/color-picker/">sélecteur de couleurs</a> pour parler des modèles de couleur, le <a href="/wcag-contrast/">vérificateur de contraste WCAG</a> pour l'accessibilité.</li>
<li><strong>Sensibilisation à la sécurité :</strong> le <a href="/password-generator/">générateur de mots de passe</a> pour parler d'entropie et de robustesse, le <a href="/jwt-decoder/">décodeur JWT</a> pour montrer ce qu'il y a vraiment dans un token.</li>
<li><strong>Maths et santé :</strong> la <a href="/percentage-calculator/">calculatrice de pourcentage</a>, le <a href="/unit-converter/">convertisseur d'unités</a> et la <a href="/bmi-calculator/">calculatrice d'IMC</a> (la page IMC porte son propre avertissement « pas un conseil médical »).</li>
</ul>

<h2>Langues supportées</h2>
<p>Chaque outil est traduit dans neuf langues, pour que les élèves puissent travailler dans leur première langue :</p>
<ul>
<li>English (anglais)</li>
<li>Deutsch (allemand)</li>
<li>Español (espagnol)</li>
<li>Français</li>
<li>Italiano (italien)</li>
<li>Português (portugais)</li>
<li>Polski (polonais)</li>
<li>日本語 (japonais)</li>
<li>Nederlands (néerlandais)</li>
</ul>

<h2>Auto-hébergement</h2>
<p>Si le réseau de l'école bloque les sites externes ou si vous voulez tout contrôler, le site entier fait environ 5 Mo et fonctionne hors-ligne en tant que Progressive Web App. Vous pouvez le mirroir sur un intranet scolaire — c'est un dossier statique de HTML, CSS et JavaScript, sans étape de build pour le servir : il suffit de poser les fichiers derrière n'importe quel serveur web.</p>
<p>Le code source complet est sur <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Compatible avec les filtres</h2>
<p>Toolhub est pensé pour bien s'entendre avec les filtres web scolaires :</p>
<ul>
<li>Pas de widgets de réseaux sociaux intégrés.</li>
<li>Pas de widget de chat ni d'overlay de chat en direct.</li>
<li>Pas de redirections automatiques vers d'autres sites.</li>
<li>Pas de vidéo ou d'audio qui se lance tout seul.</li>
<li>Contenu compatible SafeSearch — pas d'outils pour adultes, pas de paris, pas de placements d'affiliation crypto.</li>
</ul>

<h2>Contact enseignants</h2>
<p>Si vous utilisez Toolhub en classe et voulez m'en parler, suggérer un outil pour votre matière, ou contribuer à une traduction dans une langue encore mal couverte, passez par la <a href="/contact/">page de contact</a>. Les contributions de traduction de locuteurs natifs — surtout pour les langues les moins couvertes — sont très bienvenues.</p>
""".strip(),
            },
            "it": {
                "title": "Toolhub per le scuole",
                "h1": "Toolhub per le scuole",
                "description": "Strumenti per sviluppatori e utility orientati alla privacy per la classe. Senza registrazione, senza tracking, multilingua, self-hostabili. Compatibili con i filtri web e sicuri da condividere con gli studenti.",
                "body": f"""
<h2>Toolhub in classe</h2>
<p>Toolhub è una raccolta di piccoli strumenti che girano in browser e che gli studenti possono usare senza creare un account, senza essere tracciati e senza essere reindirizzati a pubblicità o funnel di affiliazione. Ogni strumento gira interamente nel browser, il che significa che ciò che lo studente scrive non lascia mai la rete della scuola — non c'è alcun backend da chiamare.</p>
<p>Se insegna in una scuola primaria, secondaria o all'università e ha bisogno di un'utility veloce (un tester di regex, un convertitore di colori, un encoder Base64, un generatore di password per una lezione di sicurezza), Toolhub è pensato per essere sicuro da proiettare e sicuro da condividere con la classe.</p>

<h2>Collegamenti con il programma</h2>
<ul>
<li><strong>Informatica:</strong> il <a href="/regex-tester/">tester di regex</a> per il pattern matching, l'<a href="/base64-encoder/">encoder Base64</a> per le lezioni sui dati, il <a href="/hash-generator/">generatore di hash</a> per parlare di integrità, il <a href="/cidr-calculator/">calcolatore CIDR</a> per le unità di reti.</li>
<li><strong>Design e media digitali:</strong> il <a href="/color-converter/">convertitore di colori</a> e il <a href="/color-picker/">selettore di colori</a> per parlare di modelli di colore, il <a href="/wcag-contrast/">verificatore di contrasto WCAG</a> per l'accessibilità.</li>
<li><strong>Consapevolezza sulla sicurezza:</strong> il <a href="/password-generator/">generatore di password</a> per parlare di entropia e forza delle password, il <a href="/jwt-decoder/">decoder JWT</a> per mostrare cosa c'è davvero dentro un token.</li>
<li><strong>Matematica e salute:</strong> il <a href="/percentage-calculator/">calcolatore di percentuali</a>, il <a href="/unit-converter/">convertitore di unità</a> e il <a href="/bmi-calculator/">calcolatore BMI</a> (la pagina BMI ha un proprio avviso "non è un consiglio medico").</li>
</ul>

<h2>Lingue supportate</h2>
<p>Ogni strumento è tradotto in nove lingue, così gli studenti possono lavorare nella loro prima lingua:</p>
<ul>
<li>English (inglese)</li>
<li>Deutsch (tedesco)</li>
<li>Español (spagnolo)</li>
<li>Français (francese)</li>
<li>Italiano</li>
<li>Português (portoghese)</li>
<li>Polski (polacco)</li>
<li>日本語 (giapponese)</li>
<li>Nederlands (olandese)</li>
</ul>

<h2>Opzione self-hosted</h2>
<p>Se la rete della scuola blocca i siti esterni o se preferisce avere il pieno controllo, il sito intero pesa circa 5 MB e funziona offline come Progressive Web App. Può replicarlo su un'intranet scolastica — è una cartella statica di HTML, CSS e JavaScript, senza passi di build per servirlo: basta mettere i file dietro un qualsiasi web server.</p>
<p>Il codice sorgente completo è su <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Compatibile con i filtri</h2>
<p>Toolhub è progettato per andare d'accordo con i filtri web scolastici:</p>
<ul>
<li>Niente widget social embeddati.</li>
<li>Niente widget di chat o overlay di live-chat.</li>
<li>Niente redirect automatici verso altri siti.</li>
<li>Niente video o audio che parte da solo.</li>
<li>Contenuti compatibili con SafeSearch — niente strumenti per adulti, niente gambling, niente piazzamenti di affiliate crypto.</li>
</ul>

<h2>Contatti per chi insegna</h2>
<p>Se usa Toolhub in classe e vuole raccontarmelo, suggerirmi uno strumento per la sua materia o contribuire a una traduzione per una lingua che copriamo ancora male, mi contatti tramite la <a href="/contact/">pagina di contatto</a>. I contributi di traduzione da madrelingua — soprattutto per le lingue meno servite — sono molto graditi.</p>
""".strip(),
            },
            "pt": {
                "title": "Toolhub para escolas",
                "h1": "Toolhub para escolas",
                "description": "Ferramentas para devs e utilitários com foco em privacidade pra sala de aula. Sem cadastro, sem tracking, multilíngue, possível de hospedar localmente. Compatível com filtros e seguro pra compartilhar com alunos.",
                "body": f"""
<h2>Toolhub na sala de aula</h2>
<p>O Toolhub é um conjunto de pequenas ferramentas que rodam no navegador e que os alunos podem usar sem criar conta, sem serem rastreados e sem serem redirecionados pra anúncios ou funis de afiliados. Cada ferramenta roda inteiramente no navegador, ou seja, o que o aluno digita nunca sai da rede da escola — não tem backend pra ser chamado.</p>
<p>Se você dá aula no ensino fundamental, médio ou superior e precisa de um utilitário rápido (um testador de regex, um conversor de cores, um codificador Base64, um gerador de senhas pra uma aula de segurança), o Toolhub é feito pra ser seguro de projetar e seguro de mandar pra turma.</p>

<h2>Ligação com o currículo</h2>
<ul>
<li><strong>Computação:</strong> o <a href="/regex-tester/">testador de regex</a> pra casamento de padrões, o <a href="/base64-encoder/">codificador Base64</a> pra aulas sobre dados, o <a href="/hash-generator/">gerador de hash</a> pra falar de integridade, a <a href="/cidr-calculator/">calculadora CIDR</a> pra módulos de redes.</li>
<li><strong>Design e mídia digital:</strong> o <a href="/color-converter/">conversor de cores</a> e o <a href="/color-picker/">seletor de cores</a> pra falar de modelos de cor, o <a href="/wcag-contrast/">verificador de contraste WCAG</a> pra acessibilidade.</li>
<li><strong>Consciência em segurança:</strong> o <a href="/password-generator/">gerador de senhas</a> pra falar de entropia e força de senha, o <a href="/jwt-decoder/">decodificador JWT</a> pra mostrar o que realmente tem dentro de um token.</li>
<li><strong>Matemática e saúde:</strong> a <a href="/percentage-calculator/">calculadora de porcentagem</a>, o <a href="/unit-converter/">conversor de unidades</a> e a <a href="/bmi-calculator/">calculadora de IMC</a> (a página de IMC tem o próprio aviso de "não é orientação médica").</li>
</ul>

<h2>Idiomas suportados</h2>
<p>Cada ferramenta está traduzida pra nove idiomas, pra que os alunos possam trabalhar na própria língua:</p>
<ul>
<li>English (inglês)</li>
<li>Deutsch (alemão)</li>
<li>Español (espanhol)</li>
<li>Français (francês)</li>
<li>Italiano</li>
<li>Português</li>
<li>Polski (polonês)</li>
<li>日本語 (japonês)</li>
<li>Nederlands (holandês)</li>
</ul>

<h2>Opção self-hosted</h2>
<p>Se a rede da escola bloqueia sites externos ou se você prefere ter controle total, o site inteiro tem cerca de 5 MB e funciona offline como Progressive Web App. Você pode espelhar isso numa intranet escolar — é uma pasta estática de HTML, CSS e JavaScript, sem build step pra servir: basta colocar os arquivos atrás de qualquer servidor web.</p>
<p>O código-fonte completo está em <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Compatível com filtros</h2>
<p>O Toolhub é desenhado pra se dar bem com filtros web de escola:</p>
<ul>
<li>Sem widgets de redes sociais embutidos.</li>
<li>Sem widgets de chat ou overlays de chat ao vivo.</li>
<li>Sem redirecionamentos automáticos pra outros sites.</li>
<li>Sem vídeo ou áudio que toca sozinho.</li>
<li>Conteúdo compatível com SafeSearch — sem ferramentas adultas, sem apostas, sem colocações de afiliado de cripto.</li>
</ul>

<h2>Contato pra educadores</h2>
<p>Se você usa o Toolhub em sala de aula e quer me contar, sugerir uma ferramenta pra sua matéria ou contribuir com uma tradução pra algum idioma que ainda cobrimos mal, fala comigo pela <a href="/contact/">página de contato</a>. Contribuições de tradução de falantes nativos — principalmente pra idiomas menos cobertos — são muito bem-vindas.</p>
""".strip(),
            },
            "pl": {
                "title": "Toolhub dla szkół",
                "h1": "Toolhub dla szkół",
                "description": "Narzędzia dla devów i utility z naciskiem na prywatność, do pracy w klasie. Bez rejestracji, bez trackingu, wielojęzyczne, możliwe do self-hostingu. Przyjazne dla filtrów i bezpieczne do udostępniania uczniom.",
                "body": f"""
<h2>Toolhub w klasie</h2>
<p>Toolhub to zestaw niewielkich narzędzi działających w przeglądarce, których uczniowie mogą używać bez zakładania konta, bez śledzenia i bez przekierowań na reklamy czy lejki afiliacyjne. Każde narzędzie działa w całości w przeglądarce, czyli to, co uczeń wpisuje, nigdy nie opuszcza sieci szkolnej — nie ma backendu, do którego trzeba by dzwonić.</p>
<p>Jeśli uczysz w szkole podstawowej, średniej albo na uczelni i potrzebujesz szybkiego utility (testera regex, konwertera kolorów, enkodera Base64, generatora haseł na lekcję o bezpieczeństwie), Toolhub jest zbudowany tak, żeby można go było bezpiecznie puścić na projektor i bezpiecznie wysłać do klasy.</p>

<h2>Powiązanie z podstawą programową</h2>
<ul>
<li><strong>Informatyka:</strong> <a href="/regex-tester/">tester regex</a> do dopasowywania wzorców, <a href="/base64-encoder/">enkoder Base64</a> do lekcji o danych, <a href="/hash-generator/">generator hash</a> do rozmów o integralności, <a href="/cidr-calculator/">kalkulator CIDR</a> do modułów sieciowych.</li>
<li><strong>Design i media cyfrowe:</strong> <a href="/color-converter/">konwerter kolorów</a> i <a href="/color-picker/">picker kolorów</a> do rozmów o modelach barwnych, <a href="/wcag-contrast/">checker kontrastu WCAG</a> do dostępności.</li>
<li><strong>Świadomość bezpieczeństwa:</strong> <a href="/password-generator/">generator haseł</a> do tematu entropii i siły hasła, <a href="/jwt-decoder/">dekoder JWT</a>, żeby pokazać, co naprawdę jest w tokenie.</li>
<li><strong>Matematyka i zdrowie:</strong> <a href="/percentage-calculator/">kalkulator procentów</a>, <a href="/unit-converter/">konwerter jednostek</a> i <a href="/bmi-calculator/">kalkulator BMI</a> (strona BMI ma własne ostrzeżenie „to nie jest porada medyczna").</li>
</ul>

<h2>Wspierane języki</h2>
<p>Każde narzędzie jest przetłumaczone na dziewięć języków, żeby uczniowie mogli pracować w swoim pierwszym języku:</p>
<ul>
<li>English (angielski)</li>
<li>Deutsch (niemiecki)</li>
<li>Español (hiszpański)</li>
<li>Français (francuski)</li>
<li>Italiano (włoski)</li>
<li>Português (portugalski)</li>
<li>Polski</li>
<li>日本語 (japoński)</li>
<li>Nederlands (niderlandzki)</li>
</ul>

<h2>Opcja self-hostingu</h2>
<p>Jeśli sieć szkolna blokuje strony zewnętrzne albo wolisz mieć pełną kontrolę — cała strona ma około 5 MB i działa offline jako Progressive Web App. Można ją zlustrzyć w intranecie szkoły — to statyczny folder z HTML, CSS i JavaScript, bez build stepu do podania: wystarczy położyć pliki za dowolnym serwerem WWW.</p>
<p>Cały kod źródłowy jest na <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Przyjazne filtrom</h2>
<p>Toolhub jest tak zrobiony, żeby grać dobrze ze szkolnymi filtrami WWW:</p>
<ul>
<li>Brak osadzonych widgetów social media.</li>
<li>Brak widgetów czatu i overlayów live-chatu.</li>
<li>Brak auto-przekierowań na inne strony.</li>
<li>Brak wideo ani audio, które samo się uruchamia.</li>
<li>Treść zgodna z SafeSearch — żadnych narzędzi dla dorosłych, żadnego hazardu, żadnych krypto-afiliacji.</li>
</ul>

<h2>Kontakt dla nauczycieli</h2>
<p>Jeśli używasz Toolhub w klasie i chcesz mi o tym powiedzieć, zaproponować narzędzie do swojego przedmiotu albo dorzucić tłumaczenie do języka, który słabo pokrywamy — skontaktuj się przez <a href="/contact/">stronę kontaktową</a>. Większe wkłady tłumaczeniowe od native speakerów — zwłaszcza do mniej pokrytych języków — są bardzo mile widziane.</p>
""".strip(),
            },
            "ja": {
                "title": "学校向け Toolhub",
                "h1": "学校向け Toolhub",
                "description": "教室向けの、プライバシー重視の開発者ツール／ユーティリティ。登録不要、トラッキングなし、多言語、セルフホスト可。フィルタとの相性がよく、生徒に共有しても安心。",
                "body": f"""
<h2>教室での Toolhub</h2>
<p>Toolhub は、ブラウザ内で動く小さなツールの集まりです。生徒はアカウントを作る必要なく、追跡されることなく、広告やアフィリエイト誘導に飛ばされることもなく利用できます。各ツールは完全にブラウザ内で動作するため、生徒が入力した内容が学校ネットワークから外に出ることはありません — 呼び出すバックエンド自体が存在しないからです。</p>
<p>小学校、中学・高校、大学・専門学校などで授業を担当されている方が、ちょっとしたユーティリティ（正規表現テスター、カラーコンバーター、Base64 エンコーダー、セキュリティの授業用パスワードジェネレーターなど）を必要とする場面で、Toolhub はプロジェクターに映しても安心、クラスに共有しても安心、というつくりになっています。</p>

<h2>カリキュラムとのつながり</h2>
<ul>
<li><strong>情報科：</strong>パターンマッチングには <a href="/regex-tester/">正規表現テスター</a>、データの単元には <a href="/base64-encoder/">Base64 エンコーダー</a>、整合性の話には <a href="/hash-generator/">ハッシュ生成ツール</a>、ネットワーク単元には <a href="/cidr-calculator/">CIDR 計算機</a>。</li>
<li><strong>デザイン・デジタルメディア：</strong><a href="/color-converter/">カラーコンバーター</a>と<a href="/color-picker/">カラーピッカー</a>でカラーモデルを、<a href="/wcag-contrast/">WCAG コントラストチェッカー</a>でアクセシビリティを。</li>
<li><strong>セキュリティ教育：</strong>エントロピーやパスワード強度の話には <a href="/password-generator/">パスワードジェネレーター</a>、トークンの中身を見せるには <a href="/jwt-decoder/">JWT デコーダー</a>。</li>
<li><strong>算数・数学・保健：</strong><a href="/percentage-calculator/">パーセンテージ計算機</a>、<a href="/unit-converter/">単位変換ツール</a>、<a href="/bmi-calculator/">BMI 計算機</a>（BMI ページには「医療アドバイスではありません」という注意書きが個別についています）。</li>
</ul>

<h2>対応言語</h2>
<p>各ツールは 9 つの言語に翻訳されているので、生徒が自分の第一言語で作業できます：</p>
<ul>
<li>English（英語）</li>
<li>Deutsch（ドイツ語）</li>
<li>Español（スペイン語）</li>
<li>Français（フランス語）</li>
<li>Italiano（イタリア語）</li>
<li>Português（ポルトガル語）</li>
<li>Polski（ポーランド語）</li>
<li>日本語</li>
<li>Nederlands（オランダ語）</li>
</ul>

<h2>セルフホストという選択肢</h2>
<p>学校のネットワークが外部サイトをブロックしている場合や、すべてを自分の管理下に置きたい場合、サイト全体は約 5 MB で、Progressive Web App としてオフラインでも動作します。校内イントラネットにミラーすることも可能です — HTML、CSS、JavaScript の静的フォルダなので、ビルド手順は不要、ファイルを任意の Web サーバーに置くだけで配信できます。</p>
<p>ソースコード全体は <a href="{REPO_URL}">{REPO_URL}</a> にあります。</p>

<h2>フィルタとの相性</h2>
<p>Toolhub は、学校の Web フィルタとうまく付き合えるように設計されています：</p>
<ul>
<li>SNS ウィジェットの埋め込みなし。</li>
<li>チャットウィジェットやライブチャットのオーバーレイなし。</li>
<li>他サイトへの自動リダイレクトなし。</li>
<li>動画・音声の自動再生なし。</li>
<li>SafeSearch と相性のよい内容 — 成人向けツール、ギャンブル、暗号資産アフィリエイトの掲載はありません。</li>
</ul>

<h2>教育関係の方へのお問い合わせ窓口</h2>
<p>Toolhub を教室で使ってくださっている、教科に合うツールを提案したい、まだ十分にカバーできていない言語の翻訳に協力したい、という方は<a href="/contact/">お問い合わせページ</a>からご連絡ください。ネイティブスピーカーによるまとまった翻訳の協力 — 特にカバーが薄い言語向け — は大歓迎です。</p>
""".strip(),
            },
            "nl": {
                "title": "Toolhub voor scholen",
                "h1": "Toolhub voor scholen",
                "description": "Privacy-first developer- en utility-tools voor in de klas. Geen registratie, geen tracking, meertalig, self-hostable. Filter-vriendelijk en veilig om met leerlingen te delen.",
                "body": f"""
<h2>Toolhub in de klas</h2>
<p>Toolhub is een set kleine in-browser tools die leerlingen kunnen gebruiken zonder een account aan te maken, zonder gevolgd te worden en zonder doorgestuurd te worden naar reclame of affiliate-funnels. Elke tool draait volledig in de browser, wat betekent dat wat een leerling intypt nooit het schoolnetwerk verlaat — er is geen backend om aan te roepen.</p>
<p>Als je lesgeeft in het basis-, voortgezet of hoger onderwijs en je hebt snel een utility nodig (een regex-tester, een colour converter, een Base64-encoder, een wachtwoordgenerator voor een security-les), dan is Toolhub gebouwd om veilig op de beamer te kunnen en veilig naar een klas te kunnen sturen.</p>

<h2>Aansluiting bij het curriculum</h2>
<ul>
<li><strong>Informatica:</strong> de <a href="/regex-tester/">regex tester</a> voor pattern matching, de <a href="/base64-encoder/">Base64 encoder</a> voor lessen over data, de <a href="/hash-generator/">hash generator</a> om over integriteit te praten, de <a href="/cidr-calculator/">CIDR calculator</a> voor netwerk-onderdelen.</li>
<li><strong>Design en digitale media:</strong> de <a href="/color-converter/">colour converter</a> en de <a href="/color-picker/">colour picker</a> om over kleurmodellen te praten, de <a href="/wcag-contrast/">WCAG contrast checker</a> voor toegankelijkheid.</li>
<li><strong>Security-bewustzijn:</strong> de <a href="/password-generator/">wachtwoordgenerator</a> om over entropie en wachtwoordsterkte te praten, de <a href="/jwt-decoder/">JWT decoder</a> om te laten zien wat er echt in een token zit.</li>
<li><strong>Wiskunde en gezondheid:</strong> de <a href="/percentage-calculator/">procentcalculator</a>, <a href="/unit-converter/">eenhedenconverter</a> en <a href="/bmi-calculator/">BMI-calculator</a> (de BMI-pagina heeft een eigen "geen medisch advies"-vermelding).</li>
</ul>

<h2>Ondersteunde talen</h2>
<p>Elke tool is vertaald naar negen talen, zodat leerlingen in hun eerste taal kunnen werken:</p>
<ul>
<li>English (Engels)</li>
<li>Deutsch (Duits)</li>
<li>Español (Spaans)</li>
<li>Français (Frans)</li>
<li>Italiano (Italiaans)</li>
<li>Português (Portugees)</li>
<li>Polski (Pools)</li>
<li>日本語 (Japans)</li>
<li>Nederlands</li>
</ul>

<h2>Self-hosted optie</h2>
<p>Als het schoolnetwerk externe sites blokkeert of als je liever volledige controle hebt, de hele site is ongeveer 5 MB en werkt offline als Progressive Web App. Je kunt hem mirroren op een school-intranet — het is een statische map met HTML, CSS en JavaScript, zonder build step om te serveren: zet de bestanden achter een willekeurige webserver.</p>
<p>De volledige source staat op <a href="{REPO_URL}">{REPO_URL}</a>.</p>

<h2>Filter-vriendelijk</h2>
<p>Toolhub is ontworpen om goed samen te werken met schoolwebfilters:</p>
<ul>
<li>Geen ingebedde social media widgets.</li>
<li>Geen chat widgets of live-chat overlays.</li>
<li>Geen automatische redirects naar andere sites.</li>
<li>Geen video of audio dat vanzelf afspeelt.</li>
<li>SafeSearch-vriendelijke inhoud — geen tools voor volwassenen, geen gokken, geen crypto-affiliate placements.</li>
</ul>

<h2>Contact voor docenten</h2>
<p>Gebruik je Toolhub in een klas en wil je het me laten weten, een tool voorstellen voor je vak, of bijdragen aan een vertaling voor een taal die we nog slecht dekken — neem dan contact op via de <a href="/contact/">contactpagina</a>. Bulk-vertaalbijdragen van native speakers — vooral voor minder bediende talen — zijn van harte welkom.</p>
""".strip(),
            },
        },
    },
}
