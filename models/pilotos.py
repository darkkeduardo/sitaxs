# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
 
class pilotos(models.Model):
    _name = 'practicabusqueda.pilotos'
    _description = 'practicabusqueda.pilotos'
    _rec_name="lastname"
    _order='id desc'

    name = fields.Char()
    lastname = fields.Char()
    cedula = fields.Char()
