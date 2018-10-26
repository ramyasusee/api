frappe.listview_settings['Movies'] = {
	add_fields: ["status"],
	get_indicator: function(doc) {
		if (doc.status == "Pending") {
			return [__("Pending"), "orange", "status,=,Pending"];
		} else if (doc.status == "Released") {
			return [__("Released"), "green", "status,=,Released"];
		} else if (doc.status == "Cancelled") {
			return [__("Cancelled"), "red", "status,=,Cancelled"];
		}
	}
};