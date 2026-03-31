from odoo import fields, models
from odoo.exceptions import UserError


class UpdateLoyaltyPoints(models.TransientModel):
    _name = 'partner.loyalty.update.points'
    _description = 'Actualizar Puntos de Fidelidad'

    points_to_add = fields.Integer(
        string='Puntos a Agregar',
        required=True,
    )

    def action_apply(self):
        active_ids = self.env.context.get('active_ids', [])
        if not active_ids:
            raise UserError('No se han seleccionado contactos.')
        partners = self.env['res.partner'].browse(active_ids)
        for partner in partners:
            new_points = max(partner.loyalty_points + self.points_to_add, 0)
            partner.write({'loyalty_points': new_points})
        return {'type': 'ir.actions.act_window_close'}
