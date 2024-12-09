from odoo import models, fields, api

class HostelRoomMember(models.Model):
    _name = 'hostel.room.member'
    _description = 'Hostel Room Member'

    name = fields.Char(string='Full name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    checkin_date = fields.Date(string='Checkin date', required=True)
    checkout_date = fields.Date(string='Checkout date', required=True)
    room_id = fields.Many2one('hostel.room', string='room', required=True, ondelete='cascade')