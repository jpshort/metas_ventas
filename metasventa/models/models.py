# -*- coding: utf-8 -*-

from datetime import datetime
from openerp import models, fields, api


class MetasVendedores(models.Model):
    _name = 'metasventa.metasvendedores'

    ano = fields.Integer(string="Año",required=True,default=datetime.today().year )
   # mes = fields.Integer(string="Mes",required=True)
    vendedor = fields.Many2one('res.users',ondelete='set null',
               string="Vendedor",required = True)
    monto = fields.Float()
    mes = fields.Selection([
        ('1','Enero' ),
        ('2','Febrero'),
        ('3','Marzo'),
        ('4','Abril'),
        ('5','Mayo'),
        ('6','Junio'),
        ('7','Julio'),
        ('8','Agosto'),
        ('9','Septiembre'),
        ('10','Octubre'),
        ('11','Noviembre'),
        ('12','Diciembre')],required = True)

    _sql_constraints = [
        ('pk_ano_mes_vendedor',
         'UNIQUE(ano,mes,vendedor)',
         'El vendedor ya tiene meta asignada para este periodo')
    ]

class MetasClientes(models.Model):
    _name = 'metasventa.metasclientes'

    ano = fields.Integer(string="Año",required=True, default=datetime.today().year)     
    cliente = fields.Many2one('res.partner',string="Cliente",
       domain=[('customer','=',True)])
    monto = fields.Float()

    _sql_constraints = [
        ('pk_ano_cliente',
         'UNIQUE(ano,cliente)',
         'El cliente tiene ya meta establecida para este periodo')
    ]

