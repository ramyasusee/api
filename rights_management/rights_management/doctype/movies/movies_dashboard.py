from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'heatmap': True,
		# 'heatmap_message': _('This is based on the attendance of this Employee'),
		'fieldname': 'movie',
		'transactions': [
			{
				'label': _('Purchase Documents'),
				'items': ['Purchase']
			},
			{
				'label': _('Sales Documents'),
				'items': ['Sales']
			},
		]
	}