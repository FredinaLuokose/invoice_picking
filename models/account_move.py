from odoo import models,api
class AccountMove(models.Model):
    inherit = 'account.move'

    @api.model
    def action_picking(self):
        for invoice in self:
            if invoice.state == 'posted':
                picking_vals ={
                    'orgin': invoice.name,
                    'type': 'direct',
                    'partner_id':invoice.partner_id.id,
                    'location_dest_id': 1,
                    'move_lines' : [],
                }
                picking = self.env['stock.picking'].create(picking_vals)
                return picking
