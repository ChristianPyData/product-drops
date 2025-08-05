#  Alerta inteligente de caídas en ventas semanales

Este pipeline automatizado detecta caídas significativas en las ventas semanales y envía alertas por correo o Telegram cuando superan un umbral definido. Pensado para pymes, equipos de ventas y retail que necesitan reaccionar rápido sin revisar reportes manualmente.

##  ¿Qué hace?
- Calcula el total de ventas semanales desde un archivo Excel o fuente conectada.
- Compara con la semana anterior.
- Si hay una caída mayor al umbral, dispara una alerta automática.
- Incluye información clave: % de caída, productos/vendedores afectados, y recomendación de acción.

##  Stack utilizado
- **n8n** para la automatización y envío de alertas.
- **Pandas** para procesar los datos.
- **Excel** como input de ventas (puede adaptarse a CSV o DB).
- **Power BI** para visualizar el histórico y entender la tendencia.

##  Impacto
Reduce el tiempo de reacción ante problemas comerciales. El jefe no tiene que revisar reportes: las alertas llegan solas.

##  Ideal para
Pymes, equipos comerciales, distribuidores y retail.


** Licencia:** MIT  
**📬 Contacto:**   
** Autor:** Cristian Garcia
