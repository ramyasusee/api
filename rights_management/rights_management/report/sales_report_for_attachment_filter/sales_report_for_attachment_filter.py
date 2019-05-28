# Copyright (c) 2013, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	sales_agreement_isAttached = filters.sales_agreement_attachment
	sales_invoice_isAttached = filters.sales_invoice_attachment

	sql_query = "SELECT movie, title, seller FROM `tabSales`"

	sales_agreement_query = ""
	sales_invoice_query = ""

	if sales_agreement_isAttached == 'True':
		sales_agreement_query = " WHERE `sales_agreement` IS NOT NULL"
	elif sales_agreement_isAttached == 'False':
		sales_agreement_query = " WHERE `sales_agreement` IS NULL "

	if sales_agreement_query != "":
		if (sales_invoice_isAttached) == 'True':
			sales_invoice_query = " AND `sales_invoices` IS NOT NULL"
		elif (sales_invoice_isAttached) == 'False':
			sales_invoice_query = " AND `sales_invoices` IS NULL"
	else:
		if (sales_invoice_isAttached) == 'True':
			sales_invoice_query = " WHERE `sales_invoices` IS NOT NULL"
		elif (sales_invoice_isAttached) == 'False':
			sales_invoice_query = " WHERE `sales_invoices` IS NULL"

	sql_query = sql_query + sales_agreement_query + sales_invoice_query

	lab_cert_query = frappe.db.sql(sql_query)

	data = lab_cert_query
	return ["movie", "title", "seller"], data
