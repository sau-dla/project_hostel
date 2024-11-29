from odoo import models, fields

class HostelStudent(models.Model):
    _name = "hostel.student"
    _description = "Hostel Stundent Information"  
    
    name = fields.Char("Student Name")
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([("male", "Man"),
                            ("female", "Woman"),
                            ("common", "31 types of gay")],
                            "gender", help="type of sex",
                            required=True)
    active = fields.Boolean("Active", default=True,
                            help="Activate/Deactivate hostel record")
    room_id = fields.Many2one("hostel.room", "Room",
                            help="Select hostel room")
    hostel_id = fields.Many2one("hostel.hostel", related='room_id.hostel_id')