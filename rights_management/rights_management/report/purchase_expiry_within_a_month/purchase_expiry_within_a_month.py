# Copyright (c) 2013, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import utils

def execute(filters=None):
	# utils.today() + 30
	# aMonthBeforeExpiry
	sqlQuery = "SELECT * from `tabPurchase` where expiry_date = "+expiry_date
	columns = ["test"]
	data = [today, todayy]
	# columns, data = [], []
	return ["Test"], data
