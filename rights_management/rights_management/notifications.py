# -*- coding: utf-8 -*-
# Copyright (c) 2018, Aftertutor Ventures Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import frappe.utils.data as utils
from datetime import datetime, time, timedelta
import re
import sys
from frappe import utils

def get_config():
	return {
		"for_doctype": {
			"Sales":
			{
				"license_ending_date": ["between", [utils.today(), utils.dateutils.parse_date(utils.add_days(utils.now(), 30))]]
			}
		}
	}

def update_purchases():
	purchases = frappe.get_all('Purchase')
	for purchase in purchases:
		try:
			doc = frappe.get_doc('Purchase', purchase)
			doc.autoname()
			#print('Updating '+doc.name)
			doc.save()
		except Exception as e:
			print('Error in '+doc.name+': '+str(e))
			print('-----------------------------------------------------------------------------------')

# def expiring_licenses():
# 	data = frappe.get_list("Sales")
