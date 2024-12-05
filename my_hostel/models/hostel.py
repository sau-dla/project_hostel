from odoo import fields, models, api

class Hostel(models.Model):
    _name = 'hostel.hostel' 
    _description = "Information about the hostel"
    _order = "id desc, name"
    _rec_name = 'city' 

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
                        help="Activar/Desactivar registro de hostal")
    other_info = fields.Text("Other Information",
                            help="Enter more information")
    description = fields.Html('Description')
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