# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'CRM Qualifications',
    'version': '1.0',
    'sequence': 170,
    'category': 'Extra tools',
    'summary': '',
    'description': "",
    'author': 'El Mahdi ICHOU',
    'website': '',
    'depends': ['crm','website'],
    'data': [
        'views/leads_views.xml',
        'wizard/create_lead_view.xml',
        'views/leads_template.xml',
        'report/o_lead_actions_report_templates.xml',
        'report/o_lead_actions_report.xml',

    ],
    'qweb': [
         'static/src/xml/lead_icon.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
