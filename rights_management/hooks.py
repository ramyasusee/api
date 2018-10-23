# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "rights_management"
app_title = "Rights Management"
app_publisher = "Aftertutor Ventures Pvt Ltd"
app_description = "Movie Rights Management for AP International"
app_icon = "fa fa-film"
app_color = "#4B3F72"
app_email = "contact@atdigitals.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rights_management/css/rights_management.css"
# app_include_js = "/assets/rights_management/js/rights_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/rights_management/css/rights_management.css"
# web_include_js = "/assets/rights_management/js/rights_management.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "rights_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "rights_management.install.before_install"
# after_install = "rights_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rights_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rights_management.tasks.all"
# 	],
# 	"daily": [
# 		"rights_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"rights_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rights_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"rights_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "rights_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rights_management.event.get_events"
# }

