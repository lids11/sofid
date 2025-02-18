# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    purchase_order_ids = fields.Many2many('purchase.order')

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.constrains('product_uom_qty')
    def _check_product_uom_qty(self):
        for record in self:
            if not isinstance(record.product_uom_qty, int) or record.product_uom_qty != int(record.product_uom_qty):
                raise ValidationError("Le champ doit être un entier.")
   
