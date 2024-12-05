from odoo import models, fields

class HostelAmenities(models.Model):
    _name = "hostel.amenities"
    _description = "Hostel Amenities"

    name = fields.Char("Name", help="Provided Hostel Amenity")
    active = fields.Boolean("Active", help="Activate/Deactivate whether the amenity should begiven or not")

    hostel_id = fields.Many2one("hostel.hostel", "hostel",
    help="Name of hostel")