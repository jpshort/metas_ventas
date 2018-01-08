# -*- coding: utf-8 -*-
{
    'name': "metasventa",

    'summary': """
       Metas y objetivo de ventas por vendedores y/o por clientes """,

    'description': """
       Controlar las metas y objetivos anuales de los vendedores y/o
       clientes
    """,

    'author': "Pedro P Nunez Araujo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Ventas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/reports_view.xml',
        'security/security.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
