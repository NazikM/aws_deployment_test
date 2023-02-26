{
    'name': 'CRM Customizations',
    'version': '1.0',
    'summary': 'CRM managment software',
    'sequence': 10,
    'description': """CRM managment software""",
    'category': 'Productivity',
    'website': '',
    'depends': [
        'crm'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_form.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
