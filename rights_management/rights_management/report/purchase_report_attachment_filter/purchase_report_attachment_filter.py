# Copyright (c) 2013, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 
from frappe.utils import today,getdate, cint, add_months, date_diff, add_days, nowdate, \
    get_datetime_str, cstr, get_datetime, time_diff, time_diff_in_seconds

def execute(filters=None):
	lab_certificate_isAttached = filters.lab_certificate_attachment
	main_agreement_isAttached = filters.main_agreement_attachment
	censor_certificate_isAttached = filters.censor_certificate_attachment
	real_image_letter_isAttached = filters.real_image_letter_attachment

	sql_query = "SELECT movie, title, name, buyer, release_date FROM `tabPurchase`"

	lab_certificate_query = ""
	main_agreement_query = ""
	censor_certificate_query = ""
	real_image_letter_query = ""

	if lab_certificate_isAttached == 'Yes':
		lab_certificate_query = " WHERE `lab_certificate` IS NOT NULL"
	elif lab_certificate_isAttached == 'No':
		lab_certificate_query = " WHERE `lab_certificate` IS NULL "

	if lab_certificate_query != "":
		if (main_agreement_isAttached) == 'Yes':
			main_agreement_query = " AND `main_agreement` IS NOT NULL"
		elif (main_agreement_isAttached) == 'No':
			main_agreement_query = " AND `main_agreement` IS NULL"
	else:
		if (main_agreement_isAttached) == 'Yes':
			main_agreement_query = " WHERE `main_agreement` IS NOT NULL"
		elif (main_agreement_isAttached) == 'No':
			main_agreement_query = " WHERE `main_agreement` IS NULL"

	# if lab_certificate_query != "" and main_agreement_query != "":
	# 	if censor_certificate_isAttached == 'True':
	# 		censor_certificate_query = " WHERE `censor_certificate` IS NOT NULL"
	# 	elif censor_certificate_isAttached == 'False':
	# 		censor_certificate_query = " WHERE `censor_certificate` IS NULL"
	# else:
	# 	if censor_certificate_isAttached == 'True':
	# 		censor_certificate_query = " AND `censor_certificate` IS NOT NULL"
	# 	elif censor_certificate_isAttached == 'False':
	# 		censor_certificate_query = " AND `censor_certificate` IS NULL"
			

	if ((main_agreement_query != "") or (lab_certificate_query != "")):
		if censor_certificate_isAttached == 'Yes':
			censor_certificate_query = " AND `censor_certificate` IS NOT NULL"
		elif censor_certificate_isAttached == 'No':
			censor_certificate_query = " AND `censor_certificate` IS NULL"
	else:
		if censor_certificate_isAttached == 'Yes':
			censor_certificate_query = " WHERE `censor_certificate` IS NOT NULL"
		elif censor_certificate_isAttached == 'No':
			censor_certificate_query = " WHERE `censor_certificate` IS NULL"

	if ((main_agreement_query != "") or (lab_certificate_query != "") or (censor_certificate_query != "")):
		if real_image_letter_isAttached == 'Yes':
			real_image_letter_query = " AND `real_image_letter` IS NOT NULL"
		elif censor_certificate_isAttached == 'No':
			real_image_letter_query = " AND `real_image_letter` IS NULL"
	else:
		if real_image_letter_isAttached == 'Yes':
			real_image_letter_query = " WHERE `real_image_letter` IS NOT NULL"
		elif censor_certificate_isAttached == 'No':
			real_image_letter_query = " WHERE `real_image_letter` IS NULL"


	sql_query = sql_query + lab_certificate_query + main_agreement_query + censor_certificate_query + real_image_letter_query

	lab_cert_query = frappe.db.sql(sql_query)

	data = lab_cert_query
	# return ["movie", "buyer", "release_date", "title"], data
	return [_("Movie ID")+":Link/Movies:100", _("Title")+":Data:200",_("Purchase ID")+":Link/Purchase:100",_("Buyer")+":Data:200", _("Release Sate")+":Date:100"], data