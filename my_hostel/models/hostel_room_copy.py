from odoo import fields, models, api, _

class HostelRoomCopy(models.Model):
    _name = "hostel.room.copy"
    _inherit = "hostel.room"
    _description = "Hostel Room Information Copy"

    amenity_ids = fields.Many2many("hostel.amenities",
    "hostel_room_amenities_copy", "room_id", "amenitiy_id",
    string="Amenities", domain="[('active', '=', True)]",
    help="Select hostel room amenities")
