#!/usr/bin/env python3
"""Converte la presentazione Markdown in HTML con stile slide."""

from pathlib import Path
from markdown_it import MarkdownIt

REPO = Path(__file__).resolve().parents[1]
SRC = REPO / "docs" / "presentazione_ia_produttiva.md"
DST = REPO / "output" / "presentazione_ia_produttiva.html"

CSS = """\
:root {
  --bg: #0f172a;
  --bg-slide: #1e293b;
  --text: #e2e8f0;
  --accent: #38bdf8;
  --accent2: #818cf8;
  --muted: #94a3b8;
  --border: #334155;
  --highlight: #fbbf24;
  --green: #4ade80;
  --red: #f87171;
  --surface: #283548;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  font-family: 'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
  padding: 2rem 1rem;
}
.container { max-width: 960px; margin: 0 auto; }
.cover {
  text-align: center;
  padding: 4rem 2rem;
  margin-bottom: 2rem;
  background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
  border: 1px solid var(--border);
  border-radius: 16px;
}
.cover h1 {
  font-size: 2.4rem;
  font-weight: 800;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: .5rem;
}
.cover .meta { color: var(--muted); font-size: .95rem; margin-top: 1rem; }
.slide {
  background: var(--bg-slide);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 2.5rem 3rem;
  margin-bottom: 2rem;
  page-break-inside: avoid;
  position: relative;
}
.slide::before {
  content: attr(data-num);
  position: absolute;
  top: 1rem;
  right: 1.5rem;
  font-size: .8rem;
  color: var(--muted);
  font-weight: 600;
}
.section-divider {
  text-align: center;
  padding: 2rem;
  margin: 2.5rem 0;
  font-size: 1rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 700;
  border-top: 2px solid var(--accent);
  border-bottom: 2px solid var(--accent);
}
h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--accent);
  margin-bottom: .25rem;
}
h3 {
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 1.2rem;
}
h4 {
  font-size: 1rem;
  color: var(--accent2);
  margin-bottom: 1rem;
}
p { margin-bottom: .8rem; }
strong { color: #f1f5f9; }
em { color: var(--highlight); font-style: italic; }
ul, ol { margin: .5rem 0 1rem 1.5rem; }
li { margin-bottom: .3rem; }
li strong { color: var(--accent); }
blockquote {
  border-left: 3px solid var(--accent2);
  padding: .8rem 1.2rem;
  margin: 1rem 0;
  background: var(--surface);
  border-radius: 0 8px 8px 0;
  color: var(--muted);
  font-style: italic;
}
blockquote strong { color: var(--text); }
pre {
  background: #0d1117;
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1rem 1.2rem;
  overflow-x: auto;
  margin: 1rem 0;
  font-size: .85rem;
  line-height: 1.5;
}
code {
  font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
  font-size: .85em;
}
p code, li code {
  background: var(--surface);
  padding: .15em .4em;
  border-radius: 4px;
  font-size: .85em;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
  font-size: .9rem;
}
th {
  background: var(--surface);
  color: var(--accent);
  font-weight: 600;
  text-align: left;
  padding: .6rem .8rem;
  border-bottom: 2px solid var(--accent);
}
td {
  padding: .5rem .8rem;
  border-bottom: 1px solid var(--border);
}
tr:hover td { background: rgba(56,189,248,.04); }
.speaker-notes {
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  border: 1px dashed var(--border);
  border-radius: 8px;
  padding: 1rem 1.2rem;
  margin-top: 1.2rem;
  font-size: .85rem;
  color: var(--muted);
  line-height: 1.5;
}
.speaker-notes::before {
  content: 'NOTE SPEAKER';
  display: block;
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .1em;
  color: var(--accent2);
  margin-bottom: .5rem;
}
.key-phrase {
  background: linear-gradient(135deg, rgba(251,191,36,.08), rgba(129,140,248,.08));
  border-left: 3px solid var(--highlight);
  padding: .8rem 1.2rem;
  margin: 1rem 0;
  border-radius: 0 8px 8px 0;
  font-style: italic;
  color: var(--highlight);
  font-size: 1.05rem;
}
hr { display: none; }
.toc {
  background: var(--bg-slide);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 2rem;
}
.toc h2 { margin-bottom: 1rem; }
.toc ol { counter-reset: toc; list-style: none; margin-left: 0; }
.toc li {
  counter-increment: toc;
  padding: .4rem 0;
  border-bottom: 1px solid var(--border);
}
.toc li::before {
  content: counter(toc, decimal-leading-zero);
  color: var(--accent);
  font-weight: 700;
  margin-right: .8rem;
  font-size: .85rem;
}
.toc a { color: var(--text); text-decoration: none; }
.toc a:hover { color: var(--accent); }
@media print {
  body { background: #fff; color: #1a1a1a; padding: 0; }
  .slide { border: 1px solid #ddd; page-break-after: always; }
  .speaker-notes { display: none; }
  pre { background: #f5f5f5; border-color: #ddd; }
  h2 { color: #2563eb; }
  .key-phrase { color: #92400e; border-color: #d97706; }
  .cover h1 { background: none; -webkit-text-fill-color: #2563eb; color: #2563eb; }
}
@media (max-width: 640px) {
  .slide { padding: 1.5rem; }
  .cover h1 { font-size: 1.6rem; }
  h2 { font-size: 1.2rem; }
  table { font-size: .8rem; }
}
"""


def convert(md_text: str) -> str:
    parser = MarkdownIt("commonmark", {"html": True}).enable("table")
    sections = md_text.split("\n---\n")

    slides_html: list[str] = []
    slide_num = 0
    is_first = True

    for section in sections:
        section = section.strip()
        if not section:
            continue

        html_block = parser.render(section)

        # Detect section dividers (all-caps headers like "PILASTRO 1 — ...")
        lines = section.strip().split("\n")
        first_line = lines[0].strip().lstrip("#").strip() if lines else ""
        is_divider = (
            first_line.startswith("PILASTRO")
            or first_line == "CHIUSURA"
            or first_line.startswith("SLIDE BACKUP")
        )

        if is_divider:
            slides_html.append(
                f'<div class="section-divider">{first_line}</div>'
            )
            continue

        # Cover slide
        if is_first:
            is_first = False
            slides_html.append(f'<div class="cover">{html_block}</div>')
            continue

        slide_num += 1

        # Extract and wrap speaker notes
        if "<strong>Note speaker:</strong>" in html_block:
            parts = html_block.split("<strong>Note speaker:</strong>")
            main = parts[0]
            notes_raw = parts[1] if len(parts) > 1 else ""
            # Find the enclosing <p> end and extract text
            notes_text = notes_raw
            # Clean up wrapping <p> tags around notes
            if notes_text.strip().startswith("</p>"):
                notes_text = notes_text.strip()[4:]
            if notes_text.strip().startswith("<p>"):
                notes_text = notes_text.strip()[3:]
            html_block = main + f'<div class="speaker-notes">{notes_text}</div>'

        # Wrap key phrases
        html_block = html_block.replace(
            "<strong>Frase chiave:</strong>", ""
        )
        html_block = html_block.replace(
            "<strong>Frase di chiusura:</strong>", ""
        )

        # Convert italic paragraphs after "Frase chiave" into key-phrase divs
        import re
        html_block = re.sub(
            r'<p>\s*<em>"([^"]*(?:"[^"]*)*)"</em>\s*</p>',
            r'<div class="key-phrase">"\1"</div>',
            html_block,
        )

        slides_html.append(
            f'<div class="slide" data-num="{slide_num:02d}">\n{html_block}\n</div>'
        )

    toc_items = []
    slide_titles = [
        ("Titolo", ""),
        ("Il Problema", "Il 90% usa l'IA come motore di ricerca"),
        ("Collaboratore Creativo", "Non un programma, un collega"),
        ("I Tre Pilastri", "Architettura, Dominio, Strategia"),
        ("Un Tool Non Scala", "La scala della maturita'"),
        ("Sistema Multi-Agente", "24 agenti, 76 skill"),
        ("Skill Come Contratti", "Workflow con garanzie"),
        ("Autonomia Controllata", "Decision gate"),
        ("Stack e Fonti Dati", "Cosa c'e' sotto il cofano"),
        ("Prototipo -> Produzione", "Claude Code prototipa, l'SDK spedisce"),
        ("Il Brillante Incompetente", "Senza dominio, errori critici"),
        ("Il Dominio Si Codifica", "Paper, codice, skill"),
        ("Compliance Come Dominio", "Il porting al framework UE"),
        ("Arricchire il Dominio", "Dallo strumento alla suite"),
        ("Non Serve un Big Bang", "Adozione progressiva"),
        ("L'Uomo nel Loop", "Matrice rischio/reversibilita'"),
        ("Misurare il Valore", "Metriche che contano"),
        ("Recap", "I tre cardini"),
        ("Call to Action", "3 azioni per lunedi'"),
        ("Pipeline Credit Risk", "Backup"),
        ("ROI dell'Approccio", "Backup"),
    ]
    for i, (title, sub) in enumerate(slide_titles, 1):
        desc = f" — {sub}" if sub else ""
        toc_items.append(f"<li>{title}{desc}</li>")

    toc_html = f"""<div class="toc">
<h2>Indice</h2>
<ol>{"".join(toc_items)}</ol>
</div>"""

    return f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>L'IA che Lavora — Architettura, Dominio, Strategia</title>
<style>{CSS}</style>
</head>
<body>
<div class="container">
{toc_html}
{"".join(slides_html)}
</div>
</body>
</html>"""


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    md_text = SRC.read_text(encoding="utf-8")
    html = convert(md_text)
    DST.write_text(html, encoding="utf-8")
    print(f"Presentazione generata: {DST}")
    print(f"Dimensione: {DST.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
