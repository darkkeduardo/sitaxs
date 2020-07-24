# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class historial(models.Model):
    _name = 'practicabusqueda.historial'
    _description = 'practicabusqueda.historial'

    # name = fields.Char()

    # tipo_seguro_id = fields.Many2one(string='Tipo de Seguro', comodel_name='flight.items',
    #                                  ondelete='restrict', domain="[('catalogo_id', '=', 8)]",)
    
    tipo_seguro_id = fields.Many2one(
        string='Tipo de Seguro',
        comodel_name='practicabusqueda.seguro',
        ondelete='restrict',
    )    
    radiograma_seguro = fields.Char(
        string="Radiograma", size=70)

    observacion_seguro = fields.Text(
        string="Observaciones", size=250)

    aeronave_id = fields.Many2one(
        string='Aeronave', comodel_name='practicabusqueda.aeronave', ondelete='cascade',)

    equipamento_adicional= fields.Text(string="Equipamento Adicional" , size=250 )

    warning = {'title': 'Advertencia!', 'message': 'Your message.'}
