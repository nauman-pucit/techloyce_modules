# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api
from openerp.osv import osv


class CustomCRMLead(models.Model):
    _inherit = 'crm.lead'

    pickup_address = fields.Char(string = "Pich Up Address")
    pickup_postcode = fields.Char(string = "Pich Up Postcode")
    pickup_time = fields.Datetime(string='Pick Up Date/Time')
    dropoff_address = fields.Char(string = "Drop Off Address")
    dropoff_postcode = fields.Char(string = "Drop Off Postcode")
    travel_duration = fields.Char(string = "Travel Duration")
    vehicle = fields.Char(string = "Vehicle")
    stops = fields.Char(string = "Stops")
    stairs = fields.Char(string = "Stairs")
    congestion_zone = fields.Char(string = "Congestion Zone")
    task_ids = fields.One2many('tubular.task','task_id')


class LeadTask(models.Model):
    _name = "tubular.task"

    task_name = fields.Char(string = "Name")
    time = fields.Datetime(string='Date/Time')
    user_id = fields.Many2many('res.users', string='Assigned to')
    is_complete = fields.Boolean(string = "is completed")
    task_id = fields.Many2one('crm.lead', string="Lead", ondelete='cascade', index=True, copy=False)
    comment_ids = fields.One2many('tubular.comment', 'comment_id')


class Comment(models.Model):
    _name = "tubular.comment"

    name = fields.Char(string = "Comment")
    comment_id = fields.Many2one('tubular.task', ondelete='cascade', index=True, copy=False)