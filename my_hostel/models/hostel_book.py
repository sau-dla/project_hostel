from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"
    is_hostel_rector = fields.Boolean("Director del Albergue",
                        help="Activar si la siguiente persona es director del albergue")
    assign_room_ids = fields.Many2many('library.book', string='Libros Autorizados') 
    count_assign_room = fields.Integer('Número de Libros Autorizados', compute="_compute_count_room")

    @api.depends('assign_room_ids')
    def _compute_count_room(self):
        for partner in self:
            partner.count_assign_room = len(partner.assign_room_ids)