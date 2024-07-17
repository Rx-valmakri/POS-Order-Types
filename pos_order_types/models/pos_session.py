# -*- coding: utf-8 -*-
from odoo import models


class PosSessions(models.Model):
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        res = super()._pos_ui_models_to_load()
        res.append('pos.order.types')
        return res

    def _loader_params_pos_order_types(self):
        return {
            'search_params': {
                'domain': [],
                'fields': ['name', 'is_pos_settings_enabled'],
            },
        }

    def _get_pos_ui_pos_order_types(self, params):
        pos_order_types_fields = self.env['pos.order.types'].search_read(**params['search_params'])
        pos_settings_fields = self.env['ir.config_parameter'].sudo().get_param('many2many.pos_order_type_ids')
        return pos_order_types_fields, pos_settings_fields



