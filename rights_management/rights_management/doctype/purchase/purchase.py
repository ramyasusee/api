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
			if self.ignore_link_agreement == 1:
				msgprint(_('Intermediary Sale is Applicable, and Link Agreement is ignored. Uncheck <b>Awaiting Link Agreement</b> to upload a new agreement.'))
			elif not self.link_agreement:
				frappe.throw(_('Intermediary Sale is Applicable. Link agreement is mandatory. If you don\'t have it, consider enabling <b>Awaiting Link Agreement</b> to prevent this check.'))
		if self.release_date and self.expiry == "":
			frappe.throw(_('Release date is specified as '+str(self.release_date)+'. Please choose an expiry term.'))

		if self.is_intermediary_sale_applicable():
			if not self.intermediatory_expiry_date:
				frappe.throw(_('Intermediary Sale is Applicable, but Intermediary Expiry Date is not provided.'))
			if not self.intermediatory_date_of_agreement:
				frappe.throw(_('Intermediary Sale is Applicable, but Intermediary Date of Agreement is not provided.'))
			if self.intermediatory_expiry_date <= self.intermediatory_date_of_agreement:
				frappe.throw(_('Intermediary Expiry Date cannot be equal to or before the Intermediary Date of Agreement.'))
			if self.intermediatory_expiry_date <= self.expiry_date:
				frappe.throw(_('Intermediary Expiry Date ('+str(self.intermediatory_expiry_date)+') is earlier than the Purchased License Date ('+str(self.expiry_date)+')'))
			self.validate_rights()
		else:
			subset_rights = list()
			for row in self.purchased_rights:
				if row.right in subset_rights:
					frappe.throw(_("Duplicate entry: <b>"+row.right+"</b> in Purchased Rights table."))
				subset_rights.append(row.right)


	def on_update(self):
		self.autoname()

	def is_intermediary_sale_applicable(self):
		return self.production_banner != self.seller

	def validate_rights(self):
		superset = self.primary_rights
		subset = self.purchased_rights

		superset_rights = list()
		subset_rights = list()
		for row in superset:
			if row.right in superset_rights:
				frappe.throw(_("Duplicate entry: <b>"+row.right+"</b> in Primary Rights table."))
			superset_rights.append(row.right)

		for row in subset:
			if row.right in subset_rights:
				frappe.throw(_("Duplicate entry: <b>"+row.right+"</b> in Purchased Rights table."))
			subset_rights.append(row.right)

		#This checks if any right not available from the primary seller is being sold to the buyer.
		if not set(superset_rights) >= set(subset_rights):
			error = "<p>The following rights are not available from the Primary Seller:</p><ol>"
			missing_right = set(subset_rights) - set(superset_rights)
			for right in list(missing_right):
				error = error + "<li>"+right+"</li>"
			error = error + "</ol><p class=\"text-danger\">Please fix all the errors to save the document.</p>"
			frappe.throw(_(error))
		else:
			primary = list()
			for row in superset:
				cset = list()
				cset_doc = frappe.get_doc('Country Set', row.c_set)
				for country in cset_doc.title.split(','):
					cset.append(country.strip())
				primary.append({
					"right": row.right,
					"type": row.type,
					"cset": set(cset)
				})

			secondary = list()
			for row in subset:
				cset = list()
				cset_doc = frappe.get_doc('Country Set', row.c_set)
				for country in cset_doc.title.split(','):
					cset.append(country.strip())
				secondary.append({
					"right": row.right,
					"type": row.type,
					"cset": set(cset)
				})

			error = ''
			for sec in secondary:
				for pr in primary:
					if sec.get('right') == pr.get('right'):
						if sec.get('type') == "Exclusion" and pr.get('type') == "Inclusion":
							error = error + "<p>In <b>"+sec.get('right')+"</b> right, you cannot purchase an <b>Exclusion</b> when the Primary Seller only has <b>Inclusion</b> with these countries:</p><ol>"
							included_counties = pr.get('cset')
							for country in list(included_counties):
								error = error + "<li>"+country+"</li>"
							error = error + "</ol>"
						elif pr.get('type') == sec.get('type') and sec.get('type') == "Inclusion":
							if not pr.get('cset') >= sec.get('cset'):
								error = error + "<p>In <b>"+sec.get('right')+"</b> right, the following countries are not available from the Primary Seller:</p><ol>"
								missing_countries = sec.get('cset') - pr.get('cset')
								for country in list(missing_countries):
									error = error + "<li>"+country+"</li>"
								error = error + "</ol>"
						elif pr.get('type') == sec.get('type') and sec.get('type') == "Exclusion":
							if not sec.get('cset') >= pr.get('cset'):
								error = error + "<p>In <b>"+sec.get('right')+"</b> right, the following countries must be excluded since it's already excluded by Primary Seller:</p><ol>"
								missing_countries = pr.get('cset') - sec.get('cset')
								for country in list(missing_countries):
									error = error + "<li>"+country+"</li>"
								error = error + "</ol>"
						elif pr.get('type') == "Exclusion" and sec.get('type') == "Inclusion":
							unavailable_countries = list(pr.get('cset') & sec.get('cset'))
							if len(unavailable_countries) > 0:
								error = error + "<p>In <b>"+sec.get('right')+"</b> right, the following countries are already excluded by the Primary Seller and you cannot include them:</p><ol>"
								for country in unavailable_countries:
									error = error + "<li>"+country+"</li>"
								error = error + "</ol>"
			if error != '':
				error = error + "<p class=\"text-danger\">Please fix all the errors to save the document.</p>"
				frappe.throw(_(error))






