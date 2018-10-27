# -*- coding: utf-8 -*-
# Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _, msgprint
from frappe.model.document import Document
import frappe.utils.data as utils

class Movies(Document):
	def validate(self):
		if not self.final_title and not self.temp_title:
			frappe.throw(_("Temporary title or Final title is mandatory."))

		title = self.final_title or self.temp_title
		name = ""
		if self.date_of_release:
			name = title + " ("+str(self.date_of_release)[:4]+")"
		else:
			name = title + " (YTR)"
		self.title = name




