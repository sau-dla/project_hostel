from odoo import models, fields, api

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

    category_id = fields.Many2one('hostel.category',
    string="Category", help="Enter category")

    hostel_id = fields.Many2one("hostel.hostel", "hostel",
    help="Name of hostel")

    student_ids = fields.One2many("hostel.student", "room_id",
    string="Student", help="Enter student")

    amenity_ids = fields.Many2many("hostel.amenities",
    "hostel_room_amenities_rel", "room_id", "amenitiy_id",
    string="Amenities", domain="[('active', '=', True)]",
    help="Select hostel room amenities")

    student_per_room = fields.Integer("Student Per Room", required=True, help="Students allocated per room")
    
    availability = fields.Integer(compute="_compute_check_availability", store=True, string="Availability", help="Room availability in hostel")
    admission_date = fields.Date(
        "Admission Date",
        help="Date of admission in hostel",
        default=fields.Datetime.today,
    )
    discharge_date = fields.Date("Discharge Date", help="Date on which student discharge")
    duration = fields.Integer(
        "Duration", compute="_compute_check_duration", inverse="_inverse_duration", help="Enter duration of living"
    )

    @api.depends("student_per_room", "student_ids")
    def _compute_check_availability(self):
        """Method to check room availability"""
        for rec in self:
            rec.availability = rec.student_per_room - len(rec.student_ids.ids)

    @api.depends("admission_date", "discharge_date")
    def _compute_check_duration(self):
        """Method to check duration based on admission and discharge dates."""
        for record in self:
            if record.discharge_date and record.admission_date:
                record.duration = (record.discharge_date - record.admission_date).days

    def _inverse_duration(self):
        for record in self:
            if record.admission_date and record.duration:
                from datetime import timedelta
                new_discharge_date = record.admission_date + timedelta(days=record.duration)
                if new_discharge_date != record.discharge_date:
                    record.discharge_date = new_discharge_date.strftime('%Y-%m-%d')