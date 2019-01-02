# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Articles(models.Model):
    
    _name='articles'    
    _inherit = 'product.template'
    isarticle = fields.Boolean(string='is_article')
    
    auteur = fields.One2many(
        string='author',
        comodel_name='enseignant',
        inverse_name='inverse_field',
    )
    

    
