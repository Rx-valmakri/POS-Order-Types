# -*- coding: utf-8 -*-
from ast import literal_eval

from odoo import models, fields, Command


class PosOrderTypes(models.Model):
    _name = "pos.order.types"
    _description = "Pos Order Types"

    name = fields.Char(string="Order Type", required=True)
    is_pos_settings_enabled = fields.Boolean(compute="compute_is_pos_settings_enabled")

    def compute_is_pos_settings_enabled(self):
        enable_or_not = self.env['ir.config_parameter'].sudo().get_param('pos_order_types.is_order_type')
        if enable_or_not:
            self.is_pos_settings_enabled = True
        else:
            self.is_pos_settings_enabled = False

