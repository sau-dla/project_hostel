from odoo import fields, models, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
import requests

class Hostel(models.Model):
    _name = 'hostel.hostel' 
    _description = "Information about the hostel"
    _order = "id desc, name"
    _rec_name = 'name' 

    name = fields.Char(string="Hostel name", required=True)
    hostel_code = fields.Char(string="Code", required=True)
    street = fields.Char('Street')
    street2 = fields.Char('Street 2')
    zip = fields.Char('Zip code', change_default=True)
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')
    image = fields.Binary(string="Image", attachment=True)
    mobile = fields.Char('Cellular', required=True)
    email = fields.Char('Email')
    active = fields.Boolean("Active", default=True,
                        help="Activate/Deactivate hostel registration")
    other_info = fields.Text("Other Information",
                            help="Enter more information")
    description = fields.Html('Description')

    category_id = fields.Many2one('hostel.category',
    string="Category", help="Enter category")

    hostel_rating = fields.Float('Average Hostel Rating',
                                digits=(14, 4)) 
    display_name = fields.Char(string='Display name', compute='_compute_display_name', store=True)
    currency_id = fields.Many2one('res.currency', string='currency')
    
    @api.depends('hostel_code')
    def _compute_display_name(self):
            for record in self:
                name = record.name
            if record.hostel_code:
                name = f'{name} ({record.hostel_code})'
            record.display_name = name
    
    @api.model
    def _referencable_models(self):
        models = self.env['ir.model'].search([
            ('field_id.name', '=', 'message_ids')
        ])
        return [(x.model, x.name) for x in models]
    
    ref_doc_id = fields.Reference(
        selection='_referencable_models',
        string='Reference document'
    )
    
    def post_to_webservice(self, data):
        try:
            req = requests.post('http://my-test-service.com', data=data, timeout=10)
            content = req.json()
        except IOError:
            error_msg = _("Something went wrong while sending data")
            raise UserError(error_msg)
        return content