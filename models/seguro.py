# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
 
class seguro(models.Model):
    _name = 'practicabusqueda.seguro'
    _description = 'practicabusqueda.seguro'
    _rec_name = "nombre"

    nombre = fields.Char()
    
    