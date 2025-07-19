from odoo import fields, models, api

class StockLocation(models.Model):
    _name = "stock.location"

    name = fields.Char()
    location_type = fields.Selection([
        ("internal", "Internal"),
        ("supplier", "Supplier"),
        ("customer", "Customer"),
        ("retail_outlet", "Retail Outlet"),
        ("main_warehouse", "Main Warehouse"),
    ])
    is_active = fields.Boolean()
    note = fields.Text()