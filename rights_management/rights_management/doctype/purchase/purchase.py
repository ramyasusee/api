# -*- coding: utf-8 -*-
# Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _, msgprint

class Purchase(Document):
	def autoname(self):
		self.current_title = self.title + " - " +str(self.agreement_date)

	def validate(self):
		if not self.movie and not self.sfc:
			frappe.throw(_(self.type + " is mandatory"))
		if self.is_intermediary_sale_applicable():
			if not self.link_agreement:
				frappe.throw(_('Intermediary Sale is Applicable. Link agreement is mandatory. If you don\'t have it, consider enabling <b>Ignore Link Agreement</b> to prevent this check.'))
			if self.ignore_link_agreement == 0:
				msgprint(_('Intermediary Sale is Applicable, and Link Agreement is ignored. Uncheck <b>Ignore Link Agreement</b> to upload a new agreement.'))
		if self.release_date and self.expiry == "":
			frappe.throw(_('Release date is specified as '+str(self.release_date)+'. Please choose an expiry term.'))
		if not self.date_of_release:
			self.yet_to_be_released = 1
		else:
			self.yet_to_be_released = 0

	def is_intermediary_sale_applicable(self):
		return self.production_banner != self.seller
