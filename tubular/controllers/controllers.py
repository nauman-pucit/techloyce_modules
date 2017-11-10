# -*- coding: utf-8 -*-
from odoo import http

# class Tubular(http.Controller):
#     @http.route('/tubular/tubular/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tubular/tubular/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tubular.listing', {
#             'root': '/tubular/tubular',
#             'objects': http.request.env['tubular.tubular'].search([]),
#         })

#     @http.route('/tubular/tubular/objects/<model("tubular.tubular"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tubular.object', {
#             'object': obj
#         })