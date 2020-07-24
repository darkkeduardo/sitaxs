# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
from string import ascii_letters, digits
import string 



class aeronave(models.Model):
    _name = 'practicabusqueda.aeronave'
    _description = 'practicabusqueda.aeronave'
    _order = 'name desc'
    # _rec_name = "name"

    name = fields.Char()

    observacion_seguro = fields.Text(
        string='Observaciones', size=250
    )

    tipo_seguro_id = fields.Many2one(
        string='Tipo de Seguro',
        comodel_name='practicabusqueda.seguro',
        ondelete='restrict',
    )
    radiograma_seguro = fields.Char(
        string="Radiograma", size=70)

    tipoaeronave_id = fields.Many2one(
        string='Tipo de aeronave:',
        comodel_name='practicabusqueda.tipoaeronave',
        ondelete='restrict',
    )

    escuadron_id = fields.Many2one(
        string='Escuadron asignado:',
        comodel_name='practicabusqueda.escuadron',
        ondelete='restrict',
    )

    fecha_adquisicion = fields.Date(
        string='Fecha adquisicion:',
        default=fields.Date.context_today,
    )

    escuadron_id = fields.Many2one(
        string='Escuadro asignado:',
        comodel_name='practicabusqueda.escuadron',
        ondelete='restrict',
    )

    equipos_ids = fields.One2many(
        string='Equipos',
        comodel_name='practicabusqueda.equipos',
        inverse_name='aeronave_id',
    )

    # MUCHOS A MUCHOS MANUAL 1
    mision_aeronave_ids = fields.One2many(
        string='Mision',
        comodel_name='practicabusqueda.pivot_aeronave_mision',
        inverse_name='aeronave_id',
    )
    # si funciona, TRAE EL CAMPO DE ALGO YA CREADO
    # prueba_related = fields.Char(related='escuadron_id.name', string='related pila', readonly=False, store=True)

    # rellenado de valores por defecto
    @api.model
    def default_get(self, fields):
        # lista_prueba =
        res = super(aeronave, self).default_get(fields)
        res['name'] = "HN-321"

        # res['escuadron_id']=1
        return res

    # ORDENAR ASCENDENTE O DESCENDENTE POR <NOMBRE><name> DE AERONAVE  ==>> mas sencillo y da el mismo resultado que esta funcion, es solo poner   _order='name'   ; en el xml dentro del field => context="{'order_display':}"/>

    def delete_line(self):
        raise ValidationError("aja")

    # Abrimos la vista historico
    def history_open_security_type(self):
        return {
            'name': ('Historico Tipo de Seguro'),
            'domain': [('aeronave_id', '=', self.id)],
            'res_model': 'practicabusqueda.historial',
            'view_id': False,
            'view_mode': 'tree',
            'type': 'ir.actions.act_window',
        }

    contador_historico = fields.Integer(
        string='Historico Tipo Seguro', compute="get_contador"
    )

    def get_contador(self):
        # hace referencia a un objeto y permite contar en base a un criterio
        contar = self.env['practicabusqueda.historial'].search_count(
            [('aeronave_id', '=', self.id)])
        self.contador_historico = contar

     # Ingreso del historico

    # Creando Historico
    @api.model
    def create(self, values):
        result = super(aeronave, self).create(values)
        listar = []
        for item in result.equip_adicional_ids:
            listar.append(item.name)
        # self.env['practicabusqueda.historial'].create(
        #     {'equipamento_adicional': str(listar), 'aeronave_id': result.id})
        vals = {
            'tipo_seguro_id': values['tipo_seguro_id'],
            'radiograma_seguro': values['radiograma_seguro'],
            'observacion_seguro': values['observacion_seguro'],
            'aeronave_id': result.id,
        }
        self.env['practicabusqueda.historial'].create(vals)
        return result

    # Modificacion del historico
    def write(self, values):
        result = super(aeronave, self).write(values)
        if 'equip_adicional_ids' in values:
            listar = []
            for item in self.equip_adicional_ids:
                listar.append(item.name)
            vals = {
                'equipamento_adicional': str(listar), 'aeronave_id': self.id,
                'tipo_seguro_id': values['tipo_seguro_id'],
                'radiograma_seguro': values['radiograma_seguro'],
                'observacion_seguro': values['observacion_seguro'],
                
            }
            self.env['practicabusqueda.historial'].create(vals)
        return result

    equip_adicional_ids = fields.Many2many(
        string='Equipos Adicionales', comodel_name='practicabusqueda.equipos',
        relation='practicabusqueda_equipos_aeronave_rel', column1='aeronave_id', column2='equipos_id')




         
   
    warning = {'title': 'Advertancia!', 'message' : 'Your message.' }
   
    @api.onchange('radiograma_seguro',)
    def _name_validation_name(self):
        flag=False            
        if set(str(self.radiograma_seguro)).difference(ascii_letters + digits + '-'):
            self.warning['message'] ="Caracteres Invalidos en campo RADIOGRAMA DE CAMBIO DE SEGURO"      
            flag=True
            self.radiograma_seguro=""   
        if flag:                                 
            return {'warning': self.warning}
    


    
    _sql_constraints = [('name', 'unique(name)', 'Estas guardando una informacion ya existente en la BD')]