from odoo import fields, api, models

class InvoiceLine(models.Model):
    _name = "invoice.line"

    invoice_id = fields.Many2one('invoice')
    product_id = fields.Many2one('product')
    description = fields.Text()
    quantity = fields.Float()
    unit_price = fields.Float()
    subtotal = fields.Monetary()
    currency_id = fields.Many2one('res.currency')