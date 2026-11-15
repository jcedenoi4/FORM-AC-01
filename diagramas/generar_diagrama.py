"""Genera el diagrama de Ishikawa del fallo de Fastly (8 de junio de 2021).

Tres salidas con la misma geometria:
  diagramas/causas-fastly.drawio   archivo editable (mxGraph / draw.io)
  diagramas/causas-fastly.pdf      version vectorial para LaTeX
  diagramas/causas-fastly.png      exportacion raster a 300 dpi

Elaborado por el equipo (MENDOZA BERMELLO ANGELLO AGUSTIN) para FORM-AC-01.
Sin dependencias de red: PyMuPDF dibuja el PDF y rasteriza el PNG.

Uso:  python generar_diagrama.py
"""
from __future__ import annotations

import os
import sys
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
# Rutas locales donde puede estar PyMuPDF (se ignoran si ya esta instalado).
for _rel in ("_libs", os.path.join("..", "_libs"),
             os.path.join("..", "..", "_libs"), os.path.join("..", "..", "..", "_libs")):
    _cand = os.path.abspath(os.path.join(HERE, _rel))
    if os.path.isdir(_cand) and _cand not in sys.path:
        sys.path.insert(0, _cand)
import pymupdf  # noqa: E402

# --------------------------------------------------------------------------
# Lienzo: 1 unidad = 1 punto PDF. Impreso a 17 cm de ancho la escala es 1:1.
# --------------------------------------------------------------------------
W, H = 482.0, 362.0
SPINE_Y = 180.0
SPINE_X0 = 10.0
SPINE_X1 = 372.0
HEAD = (384.0, 118.0, 476.0, 226.0)   # caja del efecto (cabeza del pescado)

FONT_FILES = {
    "regular": ["C:/Windows/Fonts/arial.ttf",
                "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
                "/System/Library/Fonts/Supplemental/Arial.ttf"],
    "bold": ["C:/Windows/Fonts/arialbd.ttf",
             "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
             "/System/Library/Fonts/Supplemental/Arial Bold.ttf"],
    "italic": ["C:/Windows/Fonts/ariali.ttf",
               "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf",
               "/System/Library/Fonts/Supplemental/Arial Italic.ttf"],
}
FONT_FALLBACK = {"regular": "helv", "bold": "hebo", "italic": "heit"}
_FONTS = {}


def font(kind):
    """Fuente tipografica: Arial/Liberation si existe; si no, base 14 de PDF."""
    if kind not in _FONTS:
        for path in FONT_FILES[kind]:
            if os.path.exists(path):
                _FONTS[kind] = pymupdf.Font(fontfile=path)
                break
        else:
            _FONTS[kind] = pymupdf.Font(FONT_FALLBACK[kind])
    return _FONTS[kind]

# Colores
C_LATENT = (0.62, 0.16, 0.12)     # defecto latente
C_TRIGGER = (0.85, 0.42, 0.06)    # evento desencadenante
C_AGG = (0.13, 0.36, 0.56)        # factor agravante
C_INK = (0.13, 0.13, 0.13)
C_BONE = (0.32, 0.32, 0.32)

TYPE_COLOR = {"latente": C_LATENT, "disparador": C_TRIGGER, "agravante": C_AGG}

FS_CAUSE = 6.9
FS_CAT = 8.2
FS_LEGEND = 6.4
FS_TITLE = 9.0
BOX_W = 78.0
LINE_STEP = 1.20

# --------------------------------------------------------------------------
# Modelo de causas: 6 categorias x 3 causas.
# tipo: latente | disparador | agravante
# --------------------------------------------------------------------------
BONES = [
    {
        "cat": "PERSONAS",
        "side": "up",
        "base": 62.0,
        "causes": [
            ("El cliente aplica un cambio válido sin clasificar su riesgo", "disparador"),
            ("Las pruebas del 12 de mayo no cubrieron esa combinación", "latente"),
            ("Diagnóstico manual: 40 min para aislar la configuración", "agravante"),
        ],
    },
    {
        "cat": "PROCESOS",
        "side": "up",
        "base": 174.0,
        "causes": [
            ("Despliegue del 12 de mayo sin canario ni anillos", "agravante"),
            ("Sin matriz de pruebas configuración × software", "latente"),
            ("Rollback global no automatizado ante la caída", "agravante"),
        ],
    },
    {
        "cat": "TECNOLOGÍA",
        "side": "up",
        "base": 286.0,
        "causes": [
            ("Defecto sin guarda en el propio código de borde", "latente"),
            ("El POP aborta el proceso en vez de degradar", "latente"),
            ("Configuración idéntica en el 100 % de los POP", "agravante"),
        ],
    },
    {
        "cat": "CONFIGURACIÓN",
        "side": "down",
        "base": 118.0,
        "causes": [
            ("Combinación no prevista de parámetros válidos", "disparador"),
            ("Sin validación semántica de combinaciones", "latente"),
            ("Propagación a toda la red en segundos", "agravante"),
        ],
    },
    {
        "cat": "MEDICIÓN",
        "side": "down",
        "base": 230.0,
        "causes": [
            ("Detección en <1 min, pero sin señal de la causa", "agravante"),
            ("Sin correlación entre el cambio y la caída", "agravante"),
            ("Aviso de estado sin diagnóstico asociado", "agravante"),
        ],
    },
    {
        "cat": "ENTORNO",
        "side": "down",
        "base": 342.0,
        "causes": [
            ("27 días latente sin llegar a activarse", "agravante"),
            ("Un solo proveedor CDN concentra miles de sitios", "agravante"),
            ("Sitios sin plan de contingencia multi-CDN", "agravante"),
        ],
    },
]

BONE_DX = 100.0
BONE_DY = 130.0
T_STOPS = (0.28, 0.53, 0.78)

HEAD_LINES = [
    ("FALLO GLOBAL", 8.2, "bold"),
    ("DE LA RED FASTLY", 8.2, "bold"),
    ("8 de junio de 2021", 7.0, "plain"),
    ("85 % de la red con errores", 6.4, "plain"),
    ("95 % normal en 49 min", 6.4, "plain"),
    ("Defecto latente activado", 6.4, "italic"),
    ("por una configuración", 6.4, "italic"),
    ("válida de cliente", 6.4, "italic"),
]

LEGEND = [
    ("Defecto latente (raíz técnica)", C_LATENT),
    ("Evento desencadenante", C_TRIGGER),
    ("Factor agravante", C_AGG),
]
TITLE = "Diagrama de Ishikawa — causas del fallo global de Fastly (8 de junio de 2021)"


# --------------------------------------------------------------------------
def tint(rgb, amount=0.90):
    return tuple(1.0 - (1.0 - c) * (1.0 - amount) for c in rgb)


def wrap(text, font, size, maxw):
    """Corta el texto en lineas que quepan en maxw puntos."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        probe = w if not cur else cur + " " + w
        if font.text_length(probe, size) <= maxw or not cur:
            cur = probe
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def model():
    """Calcula la geometria y las cajas de texto ya medidas."""
    fr = font("regular")
    fb = font("bold")

    boxes, cats, bones_out = [], [], []
    for b in BONES:
        sgn = -1.0 if b["side"] == "up" else 1.0
        base = (b["base"], SPINE_Y)
        tip = (b["base"] + BONE_DX, SPINE_Y + sgn * BONE_DY)
        bones_out.append((base, tip))
        cats.append(
            {
                "text": b["cat"],
                "x": tip[0],
                "y": tip[1] + (sgn * 12.5),
                "w": fb.text_length(b["cat"], FS_CAT),
            }
        )
        for t, (txt, kind) in zip(T_STOPS, b["causes"]):
            lines = wrap(txt, fr, FS_CAUSE, BOX_W - 8.0)
            bh = len(lines) * (FS_CAUSE * LINE_STEP) + 4.0
            cx = b["base"] + BONE_DX * t
            cy = SPINE_Y + sgn * BONE_DY * t
            x1 = cx - 5.0
            x0 = x1 - BOX_W
            boxes.append(
                {
                    "lines": lines,
                    "rect": (x0, cy - bh / 2.0, x1, cy + bh / 2.0),
                    "color": TYPE_COLOR[kind],
                    "kind": kind,
                    "anchor": (cx, cy),
                }
            )
    return fr, fb, boxes, cats, bones_out


def check_overlaps(boxes, cats, bones):
    def inter(a, b):
        return not (
            a[2] <= b[0] + 0.1 or b[2] <= a[0] + 0.1 or a[3] <= b[1] + 0.1 or b[3] <= a[1] + 0.1
        )

    problems = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            if inter(boxes[i]["rect"], boxes[j]["rect"]):
                problems.append(("cajas", boxes[i]["lines"][0], boxes[j]["lines"][0]))
    for bx in boxes:
        x0, y0, x1, y1 = bx["rect"]
        if x0 < 2 or x1 > W - 2 or y0 < 26 or y1 > H - 18:
            problems.append(("fuera de lienzo", bx["lines"][0], round(x0, 1)))
        if len(bx["lines"]) > 3:
            problems.append(("demasiadas lineas", bx["lines"][0], len(bx["lines"])))
    # etiquetas de categoria contra cajas y contra la caja del efecto
    for c in cats:
        crect = (c["x"] - c["w"] / 2.0 - 2, c["y"] - 5.5, c["x"] + c["w"] / 2.0 + 2, c["y"] + 5.5)
        for bx in boxes:
            if inter(crect, bx["rect"]):
                problems.append(("categoria/caja", c["text"], bx["lines"][0]))
        if inter(crect, HEAD):
            problems.append(("categoria/efecto", c["text"], ""))
        if crect[0] < 2 or crect[2] > W - 2:
            problems.append(("categoria fuera", c["text"], round(crect[0], 1)))
    # las espinas no deben entrar en la caja del efecto
    for base, tip in bones:
        for k in range(21):
            p = (base[0] + (tip[0] - base[0]) * k / 20.0, base[1] + (tip[1] - base[1]) * k / 20.0)
            if HEAD[0] <= p[0] <= HEAD[2] and HEAD[1] <= p[1] <= HEAD[3]:
                problems.append(("espina/efecto", str(base), str(tip)))
    return problems


def check_head():
    """Comprueba que el texto de la cabeza quepa en su caja."""
    fonts = {"plain": font("regular"), "bold": font("bold"), "italic": font("italic")}
    problems = []
    avail = HEAD[2] - HEAD[0] - 8.0
    total = 0.0
    for txt, size, style in HEAD_LINES:
        w = fonts[style].text_length(txt, size)
        if w > avail:
            problems.append(("cabeza demasiado ancha", txt, round(w, 1), round(avail, 1)))
        total += size * (1.58 if style == "bold" else 1.52)
    if 13.0 + total > (HEAD[3] - HEAD[1]) - 3.0:
        problems.append(("cabeza demasiado alta", "", round(13.0 + total, 1)))
    return problems


# --------------------------------------------------------------------------
def build_pdf(path):
    fr, fb, boxes, cats, bones = model()
    fi = font("italic")
    doc = pymupdf.open()
    page = doc.new_page(width=W, height=H)
    tw = pymupdf.TextWriter(page.rect)

    tw.append(((W - fb.text_length(TITLE, FS_TITLE)) / 2.0, 17.0), TITLE,
              font=fb, fontsize=FS_TITLE)

    # Espina central con punta de flecha
    shape = page.new_shape()
    shape.draw_line(pymupdf.Point(SPINE_X0, SPINE_Y), pymupdf.Point(SPINE_X1, SPINE_Y))
    shape.finish(color=C_BONE, width=2.6)
    shape.draw_polyline([
        pymupdf.Point(SPINE_X1 + 1.0, SPINE_Y - 4.6),
        pymupdf.Point(SPINE_X1 + 10.0, SPINE_Y),
        pymupdf.Point(SPINE_X1 + 1.0, SPINE_Y + 4.6),
    ])
    shape.finish(color=C_BONE, fill=C_BONE, width=0.8, closePath=True)
    for base, tip in bones:
        shape.draw_line(pymupdf.Point(*base), pymupdf.Point(*tip))
    shape.finish(color=C_BONE, width=1.6)

    # Guias
    for bx in boxes:
        x0, y0, x1, y1 = bx["rect"]
        ax, ay = bx["anchor"]
        shape.draw_line(pymupdf.Point(x1, (y0 + y1) / 2.0), pymupdf.Point(ax, ay))
    shape.finish(color=(0.55, 0.55, 0.55), width=0.5)
    shape.commit()

    # Cajas de causas
    for bx in boxes:
        x0, y0, x1, y1 = bx["rect"]
        s = page.new_shape()
        s.draw_rect(pymupdf.Rect(x0, y0, x1, y1), radius=0.16)
        s.finish(color=bx["color"], fill=tint(bx["color"]), width=0.75)
        s.commit()
        total = len(bx["lines"]) * (FS_CAUSE * LINE_STEP)
        first = (y0 + y1) / 2.0 - total / 2.0 + FS_CAUSE * 0.95
        for k, ln in enumerate(bx["lines"]):
            tw.append(((x0 + x1) / 2.0 - fr.text_length(ln, FS_CAUSE) / 2.0,
                       first + k * (FS_CAUSE * LINE_STEP)), ln, font=fr, fontsize=FS_CAUSE)

    # Categorias
    for c in cats:
        tw.append((c["x"] - c["w"] / 2.0, c["y"] + FS_CAT * 0.35), c["text"],
                  font=fb, fontsize=FS_CAT)

    # Caja del efecto
    x0, y0, x1, y1 = HEAD
    s = page.new_shape()
    s.draw_rect(pymupdf.Rect(x0, y0, x1, y1), radius=0.14)
    s.finish(color=(0.25, 0.25, 0.25), fill=(0.93, 0.93, 0.93), width=1.5)
    s.commit()
    y = y0 + 13.0
    for txt, size, style in HEAD_LINES:
        f = fb if style == "bold" else (fi if style == "italic" else fr)
        tw.append(((x0 + x1) / 2.0 - f.text_length(txt, size) / 2.0, y), txt,
                  font=f, fontsize=size)
        y += size * (1.58 if style == "bold" else 1.52)

    # Leyenda
    lx, ly = SPINE_X0 + 2.0, H - 12.0
    for txt, col in LEGEND:
        s = page.new_shape()
        s.draw_rect(pymupdf.Rect(lx, ly - 5.4, lx + 8.2, ly + 2.0), radius=0.15)
        s.finish(color=col, fill=tint(col), width=0.75)
        s.commit()
        tw.append((lx + 11.0, ly), txt, font=fi, fontsize=FS_LEGEND)
        lx += 11.0 + fi.text_length(txt, FS_LEGEND) + 18.0
    credit = "Elaborado por A. Mendoza B. — FORM-AC-01"
    tw.append((W - 4.0 - fi.text_length(credit, FS_LEGEND), ly), credit,
              font=fi, fontsize=FS_LEGEND)

    tw.write_text(page, color=C_INK)
    doc.subset_fonts()
    doc.save(path, garbage=4, deflate=True)
    doc.close()
    return boxes


def build_png(pdf_path, png_path, dpi=300):
    doc = pymupdf.open(pdf_path)
    pix = doc[0].get_pixmap(dpi=dpi, alpha=False)
    pix.save(png_path)
    doc.close()
    return pix.width, pix.height


# --------------------------------------------------------------------------
# draw.io: mismas coordenadas, 1 pt = 4/3 px
# --------------------------------------------------------------------------
S = 4.0 / 3.0
FONT_FAMILY = "Helvetica"


def px(v):
    return round(v * S, 2)


def html_text(lines):
    return "&lt;br&gt;".join(escape(ln, {'"': "&quot;"}) for ln in lines)


def hexc(rgb):
    return "#%02X%02X%02X" % tuple(int(round(c * 255)) for c in rgb)


def head_html():
    """Texto HTML de la cabeza, agrupando estilos consecutivos."""
    groups = []
    for txt, _size, style in HEAD_LINES:
        if groups and groups[-1][0] == style:
            groups[-1][1].append(escape(txt))
        else:
            groups.append((style, [escape(txt)]))
    out = []
    for style, items in groups:
        inner = "&lt;br&gt;".join(items)
        if style == "bold":
            out.append(f"&lt;b&gt;{inner}&lt;/b&gt;")
        elif style == "italic":
            out.append(f"&lt;i&gt;{inner}&lt;/i&gt;")
        else:
            out.append(inner)
    return "&lt;br&gt;".join(out)


def build_drawio(path):
    """Escribe el mxfile editable con la misma geometria del PDF."""
    fr, fb, boxes, cats, bones = model()
    fi = font("italic")
    cells = []

    def vertex(cid, value, style, x, y, w, h):
        cells.append(
            f'        <mxCell id="{cid}" value="{value}" style="{style}" vertex="1" parent="1">\n'
            f'          <mxGeometry x="{px(x)}" y="{px(y)}" width="{px(w)}" height="{px(h)}" '
            f'as="geometry"/>\n'
            f"        </mxCell>"
        )

    def edge(cid, pts, style):
        cells.append(
            f'        <mxCell id="{cid}" style="{style}" edge="1" parent="1">\n'
            f'          <mxGeometry relative="1" as="geometry">\n'
            f'            <mxPoint x="{px(pts[0][0])}" y="{px(pts[0][1])}" as="sourcePoint"/>\n'
            f'            <mxPoint x="{px(pts[-1][0])}" y="{px(pts[-1][1])}" as="targetPoint"/>\n'
            f"          </mxGeometry>\n"
            f"        </mxCell>"
        )

    vertex("titulo", escape(TITLE),
           f"text;html=1;align=center;verticalAlign=middle;fontSize={px(FS_TITLE):.1f};"
           f"fontStyle=1;fontFamily={FONT_FAMILY};fontColor=#212121;",
           0, 9, W, 13)

    edge("espina", [(SPINE_X0, SPINE_Y), (SPINE_X1 + 10.0, SPINE_Y)],
         "endArrow=block;endFill=1;html=1;strokeColor=#525252;strokeWidth=3.4;rounded=0;")
    for i, (base, tip) in enumerate(bones):
        edge(f"espina_{i}", [base, tip],
             "endArrow=none;html=1;strokeColor=#525252;strokeWidth=2.1;rounded=0;")

    for i, bx in enumerate(boxes):
        x0, y0, x1, y1 = bx["rect"]
        cells.append(
            f'        <mxCell id="causa_{i}" value="{html_text(bx["lines"])}" '
            f'style="rounded=1;arcSize=12;whiteSpace=nowrap;html=1;fillColor={hexc(tint(bx["color"]))};'
            f"strokeColor={hexc(bx['color'])};fontSize={px(FS_CAUSE):.1f};fontFamily={FONT_FAMILY};"
            f'fontColor=#212121;align=center;verticalAlign=middle;" vertex="1" parent="1">\n'
            f'          <mxGeometry x="{px(x0)}" y="{px(y0)}" width="{px(x1 - x0)}" '
            f'height="{px(y1 - y0)}" as="geometry"/>\n'
            f"        </mxCell>"
        )
        edge(f"guia_{i}", [(x1, (y0 + y1) / 2.0), bx["anchor"]],
             "endArrow=none;html=1;strokeColor=#8C8C8C;strokeWidth=0.75;rounded=0;")

    for i, c in enumerate(cats):
        vertex(f"cat_{i}", escape(c["text"]),
               f"text;html=1;align=center;verticalAlign=middle;fontSize={px(FS_CAT):.1f};"
               f"fontStyle=1;fontFamily={FONT_FAMILY};fontColor=#212121;",
               c["x"] - c["w"] / 2.0 - 6, c["y"] - 6, c["w"] + 12, 12)

    vertex("efecto", head_html(),
           "rounded=1;arcSize=12;whiteSpace=nowrap;html=1;fillColor=#EDEDED;strokeColor=#404040;"
           f"fontSize={px(7.0):.1f};fontFamily={FONT_FAMILY};fontColor=#212121;"
           "align=center;verticalAlign=middle;",
           HEAD[0], HEAD[1], HEAD[2] - HEAD[0], HEAD[3] - HEAD[1])

    lx, ly = SPINE_X0 + 2.0, H - 12.0
    for i, (txt, col) in enumerate(LEGEND):
        cells.append(
            f'        <mxCell id="leg_box_{i}" style="rounded=1;arcSize=15;html=1;'
            f'fillColor={hexc(tint(col))};strokeColor={hexc(col)};strokeWidth=0.9;" '
            f'vertex="1" parent="1">\n'
            f'          <mxGeometry x="{px(lx)}" y="{px(ly - 5.4)}" width="{px(8.2)}" '
            f'height="{px(7.4)}" as="geometry"/>\n'
            f"        </mxCell>"
        )
        wtxt = fi.text_length(txt, FS_LEGEND) + 4.0
        vertex(f"leg_txt_{i}", escape(txt),
               f"text;html=1;align=left;verticalAlign=middle;whiteSpace=nowrap;"
               f"fontSize={px(FS_LEGEND):.1f};fontStyle=2;fontFamily={FONT_FAMILY};fontColor=#212121;",
               lx + 11.0, ly - 6.5, wtxt, 9)
        lx += 11.0 + wtxt + 16.0

    credit = "Elaborado por A. Mendoza B. — FORM-AC-01"
    vertex("credito", escape(credit),
           f"text;html=1;align=right;verticalAlign=middle;whiteSpace=nowrap;"
           f"fontSize={px(FS_LEGEND):.1f};fontStyle=2;fontFamily={FONT_FAMILY};fontColor=#212121;",
           W - 132, ly - 6.5, 128, 9)

    body = "\n".join(cells)
    xml = (
        '<mxfile host="app.diagrams.net" agent="form-ac-01" version="24.7.17" type="device">\n'
        '  <diagram id="fastly-causas" name="Causas raíz Fastly 2021">\n'
        f'    <mxGraphModel dx="{px(W):.0f}" dy="{px(H):.0f}" grid="0" gridSize="10" guides="1" '
        'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
        f'pageWidth="{px(W):.0f}" pageHeight="{px(H):.0f}" math="0" shadow="0" background="#FFFFFF">\n'
        "      <root>\n"
        '        <mxCell id="0"/>\n'
        '        <mxCell id="1" parent="0"/>\n'
        f"{body}\n"
        "      </root>\n"
        "    </mxGraphModel>\n"
        "  </diagram>\n"
        "</mxfile>\n"
    )
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(xml)


# --------------------------------------------------------------------------
def main():
    out = os.path.dirname(HERE)          # .../FORM-AC-01
    out = os.path.join(out, "diagramas")
    os.makedirs(out, exist_ok=True)
    pdf = os.path.join(out, "causas-fastly.pdf")
    png = os.path.join(out, "causas-fastly.png")
    drw = os.path.join(out, "causas-fastly.drawio")

    fr, fb, boxes, cats, bones = model()
    problems = check_overlaps(boxes, cats, bones) + check_head()
    if problems:
        print("REVISAR: solapamientos o desbordes detectados")
        for p in problems:
            print("  -", p)
        raise SystemExit(1)

    build_drawio(drw)
    build_pdf(pdf)
    w, h = build_png(pdf, png)
    print(f"OK  {pdf}")
    print(f"OK  {png}  ({w}x{h} px, 300 dpi)")
    print(f"OK  {drw}  ({os.path.getsize(drw)} bytes)")
    print(f"cajas={len(boxes)} categorias={len(cats)} espinas={len(bones)} sin solapamientos")


if __name__ == "__main__":
    main()
