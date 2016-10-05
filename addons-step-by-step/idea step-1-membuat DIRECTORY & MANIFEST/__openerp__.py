{
    'name': 'Idea',
	'version': '1.0',
	'author': 'Edaptec',
    'summary': 'Modul tentang ide',
	'description': """
Idea - Modul pertama Saya
=========================
Fitur
-------
* Input ide
* Approve ide
* Vote ide
""",
 	'category': 'Latihan',
 	'website': 'https://www.edaptec.com',
 	'depends': ['base'], 	# list of dependencies, conditioning startup order
 	'data':[ 					# data files to load at module install
 		'security/groups.xml', 	# always load groups first!
 		'security/ir.model.access.csv', # load access rights after groups
 		'view/views.xml',
 		'wizard/wizard.xml',
 		'report/report.xml',
    ],
    'demo': ['demo/demo.xml'], 	# demo data (for unit tests)
    'installable': True,
    'auto_install': False, 		# indikasi install, saat buat database baru
}