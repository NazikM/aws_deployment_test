{
    'name': 'Hospital managment',
    'version': '1.0',
    'summary': 'Hospital managment software',
    'sequence': 10,
    'description': """Hospital managment software""",
    'category': 'Productivity',
    'website': '',
    'depends': [
        'sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
