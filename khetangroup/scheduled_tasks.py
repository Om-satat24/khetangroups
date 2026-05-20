import frappe

def daily():
    frappe.logger().info("khetangroup daily scheduled task triggered")
    from khetangroup.update_stock_entry import update_stock_entry
    update_stock_entry()
