# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class equipos(models.Model):
    _name = 'practicabusqueda.equipos'
    _description = 'practicabusqueda.equipos'

    name = fields.Char()

    aeronave_id = fields.Many2one(
        string='Aeronave',
        comodel_name='practicabusqueda.aeronave',
        ondelete='restrict',
    )
    