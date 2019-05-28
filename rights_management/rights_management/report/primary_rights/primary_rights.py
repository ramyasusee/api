# Copyright (c) 2013, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	sql_query = "SELECT purchase.name, purchase.type_of_purchase, purchase.main_agreement, purchase.title, purchase.movie, purchase.expires_in, purchase.seller, purchase.title_language, rights.right, rights.c_set, rights.exclusivity  from `tabPlatform Rights` rights, `tabPurchase` purchase  where rights.parentfield = 'primary_rights' and rights.parent = purchase.name"

	data = frappe.db.sql(sql_query)

	# if data[10] == 0:
	# 	data[10] = "False"
	# if data[10] == 1:
	# 	data[10] = "True"

	return ['Name', "Type Of Purchase", "Main Agreement", "Title", "Movie", "Expires In", "Seller", "Title Language", "Rights", "Country Sets", "Exclusivity"], data


# select purchase.name, purchase.type_of_purchase, purchase.main_agreement, purchase.title, purchase.movie, purchase.expires_in, purchase.seller, purchase.title_language from `tabPlatform Rights` rights, `tabPurchase` purchase  where rights.parentfield = 'primary_rights' and rights.parent = purchase.name;;

# select * from `tabPlatform Rights` rights, `tabPurchase` purchase  where rights.parentfield = 'primary_rights' and rights.parent = purchase.name;;