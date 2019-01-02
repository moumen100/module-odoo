# -*- coding: utf-8 -*-


from odoo import api, fields, models

class Cours(models.Model):

	_name='cours'
	name = fields.Char(required =True , string="Intitulé")
	niveau = fields.Selection([('niv1','Niveau 1'),('niv2','Niveau 2'),('niv3','Niveau 3')] , string="Niveau")
	nb_chapitre = fields.Integer(string="Nombre de chapitre")
	coef = fields.Integer("coefficient")
	dure = fields.Float(string="Durée de cours")
	pre_required = fields.Text(string = "pré requis")
	goals = fields.Text(string = "Objectifs pédagogique")
	logistics = fields.Text(string= "Matériels Nécessaire")
	deroulement = fields.Text(string = "Déroulement du cours")
	prologement = fields.Text(string = "Prolongement du cours")
	comment = fields.Text(string= "Commentaire")
	ens_ids = fields.One2many('enseignant','cour_id', string="Enseignants Liste")
	date = fields.Date('Date du début')

	# @api.multi
    # def print_cour(self):
    #     return self.env['report'].get_action(self, 'report_cours')





