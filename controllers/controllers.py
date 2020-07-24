# -*- coding: utf-8 -*-
# from odoo import http


# class Practicabusqueda(http.Controller):
#     @http.route('/practicabusqueda/practicabusqueda/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/practicabusqueda/practicabusqueda/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('practicabusqueda.listing', {
#             'root': '/practicabusqueda/practicabusqueda',
#             'objects': http.request.env['practicabusqueda.practicabusqueda'].search([]),
#         })

#     @http.route('/practicabusqueda/practicabusqueda/objects/<model("practicabusqueda.practicabusqueda"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('practicabusqueda.object', {
#             'object': obj
#         })
