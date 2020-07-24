# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
 
class ruta2(models.Model):
    _name = 'practicabusqueda.ruta2'
    _description = 'practicabusqueda.ruta2'

    siglas = fields.Char()
    name = fields.Char()
    