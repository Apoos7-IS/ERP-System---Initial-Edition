from odoo import api, models, fields

class Product(models.Model):
    _name = "product"

    name = fields.Char()
    sku = fields.Char()
    description = fields.Text()
    category_id = fields.Many2one('product.category.custom')
    quantity_available = fields.Float()
    cost_price = fields.Float()
    sale_price = fields.Float()
    is_active = fields.Boolean()
    