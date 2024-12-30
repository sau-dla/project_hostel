from odoo import models, fields, api
from odoo.exceptions import UserError

class HostelStudent(models.Model):
    _name = "hostel.student"
    _description = "Hostel Stundent Information"  

    status = fields.Selection([
        ('paid', 'Pagado'),
        ('unpaid', 'No Pagado')],
        string='Payment Status', default="unpaid")
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

    def action_assign_room(self):
        self.ensure_one()
        if self.status != "paid":
            raise UserError(_("You can't assign a room if it's not paid."))
        room_as_superuser = self.env['hostel.room'].sudo()

        room_rec = room_as_superuser.create({
            "name": "Room A-103",
            "room_no": "A-103",
            "floor_no": 1,
            "room_category_id": 37,  
            "hostel_id": self.hostel_id.id,
        })