# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
 
class tripulantes(models.Model):
    _name = 'practicabusqueda.tripulantes'
    _description = 'practicabusqueda.tripulantes'

    name = fields.Char()