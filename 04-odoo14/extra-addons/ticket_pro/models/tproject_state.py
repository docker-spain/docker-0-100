# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class TprojectState(models.Model):
    _description = "Tproject State"
    _name = 'tproject.state'
    _inherit = ['mail.activity.mixin', 'mail.thread']
    _order = 'id desc'

    name = fields.Char('Name', default="Etapa 01", copy=False)