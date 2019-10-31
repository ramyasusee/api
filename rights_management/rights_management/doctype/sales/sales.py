# -*- coding: utf-8 -*-
# Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from frappe import _,msgprint
import frappe.utils.data as utils

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
        if self.date_of_agreement > self.license_starting_date:
            frappe.throw(_("License must start only after the Date of Agreement."))
        if self.license_starting_date >= self.license_ending_date:
            frappe.throw(_("License ending date cannot be equal or before the license starting date."))
        for file in file_list:
            if self.type_of_content == "Movies":
                purchases = frappe.get_all("Purchase", filters={'type': 'Movies', 'movie': file}, fields=['name'])
            if self.type_of_content == "Short Format Content":
                purchases = frappe.get_all("Purchase", filters={'type': 'Short Format Content', 'sfc': file}, fields=['name'])

            purchased_rights = list()
            for purchase in purchases:
                if purchase.name == self.purchase_id:
                    doc = frappe.get_doc("Purchase", purchase.name)
                    difby = False
                    err = "<p>Expected Seller: <b>"+self.seller+"</b>. You cannot sell movies from different seller names in one record. The following movies are from different sellers:</p><ol>"
                    if self.seller != doc.buyer:
                        difby = True
                        err += "<li>"+doc.title +" - "+ doc.buyer +"</li>"
                    if difby:
                        err = err + "</ol> <p class=\"text-danger\">Please fix all errors to save the record.</p>"
                    if self.license_ending_date:
                        if doc.expiry == 'Specific' and utils.getdate(self.license_ending_date) > doc.expiry_date:
                            frappe.throw(_('<b>'+doc.current_title +"</b> has an expiry of <b>"+str(doc.expiry_date)+"</b> while the current sale expires on <b>"+str(self.license_ending_date)+"</b>. Please fix the license dates."))
                        if doc.expiry == 'Perpetual' and utils.getdate(self.license_ending_date) > utils.add_to_date(utils.getdate(doc.agreement_date), years=99):
                            frappe.throw(_('<b>'+doc.current_title +"</b> has an <b>Perpetual</b> expiry of <b>"+str(utils.add_to_date(doc.agreement_date, years=99))+"</b> while the current sale expires on <b>"+str(self.license_ending_date)+"</b>. Please fix the license dates."))
                    purchased_rights.extend(doc.purchased_rights)
            valid = validate_rights(purchased_rights, self.platform_rights, doc.title)
            if valid:
                frappe.msgprint(_('All the rights are matched perfectly. You are good to go :)'))
            else:
                frappe.msgprint(_('Please fix all the errors to finalize sale.'))



def validate_rights(superset, subset, title):
    superset_rights = list()
    subset_rights = list()

    for row in superset:
        #if row.right in superset_rights:
            #frappe.throw(_("Duplicate entry: <b>"+row.right+"</b> in Primary Rights table on "+title)) #this is never likely to happen
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
            cset_doc = frappe.get_doc('Country Set', row.c_set)
            l = list()
            for c in cset_doc.country_table:
                l.append(c.country)
            for country in l:
                cset.append(country.strip())
            primary.append({
                "right": row.right,
                "type": row.type,
                "cset": set(cset)
            })

        secondary = list()
        for row in subset:
            cset = list()
            cset_doc = frappe.get_doc('Country Set', row.c_set)
            l = list()
            for c in cset_doc.country_table:
                l.append(c.country)
            for country in l:
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
                        error = error + "<p>In <b>"+sec.get('right')+"</b> right, you cannot sell an <b>Exclusion</b> when you only have <b>Inclusion</b> with these countries:</p><ol>"
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
            error = 'For <b>'+title+'</b>' +error + "<p class=\"text-danger\">Please fix all the errors to save the document.</p>"
            frappe.throw(_(error))
            return False
        else:
            return True

