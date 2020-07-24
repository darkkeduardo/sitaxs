# -*- coding: utf-8 -*-
{
    'name': "practicabusqueda",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/aeronave.xml',
        'views/equipos.xml',
        'views/historial.xml',
        'views/parametros.xml',
        'views/pilotos.xml',
        'views/pvs.xml',
        'views/pvsinstr.xml',
        'views/traspasoaeronave.xml',
        'views/tripulantes.xml',
        'views/tipoaeronave.xml',
        'views/escuadron.xml',
        'views/ruta.xml',
        'views/misiones.xml',
        'views/pvs_detalle.xml',
        'views/ruta_pvs.xml',
        'views/report_view1.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
