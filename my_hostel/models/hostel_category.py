from odoo import models, fields, api, exceptions

class HostelCategory(models.Model):
    _name = "hostel.category"
    _description = "Hostel category Information"  
    _parent_store = True
    _parent_name = "parent_id"

    name = fields.Char(string='Name_category', required=True, translate=True)
    parent_path = fields.Char(index=True)
    parent_id = fields.Many2one('hostel.category', string='Parent Category', ondelete='cascade')
    child_ids = fields.One2many('hostel.category', 'parent_id', string='Child Categories')
    active = fields.Boolean(string='Active', default=True)
    description = fields.Char(string="information")

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise exceptions.ValidationError('Error! You cannot create recursive categories.')

    def create_categories(self):
        """Creates a parent category with two child categories."""
        parent_category_val = {
            'name': 'Main category',
            'description': 'Description for parent category',
            'child_ids': [
                (0, 0, {'name': 'Child category 1', 'description': 'Description for child 1'}),
                (0, 0, {'name': 'Child category 2', 'description': 'Description for child 2'}),
            ]
        }
        record = self.env['hostel.category'].create(parent_category_val)
        return record