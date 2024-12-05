from odoo import models, fields, api

class HostelCategory(models.Model):
    _name = "hostel.category"
    _description = "Hostel category Information"  
    _parent_store = True
    _parent_name = "parent_id"

    name_category = fields.Char(string='Name_category', required=True, translate=True)
    parent_path = fields.Char(index=True)
    parent_id = fields.Many2one('hostel.category', string='Parent Category', ondelete='cascade')
    child_ids = fields.One2many('hostel.category', 'parent_id', string='Child Categories')
    active = fields.Boolean(string='Active', default=True)
    description = fields.Html('Description')
    room_id = fields.Many2one("hostel.room", "Room",
                            help="Select hostel room")
    hostel_id = fields.Many2one("hostel.hostel", related='room_id.hostel_id')

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError(
                'Error! You cannot create recursive categories.')