// Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Purchase', {
	movie: function(frm) {
		frappe.db.get_value("Movies", {name: frm.doc.movie}, "production_banner", function(data){
			frm.set_value("production_banner", data.production_banner);
		});

		frappe.db.get_value("Movies", {name: frm.doc.movie}, "title", function(data){
			frm.set_value("title", data.title);
		});

		frappe.db.get_value("Movies", {name: frm.doc.movie}, "title_language", function(data){
			frm.set_value("title_language", data.title_language);
		});
	},
	sfc: function(frm) {
		frappe.db.get_value("Short Format Content", {name: frm.doc.movie}, "production_banner", function(data){
			frm.set_value("production_banner", data.production_banner);
		});

		frappe.db.get_value("hort Format Content", {name: frm.doc.movie}, "title", function(data){
			frm.set_value("title", data.title);
		});

		frappe.db.get_value("hort Format Content", {name: frm.doc.movie}, "title_language", function(data){
			frm.set_value("title_language", data.title_language);
		});
	}
});
