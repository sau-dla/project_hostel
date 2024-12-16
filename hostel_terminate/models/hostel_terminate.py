from odoo import fields, models, api

class HostelTerminate(models.Model):
    _inherit = 'hostel.room'
    date_terminate = fields.Date('Date of Termination')
