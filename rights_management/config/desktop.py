# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Rights Management",
			"color": "#4B3F72",
			"icon": "fa fa-film",
			"type": "module",
			"label": _("Rights Management")
		},
		{
			"module_name": "Movies",
			"_doctype": "Movies",
			"color": "#A71D31",
			"icon": "fa fa-video-camera",
			"type": "link",
			"link": "List/Movies/List",
		},
		{
			"module_name": "Short Format Content",
			"_doctype": "Short Format Content",
			"color": "#C45BAA",
			"icon": "fa fa-file-video-o",
			"type": "link",
			"link": "List/Short Format Content/List",
		},
		{
			"module_name": "Purchase",
			"_doctype": "Purchase",
			"color": "#149911",
			"icon": "fa fa-file-text-o",
			"type": "link",
			"link": "List/Purchase/List",
		},
		{
			"module_name": "Sales",
			"_doctype": "Sales",
			"color": "#2364AA",
			"icon": "fa fa-money",
			"type": "link",
			"link": "List/Sales/List",
		},
		{
			"module_name": "Director",
			"_doctype": "Director",
			"color": "#3DA5D9",
			"icon": "fa fa-address-card",
			"type": "link",
			"link": "List/Director/List",
		},
		{
			"module_name": "Producer",
			"_doctype": "Producer",
			"color": "#73BFB8",
			"icon": "fa fa-briefcase",
			"type": "link",
			"link": "List/Producer/List",
		},
		{
			"module_name": "Production Banner",
			"_doctype": "Production Banner",
			"color": "#FEC601",
			"icon": "fa fa-shield",
			"type": "link",
			"link": "List/Production Banner/List",
		},
		{
			"module_name": "Traders",
			"_doctype": "Traders",
			"color": "#EA7317",
			"icon": "fa fa-users",
			"type": "link",
			"link": "List/Traders/List",
		},
		{
			"module_name": "Stars",
			"_doctype": "Stars",
			"color": "#783F8E",
			"icon": "fa fa-user-secret",
			"type": "link",
			"link": "List/Stars/List",
		},
		{
			"module_name": "Countries",
			"_doctype": "Countries",
			"color": "#DA627D",
			"icon": "fa fa-flag",
			"type": "link",
			"link": "List/Countries/List",
		},
		{
			"module_name": "Languages",
			"_doctype": "Languages",
			"color": "#F7CE5B",
			"icon": "fa fa-globe",
			"type": "link",
			"link": "List/Languages/List",
		},
		{
			"module_name": "Genre",
			"_doctype": "Genre",
			"color": "#E8AA14",
			"icon": "fa fa-tags",
			"type": "link",
			"link": "List/Genre/List",
		},
		{
			"module_name": "Platforms",
			"_doctype": "Platforms",
			"color": "#FF5714",
			"icon": "fa fa-certificate",
			"type": "link",
			"link": "List/Platforms/List",
		}
	]
