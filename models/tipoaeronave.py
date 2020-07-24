# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
 
class tipoaeronave(models.Model):
    _name = 'practicabusqueda.tipoaeronave'
    _description = 'practicabusqueda.tipoaeronave'

    name = fields.Char()

    
    aeronave_ids = fields.One2many(
        string='Aeronave',
        comodel_name='practicabusqueda.aeronave',
        inverse_name='tipoaeronave_id',
    )
    
    