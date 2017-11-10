# -*- coding: utf-8 -*-
{
    'name': "ODOO Salesforce Connector",
    'version': '1.0',
    'category': 'Sales',
    'summary': 'ODOO Salesforce',
    'author': 'Techloyce',
    'website': 'http://www.techloyce.com',
    'depends': ['sale'],
    'price': 499,
    'currency': 'EUR', 

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
}