# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HsCode(models.Model):
    _name = 'import.line'
    _description = 'Line Master'

    expense_type = fields.Selection(selection=[('amount', 'Amount'), ('percentage', 'Percentage')],
                                    string='Type', defauilt='amount')
    expense_value = fields.Float(string='Value')
    import_product_id = fields.Many2one('product.product', 'name', required=False)
    expense_amount = fields.Float(string='Amount', readonly=True)
    # code_relation = fields.Many2one('import.code', string="Relation")


class HsCode(models.Model):
    _name = 'import.code'
    _description = 'HSCode Master Data'
    _rec_name = 'code_name'

    code_name = fields.Char(string='Name', required=True)
    code_expenses = fields.One2many('import.line', 'import_product_id', string='Expenses')


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    hsNumber = fields.Many2one('import.code', string='HsCode')


class ProductTemplateInherit(models.Model):
    _inherit = 'purchase.order.line'

    @api.onchange('product_id')
    def set_hs_code(self):
        for rec in self:
            if rec.product_id:
                rec.hsNumber = rec.product_id.hsNumber
                print("hsNumber", rec.hsNumber)

    @api.onchange('product_id')
    def set_amount(self):
        for rec in self:
            hs_line = self.env['purchase.order.line'].search([('hsNumber.id', '=', rec.hsNumber.id)])
            rec.amount = rec.hsNumber.code_expenses.expense_value

    hsNumber = fields.Many2one('import.code', string='HsCode')
    amount = fields.Float(string='Amount', readonly=True, compute="set_amount")








