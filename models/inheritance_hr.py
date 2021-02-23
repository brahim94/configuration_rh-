from odoo import api, fields, models, _


class EgovRhMaZone2(models.Model):
    _inherit = "egov_rh_ma.zone2"

    calcule_days = fields.Selection(readonly=True, default="ouvrable")

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    nom_arab = fields.Char('الاسم الكامل')
    echelle_id = fields.Many2one("egov_rh_ma.hr.echelle", string="Echelle")

class HrDepartment(models.Model):
    _inherit = "hr.department"

    department_arab = fields.Char('اسم الوحدة')

