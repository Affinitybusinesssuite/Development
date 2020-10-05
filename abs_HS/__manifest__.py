# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'ABS Import',
    'version': '13.0.1.1.2',
    'category': 'Purchase',
    'summary': 'Module for Item HS Code and Expenses',
    'sequence': '4',
    'author': 'Affinity Business Suite',
    'maintainer': 'ABS',
    'depends': ['stock', 'purchase'],
    'demo': [],
    'data': [
        'Expense.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.gif'],
}
