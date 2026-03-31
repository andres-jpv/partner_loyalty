from odoo import api, fields, models

RANK_MAP = {
    'Bronce': 'bronze',
    'Plata': 'silver',
    'Oro': 'gold',
    'Platino': 'platinum',
}


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

    def _update_loyalty_level(self):
        ranks = self.env['partner.loyalty.rank'].search([], order='min_points asc')
        for partner in self:
            for rank in ranks:
                if rank.min_points <= partner.loyalty_points <= rank.max_points:
                    level = RANK_MAP.get(rank.name, 'bronze')
                    if partner.loyalty_level != level:
                        partner.loyalty_level = level
                    break

    def write(self, vals):
        res = super().write(vals)
        if 'loyalty_points' in vals:
            self._update_loyalty_level()
        return res

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records.filtered(lambda r: r.loyalty_points)._update_loyalty_level()
        return records
