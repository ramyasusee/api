// Copyright (c) 2018, Aftertutor Ventures Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sales', {
	type_of_content: function(frm) {
		frm.set_value("title", null);
		frm.set_value("title_language", null);
		frm.set_value("movie", null);
		frm.set_value("sfc", null);
	},
	movie: function(frm) {
		if(typeof frm.doc.movie != "undefined"){
			frappe.db.get_value("Movies", {name: frm.doc.movie}, "title", function(data){
				frm.set_value("title", data.title);
			});

			frappe.db.get_value("Movies", {name: frm.doc.movie}, "title_language", function(data){
				frm.set_value("title_language", data.title_language);
			});

			frappe.db.get_value("Purchase", {movie: frm.doc.movie}, "buyer", function(data){
				frm.set_value("seller", data.buyer);
			});
		}
	},
	sfc: function(frm) {
		if(typeof frm.doc.sfc != "undefined"){
			frappe.db.get_value("Short Format Content", {name: frm.doc.sfc}, "title", function(data){
				frm.set_value("title", data.title);
			});

			frappe.db.get_value("Short Format Content", {name: frm.doc.sfc}, "title_language", function(data){
				frm.set_value("title_language", data.title_language);
			});

			frappe.db.get_value("Purchase", {sfc: frm.doc.sfc}, "buyer", function(data){
				frm.set_value("seller", data.buyer);
			});
		}
	},
});


frappe.ui.form.on('Platform Rights', {
	right: function(frm, cdt, cdn){
	    var child = locals[cdt][cdn];
	    frappe.call({
	        "method": "frappe.client.get",
	        args:{
	            "doctype": "Purchase",
	            "name":frm. doc.purchase_id
	        },
	        callback: function(r){
	            var pr = r.message.purchased_rights;
                var pr_len = pr.length
                var result = 0
                for(var i = 0; i< pr_len;i++){
                    if(child.right == pr[i].right){
                        result = 1
                    }
                }
                if(result == 0){
                    frappe.msgprint("The Purchased Rights only be allowed to sale")
                }
	        }
	    })
	},
})
