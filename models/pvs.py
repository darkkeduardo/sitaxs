# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)


class pvs(models.Model):
    _name = 'practicabusqueda.pvs'
    _description = 'practicabusqueda.pvs'

    # Semana del 1 al 7 de junio
    name = fields.Char(
        string='field_name',
    ) 
    # AERONAVE
    escuadron_id = fields.Many2one(
        string='Escuadron:',
        comodel_name='practicabusqueda.escuadron',
        ondelete='restrict',
    )
    # FECHA INICIO
    fecha_inicio = fields.Date(
        string='Fecha Inicio:',
        default=fields.Date.context_today,
    )
    # FECHA FIN
    fecha_fin = fields.Date(
        string='Fecha Fin:',
        default=fields.Date.context_today,
    )
    # relacionando con cabecera - >detalle< -
    pvs_detalle_ids = fields.One2many(
        string='PVS Detalle',
        comodel_name='practicabusqueda.pvs_detalle',
        inverse_name='pvs_id',
    )

    # relacionando con cabecera - >detalle REGISTRO DE HORAS DE VUELO< -
    pvs_detalle_ids2 = fields.One2many(
        string='PVS Detalle',
        comodel_name='practicabusqueda.pvs_detalle',
        inverse_name='pvs_id',
    )
    # 2 ejemplos con related
    # si funciona
    # relacionando directamente un campo de otro lado
    prueba_relatedMo2 = fields.Many2one(
        string='ree',
        comodel_name='practicabusqueda.aeronave',
        ondelete='restrict',
        related='pvs_detalle_ids.aeronave_id',
        readonly=False,
        store=True,
        # si funciona
        # domain=[('id','=','1')]
    )
    prueba2_relatedMo2 = fields.Many2many(
        string='field_name',
        comodel_name='practicabusqueda.pilotos',
        relation='practicabusqueda_pvs_pilotos_rel',
        column1='pvs_id',
        column2='pilotos_id',
        related='pvs_detalle_ids.pvs_pilotos_ids',
        readonly=False,
    )
    # ESTADOS DE FIRMA
    state = fields.Selection(
        string='State',
        selection=[('activo', 'Activo'), ('aprobar1', 'Operaciones'),  ('aprobar2', 'Comandante'),  ('aprobar3', 'Operaciones COAVNA'),  ('aprobar4', 'Comandante COAVNA')],
        default='activo',
        readonly=True,
    )
    
    
    def action_aprobar0(self):
        self.write({'state': 'aprobar1'})
    
    def action_aprobar1(self):
        self.write({'state': 'aprobar2'})
    
    def action_aprobar2(self):
        self.write({'state': 'aprobar3'})
    
    def action_aprobar3(self):
        self.write({'state': 'aprobar4'})
    
    # VALORES POR DEFECTO PVS
    @api.model
    def default_get(self, fields):
        res = super(pvs, self).default_get(fields)
        pvs_detalle_ids =[(5,0,0)]
        pvs_detalle_rec = self.env['practicabusqueda.pvs_detalle'].search([]) # O2M a recorrer
        # var = str(pvs_detalle_rec[-1].fecha)
        # d = var.split('-')
        # raise ValidationError("LOS NOMBRES SON {}".format(d[2]))

        for detalle in pvs_detalle_rec:
            line = (0,0,{
                # campos de la clase pvs_detalle
                'fecha': detalle.fecha,
                'hora': detalle.hora,
                # 'aeronave_id': detalle.aeronave_id
                
            })
            pvs_detalle_ids.append(line)
        res.update({
            'pvs_detalle_ids': pvs_detalle_ids,
            
            'fecha_inicio': '07/06/2020',
            'fecha_fin': '07/12/2020',
            'name': 'SEMANA DEL AL '
        })
        
        return res
        
    