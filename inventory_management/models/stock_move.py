from odoo import api, fields, models

class StockMove(models.Model):
    _name = "stock.move"

    product_id = fields.Many2one('product')
    quantity = fields.Float()
    source_location_id = fields.Many2one('stock.location')
    dest_location_id = fields.Many2one('stock.location')
    move_type = fields.Selection([
        ("in", "Incoming"),
        ("out", "Outgoing"),
        ("internal", "Internal Transfer"),
    ])
    date = fields.Datetime()