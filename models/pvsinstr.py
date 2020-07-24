# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
 
class pvsinstr(models.Model):
    _name = 'practicabusqueda.pvsinstr'
    _description = 'practicabusqueda.pvsinstr'

    name = fields.Char()