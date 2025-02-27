from odoo import models, fields, api
from odoo.exceptions import UserError

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
    admission_date = fields.Date(string="Admission Date")

    status = fields.Selection([
        ("draft", "Draft"),
        ("reservation", "Reservation"), 
        ("pending", "Pending"),
        ("paid", "Done"), 
        ("discharge", "Discharge"), 
        ("cancel", "Cancel")
    ], string="Status", default="draft") 

    def action_assign_room(self):
        self.ensure_one()

        if self.status not in ["paid", "discharge"]:
            raise UserError(("You can't assign a room if the student status is not 'Paid' or 'Discharge'."))

        room_as_superuser = self.env['hostel.room'].sudo()
        room_rec = room_as_superuser.create({
            "room_name": "Room A-103",
            "room_number": "A-103",
            "floor_number": 1,
            "hostel_id": self.hostel_id.id,
            "student_per_room": 4,
        })

        self.write({'room_id': room_rec.id, 'status': 'pending'}) 

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
            'context': {'success': True}
        }

    def action_remove_room(self):
        if self.env.context.get("is_hostel_room"):
            self.room_id = False