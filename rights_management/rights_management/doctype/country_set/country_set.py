# -*- coding: utf-8 -*-
# Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import frappe.model.rename_doc as rd

class CountrySet(Document):
	def validate(self):
		l = [row.country for row in self.country_table]
		self.title = ', '.join(l)

def add_world():
	world = frappe.new_doc('Country Set')
	world.title = 'Entire World'
	cs = frappe.get_all('Countries')
	for c in cs:
		world.append('country_table', {'country': c.name})
		print('Adding: '+c.name)
	world.save()
