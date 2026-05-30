#!/usr/bin/env python3
"""Libreria di diagrammi SVG per la presentazione 'L'IA che Lavora'.

Ogni funzione restituisce una stringa SVG autosufficiente, disegnata con la
palette del template Qubit On Cloud e font Montserrat (con fallback per il
rendering raster). Gli schemi rimpiazzano gli schizzi ASCII della presentazione.
"""

from __future__ import annotations

# --- Palette Qubit On Cloud -------------------------------------------------
BLUE_DARK = "#003BA3"
BLUE = "#4A8CFF"
BLUE_SOFT = "#9EC2FF"
SURFACE = "#F5F7FA"
SURFACE2 = "#E8EEF7"
INK = "#1A1A2E"
MUTED = "#5A6072"
WHITE = "#FFFFFF"
AMBER = "#F0A500"
GREEN = "#2E9E5B"
RED = "#D64550"
LINE = "#D5DEEC"

FONT = "Montserrat, 'Liberation Sans', 'DejaVu Sans', sans-serif"

W, H = 900, 405  # viewBox standard per le slide-contenuto


# --- Primitive --------------------------------------------------------------
def _esc(s: str) -> str:
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def rrect(x, y, w, h, fill, rx=14, stroke="none", sw=0, opacity=None):
    op = f' opacity="{opacity}"' if opacity is not None else ""
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke != "none" else ""
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
        f'rx="{rx}" ry="{rx}" fill="{fill}"{st}{op}/>'
    )


def circle(cx, cy, r, fill, stroke="none", sw=0):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke != "none" else ""
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}"{st}/>'


def poly(points, fill, stroke="none", sw=0, opacity=None):
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    op = f' opacity="{opacity}"' if opacity is not None else ""
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke != "none" else ""
    return f'<polygon points="{pts}" fill="{fill}"{st}{op}/>'


def ln(x1, y1, x2, y2, stroke=LINE, sw=2, dash=None, cap="round"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}/>'
    )


def txt(x, y, s, size, fill=INK, weight=400, anchor="middle", italic=False,
        spacing=None):
    it = ' font-style="italic"' if italic else ""
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
        f'font-weight="{weight}" text-anchor="{anchor}"{it}{ls}>{_esc(s)}</text>'
    )


def tlines(x, y, lines, size, fill=INK, weight=400, anchor="middle", lh=None):
    lh = lh or size * 1.35
    out = []
    for i, line in enumerate(lines):
        out.append(txt(x, y + i * lh, line, size, fill, weight, anchor))
    return "".join(out)


def arrow(x1, y1, x2, y2, stroke=BLUE, sw=3):
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{stroke}" stroke-width="{sw}" marker-end="url(#ah)" '
        f'stroke-linecap="round"/>'
    )


def chip(cx, cy, w, h, label, size, fill, fg, weight=700, rx=8):
    return (
        rrect(cx - w / 2, cy - h / 2, w, h, fill, rx=rx)
        + txt(cx, cy + size * 0.35, label, size, fg, weight)
    )


def doc(body, w=W, h=H):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
        f'font-family="{FONT}">'
        f'<defs>'
        f'<marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" '
        f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{BLUE}"/></marker>'
        f'<marker id="ahd" viewBox="0 0 10 10" refX="8" refY="5" '
        f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{BLUE_DARK}"/></marker>'
        f'</defs>{body}</svg>'
    )


# --- Diagrammi --------------------------------------------------------------
def pyramid_adozione() -> str:
    """Slide 2 — Piramide dell'adozione IA (4 livelli)."""
    apex = (255, 20)
    bl, br = (70, 360), (440, 360)
    ys = [20, 105, 190, 275, 360]
    bands = [
        ("5%", "Sistema produttivo", BLUE_DARK, WHITE),
        ("10%", "Automazione task", BLUE, WHITE),
        ("25%", "Assistente ad hoc", BLUE_SOFT, INK),
        ("60%", "Chatbot / Q&A", SURFACE2, INK),
    ]

    def hw(y):  # mezza larghezza del triangolo all'altezza y
        return (y - apex[1]) / (br[1] - apex[1]) * (br[0] - bl[0]) / 2

    body = []
    for i, (pct, label, fill, fg) in enumerate(bands):
        yt, yb = ys[i], ys[i + 1]
        cx = apex[0]
        body.append(poly(
            [(cx - hw(yt), yt), (cx + hw(yt), yt),
             (cx + hw(yb), yb), (cx - hw(yb), yb)], fill,
            stroke=WHITE, sw=3))
        ymid = (yt + yb) / 2
        body.append(txt(cx, ymid + 8, pct, 22, fg, 800))
        # connettore + etichetta a destra
        body.append(ln(cx + hw(ymid) + 6, ymid, 520, ymid, LINE, 1.5))
        body.append(circle(cx + hw(ymid) + 6, ymid, 3, fill))
        body.append(txt(534, ymid - 2, label, 17, INK, 700, anchor="start"))
    body.append(txt(534, ys[1] / 2 + 30, "Pochi ci arrivano",
                    13, MUTED, 600, anchor="start", italic=True))
    body.append(txt(534, 352, "Dove si ferma il 60%",
                    13, MUTED, 600, anchor="start", italic=True))
    body.append(txt(255, 392, "Maturità dell'adozione",
                    14, MUTED, 600))
    return doc("".join(body))


def triangle_pilastri() -> str:
    """Slide 4 — Triangolo dei tre pilastri."""
    cx, cy = 450, 210
    top = (450, 72)
    bl = (195, 322)
    br = (705, 322)
    body = []
    # triangolo
    body.append(poly([top, bl, br], "none", stroke=BLUE, sw=3))
    # medaglione centrale
    body.append(circle(cx, cy + 5, 66, BLUE_DARK))
    body.append(txt(cx, cy - 4, "IA", 26, WHITE, 800))
    body.append(txt(cx, cy + 24, "PRODUTTIVA", 14, BLUE_SOFT, 700, spacing="2"))
    # vertici
    verts = [
        (top[0], top[1], "ARCHITETTURA", "Dal prompt al sistema", "below"),
        (bl[0], bl[1], "DOMINIO", "La conoscenza che rende competenti", "left"),
        (br[0], br[1], "STRATEGIA", "Il percorso di adozione", "right"),
    ]
    for vx, vy, label, sub, side in verts:
        body.append(circle(vx, vy, 13, BLUE))
        body.append(circle(vx, vy, 6, WHITE))
        if side == "below":
            body.append(txt(vx, vy - 34, label, 22, BLUE_DARK, 800))
            body.append(txt(vx, vy - 16, sub, 13, MUTED, 600))
        elif side == "left":
            body.append(txt(vx, vy + 32, label, 22, BLUE_DARK, 800, anchor="middle"))
            body.append(txt(vx, vy + 50, sub, 11.5, MUTED, 600, anchor="middle"))
        else:
            body.append(txt(vx, vy + 32, label, 22, BLUE_DARK, 800, anchor="middle"))
            body.append(txt(vx, vy + 50, sub, 11.5, MUTED, 600, anchor="middle"))
    return doc("".join(body))


def staircase_maturita() -> str:
    """Slide 5 — Scala della maturità a 4 gradini."""
    body = []
    steps = [
        ("L1", ["PROMPT", "SINGOLO"], "Risposta generica, non verificabile", SURFACE2, INK),
        ("L2", ["SCRIPT", "+ IA"], "Riproducibile ma rigido", BLUE_SOFT, INK),
        ("L3", ["AGENTE", "SPECIALIZZATO"], "Smette di essere chiamato: decide", BLUE, WHITE),
        ("L4", ["SISTEMA", "MULTI-AGENTE"], "Orchestratore + agenti + workflow", BLUE_DARK, WHITE),
    ]
    cw, chh = 196, 150
    x0 = 40
    # freccia ascendente di sfondo
    body.append('<path d="M44,372 L860,150" stroke="%s" stroke-width="3" '
                'marker-end="url(#ahd)" stroke-linecap="round"/>' % LINE)
    for i, (lv, title_lines, sub, fill, fg) in enumerate(steps):
        x = x0 + i * (cw + 10)
        bottom = 372 - i * 50
        y = bottom - chh
        body.append(rrect(x, y, cw, chh, fill, rx=14))
        body.append(txt(x + 18, y + 38, lv, 24, fg, 800, anchor="start"))
        for k, tl in enumerate(title_lines):
            body.append(txt(x + 18, y + 62 + k * 20, tl, 14, fg, 800, anchor="start"))
        # descrizione: wrap
        words, cur, lines = sub.split(" "), "", []
        for w_ in words:
            if len(cur) + len(w_) > 24:
                lines.append(cur.strip()); cur = w_ + " "
            else:
                cur += w_ + " "
        lines.append(cur.strip())
        oy = y + 62 + len(title_lines) * 20 + 8
        for j, lnx in enumerate(lines[:3]):
            body.append(txt(x + 18, oy + j * 16, lnx, 11.5,
                            (BLUE_SOFT if fg == WHITE else MUTED), 500, anchor="start"))
    body.append(txt(450, 398, "Un tool risolve un problema · un'architettura una classe di problemi",
                    13, MUTED, 600, italic=True))
    return doc("".join(body))


def hub_spoke_sistema() -> str:
    """Slide 6 — Hub-and-spoke multi-agente + pannello metriche."""
    body = []
    # area sinistra: hub & spoke
    hx, hy = 250, 200
    agents = [
        (95, 75, "DCF", "skill 1·8"),
        (405, 75, "Risk", "skill 2·9"),
        (95, 325, "Comparabili", "skill 3·10"),
        (405, 325, "Credit Risk", "skill 4–7"),
    ]
    # 1) raggi (sotto i nodi)
    for ax, ay, name, sk in agents:
        body.append(ln(hx, hy, ax, ay, BLUE, 2.5))
    # 2) hub centrale (sopra i raggi)
    body.append(circle(hx, hy, 58, BLUE_DARK))
    body.append(circle(hx, hy, 58, "none", stroke=WHITE, sw=3))
    body.append(txt(hx, hy + 5, "Orchestratore", 13.5, WHITE, 800))
    # 3) nodi agente (sopra i raggi)
    for ax, ay, name, sk in agents:
        fs = 12 if len(name) > 6 else 14
        body.append(circle(ax, ay, 46, BLUE))
        body.append(circle(ax, ay, 46, "none", stroke=WHITE, sw=2))
        body.append(txt(ax, ay - 2, name, fs, WHITE, 800))
        body.append(txt(ax, ay + 18, sk, 10.5, BLUE_SOFT, 600))
    body.append(txt(250, 392, "Un team di specialisti che collabora",
                    13, MUTED, 600, italic=True))
    # pannello metriche a destra
    px, pw = 540, 330
    body.append(rrect(px, 24, pw, 360, SURFACE, rx=16))
    body.append(txt(px + pw / 2, 58, "I NUMERI DEL CASO REALE",
                    14, BLUE_DARK, 800, spacing="1"))
    metrics = [
        ("24", "agenti specializzati"),
        ("76", "skill (workflow codificati)"),
        ("348", "test automatizzati"),
        ("40+", "moduli Python"),
        ("26k+", "righe di codice"),
        ("3", "modalità operative"),
    ]
    for i, (val, lab) in enumerate(metrics):
        yy = 92 + i * 47
        body.append(txt(px + 26, yy + 6, val, 26, BLUE, 800, anchor="start"))
        body.append(txt(px + 118, yy + 4, lab, 14, INK, 600, anchor="start"))
        if i < len(metrics) - 1:
            body.append(ln(px + 22, yy + 22, px + pw - 22, yy + 22, LINE, 1))
    return doc("".join(body))


def before_after_skill() -> str:
    """Slide 7 — Prompt generico vs Skill strutturata."""
    body = []
    # PRIMA
    body.append(rrect(30, 30, 380, 320, SURFACE, rx=16))
    body.append(rrect(30, 30, 380, 46, SURFACE2, rx=16))
    body.append(rrect(30, 56, 380, 20, SURFACE2, rx=0))
    body.append(txt(220, 60, "PRIMA — prompt generico", 16, MUTED, 800))
    body.append(txt(50, 112, "“Calcola il DCF di questa azienda”",
                    15, INK, 700, anchor="start", italic=True))
    for i, t in enumerate([
        "Output variabile",
        "Nessun controllo",
        "Non riproducibile",
        "Nessun punto di verifica",
    ]):
        body.append(txt(50, 152 + i * 30, "✗", 15, RED, 800, anchor="start"))
        body.append(txt(74, 152 + i * 30, t, 14, INK, 500, anchor="start"))
    body.append(rrect(50, 296, 120, 34, WHITE, rx=8, stroke=LINE, sw=1.5))
    body.append(txt(110, 318, "40 righe", 15, MUTED, 800))
    # DOPO
    body.append(rrect(490, 30, 390, 320, "#EAF1FF", rx=16, stroke=BLUE, sw=2))
    body.append(rrect(490, 30, 390, 46, BLUE_DARK, rx=16))
    body.append(rrect(490, 56, 390, 20, BLUE_DARK, rx=0))
    body.append(txt(685, 60, "DOPO — skill strutturata", 16, WHITE, 800))
    blocks = [
        ("VINCOLI CRITICI", ["FCFF si sconta al WACC, mai al Ke",
                             "Terminal growth ≤ PIL nominale",
                             "TV non oltre il 75% del valore"]),
        ("WORKFLOW A CHECKPOINT", ["5 step, ognuno con GATE di verifica"]),
        ("ERRORI COMUNI", ["Cosa NON fare, codificato"]),
    ]
    yy = 96
    for title, items in blocks:
        body.append(txt(510, yy, title, 13, BLUE_DARK, 800, anchor="start"))
        yy += 20
        for it in items:
            body.append(txt(522, yy, "•", 13, BLUE, 800, anchor="start"))
            body.append(txt(536, yy, it, 12.5, INK, 500, anchor="start"))
            yy += 19
        yy += 4
    body.append(rrect(700, 300, 160, 34, BLUE, rx=8))
    body.append(txt(780, 322, "250 righe", 15, WHITE, 800))
    # freccia di trasformazione
    body.append(arrow(420, 190, 482, 190, BLUE_DARK, 4))
    return doc("".join(body))


def gate_timeline() -> str:
    """Slide 8 — Workflow con 5 nodi e 4 decision gate."""
    body = []
    nodes = ["Dati", "WACC", "DCF", "Risk", "Report"]
    gates = [
        "Config OK.\nPaese: IT.\nProcedo?",
        "WACC = 8.2%.\nConfermi?",
        "EV = 450M.\nTV peso 68%.\nCoerenza OK.",
        "Range 380–520M.\nIC 90%.\nGenero report?",
    ]
    y = 150
    x0, dx = 70, 190
    # linea base
    body.append(ln(x0, y, x0 + dx * 4, y, LINE, 3))
    for i, n in enumerate(nodes):
        x = x0 + i * dx
        body.append(circle(x, y, 34, BLUE_DARK if i in (0, 4) else BLUE))
        body.append(circle(x, y, 34, "none", stroke=WHITE, sw=2))
        body.append(txt(x, y + 5, n, 14, WHITE, 800))
    for i, g in enumerate(gates):
        gx = x0 + i * dx + dx / 2
        # diamante GATE
        s = 16
        body.append(poly([(gx, y - s), (gx + s, y), (gx, y + s), (gx - s, y)],
                         AMBER, stroke=WHITE, sw=2))
        body.append(txt(gx, y + 4, "G", 13, WHITE, 800))
        # callout sotto
        lines = g.split("\n")
        cy = y + 56
        body.append(rrect(gx - 86, cy - 18, 172, 22 + len(lines) * 17, WHITE,
                          rx=10, stroke=LINE, sw=1.5))
        body.append(txt(gx, cy, "GATE", 11, AMBER, 800, spacing="1"))
        for j, lx in enumerate(lines):
            body.append(txt(gx, cy + 18 + j * 16, lx, 11.5, INK, 500))
    body.append(txt(450, 38, "Procede da solo dove il rischio è basso · si ferma dove conta",
                    14, MUTED, 600, italic=True))
    return doc("".join(body))


def two_outputs() -> str:
    """Slide 9 — IA generica vs IA con dominio (stesso prompt)."""
    body = []
    # banner prompt
    body.append(rrect(120, 16, 660, 40, INK, rx=10))
    body.append(txt(450, 42, "PROMPT:  “Valuta il Terminal Value di questa azienda”",
                    15, WHITE, 700))
    # generica
    body.append(rrect(30, 78, 390, 300, SURFACE, rx=16))
    body.append(txt(225, 110, "IA GENERICA", 16, MUTED, 800))
    body.append(txt(225, 138, "TV = FCF·(1+g)/(WACC−g)", 14, INK, 700))
    body.append(txt(225, 162, "TV = 2.472M", 15, INK, 800))
    body.append(rrect(70, 196, 310, 150, WHITE, rx=12, stroke=LINE, sw=1.5))
    body.append(txt(225, 232, "“Il Terminal Value", 14, INK, 600))
    body.append(txt(225, 254, "è 2.472M.”", 14, INK, 600))
    body.append(txt(225, 300, "Matematicamente corretto", 13, MUTED, 600, italic=True))
    body.append(txt(225, 320, "professionalmente inutile", 13, RED, 700, italic=True))
    # con dominio
    body.append(rrect(480, 78, 390, 300, "#EAF1FF", rx=16, stroke=BLUE, sw=2))
    body.append(txt(675, 110, "IA CON DOMINIO", 16, BLUE_DARK, 800))
    body.append(txt(675, 134, "TV = NOPAT·(1−g/ROIC)/(wacc−g)", 13, INK, 700))
    checks = [
        ("✓", GREEN, "ROIC nuovi inv. 12% > WACC 8%"),
        ("✗", RED, "Peso TV su EV: 82% — anomalo (>75%)"),
        ("✗", RED, "g 3% > PIL Italia 1,5% — rivedere"),
    ]
    for i, (mk, col, t) in enumerate(checks):
        yy = 162 + i * 26
        body.append(txt(505, yy, mk, 15, col, 800, anchor="start"))
        body.append(txt(525, yy, t, 12.5, INK, 600, anchor="start"))
    body.append(rrect(505, 250, 340, 96, WHITE, rx=12, stroke=BLUE, sw=1.5))
    body.append(txt(675, 276, "“TV = 1.890M ma due check falliti.", 12.5, INK, 600))
    body.append(txt(675, 296, "Raccomando: ridurre g a 1,5%.", 12.5, INK, 600))
    body.append(txt(675, 322, "Procedo o rivediamo?”", 13, BLUE_DARK, 800))
    return doc("".join(body))


def knowledge_pipeline() -> str:
    """Slide 10 — Paper → Codice Python → Skill operativa."""
    body = []
    cols = ["PAPER ACCADEMICI", "CODICE PYTHON", "SKILL OPERATIVA"]
    cx = [150, 450, 750]
    for x, c in zip(cx, cols):
        body.append(txt(x, 40, c, 14, BLUE_DARK, 800, spacing="1"))
    rows = [
        ("Scarano/Brughera 2008", "Bilancio Medio Standard",
         "bms/builder.py", "386 righe · 15 metodi",
         "bms-builder", "144 righe · 4 gate"),
        ("Scarano/Di Napoli 2008", "Terminal Value coerente",
         "dcf/coherence.py", "428 righe · 7 check",
         "dcf-tv-coherence", "211 righe · 5 gate"),
        ("Montesi/Papiro 2014", "Credit Risk Monte Carlo",
         "agentic_credit_risk/", "1.430 righe · 6 moduli",
         "agentic-credit-risk", "187 righe · 6 gate"),
    ]
    cw = 232
    for i, r in enumerate(rows):
        y = 64 + i * 108
        cards = [
            (r[0], r[1], SURFACE2, INK, BLUE_DARK),
            (r[2], r[3], BLUE, WHITE, WHITE),
            (r[4], r[5], BLUE_DARK, WHITE, BLUE_SOFT),
        ]
        for j, (t1, t2, fill, fg, fg2) in enumerate(cards):
            x = cx[j] - cw / 2
            body.append(rrect(x, y, cw, 80, fill, rx=12))
            body.append(txt(cx[j], y + 34, t1, 13.5, fg, 800))
            body.append(txt(cx[j], y + 58, t2, 12, fg2, 500))
            if j < 2:
                body.append(arrow(cx[j] + cw / 2 + 2, y + 40,
                                  cx[j + 1] - cw / 2 - 2, y + 40, BLUE_DARK, 3))
    return doc("".join(body))


def domain_enrichment() -> str:
    """Slide — Piramide dell'arricchimento del dominio (3 strati).

    Racconta la storia del progetto: dagli strumenti specifici, al porting sul
    framework regolatorio europeo, fino alla suite integrata e omogenea.
    """
    apex = (250, 30)
    bl, br = (60, 360), (440, 360)
    ys = [30, 140, 250, 360]
    body = []

    def hw(y):
        return (y - apex[1]) / (br[1] - apex[1]) * (br[0] - bl[0]) / 2

    levels = [
        ("INTEGRAZIONE", AMBER, INK,
         "I tre progetti fusi in una suite ampliata e omogenea: modelli e regole si compongono"),
        ("FRAMEWORK UE", BLUE, WHITE,
         "Porting dei financial tool al quadro normativo europeo: MiFID II, Golden Power, SFDR, DORA"),
        ("STRUMENTI", SURFACE2, INK,
         "Valuation Analyst (Damodaran) e Rating & Valuation: modelli su misura per le PMI italiane"),
    ]
    for i, (label, fill, fg, ex) in enumerate(levels):
        yt, yb = ys[i], ys[i + 1]
        cx = apex[0]
        body.append(poly([(cx - hw(yt), yt), (cx + hw(yt), yt),
                          (cx + hw(yb), yb), (cx - hw(yb), yb)], fill,
                         stroke=WHITE, sw=3))
        ymid = (yt + yb) / 2
        body.append(txt(cx, ymid + 6, label, 17, fg, 800))
        # esempio a destra
        body.append(ln(cx + hw(ymid) + 6, ymid, 500, ymid, LINE, 1.5))
        wrap = []
        words, cur = ex.split(" "), ""
        for w_ in words:
            if len(cur) + len(w_) > 42:
                wrap.append(cur.strip()); cur = w_ + " "
            else:
                cur += w_ + " "
        wrap.append(cur.strip())
        for j, lx in enumerate(wrap[:3]):
            body.append(txt(512, ymid - 16 + j * 17, lx, 12.5,
                            (BLUE_DARK if i == 0 else INK),
                            (700 if i == 0 else 500), anchor="start"))
    body.append(txt(250, 392, "Ogni strato eredita e arricchisce quello sotto",
                    13, MUTED, 600, italic=True))
    return doc("".join(body))


def three_rails() -> str:
    """Slide 13 — Tre modalità coesistenti che convergono."""
    body = []
    rails = [
        ("MODALITÀ 1 · Damodaran", "Config JSON → Script → Report PDF",
         "Società quotate · curva bassa", SURFACE2, INK, BLUE_DARK),
        ("MODALITÀ 2 · FSI Excel", "Claude guida → Review a ogni step",
         "Italiane quotate · curva media", BLUE_SOFT, INK, BLUE_DARK),
        ("MODALITÀ 3 · Rating & Valuation", "BMS → DCF → Monte Carlo → Rating",
         "PMI non quotate · curva alta", BLUE, WHITE, WHITE),
    ]
    for i, (title, flow, target, fill, fg, fg2) in enumerate(rails):
        y = 40 + i * 104
        body.append(rrect(40, y, 600, 86, fill, rx=14))
        body.append(txt(64, y + 30, title, 16, fg, 800, anchor="start"))
        body.append(txt(64, y + 54, flow, 13.5, fg, 600, anchor="start"))
        body.append(txt(64, y + 74, target, 12, fg2, 500, anchor="start"))
        body.append(arrow(648, y + 43, 712, y + 43, BLUE_DARK, 3))
    # nodo di convergenza
    body.append(rrect(720, 120, 150, 150, BLUE_DARK, rx=20))
    body.append(txt(795, 178, "ADOZIONE", 15, WHITE, 800))
    body.append(txt(795, 202, "PROGRESSIVA", 14, BLUE_SOFT, 700))
    body.append(txt(795, 232, "non sostitutiva", 12, WHITE, 500, italic=True))
    body.append(txt(440, 396, "Parti da dove il valore è visibile e il rischio è basso",
                    13, MUTED, 600, italic=True))
    return doc("".join(body))


def matrix_2x2() -> str:
    """Slide 14 — Matrice rischio × reversibilità."""
    body = []
    x0, y0, cw, chh = 180, 70, 320, 135
    cells = [
        (0, 0, "IA DECIDE", "Calcoli, formattazione, data retrieval, bozza report", GREEN),
        (1, 0, "IA PROPONE · UMANO CONFERMA", "Scelta comparabili, pubblicazione report", BLUE),
        (0, 1, "IA PROPONE · UMANO CONFERMA", "Assunzioni DCF, parametri WACC, scelta modello", BLUE),
        (1, 1, "UMANO DECIDE · IA SUPPORTA", "Raccomandazione BUY/SELL, rating creditizio", BLUE_DARK),
    ]
    for cxi, cyi, title, desc, accent in cells:
        x = x0 + cxi * cw
        y = y0 + cyi * chh
        body.append(rrect(x + 4, y + 4, cw - 8, chh - 8, SURFACE, rx=12))
        body.append(rrect(x + 4, y + 4, cw - 8, 6, accent, rx=3))
        # titolo wrap
        words, cur, lines = title.split(" "), "", []
        for w_ in words:
            if len(cur) + len(w_) > 24:
                lines.append(cur.strip()); cur = w_ + " "
            else:
                cur += w_ + " "
        lines.append(cur.strip())
        for j, lx in enumerate(lines):
            body.append(txt(x + cw / 2, y + 36 + j * 20, lx, 14.5, accent, 800))
        dwords, dcur, dlines = desc.split(" "), "", []
        for w_ in dwords:
            if len(dcur) + len(w_) > 32:
                dlines.append(dcur.strip()); dcur = w_ + " "
            else:
                dcur += w_ + " "
        dlines.append(dcur.strip())
        oy = y + 36 + len(lines) * 20 + 6
        for j, lx in enumerate(dlines[:3]):
            body.append(txt(x + cw / 2, oy + j * 17, lx, 12, MUTED, 500))
    # assi
    body.append(txt(x0 + cw / 2, 56, "REVERSIBILE", 13, BLUE_DARK, 800))
    body.append(txt(x0 + cw + cw / 2, 56, "IRREVERSIBILE", 13, BLUE_DARK, 800))
    body.append(f'<text x="158" y="{y0 + chh / 2}" font-size="13" '
                f'fill="{BLUE_DARK}" font-weight="800" text-anchor="middle" '
                f'transform="rotate(-90 158 {y0 + chh / 2})">RISCHIO BASSO</text>')
    body.append(f'<text x="158" y="{y0 + chh + chh / 2}" font-size="13" '
                f'fill="{BLUE_DARK}" font-weight="800" text-anchor="middle" '
                f'transform="rotate(-90 158 {y0 + chh + chh / 2})">RISCHIO ALTO</text>')
    return doc("".join(body))


# Mappa nome → funzione, per generazione batch
DIAGRAMS = {
    "02_piramide_adozione": pyramid_adozione,
    "04_triangolo_pilastri": triangle_pilastri,
    "05_scala_maturita": staircase_maturita,
    "06_hub_spoke": hub_spoke_sistema,
    "07_skill_contratto": before_after_skill,
    "08_gate_timeline": gate_timeline,
    "09_due_output": two_outputs,
    "10_knowledge_pipeline": knowledge_pipeline,
    "11_arricchimento_dominio": domain_enrichment,
    "13_tre_binari": three_rails,
    "14_matrice_2x2": matrix_2x2,
}


def main() -> None:
    import cairosvg
    from pathlib import Path
    out = Path(__file__).resolve().parents[1] / "output" / "assets_svg"
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in DIAGRAMS.items():
        svg = fn()
        (out / f"{name}.svg").write_text(svg, encoding="utf-8")
        cairosvg.svg2png(bytestring=svg.encode("utf-8"),
                         write_to=str(out / f"{name}.png"),
                         output_width=1800, output_height=810)
    print(f"Generati {len(DIAGRAMS)} diagrammi SVG+PNG in {out}")


if __name__ == "__main__":
    main()
