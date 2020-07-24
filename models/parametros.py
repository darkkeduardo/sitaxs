# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
 
class parametros(models.Model):
    _name = 'practicabusqueda.parametros'
    _description = 'practicabusqueda.parametros'

    name = fields.Char()