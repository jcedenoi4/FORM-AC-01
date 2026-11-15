# Fuentes bibliográficas — FORM-AC-01

Ocho fuentes de **acceso gratuito** descargadas en esta carpeta, con su DOI o URL verificada,
para respaldar todas las secciones del análisis del fallo de Fastly del 8 de junio de 2021.
La fuente principal es el informe oficial de la empresa, que se consulta en línea: su URL está
en `informe/referencias.bib` y no se guarda copia en PDF porque el original es una página web.
Las demás son artículos académicos con DOI verificable o reportes técnicos reconocidos.

Verificación realizada el **15 de noviembre de 2026**: se comprobó que cada PDF abre, que su
título y autores corresponden a la referencia citada y que el DOI resuelve en el editor
(ACM, IEEE, Springer) o que la URL responde.

## Qué respalda cada fuente

| N.º | Archivo | Referencia | Acceso |
|---|---|---|---|
| 01 | `01_cook_1998_how_complex_systems_fail.pdf` | Cook, *How Complex Systems Fail*, Technical Report, University of Chicago, 1998 (rev. D, 2000) | Acceso libre |
| 02 | `02_gunawi_2016_why_cloud_stops_computing.pdf` | Gunawi et al., *Why Does the Cloud Stop Computing?*, SoCC 2016, pp. 1–16, [doi:10.1145/2987550.2987583](https://doi.org/10.1145/2987550.2987583) | Copia de autor |
| 03 | `03_yuan_2014_simple_testing_prevents_failures.pdf` | Yuan et al., *Simple Testing Can Prevent Most Critical Failures*, OSDI 2014, pp. 249–265 | USENIX Open Access |
| 04 | `04_xu_2016_early_detection_configuration_errors.pdf` | Xu et al., *Early Detection of Configuration Errors to Reduce Failure Damage*, OSDI 2016, pp. 619–634 | USENIX Open Access |
| 05 | `05_basiri_2016_chaos_engineering.pdf` | Basiri et al., *Chaos Engineering*, IEEE Software 33(3), pp. 35–41, [doi:10.1109/MS.2016.60](https://doi.org/10.1109/MS.2016.60) | arXiv (verde) |
| 06 | `06_gilbert_lynch_2012_perspectives_cap.pdf` | Gilbert y Lynch, *Perspectives on the CAP Theorem*, Computer 45(2), pp. 30–36, [doi:10.1109/MC.2011.389](https://doi.org/10.1109/MC.2011.389) | Copia de autor (MIT) |
| 07 | `07_abadi_2012_pacelc.pdf` | Abadi, *Consistency Tradeoffs in Modern Distributed Database System Design*, Computer 45(2), pp. 37–42, [doi:10.1109/MC.2012.33](https://doi.org/10.1109/MC.2012.33) | Copia de autor (UMD) |
| 08 | `08_van_steen_tanenbaum_2016_brief_introduction.pdf` | van Steen y Tanenbaum, *A Brief Introduction to Distributed Systems*, Computing 98(10), pp. 967–1009, [doi:10.1007/s00607-016-0508-7](https://doi.org/10.1007/s00607-016-0508-7) | Open access (CC BY) |

## Correspondencia con las secciones del informe

| Sección del informe | Fuentes recomendadas |
|---|---|
| Descripción del incidente y línea de tiempo | informe oficial de Fastly (en línea) |
| Causas raíz y diagrama | 01 (puntos 3, 4, 7 y 14), 02, 03, 04, 05 |
| Relación con la Unidad 1 | 08 (transparencias, tolerancia a fallos), 06 (CAP), 07 (PACELC), 02 |
| Impacto cuantificado y mitigación | informe oficial de Fastly (en línea), 02 (SLA y cadenas de recuperación), 04, 05 |
| Lecciones aprendidas para el PFC | 03, 04, 05, 02 |

## Detalle y qué aporta cada una

**01 — Cook, *How Complex Systems Fail*.** Sostiene el argumento central de las causas raíz: la
catástrofe exige múltiples fallos que por separado son inocuos (punto 3) y atribuirla a una
«causa raíz» única es incorrecto (punto 7); además, todo cambio introduce nuevas formas de
fallo (punto 14). Sirve para separar el defecto latente del evento desencadenante.

**02 — Gunawi et al.** Estudio de 597 caídas no planificadas en 32 servicios entre 2009 y 2015:
clasifica causas, duraciones y procedimientos de corrección, y muestra que la redundancia no
basta si falla la cadena de recuperación (detección, failover y respaldo). Respalda tanto las
causas como el impacto y las medidas de mitigación.

**03 — Yuan et al.** Analiza 198 fallos reales en Cassandra, HBase, HDFS, MapReduce y Redis:
la mayoría de las caídas catastróficas se habría evitado probando el código de manejo de
errores. Respalda la afirmación de que el defecto de Fastly pudo detectarse con pruebas simples.

**04 — Xu et al.** Documenta los errores latentes de configuración: parámetros que controlan la
tolerancia a fallos suelen no validarse al inicio y permanecen ocultos hasta que el error se
manifiesta. Es la evidencia directa del «defecto sin guarda» y de la falta de validación
semántica del diagrama.

**05 — Basiri et al.** Define la ingeniería del caos y el concepto de radio de impacto
(*blast radius*): por qué un despliegue progresivo y experimentos controlados contienen el
fallo antes de exponerlo a toda la red.

**06 — Gilbert y Lynch.** Referencia canónica del teorema CAP: qué significa realmente elegir
entre consistencia y disponibilidad ante una partición, y qué malinterpretaciones conviene
evitar al aplicar CAP a un caso real.

**07 — Abadi.** Añade PACELC: además del trade-off de CAP ante particiones, existe el de
consistencia frente a latencia cuando el sistema opera normalmente. Útil para discutir qué se
sacrificó en el incidente.

**08 — van Steen y Tanenbaum.** Panorámica de sistemas distribuidos con las transparencias de
distribución (pp. 970–976), la tolerancia a fallos (p. 988) y el teorema CAP (pp. 1007–1008).
Es la fuente que conviene citar para la sección de Unidad 1.

## Notas de uso

- Las claves BibTeX de todas las fuentes están en `informe/referencias.bib`. Solo aparecen en
  el PDF las que se citan con `\cite`.
- En LaTeX, para citar el informe oficial use la clave `fastly2021`; para las demás, la clave
  coincide con el apellido y el año (por ejemplo `gunawi2016`, `gilbert2012`, `vansteen2016`).
- Las copias de autor (02, 06, 07) y los PDF de USENIX (03, 04) son versiones de acceso libre
  del mismo trabajo cuyo DOI se indica; la cita siempre debe llevar el DOI del editor.
- Esta carpeta no se compila ni se procesa: los PDF se conservan tal como se descargaron.
