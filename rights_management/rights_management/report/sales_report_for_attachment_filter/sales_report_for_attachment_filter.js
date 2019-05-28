// Copyright (c) 2016, Aftertutor Ventures Pvt Ltd and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Sales Report For Attachment Filter"] = {
	"filters": [
		{
			"fieldname": "sales_agreement_attachment",
			"label": __("Sales Agreement"),
			"fieldtype": "Select",
			"options": ['', 'True', 'False'],
			'default': ''
		},
		{
			"fieldname": "sales_invoice_attachment",
			"label": __("Sales Invoice"),
			"fieldtype": "Select",
			"options": ['', 'True', 'False'],
			'default': ''
		}

	]
}
