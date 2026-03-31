from odoo import fields, models


class LoyaltyRank(models.Model):
    _name = 'partner.loyalty.rank'
    _description = 'Rango de Fidelidad'
    _order = 'min_points asc'

    name = fields.Char(
        string='Nombre del Rango',
        required=True,
    )
    level_key = fields.Selection(
        selection=[
            ('bronze', 'Bronce'),
            ('silver', 'Plata'),
            ('gold', 'Oro'),
            ('platinum', 'Platino'),
        ],
        string='Nivel',
        required=True,
    )
    min_points = fields.Integer(
        string='Puntos Mínimos',
        required=True,
    )
    max_points = fields.Integer(
        string='Puntos Máximos',
        required=True,
    )
