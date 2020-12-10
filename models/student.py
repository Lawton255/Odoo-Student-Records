# -*- coding: utf-8 -*-

from odoo import models, fields, api



class StudentStudent(models.Model):
	_name = 'student.student'
	#_inherit = 'mail.thread'
	_description = 'Student Recors'

	@api.multi
	def button_done(self):
		for rec in self:
			rec.write({'state': 'done'})
	
	@api.multi
	def button_reset(self):
		for rec in self:
			rec.state = 'draft'

	@api.multi
	def button_cancel(self):
		for rec in self:
			rec.write({'state': 'cancel'})
	


	name = fields.Char(string='Student name', required=True, track_visibility='always')
	age = fields.Integer(string='Age' , track_visibility='always')
	photo = fields.Binary(string='Image')
	gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
	student_dob = fields.Date(string="Date of Birth")
	student_blood_group = fields.Selection(
    	[('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
     	('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
    	string='Blood Group')
	nationality = fields.Many2one('res.country', string='Nationality', auto_join=True, index=True, ondelete='cascade')
	state = fields.Selection([
			('draft', 'Draft'),
			('done', 'Done'),
			('cancel', 'Cancelled'),
			], required=True, default='draft')

	#Teacher info
	parent_id = fields.Many2one(comodel_name='student.student', string='Parent ID', auto_join=True, index=True, ondelete='cascade')
	child_id = fields.One2many(comodel_name='student.student', inverse_name='parent_id', string='Teacher', auto_join=True, index=True, ondelete='cascade')
	teacher_name = fields.Many2one('teacher.name', auto_join=True, index=True, ondelete='cascade')
	subject = fields.Char(string="Subject")
	teacher_salary = fields.Float(string="Salary")
	bonus	=	fields.Float(string="Bonus")
	#total_salary = fields.Flaot(string="Total salary" , compute='_compute_total_salary', required=False, readonly=True)

	#@api.dependes('teacher_salary','bonus')
	#def _compute_total_salary(self):
	#	for line in self:
	#		line['total_salary'] = line.teacher_salary * line.bonus

class TeacherName(models.Model):
	_name = 'teacher.name'
	_rec_name = 'teacher_name'

	teacher_name = fields.Char(string="Teacher name")
