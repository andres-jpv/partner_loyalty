{
    'name': 'Partner Loyalty',
    'version': '19.0.1.0.0',
    'summary': 'Sistema de fidelidad para contactos',
    'description': """
        Módulo de fidelidad para clasificar contactos por nivel (Bronce, Plata, Oro, Platino),
        gestionar puntos de fidelidad, actualizar puntos masivamente mediante un wizard
        y generar fichas de fidelidad en PDF.
    """,
    'author': 'Jordan Andres Pincay Vinces',
    'category': 'Sales',
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/update_loyalty_points_views.xml',
        'views/res_partner_views.xml',
        'views/loyalty_rank_views.xml',
        'report/loyalty_card_report.xml',
        'report/loyalty_card_template.xml',
        'data/loyalty_rank_data.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
