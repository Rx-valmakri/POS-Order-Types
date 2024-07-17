# -*- coding: utf-8 -*-
{
    'name': "POS Order Types",
    'summary': 'Pos Order Types',
    'description': 'Pos Order Types',
    'license': 'LGPL-3',
    'application': True,
    'depends': ['base', 'point_of_sale'],

    'data': [
        'security/ir.model.access.csv',

        'data/pos_order_types.xml',

        'views/res_config_settings_views.xml',
        'views/pos_order_types.xml',
        'views/pos_order_view.xml',
        'views/pos_order_types_menu.xml',
    ],
    'assets': {
         'point_of_sale._assets_pos': [
             'pos_order_types/static/src/xml/pos_order_types_button.xml',
             'pos_order_types/static/src/xml/pos_order_receipt.xml',
             'pos_order_types/static/src/js/pos_order_types.js',
             'pos_order_types/static/src/js/pos_order.js',
             'pos_order_types/static/src/js/pos_order_types_button.js',
          ],
    },
}
