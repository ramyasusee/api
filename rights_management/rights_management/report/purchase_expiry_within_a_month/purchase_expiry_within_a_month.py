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
    if not filters:
        filters = {}
    columns, data = [], []
    row = [] 
    columns = get_columns()
    before_date = add_days(today(),-30)
    to_date = (datetime.strptime(today(), '%Y-%m-%d')).date()
    from_date = (datetime.strptime(before_date, '%Y-%m-%d')).date()
    sql_query = """SELECT * from `tabPurchase` where expiry_date between '%s' and '%s' """%(from_date,to_date)
    purchase = frappe.db.sql(sql_query,as_dict=True)
    for p in purchase:
        row = [p.movie,p.title,p.name,p.current_title,p.expiry,p.expiry_date]
    data.append(row)
    return columns,data



def get_columns():
    columns = [
        _("Movie Title") + ":Data:100",
        _("Movie ID") + ":Link/Movies:250",
        _("Purchase ID") + ":Link/Purchase:100", 
        _("Purchase Title") + ":Data:250",
        _("Expiry Type") + ":Data:90",
        _("Expiry Date") + ":Date:90",
        #  _("Director") + ":Data:90",
        # _("Music Director") + ":Data:90",
        # _("Stars") + ":Data:90",
    ]
    return columns