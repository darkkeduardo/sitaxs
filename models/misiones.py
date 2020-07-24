# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
 
class misiones(models.Model):
    _name = 'practicabusqueda.misiones'
    _description = 'practicabusqueda.misiones'

    name = fields.Char()

    # MUCHOS A MUCHOS MANUAL 1
    aeronave_mision_ids = fields.One2many(
        string='Aeronave',
        comodel_name='practicabusqueda.pivot_aeronave_mision',
        inverse_name='mision_id',
    )
    
