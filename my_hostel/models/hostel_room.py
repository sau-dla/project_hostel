from odoo import models, fields

class HostelRoom(models.Model):
    _name = "hostel.room"
    _description = "Hostel Room Information"  
    
    room_name = fields.Char(
        'Room Name')

    room_number = fields.Char(
        'Room No.')

    floor_number = fields.Char(
        'FLoor No.', help="Enter the floor number")

    currency_id = fields.Many2one('res.currency',
    string='Currency')

    rent_amount = fields.Monetary(
        'Rent Amount', help="Enter the floor number")

    hostel_id = fields.Many2one("hostel.hostel", "hostel",
    help="Name of hostel")

    student_ids = fields.One2many("hostel.student", "room_id",
    string="Student", help="Enter student")

    hostel_amenities_ids = fields.Many2many("hostel.amenities",
    "hostel_room_amenities_rel", "room_id", "amenitiy_id",
    string="Amenities", domain="[('active', '=', True)]",
    help="Select hostel room amenities")