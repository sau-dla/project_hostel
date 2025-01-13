from odoo import models, fields, api
from datetime import timedelta

class AssignRoomStudentWizard(models.TransientModel):
    _name = 'assign.room.student.wizard'
    _description = 'Assign room student information' 

    name_student = fields.Char(string='Student Name')
    room_id = fields.Many2one("hostel.room", "Room",
                            help="Select hostel room")
    hostel_id = fields.Many2one("hostel.hostel", related='room_id.hostel_id')

    admission_date = fields.Date(
        "Admission Date",
        help="Date of admission in hostel",
        default=fields.Datetime.today,
    )

    def add_room_in_student(self):
        hostel_room_student = self.env['hostel.student'].browse(
            self.env.context.get('active_id'))
        if hostel_room_student:
            hostel_room_student.update({
                'hostel_id': self.room_id.hostel_id.id,
                'room_id': self.room_id.id,
                'admission_date': fields.Date.today(),
            })