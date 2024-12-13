from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
from datetime import timedelta

class HostelRoom(models.Model):
    _name = "hostel.room"
    _inherit = ['base.archive']
    _description = "Hostel Room Information" 
    _rec_name_search = ['room name', 'room state', 'rent amount']
    
    room_name = fields.Char('Room Name')

    room_number = fields.Char(
        'Room No.')

    floor_number = fields.Char(
        'FLoor No.', help="Enter the floor number")
                            
    state = fields.Selection([
        ('draft', 'Unavailable'),
        ('available', 'Available'),
        ('closed', 'Closed')],
        'State', default="draft")

    currency_id = fields.Many2one('res.currency',
    string='Currency')

    rent_amount = fields.Monetary(
        'Rent Amount', help="Enter the floor number")

    hostel_id = fields.Many2one("hostel.hostel", "hostel",
    help="Name of hostel")

    category_id = fields.Many2one('hostel.category',
    string="Category", help="Enter category")

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
                new_discharge_date = record.admission_date + timedelta(days=record.duration)
                if new_discharge_date != record.discharge_date:
                    record.discharge_date = new_discharge_date.strftime('%Y-%m-%d')

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft', 'available'),
                ('available', 'closed'),
                ('closed', 'draft')] 
        return (old_state, new_state) in allowed

    def change_state(self, new_state):
        for room in self:
            if room.is_allowed_transition(room.state, new_state):
                room.state = new_state
            else:
                msg = _('Moving from %s to %s is not allowed') % (room.state, new_state) 
                raise UserError(msg)
                
    def make_available(self):
        self.change_state('available')

    def make_closed(self):
        self.change_state('closed')  

    def log_all_room_members(self):
        hostel_room_obj = self.env['hostel.student']
        all_members = hostel_room_obj.search([])
        print("ALL MEMBERS:", all_members)
        return True

    def update_room_number(self):
        self.ensure_one()
        self.room_number = "RM002"

    def find_room(self):
        """
        Finds rooms that match the specified criteria.
        """
        domain = [
            '|', 
                '&', ('room_name', 'ilike', 'Room 1'), ('category_id.name', 'ilike', 'Category 1'),
                '&', ('room_name', 'ilike', 'Room 2'), ('category_id.name', 'ilike', 'Category 2')
            ]
        rooms = self.search(domain)           
        return rooms

    def find_partner(self):
        """
        Finds partners that match the specified criteria.
        """
        PartnerObj = self.env['res.partner'] 
        domain = [
            ('name', 'ilike', 'SerpentCS'), 
            ('company_id.name', '=', 'SCS') 
        ]
        partners = PartnerObj.search(domain)
        return partners
        
    def get_rooms_with_kitchen_and_balcony(self):
        """
        Finds all rooms that have both a kitchen and a balcony.
        """
        rooms_with_kitchen = self.search([('amenity_ids', 'in', self.env['hostel.amenities'].search([('name', '=', 'Kitchen')]).ids)])
        rooms_with_balcony = self.search([('amenity_ids', 'in', self.env['hostel.amenities'].search([('name', '=', 'Balcony')]).ids)])

        rooms_with_both = rooms_with_kitchen & rooms_with_balcony 
        return rooms_with_both

    def filter_rooms_with_multiple_members(self):
        all_rooms = self.search([])
        filtered_rooms = self.get_rooms_with_multiple_members(all_rooms)
        return filtered_rooms

    @api.model
    def get_rooms_with_multiple_members(self, all_rooms):
        def predicate(room):
            if len(room.student_ids) > 1:
                return True
            return False
        return all_rooms.filtered(predicate) 

    @api.model
    def sort_rooms_by_rating(self, rooms):
        return rooms.sorted(key='room_rating')