# Fragmentos que usa la sección de causas raíz

Parte del informe: **Causas raíz y diagrama de Ishikawa** (MENDOZA BERMELLO ANGELLO AGUSTIN).

Estos son **solo los fragmentos que aparecen citados** en `informe/secciones/02_causas.tex`, en
el orden del texto. Cada cita es literal y lleva la página que se ve en el PDF.

- En **Cook** y **Gunawi** la página del visor coincide con el folio impreso.
- En **Yuan** y **Xu** hay que restar 1 y 2 páginas respectivamente: la 250 y la 619 son los
  folios de las memorias USENIX.
- En **Basiri** no hay folio impreso (es el manuscrito aceptado), por eso la cita va sin página.
- El **informe de Fastly** es una página web: se cita con su URL y no se subraya ningún PDF.

Para subrayar, en `notas/extractos/` están solo las páginas que hacen falta:

| Extracto | Páginas | Sirve para |
|---|---|---|
| `01_cook_paginas-1-2.pdf` | 1 y 2 | fragmentos 1 y 2 |
| `02_gunawi_paginas-5-6-8.pdf` | 5, 6 y 8 | fragmentos 3, 4 y 5 |
| `03_yuan_pagina-3.pdf` | 3 (folio 250) | fragmento 6 |
| `04_xu_pagina-2.pdf` | 2 (folio 619) | fragmentos 7 y 8 |
| `05_basiri_pagina-1.pdf` | 1 | fragmento 9 |

---

## 1. Cook, pág. 2, punto 7 — párrafo 1

> "Post-accident attribution accident to a 'root cause' is fundamentally wrong. Because overt
> failure requires multiple faults, there is no isolated 'cause' of an accident. There are
> multiple contributors to accidents. Each of these is necessary insufficient in itself to
> create an accident. Only jointly are these causes sufficient to create an accident."

Es la base de «ningún fallo tiene una sola causa». **Erratas del original:** «attribution
accident to» y «is necessary insufficient» (falta «is»). Si se transcribe literal, va `[sic]`.

## 2. Cook, pág. 1, punto 3 — párrafo 5

> "Catastrophe requires multiple failures – single point failures are not enough.. Overt
> catastrophic failure occurs when small, apparently innocuous failures join to create
> opportunity for a systemic accident. Each of these small failures is necessary to cause
> catastrophe but only the combination is sufficient to permit failure."

Sostiene que los seis grupos del diagrama no están aislados. El doble punto final está en el
original.

## 3. Gunawi, pág. 5, §4.1 — párrafo 2

> "The developers had tested the software upgrades, but when the updates were pushed to the
> full ecosystem, they caused new failures/anomalies that were undetected in the offline
> testing."

Es el respaldo del error que pasó las pruebas del 12 de mayo y apareció solo con la
configuración real.

## 4. Gunawi, pág. 6, §4.3 — párrafo 3

> "Cascading bugs happen because the same software logic runs in multiple redundant
> supposedly-independent nodes."

Explica por qué un solo error afectó a toda la red al mismo tiempo.

## 5. Gunawi, pág. 8, §5.3 — párrafo 4

> "In reality, bugs also appear in monitoring systems and error-checking code. For example, a
> monitoring bug failed to detect a specific case of memory leaks."

Respalda que el sistema de vigilancia también puede fallar. Ojo: Fastly **sí** detectó en un
minuto; lo que tardó fue el diagnóstico.

## 6. Yuan, pág. 3 (folio 250) — párrafo 2

> "in 58% of the catastrophic failures, the underlying faults could easily have been detected
> through simple testing of error handling code."

Es la cifra que respalda que una prueba sencilla habría encontrado el error.

## 7. Xu, pág. 2 (folio 619) — párrafo 3

> "Moreover, very often, the same configuration error is deployed onto thousands of nodes and
> resides in persistent files on each node, making it hard to tolerate by redundancy or server
> rebooting."

Explica por qué tener copias no sirve y por qué reiniciar no arregla el problema: el error está
guardado en cada servidor.

## 8. Xu, pág. 2 (folio 619) — tabla de riesgos, fila 1

> "One root cause is that many (14.0%–93.2%) of these configurations do not have any special
> code for checking the correctness of their settings at the system's initialization time."

Respalda la medida de validar la configuración al inicio y no cuando ya está en producción.

## 9. Basiri, pág. 1 — tabla de riesgos, fila 2

> "we also run Failure Injection Testing (FIT) exercises where we cause requests between
> Netflix services to fail and verify that the system degrades gracefully."

Respalda provocar el fallo a propósito para comprobar que solo se cae una parte y no todo.

---

## Lo que se cita sin PDF (informe de Fastly)

Estas frases del informe oficial se usan en los párrafos 1, 4 y 5, pero no hay PDF que subrayar:

- «85 % de la red devolvió errores» y «95 % restablecido en 49 minutos».
- El despliegue del 12 de mayo y los 27 días hasta que el error se activó.
- La línea de tiempo 09:47 → 10:27.
- «Even though there were specific conditions that triggered this outage, we should have
  anticipated it».

## Regla que cumple el texto

Cada párrafo tiene dos citas de fuentes distintas, y ningún par se repite:

| Párrafo | Citas |
|---|---|
| 1 | `fastly2021` + Cook p. 2 |
| 2 | Gunawi p. 5 + Yuan p. 250 |
| 3 | Xu p. 619 + Gunawi p. 6 |
| 4 | `fastly2021` + Gunawi p. 8 |
| 5 | Cook p. 1 + `fastly2021` |

La nota de transparencia sobre el uso de IA no lleva citas a propósito: no afirma hechos del
caso.
