from odoo import api, fields, models, _


class EgovRhMaZone2(models.Model):
    _inherit = "egov_rh_ma.zone2"

    calcule_days = fields.Selection(readonly=True, default="ouvrable")