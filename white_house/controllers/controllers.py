# -*- coding: utf-8 -*-
# from odoo import http


# class WhiteHouse(http.Controller):
#     @http.route('/white_house/white_house', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/white_house/white_house/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('white_house.listing', {
#             'root': '/white_house/white_house',
#             'objects': http.request.env['white_house.white_house'].search([]),
#         })

#     @http.route('/white_house/white_house/objects/<model("white_house.white_house"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('white_house.object', {
#             'object': obj
#         })

