# Exposición: causas raíz — 2 minutos

Guion para la parte de MENDOZA BERMELLO ANGELLO AGUSTIN en la exposición de FORM-AC-01.
Duración objetivo: 2 minutos (unas 280 palabras). El diagrama se proyecta desde el inicio.

---

## Guion

**(0:00–0:20) Qué voy a explicar.**
Mi parte responde una sola pregunta: por qué falló Fastly. La respuesta corta es que no hubo
una causa, hubo tres niveles que se acoplaron. El diagrama que ven es de elaboración propia,
hecho en draw.io, con 18 causas agrupadas en seis categorías.

**(0:20–0:55) La distinción que importa.**
El 12 de mayo Fastly desplegó software con un defecto. Ese defecto estuvo 27 días sin
activarse: era una bomba sin detonador. El 8 de junio, un cliente cambió su configuración; el
cambio era válido según las reglas del sistema, pero llevó al defecto a ejecutarse. Ese cambio
es el disparador, no la raíz. Si confundimos el disparador con la causa, la lección sería
«cuidado con los clientes», y la lección correcta es «nuestro código no tenía guarda para esa
combinación y nuestras pruebas no la cubrían».

**(0:55–1:25) Cómo se leen los colores.**
En naranja está el disparador: el cambio válido del cliente y la combinación no prevista de
parámetros. En rojo está la raíz técnica: el defecto sin guarda en el código de borde y la
falta de validación semántica, más las pruebas que no cubrieron ese caso. En azul están los
agravantes: el despliegue sin canario, el proceso que aborta en vez de degradarse, la
configuración idéntica en el 100 % de los POP, y 40 minutos para diagnosticar porque no había
correlación entre el cambio aplicado y la caída.

**(1:25–1:50) Por qué el diagrama tiene respaldo.**
No es una lluvia de ideas. Gunawi y otros revisaron 597 caídas de 32 servicios y encontraron
que las actualizaciones y los defectos de software están entre las causas más frecuentes, y
que la redundancia no basta si la cadena de recuperación falla. Basiri y otros explican por
qué un despliegue progresivo con impacto limitado habría contenido el fallo.

**(1:50–2:00) Cierre.**
De ahí salen nuestros tres riesgos: reglas de transición de estados que bloquean solicitudes,
un módulo que tumba toda la aplicación, y falta de trazabilidad para diagnosticar. Cada uno
tiene su prueba para TA-PFC-E1.

---

## Preguntas probables de los equipos evaluadores

**¿El cliente tuvo la culpa?**
No. El informe oficial dice que el cambio era válido según las reglas de Fastly; la falla es
del sistema que lo aceptó sin una guarda. Por eso el disparador está en naranja y no en rojo.

**¿Por qué Ishikawa y no un árbol de fallos?**
Ishikawa agrupa las causas por categorías, que es lo que pide la rúbrica. El árbol de fallos
sería más preciso para modelar la lógica «defecto Y configuración»; lo resolvimos marcando esa
conjunción con colores y con la explicación del encadenamiento.

**¿Cómo evitan que el diagrama sea una lista de deseos?**
Cada causa está atada a un hecho del informe: 27 días entre despliegue y activación, 40 minutos
hasta identificar la configuración, 85 % de la red con errores, 49 minutos hasta el 95 %
restablecido. Las causas que no tienen un hecho detrás no se incluyeron.
