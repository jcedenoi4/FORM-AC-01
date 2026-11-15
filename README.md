# FORM-AC-01 — Fastly 2021

Cada integrante aplica las lecciones del incidente a **su propio Proyecto Fin de Curso (PFC)**.
No hay un PFC único del equipo: los riesgos se agrupan por proyecto, como pide el enunciado.

## Equipo

| Integrante | Aporte | PFC que analiza |
|---|---|---|
| CEDEÑO INTRIAGO JILMAR JESUS | Descripción y línea de tiempo | Sistema de Gestión de Pre-Sustentaciones |
| MENDOZA BERMELLO ANGELLO AGUSTIN | Causas raíz y diagrama | SGIRI — Sistema de Gestión de Incidencias |
| SANCHEZ VERA DARWIN JOEL | Relación con la Unidad 1 | Sistema de Gestión de Pre-Sustentaciones |
| ZAMBRANO TRIVIÑO LEONEL LEONIDAS | Impacto y mitigación | por confirmar |

## Archivos

- `informe/informe.tex`: aporte individual compilable.
- `informe/secciones/`: descripción y tabla del incidente, causas raíz con el diagrama,
  impacto cuantificado y mitigación, y lecciones con tres riesgos del PFC por integrante.
- `informe/referencias.bib`: fuente oficial verificada y dos fuentes complementarias con DOI.
- `diagramas/causas-fastly.drawio`: diagrama de Ishikawa editable, elaborado por el equipo.
- `diagramas/causas-fastly.pdf` y `.png`: exportaciones vectorial y a 300 dpi del diagrama.
- `diagramas/generar_diagrama.py`: script que genera el `.drawio` y sus exportaciones.
- `notas/exposicion-causas.md`: guion de la exposición de 2 minutos de causas raíz.
- `informe/entrega/form-ac-01_fastly.pdf`: documento principal con la carátula grupal como primera página.
- `informe/entrega/Entrega_SGA_FORM-AC-01.pdf`: carátula independiente para SGA, generada al compilar desde `informe/caratula.tex`.
- `artículos científicos/`: las ocho fuentes de acceso gratuito en PDF, con su índice en
  `artículos científicos/README.md` (qué respalda cada una y en qué páginas). El informe
  oficial de Fastly se cita por su URL y no se guarda copia.

## Diagrama de causas

El diagrama agrupa 18 causas en seis categorías (personas, procesos, tecnología,
configuración, medición y entorno) y distingue con color el defecto latente, el evento
desencadenante y los factores agravantes. Es de elaboración propia: no se copió de internet.

- Editable: `diagramas/causas-fastly.drawio` (abrir en [draw.io](https://app.diagrams.net)).
- Exportaciones: `diagramas/causas-fastly.pdf` (usada en LaTeX) y `diagramas/causas-fastly.png` (300 dpi).

Para regenerar el `.drawio`, el PDF y el PNG con la misma geometría:

```bash
pip install pymupdf
python diagramas/generar_diagrama.py
```

El script verifica que ninguna caja se solape ni se salga del lienzo antes de escribir los
archivos; si la comprobación falla, no escribe nada y enumera los conflictos.

## Compilar

Requiere MiKTeX o TeX Live con pdfLaTeX y BibTeX. Desde la carpeta `informe`, compilar primero la carátula y después el análisis:

```powershell
pdflatex caratula.tex
Copy-Item caratula.pdf entrega/Entrega_SGA_FORM-AC-01.pdf
pdflatex informe.tex
bibtex informe
pdflatex informe.tex
pdflatex informe.tex
Copy-Item informe.pdf entrega/form-ac-01_fastly.pdf
```

En Overleaf, subir `informe/` y `diagramas/` conservando la ruta relativa
`../diagramas/causas-fastly.pdf`, compilar `caratula.tex` y guardar su PDF como
`entrega/Entrega_SGA_FORM-AC-01.pdf`; después seleccionar `informe.tex` como principal.
Para integrar al documento grupal, usar los archivos de `secciones/` mediante `\input` y
conservar la bibliografía y los paquetes del documento individual (`graphicx`, `float`,
`lmodern`; el documento ya no depende de `pdfpages`).

## Pendientes del equipo

Este aporte individual no es el informe grupal final ni el PDF identificativo de la plataforma SGA. Las pruebas descritas son propuestas para TA-PFC-E1, todavía no ejecutadas.

- Integrar la sección de Unidad 1 y consolidar los 12 riesgos del PFC en una sola tabla.
- Ajustar el análisis integrado a dos páginas, sin carátula ni referencias.
- Incorporar las evaluaciones de pares y la tabla de retroalimentación reales.
- Revisar la declaración de IA incluida.
- Cada integrante debe hacer sus propios commits.

Fuente principal: [Fastly, Summary of June 8 outage](https://www.fastly.com/blog/summary-of-june-8-outage), Nick Rockwell, 8 de junio de 2021. Consulta: 15 de noviembre de 2026.

Fuentes complementarias (PDF en `artículos científicos/`, claves BibTeX en `informe/referencias.bib`):

| Clave | Referencia | Acceso |
|---|---|---|
| `cook1998` | Cook, *How Complex Systems Fail*, Technical Report, University of Chicago, 1998 | Libre |
| `gunawi2016` | Gunawi et al., *Why Does the Cloud Stop Computing?*, SoCC 2016, pp. 1–16, [doi:10.1145/2987550.2987583](https://doi.org/10.1145/2987550.2987583) | Copia de autor |
| `yuan2014` | Yuan et al., *Simple Testing Can Prevent Most Critical Failures*, OSDI 2014, pp. 249–265 | USENIX OA |
| `xu2016` | Xu et al., *Early Detection of Configuration Errors to Reduce Failure Damage*, OSDI 2016, pp. 619–634 | USENIX OA |
| `basiri2016` | Basiri et al., *Chaos Engineering*, IEEE Software 33(3), pp. 35–41, [doi:10.1109/MS.2016.60](https://doi.org/10.1109/MS.2016.60) | arXiv |
| `gilbert2012` | Gilbert y Lynch, *Perspectives on the CAP Theorem*, Computer 45(2), pp. 30–36, [doi:10.1109/MC.2011.389](https://doi.org/10.1109/MC.2011.389) | Copia de autor |
| `abadi2012` | Abadi, *Consistency Tradeoffs in Modern Distributed Database System Design*, Computer 45(2), pp. 37–42, [doi:10.1109/MC.2012.33](https://doi.org/10.1109/MC.2012.33) | Copia de autor |
| `vansteen2016` | van Steen y Tanenbaum, *A Brief Introduction to Distributed Systems*, Computing 98(10), pp. 967–1009, [doi:10.1007/s00607-016-0508-7](https://doi.org/10.1007/s00607-016-0508-7) | CC BY |
