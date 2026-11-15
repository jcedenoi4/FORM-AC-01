# Diagrama de causas raíz

Diagrama de Ishikawa del fallo global de Fastly del 8 de junio de 2021, elaborado por el
equipo para FORM-AC-01 (apartado «Causas raíz», a cargo de MENDOZA BERMELLO ANGELLO AGUSTIN).
No está copiado de internet: se construyó a partir del informe oficial de Fastly y de las dos
fuentes complementarias de `informe/referencias.bib`.

## Archivos

| Archivo | Uso |
|---|---|
| `causas-fastly.drawio` | Diagrama editable; se abre en [draw.io](https://app.diagrams.net) o en la aplicación de escritorio. |
| `causas-fastly.pdf` | Exportación vectorial que incluye el documento LaTeX. |
| `causas-fastly.png` | Exportación a 300 dpi para diapositivas o para el README. |
| `generar_diagrama.py` | Genera los tres archivos anteriores con la misma geometría. |

## Cómo está construido

- Seis categorías: personas, procesos, tecnología, configuración, medición y entorno.
- Dieciocho causas, tres por categoría, con la misma posición en el `.drawio` y en el PDF.
- Tres colores: rojo para el defecto latente y las condiciones que lo mantuvieron oculto,
  naranja para el evento desencadenante y azul para los factores agravantes.
- La cabeza resume el efecto: 85 % de la red con errores y 95 % restablecido en 49 minutos.

## Regenerar

```bash
pip install pymupdf
python generar_diagrama.py
```

El script comprueba que ninguna caja se solape, que el texto no salga del lienzo y que la
cabeza quepa en su caja; si algo falla, termina con error y enumera los conflictos antes de
escribir archivos. Para editar el diagrama a mano basta con abrir el `.drawio`, ajustar las
cajas y volver a exportar el PDF y el PNG desde draw.io.
