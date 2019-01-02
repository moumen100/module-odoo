# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
	'name' : 'module AYRADE',
	'version' : '1.1',
	'summary': '',
	'sequence': 2,
	'description': """
Exploitation des paneaux d'affichage
====================

	""",
	'author': 'AYRADE',
	'category': '',
	'website': 'https://www.ayrade.com',
	'images' : [],
	'depends' : ['base','product'],
	'data': ["views/enseignement.xml",
	"views/report.xml",
	"views/template.xml",
	"views/import.xml",
	"views/workflow.xml",
	"views/projects.xml"
	],
	'demo': [

	],
	
	'installable': True,
	'application': True,
	'auto_install': False,

}
