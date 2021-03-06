from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
			{
				"label": _("Datastore"),
				"items": [
					{
						"type": "doctype",
						"name": "Movies"
					},
					{
						"type": "doctype",
						"name": "Short Format Content"
					},
					{
						"type": "doctype",
						"name": "Purchase"
					},
					{
						"type": "doctype",
						"name": "Sales"
					}
				]
			},
			{
				"label": _("Personnel"),
				"items": [
					{
						"type": "doctype",
						"name": "Director"
					},
					{
						"type": "doctype",
						"name": "Producer"
					},
					{
						"type": "doctype",
						"name": "Production Banner"
					},
					{
						"type": "doctype",
						"name": "Traders"
					},
					{
						"type": "doctype",
						"name": "Stars"
					},
					{
						"type": "doctype",
						"name": "Buyer"
					}
				]
			},
			{
				"label": _("Metadata"),
				"items": [
					{
						"type": "doctype",
						"name": "Countries"
					},
					{
						"type": "doctype",
						"name": "Languages"
					},
					{
						"type": "doctype",
						"name": "Genre"
					},
					{
						"type": "doctype",
						"name": "Platforms"
					},
					{
						"type": "doctype",
						"name": "Rights"
					}
				]
			}
        ]