from odoo import fields, models

class HostelTermination(models.Model):
    _name = 'hostel.termination'
    _description = 'Hostel Termination'

    room_id = fields.Many2one('hostel.room', string='Room')
    termination_date = fields.Date(string='Termination Date')
    reason = fields.Text(string='Reason')

    from odoo import fields, models

class HostelTermination(models.Model):
    _name = 'hostel.termination'
    _description = 'Hostel Termination'

    room_id = fields.Many2one('hostel.room', string='Room')
    termination_date = fields.Date(string='Termination Date')
    reason = fields.Text(string='Reason')

    