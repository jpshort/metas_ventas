# -*- coding: utf-8 -*-
from odoo import http

# class CustomAddons/metasventa(http.Controller):
#     @http.route('/custom_addons/metasventa/custom_addons/metasventa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_addons/metasventa/custom_addons/metasventa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_addons/metasventa.listing', {
#             'root': '/custom_addons/metasventa/custom_addons/metasventa',
#             'objects': http.request.env['custom_addons/metasventa.custom_addons/metasventa'].search([]),
#         })

#     @http.route('/custom_addons/metasventa/custom_addons/metasventa/objects/<model("custom_addons/metasventa.custom_addons/metasventa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_addons/metasventa.object', {
#             'object': obj
#         })