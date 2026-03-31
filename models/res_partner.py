from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    loyalty_level = fields.Selection(
        selection=[
            ('bronze', 'Bronce'),
            ('silver', 'Plata'),
            ('gold', 'Oro'),
            ('platinum', 'Platino'),
        ],
        string='Nivel de Fidelidad',
        default='bronze',
    )
    loyalty_points = fields.Integer(
        string='Puntos de Fidelidad',
        default=0,
    )
