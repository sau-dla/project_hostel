from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"
    is_hostel_rector = fields.Boolean("Hostel Director",
                        help="Activate if the following person is the hostel director")
    assign_room_ids = fields.Many2many('hostel.room', string="Assigned Rooms" )
    count_assign_room = fields.Integer('Number of Authorized Books', compute="_compute_count_room")

    @api.depends('assign_room_ids')
    def _compute_count_room(self):
        for partner in self:
            partner.count_assign_room = len(partner.assign_room_ids)