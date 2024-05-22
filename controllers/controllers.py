# -*- coding: utf-8 -*-
# from odoo import http


# class ProductSynonyms(http.Controller):
#     @http.route('/product_synonyms/product_synonyms', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_synonyms/product_synonyms/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_synonyms.listing', {
#             'root': '/product_synonyms/product_synonyms',
#             'objects': http.request.env['product_synonyms.product_synonyms'].search([]),
#         })

#     @http.route('/product_synonyms/product_synonyms/objects/<model("product_synonyms.product_synonyms"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_synonyms.object', {
#             'object': obj
#         })

