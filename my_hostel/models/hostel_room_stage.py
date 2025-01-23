from odoo import models, fields, api

class HostelRoomStage(models.Model):
    _name = 'hostel.room.stage'
    _order = 'sequence,name'
    _description = 'Information'

    name = fields.Char("Name")
    sequence = fields.Integer("Sequence")
    fold = fields.Boolean("Fold?")