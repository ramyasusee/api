from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _, msgprint


@frappe.whitelist()
def update_rights_type():
    # purchase = frappe.get_list("Purchase", filters={}, fields=["name"])
    # for p in purchase:
    #     purchase_doc = frappe.get_doc("Purchase", p.name)
    #     primary_rights = purchase_doc.primary_rights
    #     primary_rights_len = len(primary_rights)
    #     i = 0
    #     for i in range(primary_rights_len):
    #         if primary_rights[i].type == "Inclusion":
    #             primary_rights[i].type = "Include"
    #     purchased_rights = purchase_doc.purchased_rights
    #     purchased_rights_len = len(purchased_rights)
    #     j = 0
    #     for j in range(purchased_rights_len):
    #         if purchased_rights[j].type == "Inclusion":
    #             purchased_rights[j].type = "Include"
    #     purchase_doc.save(ignore_permissions=True)

    sales = frappe.get_list("Sales", filters={}, fields=["name"])
    for s in sales:
        sales_doc = frappe.get_doc("Sales", s.name)
        platform_rights = sales_doc.platform_rights
        platform_rights_len = len(platform_rights)
        k = 0
        for k in range(platform_rights_len):
            if platform_rights[k].type == "Inclusion":
                platform_rights[k].type = "Include"
        sales_doc.save(ignore_permissions=True)



@frappe.whitelist()
def update_country_set_title():
    # purchase = frappe.get_list("Purchase", filters={}, fields=["name"])
    # for p in purchase:
    #     doc = frappe.get_doc("Purchase", p.name)
    #     child = doc.primary_rights
    #     child_len = len(child)
    #     i = 0
    #     for i in range(child_len):
    #         if not child[i].countries:
    #             cs = frappe.get_doc("Country Set", child[i].c_set)
    #             child[i].countries = cs.title
    #             child[i].save(ignore_permissions=True)
    #             frappe.db.commit()
        
        sales = frappe.get_list("Sales", filters={}, fields=["name"])
        for s in sales:
            sales_doc = frappe.get_doc("Sales", s.name)
            platform_rights = sales_doc.platform_rights
            platform_rights_len = len(platform_rights)
            k = 0
            for k in range(platform_rights_len):
                if not platform_rights[k].countries:
                    cs = frappe.get_doc("Country Set", platform_rights[k].c_set)
                    platform_rights[k].countries = cs.title
            sales_doc.save(ignore_permissions=True)