# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Idea Website',
    'category': 'Website',
    'website': 'https://www.edaptec.com/idea',
    'summary': 'Publish Your Idea',
    'version': '1.0',
    'description': """
Edaptec - Idea Website
======================
""",
    'depends': [
        'website',
        'idea',
    ],
    'demo': [],
    'data': [
        'views/website_idea_template.xml',
        'views/website_vote_template.xml',
    ],
    'qweb': [],
    'installable': True,
}
