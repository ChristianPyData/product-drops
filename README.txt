#  Alerta inteligente de caídas en ventas semanales

Este pipeline automatizado detecta caídas significativas en las ventas semanales y envía alertas por Telegram cuando superan un umbral del 30%. Pensado para pymes, equipos de ventas y retail que necesitan reaccionar rápido sin revisar reportes manualmente.

##  ¿Qué hace?
- Calcula el total de ventas semanales desde un archivo Excel o fuente conectada.
- Compara con la semana anterior.
- Si hay una caída mayor al umbral, dispara una alerta automática.
- Incluye información clave: % de caída y productos/vendedores afectados.

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
**📬 Contacto:** https://www.linkedin.com/public-profile/settings?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_self_edit_contact-info%3BdM7jAZ%2FvRDO5sj3sOk9v5w%3D%3D  
** Autor:** Cristian Garcia

