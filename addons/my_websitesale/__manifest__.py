{
    'name': 'Custom website-sales',
    'version': '1.0',
    'summary': 'Custom module',
    'sequence': 10,
    'description': """Custom""",
    'category': 'Productivity',
    'website': '',
    'depends': [
        'base', 'website', 'website_sale', 'web'
    ],
    'data': [
        'views/assets.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
