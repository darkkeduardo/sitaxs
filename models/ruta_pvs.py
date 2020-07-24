# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class ruta_pvs(models.Model):
    _name = 'practicabusqueda.ruta_pvs'
    _description = 'practicabusqueda.ruta_pvs'

    _rec_name = "ruta_id"
    # para que no me salga el nombredelmodulo,1 sino el dato que quiero

    ruta_id = fields.Many2one(
        string='ruta inicio',
        comodel_name='practicabusqueda.ruta',
    )

    ruta2_id = fields.Many2one(
        string='ruta Fin',
        comodel_name='practicabusqueda.ruta',
    )
  
    pvs_detalle_id = fields.Many2one(
        string='detalle ruta',
        comodel_name='practicabusqueda.pvs_detalle',
        ondelete='cascade',
    )
    

    def name_get(self):
        result = []
        for rec in self:
            # name = rec.ruta2_id.name
            if rec.ruta_id:
                result.append((rec.id, "%s-%s" %
                              (rec.ruta_id.name, rec.ruta2_id.name)))
            #     name = rec.ruta_id.name + '-' + name
            # result.append((rec.id, name))
        return result

    
    @api.model
    def name_search(self, name, args=None, operator='=', limit=100):
        args = args or []
        domain = []
        if name:
            domain = [
                '|', ('rec.ruta_id.name', '=ilike', name), ('rec.ruta_id.name', operator, name)
            ]
      
        records = self.search(domain + args, limit=limit)
        return records.name_get()
    