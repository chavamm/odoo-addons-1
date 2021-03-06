# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jacques-Etienne Baudoux
#    Copyright 2013 Camptocamp SA
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

{"name": "Sale Order Validity",
 "version": "7.0.0",
 "depends": ["sale_prices_update"],
 "author": "Sistemas ADHOC",
 "category": "Sales",
 "website": "http://www.sistemasadhoc.com.ar",
 "description": """
Sale order validity
===================

""",
 'data': [
 	'sale_order_view.xml',
 	'company_view.xml',
 	'workflow/sale_workflow.xml',
 	],
 'installable': True,
 'active': False,
 }
