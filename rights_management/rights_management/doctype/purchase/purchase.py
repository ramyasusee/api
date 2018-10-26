# -*- coding: utf-8 -*-
# Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Purchase(Document):
	def autoname(self):
		self.current_title = self.title + " - " +str(self.agreement_date)

	def validate(self):
		if not self.movie and not self.sfc:
			frappe.throw(_(self.type + " is mandatory"))
