# -*- coding: utf-8 -*-
# from odoo import http


# class ConfigurationRh(http.Controller):
#     @http.route('/configuration_rh/configuration_rh/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/configuration_rh/configuration_rh/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('configuration_rh.listing', {
#             'root': '/configuration_rh/configuration_rh',
#             'objects': http.request.env['configuration_rh.configuration_rh'].search([]),
#         })

#     @http.route('/configuration_rh/configuration_rh/objects/<model("configuration_rh.configuration_rh"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('configuration_rh.object', {
#             'object': obj
#         })
