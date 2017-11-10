# -*- coding: utf-8 -*-
{
    'name': "ODOO Shopify",

    'summary': """
        Connect Shopify with ODOO""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Techloyce",
    'website': "http://www.techloyce.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],
    'images': [
        'static/description/icon.png',
    ],
    'price': 900,
    'currency': 'EUR',
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/customuser.xml',
        'views/shopify_import_export_wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}