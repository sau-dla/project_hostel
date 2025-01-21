from odoo import models, fields, api

class HostelRoomStage(models.Model):
    _name = 'hostel.room.stage'
    _order = 'sequence,name'

    name = fields.Char("Nombre")
    sequence = fields.Integer("Secuencia")  
    fold = fields.Boolean("¿Plegar?")  