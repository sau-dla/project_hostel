from odoo import models, fields, api

class HostelRoomAvailability(models.Model):
    _name = 'hostel.room.availability'
    _description = "Hostel Room Availability"
    _auto = False

    room_id = fields.Many2one('hostel.room', 'Room', readonly=True)
    student_per_room = fields.Integer(string="Student Per Room", readonly=True)
    availability = fields.Integer(string="Availability", readonly=True)
    amount = fields.Integer(string="Amount", readonly=True)
