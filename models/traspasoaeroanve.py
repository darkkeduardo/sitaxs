# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
 
class traspasoaeronave(models.Model):
    _name = 'practicabusqueda.traspasoaeronave'
    _description = 'practicabusqueda.traspasoaeronave'

    name = fields.Char()