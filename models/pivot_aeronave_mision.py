# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

# MUCHOS A MUCHOS DE FORMA MANUAL 1
class pivot_aeronave_mision(models.Model):
    _name = 'practicabusqueda.pivot_aeronave_mision'
    _description = 'practicabusqueda.pivot_aeronave_mision'
    _rec_name = "mision_id"

    
    aeronave_id = fields.Many2one(
        string='Aeronave',
        comodel_name='practicabusqueda.aeronave',
        ondelete='restrict',
    )

    mision_id = fields.Many2one(
        string='Mision',
        comodel_name='practicabusqueda.misiones',
        ondelete='restrict',
    )
    

   