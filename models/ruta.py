# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
 
class ruta(models.Model):
    _name = 'practicabusqueda.ruta'
    _description = 'practicabusqueda.ruta'

    siglas = fields.Char()
    name = fields.Char()
    