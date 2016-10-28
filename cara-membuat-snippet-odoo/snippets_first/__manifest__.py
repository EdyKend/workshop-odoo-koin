# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'My First Snippet',
    'category': 'Website',
    'website': 'https://www.edaptec.com/idea',
    'summary': 'I like odoo snippet',
    'version': '1.0',
    'author': 'Edaptec',
    'description': """
Edaptec - My First Snippet
======================
""",
    'depends': [
        'website'
    ],
    'demo': [],
    'data': [
        'views/assets.xml',
        'views/snippets.xml',
        'views/snippets-2.xml'
    ],
    'qweb': [],
    'installable': True,
}
