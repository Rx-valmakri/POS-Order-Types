# -*- coding: utf-8 -*-
from odoo import models, fields


class PosOrder(models.Model):
    _inherit = 'pos.order'

    order_type_id = fields.Many2one('pos.order.types',
                                    string="Order Type", readonly=True)

    def _order_fields(self, ui_order):
        result = super()._order_fields(ui_order)
        print("SSS", ui_order.get('selected_order_Type_id'))
        result['order_type_id'] = ui_order.get('selected_order_Type_id')
        return result
