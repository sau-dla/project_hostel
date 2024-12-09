from odoo import models, fields

class HostelStudent(models.Model):
    _name = "hostel.student"
    _description = "Hostel Stundent Information"  
    
    name = fields.Char("Student Name")
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([(u"male", u"Male"), (u"female", u"Female"), (u"other", u"31 type of gay")],
                            string="Gender", help="Student's gender")
    active = fields.Boolean("Active", default=True,
                            help="Activate/Deactivate hostel record")
    room_id = fields.Many2one("hostel.room", "Room",
                            help="Select hostel room")
    hostel_id = fields.Many2one("hostel.hostel", related='room_id.hostel_id')
    partner_id = fields.Many2one('res.partner', ondelete='cascade') 
