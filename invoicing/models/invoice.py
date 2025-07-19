from odoo import fields, api, models

class Invoice(models.Model):
    _name = "invoice"

    invoice_number = fields.Char()
    partner_id = fields.Many2one('res.partner')
    invoice_date = fields.Date()
    due_date = fields.Date()
    state = fields.Selection([
    ('draft', 'Draft'),
    ('posted', 'Posted'),
    ('paid', 'Paid'),
    ('cancel', 'Cancel'),
    ], default='draft')
    invoice_line_ids = fields.One2many('invoice.line', 'invoice_id')
    total_amount = fields.Monetary()
    currency_id = fields.Many2one('res.currency')
    