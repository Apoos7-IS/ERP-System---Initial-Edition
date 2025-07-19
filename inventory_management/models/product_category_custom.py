from odoo import fields, api, models

class ProductCategory(models.Model):
    _name = "product.category.custom"

    name = fields.Char()
    description = fields.Text()
