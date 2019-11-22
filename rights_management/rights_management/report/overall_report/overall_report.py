# Copyright (c) 2013, AT Digitals and contributors
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
    # if not filters:
    #     filters = {}
    columns, data = [], []
    row = []   
    movie = filters.movie
    countries_p = filters.countries_p
    countries_in_purchase = ""
    countries_in_sales = ""
    movie_filter = ""
    rights_sales = ""
    rights_purchase = ""

    sql_query = """ SELECT purchase.movie, purchase.title,purchase.title_language,purchase.director,purchase.music_director,purchase.cast,purchase.name, purchase.production_banner, purchase.buyer, purchase.seller, purchase.type_of_purchase, purchase.purchase_cost,purchase.currency,purchase.agreement_date,purchase.release_date,purchase.expiry, purchase.expires_in, 
                   rights.right, rights.type,rights.c_set, rights.countries,rights.exclusivity,sales.name,sales.seller,sales.customer,sales.type_of_sale,sales.sale_value,sales.currency,sales.share_percentage,sales.has_mg,sales.mg,sales.date_of_agreement,sales.license_starting_date,sales.license_ending_date,sales_rights.right, sales_rights.type,sales_rights.c_set, sales_rights.countries,sales_rights.exclusivity,sales.licensed_channel,
                   sales.exclusivity,sales.exclusive_till,sales.permitted_runs from `tabPlatform Rights` rights, `tabPurchase` purchase  
                   LEFT JOIN `tabSales` sales ON purchase.movie = sales.movie
                   LEFT JOIN `tabPlatform Rights` sales_rights ON sales_rights.parentfield = 'platform_rights' and sales_rights.parent = sales.name
                   where rights.parentfield = 'purchased_rights' and rights.parent = purchase.name"""
    
    if movie:
        movie_filter = " and purchase.movie = '%s'"%filters["movie"]
    if countries_p:
        countries_in_purchase = " and (rights.countries like "+"'%"+"%s" %filters["countries_p"]+"%'"+" or rights.countries like "+"'%"+"Entire World%')"
    if filters.countries_s:
        countries_in_sales = " and (sales_rights.countries like "+"'%"+"%s" %filters["countries_s"]+"%'"+" or sales_rights.countries like "+"'%"+"Entire World%')"
    if filters.rights_p:
        rights_purchase = " and rights.right = '%s'"%filters["rights_p"]
    if filters.rights_s:
        rights_sales = " and sales_rights.right = '%s'"%filters["rights_s"]


    sql_query = sql_query + movie_filter + countries_in_purchase + countries_in_sales + rights_purchase + rights_sales

    data = frappe.db.sql(sql_query)

    return [_("Movie ID")+":Data:100",_("Title")+":Data:250", _("Title Language")+":Data:100",_("Director")+":Data:150",_("Music Director")+":Data:150",_("Cast")+":Data:250",_("Purchase ID")+":Data:100", _("Production Banner")+":Data:250",_("Buyer")+":Data:150",_("Seller(Purchase)")+":Data:150",_("Type Of Purchase")+":Data:100", _("Purchase Cost")+":Currency:200",_("PC Currency")+":Data:100",_("Original Agreement Date")+":Date:200",_("Release Date")+":Date:200", _("Expiry Type")+":Data:100",_("Expires in(Years)")+":Int:100", _("Purchased Rights")+":Data:250", _("Type(purchase)")+":Data:100",_("Country Sets(Purchase)")+":Data:100", _("Countries(Purchase)")+":Data:300",_("Exclusivity(purchase)")+":Data:100",_("Sales ID")+":Data:100",
            _("Seller")+":Data:150",_("Customer Name")+":Data:150",_("Sales Type")+":Data:100",_("Sales Value")+":Currency:150", _("SV Currency")+":Data:100",_("Share %")+":Percentage:100",_("Minimum Guarantee Applicable")+":Data:100", _("Minimum Guarantee")+":Data:150",_("Date of Agreement")+":Date:150", _("License Starting Date")+":Date:150", _("License Ending Date")+":Date:150",_("Rights")+":Data:250", _("Type")+":Data:100",_("Country Sets")+":Data:100", _("Countries")+":Data:300",_("Exclusivity")+":Data:100",_("Licensed Channel")+":Data:100", _("Exclusivity")+":Data:100",_("Exclusive Till")+":Date:100", _("Permitted Runs")+":Int:100"], data



