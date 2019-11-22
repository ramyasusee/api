// Copyright (c) 2016, Aftertutor Ventures Pvt Ltd and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Purchase Report Attachment Filter"] = {
	"filters": [
		{
			"fieldname": "lab_certificate_attachment",
			"label": __("Lab Certificate"),
			"fieldtype": "Select",
			"options": ['', 'Yes', 'No'],
			'default': ''
		},
		{
			"fieldname": "main_agreement_attachment",
			"label": __("Main Agreement"),
			"fieldtype": "Select",
			"options": ['', 'Yes', 'No'],
			'default': ''
		},
		{
			"fieldname": "censor_certificate_attachment",
			"label": __("Censor Certificate"),
			"fieldtype": "Select",
			"options": ['', 'Yes', 'No'],
			'default': ''
		},
		{
			"fieldname": "real_image_letter_attachment",
			"label": __("Real Image Letter"),
			"fieldtype": "Select",
			"options": ['', 'Yes', 'No'],
			'default': ''
		}
	]
}
