// Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Purchase', {
	movie: function(frm) {
		if(typeof frm.doc.movie != "undefined"){
            frappe.call({
                "method": "frappe.client.get",
                args:{
                    "doctype": "Movies",
                    "name": frm.doc.movie
                },
                callback: function(r){
                    frm.set_value("production_banner", r.message.production_banner);
                    frm.set_value("title", r.message.title);
                    frm.set_value("title_language", r.message.title_language);
                    frm.set_value("video_format", r.message.video_format);
                    frm.set_value("source_availability", r.message.source_availability);

                    dir = r.message.director_table
                    for (d in dir){
	                        frm.set_value("director",dir[d].director)
                    }
					mdir = r.message.music_director_table
                    for (d in mdir){
	                        frm.set_value("music_director",mdir[d].music_director)
                    }
					cast = r.message.key_star_cast
                    var cast_list = []
                    for (c in cast){
	                       cast_list.push(cast[c].star+",")
                    }
					frm.set_value("cast",cast_list)
                }
            })
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



frappe.ui.form.on('Platform Rights', {
	c_set: function(frm, cdt, cdn){
	    var child = locals[cdt][cdn];
	    frappe.call({
	        "method": "frappe.client.get",
	        args:{
	            "doctype": "Country Set",
	            "name": child.c_set
	        },
	        callback: function(r){
	            frappe.model.set_value(child.doctype, child.name, "countries", r.message.title);
	        }
	    })
	}
})
