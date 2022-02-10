# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError


class NewModule(models.Model):
    _inherit = 'hr.payslip'


    @api.multi
    def action_payslip_cancel(self):
        asiento=self.env['account.move'].search([('id','=',self.move_id.id)])
        asiento.button_cancel()
        if self.move_id.state=='posted':
            raise UserError(("Debe cancelar el asiento contable primero!"))
        return self.write({'state': 'draft'})