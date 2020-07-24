# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class pvs_detalle(models.Model):
    _name = 'practicabusqueda.pvs_detalle'
    _description = 'practicabusqueda.pvs_detalle'
    _order = 'fecha,hora'

    fecha = fields.Date(
        string='Fecha',
        default=fields.Date.context_today,
    )

    hora = fields.Float(
        string='Hora',
    )
    # AERONAVE
    aeronave_id = fields.Many2one(
        string='AN/HN',
        comodel_name='practicabusqueda.aeronave',
        ondelete='restrict',
    )
    # PILOTO
    pvs_pilotos_ids = fields.Many2many(
        string='Pilotos',
        comodel_name='practicabusqueda.pilotos',
        relation='practicabusqueda_pvs_pilotos_rel',
        column1='pvs_id',
        column2='pilotos_id',
    )
    # MISION
    pvs_pivot_aeronave_mision_ids = fields.Many2many(
        string='Mision',
        comodel_name='practicabusqueda.pivot_aeronave_mision',
        relation='practicabusqueda_pvs_pivot_aeronave_mision_rel',
        column1='pvs_id',
        column2='pivot_aeronave_mision_id',
    )

    descripcion = fields.Char()

    # RELACION CON PVS
    pvs_id = fields.Many2one(
        string='Plan de Vuelo Cabeza',
        comodel_name='practicabusqueda.pvs',
        ondelete='cascade',
    )
    # RUTAS
    ruta_pvs_ids = fields.One2many(
        string='Ruta',
        comodel_name='practicabusqueda.ruta_pvs',
        inverse_name='pvs_detalle_id',        
    )
