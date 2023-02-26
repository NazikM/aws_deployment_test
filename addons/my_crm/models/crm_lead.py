from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    telegram_nickname = fields.Char(string='Telegram Nickname')
    telegram_avatar = fields.Binary(string='Telegram Avatar')

    @api.model_create_multi
    def create(self, vals_list):
        opportunities = super().create(vals_list)
        print(opportunities)
        return opportunities
