# -*- coding: utf-8 -*-
# Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class ShortFormatContent(Document):
	def validate(self):
		if not self.final_title and not self.temp_title:
			frappe.throw(_("Temporary title or Final title is mandatory."+self.final_title))

		self.title = self.final_title or self.temp_title
		self.no_of_seasons = len(self.seasons_table)
		ep = 0
		for season in self.seasons_table:
			ep = ep + int(season.no_of_episodes)
		self.no_of_episodes = ep
