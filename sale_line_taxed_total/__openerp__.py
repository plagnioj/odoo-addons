##############################################################################
#
#    Copyright (C) 2016 JCrosoft Limited
#    Jean-Christophe PLAGNIOL-VILLARD <plagnioj@jcrosoft.com>
#
#    Licence: AGPLv3
#
##############################################################################
{
    'name': 'Taxed total on Sale order lines and invoices line',
    'version': '9.0.4.0',
    'author' : 'JCrosoft',
    'license' : 'AGPL-3',
    'contributors' : ['Jean-Christophe PLAGNIOL-VILLARD <plagnioj@jcrosoft.com>'],
    'category': 'Sales',
    'description': """
    """,
    'website': 'http:s//www.jcrosoft.com',
    'depends': ['sale', 'account'],
    'data': [
        'views/sale.xml',
        'views/invoice.xml'
     ],
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
