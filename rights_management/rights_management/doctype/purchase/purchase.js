// Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Purchase', {
	movie: function(frm) {
		if(typeof frm.doc.movie != "undefined"){
			frappe.db.get_value("Movies", {name: frm.doc.movie}, "production_banner", function(data){
				frm.set_value("production_banner", data.production_banner);
			});

			frappe.db.get_value("Movies", {name: frm.doc.movie}, "title", function(data){
				frm.set_value("title", data.title);
			});

			frappe.db.get_value("Movies", {name: frm.doc.movie}, "title_language", function(data){
				frm.set_value("title_language", data.title_language);
			});
		}
	},
	sfc: function(frm) {
		if(typeof frm.doc.sfc != "undefined"){
			frappe.db.get_value("Short Format Content", {name: frm.doc.sfc}, "production_banner", function(data){
				frm.set_value("production_banner", data.production_banner);
			});

			frappe.db.get_value("Short Format Content", {name: frm.doc.sfc}, "title", function(data){
				frm.set_value("title", data.title);
			});

			frappe.db.get_value("Short Format Content", {name: frm.doc.sfc}, "title_language", function(data){
				frm.set_value("title_language", data.title_language);
			});
		}
	},
	ignore_link_agreement: function(frm){
		if(frm.doc.ignore_link_agreement == 1){
			frm.set_value('link_agreement', null)
		}
	},
	expires_in: function(frm) {
		if(frm.doc.expires_in < 0 ){
			frappe.msgprint("'Expires in' cannot be negative");
			frm.set_value("expires_in", null);
		}
		if(typeof frm.doc.release_date != "undefined"){
			var years = 0;
			if(frm.doc.expiry == "Perpetual") {
				years = 99;
				frm.set_value("expires_in", 99);
			}
			if(frm.doc.expiry == "Specific") years = parseFloat(frm.doc.expires_in)
			if(frm.doc.expiry == "")
				frm.set_value("expiry_date", null);
			if(years > 0)
				frm.set_value("expiry_date", frappe.datetime.add_months(frm.doc.release_date, years * 12));
			else
				frm.set_value("expiry_date", null);
		}
	},
	expiry: function(frm){
		if(frm.doc.expires_in < 0 ){
			frappe.msgprint("'Expires in' cannot be negative");
			frm.set_value("expires_in", null);
		}
		if(typeof frm.doc.release_date != "undefined"){
			var years = 0;
			if(frm.doc.expiry == "Perpetual") {
				years = 99;
				frm.set_value("expires_in", 99);
			}
			if(frm.doc.expiry == "Specific") years = parseFloat(frm.doc.expires_in)
			if(frm.doc.expiry == "")
				frm.set_value("expiry_date", null);
			if(years > 0)
				frm.set_value("expiry_date", frappe.datetime.add_months(frm.doc.release_date, years * 12));
			else
				frm.set_value("expiry_date", null);
		}
	},
	release_date: function (frm) {
		if(typeof frm.doc.release_date == "undefined"){
			frm.set_value("expiry_date", null);
			frm.set_value('yet_to_be_released', 1);
		} else {
			frm.set_value('yet_to_be_released', 0);
		}
	},
	type: function(frm) {
		frm.set_value("movie", null);
		frm.set_value("sfc", null);
		frm.set_value("title", null);
		frm.set_value("title_language", null);
		frm.set_value("production_banner", null);
	}
});
