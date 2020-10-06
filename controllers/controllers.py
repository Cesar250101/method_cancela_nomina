# -*- coding: utf-8 -*-
from odoo import http

# class MethodCancelaNomina(http.Controller):
#     @http.route('/method_cancela_nomina/method_cancela_nomina/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_cancela_nomina/method_cancela_nomina/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_cancela_nomina.listing', {
#             'root': '/method_cancela_nomina/method_cancela_nomina',
#             'objects': http.request.env['method_cancela_nomina.method_cancela_nomina'].search([]),
#         })

#     @http.route('/method_cancela_nomina/method_cancela_nomina/objects/<model("method_cancela_nomina.method_cancela_nomina"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_cancela_nomina.object', {
#             'object': obj
#         })