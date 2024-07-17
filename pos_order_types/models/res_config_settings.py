# -*- coding: utf-8 -*-
from ast import literal_eval

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_order_type = fields.Boolean(string='Enable Order Types',
                                       config_parameter='pos_order_types.is_order_type',
                                       help='Check this field for enabling Pos Order Types')
    pos_order_type_ids = fields.Many2many('pos.order.types')

    def set_values(self):
        res = super().set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'many2many.pos_order_type_ids', self.pos_order_type_ids.ids)
        return res

    @api.model
    def get_values(self):
        res = super().get_values()

        with_user = self.env['ir.config_parameter'].sudo()
        com_orders = with_user.get_param('many2many.pos_order_type_ids')
        res.update(
           pos_order_type_ids=[
            (6, 0, literal_eval(com_orders))] if com_orders else False, )
        return res
