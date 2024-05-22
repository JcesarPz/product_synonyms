# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ProductSynonym(models.Model):
    _name="product.template.synonym"
    _description="Product template synonym"
    
    product_id=fields.Many2one(
        comodel_name="product.template",
        string="Producto"
    )
    name=fields.Char(
        string="Name",
        required=True
    )
    
class ProductTemplate(models.Model):
    _inherit="product.template"
    
    synonym_ids=fields.One2many(
        string="Other names",
        comodel_name="product.template.synonym",
        inverse_name="product_id"
    )
    
    all_names=fields.Char(
        compute="_compute_all_names"
    )
    
    
    @api.depends('name','synonym_ids')
    def _compute_all_names(self):
        for rec in self:
            name_list=[] 
            if rec.synonym_ids:           
                for syn in rec.synonym_ids:
                    name_list.append(syn.name)
            name_list.append(rec.name)        
            rec.all_names= "",name_list
    
    @api.model        
    def _search_all_names(self, operator, value):
        return ['|','|',('name',operator,value),('synonym_ids',operator,value)]
            
            
    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args=args or []
        domain=[]
        if name:
            domain=[('all_names',operator,name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
            


    
    
        
