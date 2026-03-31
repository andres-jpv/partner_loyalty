# Partner Loyalty - Odoo 19

Módulo de fidelidad para la gestión de clientes en Odoo 19. Permite clasificar contactos por nivel de fidelidad, gestionar puntos, realizar actualizaciones masivas y generar fichas de fidelidad en PDF.

## Características

- **Niveles de fidelidad**: Bronce, Plata, Oro y Platino para cada contacto.
- **Puntos de fidelidad**: Acumulación de puntos por cliente.
- **Menú Clientes VIP**: Vista filtrada que muestra solo clientes Oro y Platino.
- **Wizard de actualización masiva**: Permite sumar puntos a múltiples contactos seleccionados desde la vista lista.
- **Reporte PDF**: Ficha de Fidelidad imprimible desde la vista formulario del contacto.

## Instalación

1. Copiar la carpeta `partner_loyalty` dentro del directorio de addons personalizados de tu instancia de Odoo 19.
2. Asegurarse de que la ruta de addons personalizados esté configurada en el archivo `odoo.conf`:
   ```
   addons_path = /ruta/a/odoo/addons,/ruta/a/custom-addons
   ```
3. Reiniciar el servidor de Odoo.
4. Ir a **Aplicaciones**, buscar "Partner Loyalty" e instalar el módulo.

## Estructura del Módulo

```
partner_loyalty/
├── __init__.py
├── __manifest__.py
├── README.md
├── models/
│   ├── __init__.py
│   └── res_partner.py          # Herencia de res.partner con campos de fidelidad
├── wizard/
│   ├── __init__.py
│   ├── update_loyalty_points.py        # Modelo transitorio del wizard
│   └── update_loyalty_points_views.xml # Vista y acción del wizard
├── views/
│   └── res_partner_views.xml   # Vistas heredadas y menú Clientes VIP
├── report/
│   ├── loyalty_card_report.xml     # Acción del reporte PDF
│   └── loyalty_card_template.xml   # Plantilla QWeb del reporte
└── security/
    └── ir.model.access.csv     # Reglas de acceso
```

## Uso

### Pestaña Fidelidad
Abrir cualquier contacto y navegar a la pestaña **Fidelidad** para ver y editar el nivel y los puntos.

### Clientes VIP
En el menú principal de **Contactos**, hacer clic en **Clientes VIP** para ver solo los contactos con nivel Oro o Platino.

### Actualización Masiva de Puntos
1. Ir a la vista lista de Contactos.
2. Seleccionar los contactos deseados.
3. Ir a **Acción** > **Actualizar Puntos**.
4. Ingresar los puntos a agregar y hacer clic en **Aplicar**.

### Ficha de Fidelidad (PDF)
Desde la vista formulario de un contacto, ir a **Imprimir** > **Ficha de Fidelidad** para generar el PDF.

## Requisitos

- Odoo 19 (Community o Enterprise)
- Módulo **Contactos** (`contacts`) instalado

## Autor

Jordan Andres Pincay Vinces

## Licencia

LGPL-3
