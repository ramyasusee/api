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
	},
	onload: function (me) {
		me.page.sidebar.find(".list-link[data-view='Kanban']").addClass("hide");
		me.page.sidebar.find(".list-link[data-view='Calendar']").addClass("hide");
        me.page.sidebar.find(".list-link[data-view='Tree']").addClass("hide");
        me.page.sidebar.find(".assigned-to-me a").addClass("hide");
    }
};