##############################################################################
#
#    Copyright (C) 2016 JCrosoft Limited
#    Jean-Christophe PLAGNIOL-VILLARD <plagnioj@jcrosoft.com>
#
#    Licence: AGPLv3
#
##############################################################################

#from openerp.osv import fields, osv, models
from openerp import api, fields, models
import openerp.addons.decimal_precision as dp

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    price_total_taxes = fields.Monetary(compute='_price_total_taxes', string='Total', readonly=True, store=True)

    @api.depends('quantity', 'discount', 'price_unit', 'invoice_line_tax_ids')
    def _price_total_taxes(self):
        """
        Compute the amounts including taxes of the Invoice line.
        """
        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
	    taxes = line.invoice_line_tax_ids.compute_all(price, line.currency_id, line.quantity, product=line.product_id, partner=line.partner_id)
	    line.update({'price_total_taxes': taxes['total_included']})

