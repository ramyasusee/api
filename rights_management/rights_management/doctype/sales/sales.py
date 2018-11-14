# -*- coding: utf-8 -*-
# Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from frappe import _,msgprint

class Sales(Document):
	def validate(self):
		add_more = False
		items = 0
		error = ''
		if self.type_of_content == "Movies":
			file = self.movie
			if self.add_more_movies == 1:
				add_more = True
				items = self.movie_list
		elif self.type_of_content == "Short Format Content":
			file = self.sfc
			if self.add_more_sfc == 1:
				add_more = True
				items = self.sfc_list

		file_list = [file]
		if add_more:
			for row in items:
				if row.item in item_list:
					error += "<li> Duplicate Record: <b>"+file+" - "+row.title+"</b> is already in added. Please remove the duplicate from the table. </li>"
				file_list.append((row.item))
			if error != '':
				error = error + "<p class=\"text-danger\">Please fix all the errors to save the document.</p>"
				frappe.throw(_(error))
		for file in file_list:
			if self.type_of_content == "Movies":
				purchases = frappe.get_all("Purchase", filters={'type': 'Movies', 'movie': file}, fields=['name'])
			if self.type_of_content == "Short Format Content":
				purchases = frappe.get_all("Purchase", filters={'type': 'Short Format Content', 'sfc': file}, fields=['name'])
			for purchase in purchases:
				doc = frappe.get_doc("Purchase", purchase.name)
				validate_rights(doc.purchased_rights, self.platform_rights, doc.title)

def validate_rights(superset, subset, title):
	superset_rights = list()
	subset_rights = list()

	for row in superset:
		if row.right in superset_rights:
			frappe.throw(_("Duplicate entry: <b>"+row.right+"</b> in Primary Rights table on "+title)) #this is never likely to happen
		superset_rights.append(row.right)

	for row in subset:
		if row.right in subset_rights:
			frappe.throw(_("Duplicate entry: <b>"+row.right+"</b> in Selling Rights table."))
		subset_rights.append(row.right)

	#This checks if any right not available from the primary seller is being sold to the buyer.
	if not set(superset_rights) >= set(subset_rights):
		error = 'For <b>'+title+'</b>' +"<p>The following rights are not available with you, so you cannot sell them:</p><ol>"
		missing_right = set(subset_rights) - set(superset_rights)
		for right in list(missing_right):
			error = error + "<li>"+right+"</li>"
		error = error + "</ol><p class=\"text-danger\">Please fix all the errors to save the document.</p>"
		frappe.throw(_(error))
	else:
		primary = list()
		for row in superset:
			cset = list()
			for country in row.c_set.split(','):
				cset.append(country.strip())
			primary.append({
				"right": row.right,
				"type": row.type,
				"cset": set(cset)
			})

		secondary = list()
		for row in subset:
			cset = list()
			for country in row.c_set.split(','):
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
						error = error + "<p>In <b>"+sec.get('right')+"</b> right, you cannot sell an <b>Exclusion</b> when the you only have <b>Inclusion</b> with these countries:</p><ol>"
						included_counties = pr.get('cset')
						for country in list(included_counties):
							error = error + "<li>"+country+"</li>"
						error = error + "</ol>"
					elif pr.get('type') == sec.get('type') and sec.get('type') == "Inclusion":
						if not pr.get('cset') >= sec.get('cset'):
							error = error + "<p>In <b>"+sec.get('right')+"</b> right, the following countries are not available with you:</p><ol>"
							missing_countries = sec.get('cset') - pr.get('cset')
							for country in list(missing_countries):
								error = error + "<li>"+country+"</li>"
							error = error + "</ol>"
					elif pr.get('type') == sec.get('type') and sec.get('type') == "Exclusion":
						if not sec.get('cset') >= pr.get('cset'):
							error = error + "<p>In <b>"+sec.get('right')+"</b> right, the following countries must be excluded since it's already excluded by you:</p><ol>"
							missing_countries = pr.get('cset') - sec.get('cset')
							for country in list(missing_countries):
								error = error + "<li>"+country+"</li>"
							error = error + "</ol>"
					elif pr.get('type') == "Exclusion" and sec.get('type') == "Inclusion":
						unavailable_countries = list(pr.get('cset') & sec.get('cset'))
						if len(unavailable_countries) > 0:
							error = error + "<p>In <b>"+sec.get('right')+"</b> right, the following countries are already excluded by the you and you cannot include them in the sale:</p><ol>"
							for country in unavailable_countries:
								error = error + "<li>"+country+"</li>"
							error = error + "</ol>"
		if error != '':
			error = 'For <b>'+title+'</b>' +error + "<p class=\"text-danger\">Please fix all the errors to save the document.</p><hr>"
			frappe.throw(_(error))

