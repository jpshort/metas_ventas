#-*- coding: utf-8 -*-
from openerp import tools
from openerp import models,fields,api

class MetasventaDataReport(models.Model):
    _name ='metasventa.vendedoresreport'
#    _auto = False

 #   id  = fields.Integer()    
    ano = fields.Integer(string = "Año")
    mes = fields.Selection ([(1,'Enero'),
                             (2,'Febrero'),
                             (3,'Marzo'),
                             (4,'Abril'),
                             (5,'Mayo'),
                             (6,'Junio'),
                             (7,'Julio'),
                             (8,'Agosto'),
                             (9,'Septiembre'),
                             (10,'Octubre'),
                             (11,'Noviembre'),
                             (12,'Diciembre')]) # fields.Integer()
    name   = fields.Char(string="Vendedor")
    montofacturado = fields.Float(string="Monto Facturado")
    montometa      = fields.Float(string="Monto Pronosticado")
    logro          = fields.Float(string="% Logrado")

class MetasventaClientesReport(models.Model):
    _name ='metasventa.clientesreport'
    _auto = False

    id  = fields.Integer()    
    ano = fields.Integer(string = "Año")
    name   = fields.Char(string="Cliente")
    montofacturado = fields.Float(string="Monto Facturado")
    montometa      = fields.Float(string="Monto Pronosticado")
    logro          = fields.Float(string="% Logrado")

    def init(self,cr):
        tools.drop_view_if_exists(cr,self._table)
        cr.execute("""
                    create or replace view %s as (                        
                        select u.id, 
                               u.name as name,
                               m.ano as ano,                               
                               m.monto as montometa,
                               sum(i.amount_untaxed) as montofacturado,
                               sum((i.amount_untaxed/m.monto) * 100) as logro
                        from metasventa_metasclientes as m                        
                        join res_partner u 
                          on u.id = m.cliente
                        join account_invoice i 
                          on m.cliente = i.partner_id
                         and u.id  = i.partner_id
                         and i.state in ('paid','open')
                         and m.ano = extract(year from  i.date_invoice)::int
                        group by u.id,u.name,m.ano,m.monto
                          )
                """ %(self._table))
