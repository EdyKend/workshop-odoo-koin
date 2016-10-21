from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    ship_via = fields.Char('Ship Via')