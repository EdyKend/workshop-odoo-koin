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
 	'data':['views/idea_view.xml'],
    'demo': [], 	# demo data (for unit tests)
    'installable': True,
    'auto_install': False, 		# indikasi install, saat buat database baru
}