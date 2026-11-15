# FORM-AC-01 — Fastly 2021

PFC: Sistema de Gestión de Pre-Sustentaciones de trabajos de titulación de la UTEQ.

## Equipo

| Integrante | Aporte |
|---|---|
| CEDEÑO INTRIAGO JILMAR JESUS | Descripción y línea de tiempo |
| MENDOZA BERMELLO ANGELLO AGUSTIN | Causas y diagrama |
| SANCHEZ VERA DARWIN JOEL | Unidad 1 |
| ZAMBRANO TRIVIÑO LEONEL LEONIDAS | Impacto y mitigación |

## Archivos

- `informe/informe.tex`: aporte individual compilable.
- `informe/secciones/`: descripción, tabla y tres riesgos del PFC.
- `informe/referencias.bib`: fuente oficial verificada.
- `diagramas/`: espacio para el diagrama editable de Angello.
- `informe/entrega/form-ac-01_fastly.pdf`: documento principal con la carátula grupal como primera página.
- `informe/entrega/Entrega_SGA_FORM-AC-01.pdf`: carátula independiente para SGA, generada al compilar desde `informe/caratula.tex`.

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

En Overleaf, subir `informe/`, compilar `caratula.tex` y guardar su PDF como `entrega/Entrega_SGA_FORM-AC-01.pdf`; después seleccionar `informe.tex` como principal. Para integrar al documento grupal, usar los archivos de `secciones/` mediante `\input` y conservar la bibliografía y los paquetes del documento individual.

## Pendientes del equipo

Este aporte individual no es el informe grupal final ni el PDF identificativo del SGA. Las pruebas descritas son propuestas para TA-PFC-E1, todavía no ejecutadas.

- Integrar las demás secciones y el diagrama original `.drawio`.
- Añadir dos fuentes complementarias admitidas, verificando sus DOI o URL.
- Ajustar el análisis integrado a dos páginas, sin carátula ni referencias.
- Incorporar las evaluaciones y la tabla de retroalimentación reales.
- Revisar la declaración de IA incluida.
- La compilación genera el PDF identificativo para SGA en `informe/entrega/Entrega_SGA_FORM-AC-01.pdf`, con la URL completa en una línea.
- Cada integrante debe hacer sus propios commits. No se han creado commits ni publicado cambios automáticamente.

Fuente principal: [Fastly, Summary of June 8 outage](https://www.fastly.com/blog/summary-of-june-8-outage), Nick Rockwell, 8 de junio de 2021. Consulta: 15 de noviembre de 2026.
