# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Enseignant(models.Model):

	_name="enseignant"

	name = fields.Char(required =True , string="Nom")
	prenom = fields.Char(required= True , string="Prénom")
	adresse = fields.Char(string = "Adresse")
	grade = fields.Selection([('vac','Vacataire') , ('fonc', 'Fonctionaire'), ('doc','Doctorant'), ('prof','Professeur'), ('dem','Démession')] ,string ="Grade", default="vac")
	contrat = fields.Selection([('cdd','CDD') , ('cdi', 'CDI'), ('other','Autre')])
	diplome = fields.Selection([('mas','Master') , ('mag', 'Magister'), ('doct','Doctorat')])
	cour_id = fields.Many2one('cours' , string=" Cour enseigné")

	@api.multi
	def action_promote(self):
		for ens in self:
            # if ens.contrat == 'cdd' or ens.contrat == 'cdi':
				# ens.grade = 'fonc'
			if ens.diplome == 'doct' and ens.grade == 'fonc':
				ens.grade = 'doc'
			if ens.grade == 'vac' and ens.contrat == 'cdd' or ens.contrat == 'cdi':
				ens.grade = 'fonc'
	@api.multi
	def action_leave(self):
		for ens in self:
            # ens.grade = 'dem'
			ens.grade = 'dem'