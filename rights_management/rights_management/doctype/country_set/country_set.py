# -*- coding: utf-8 -*-
# Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CountrySet(Document):
	def autoname(self):
		l = [row.country for row in self.country_table]
		self.name = ', '.join(l)
