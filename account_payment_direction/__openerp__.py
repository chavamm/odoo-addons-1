# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{   'active': False,
    'author': 'Sistemas ADHOC',
    'category': 'Accounting & Finance',
    'demo_xml': [],
    'depends': ['account_voucher'],
    'description': 'Extends Account Journal and adds a field direction (in or out) for bank and cash Journals. Then, for costumer payments only out or none payments will be shown. Same for suppliers',
    'init_xml': [],
    'installable': True,
    'name': 'Account Payment Direction',
    'test': [],
    'update_xml': [
        'account_journal_view.xml',
        'voucher_payment_receipt_view.xml',
        ],
    'version': '0.0',
    'website': 'http://www.sistemasadhoc.com.ar/'}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: