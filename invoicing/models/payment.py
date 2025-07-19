from odoo import fields, models, api

class Payment(models.Model):
    _name = "payment"

    partner_id = fields.Many2one('res.partner')
    invoice_id = fields.Many2one('invoice')
    payment_date = fields.Date()
    amount = fields.Monetary()
    currency_id = fields.Many2one('res.currency')
    note = fields.Text()