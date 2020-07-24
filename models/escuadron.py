# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
 
class escuadron(models.Model):
    _name = 'practicabusqueda.escuadron'
    _description = 'practicabusqueda.escuadron'

    siglas = fields.Char()
    name = fields.Char()
    
    
    aeronave_ids = fields.One2many(
        string='Aeronaves:',
        comodel_name='practicabusqueda.aeronave',
        inverse_name='escuadron_id',
    )
    