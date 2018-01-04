from openerp import tools
from openerp import models,fields,api

class MetasventaDataReport(models.Model):
    _name ='metasventa.vendedoresreport'
    _auto = False

    id  = fields.Integer()    
    ano = fields.Integer()
    mes = fields.Integer()
    name   = fields.Char(string="Vendedor")
    montofacturado = fields.Float(string="Monto Facturado")
    montometa      = fields.Float(string="Monto Pronosticado")

    def init(self,cr):
        tools.drop_view_if_exists(cr,self._table)
        cr.execute("""
                    create or replace view %s as (                        
                        select u.id, 
                               u.login as name,
                               m.ano as ano,
                               m.mes as mes,
                               m.monto as montometa,
                               sum(i.amount_untaxed) as montofacturado
                        from metasventa_metasvendedores as m                        
                        join res_users u 
                          on u.id = m.vendedor
                        join account_invoice i 
                          on m.vendedor = i.user_id
                         and u.id  = i.user_id
                         and m.ano = extract(year from  i.date_invoice)::int
                         and m.mes = extract(month from  i.date_invoice)::int
                        group by u.id,u.login,m.ano,m.mes,m.monto
                          )
                """ %(self._table))

class MetasventaClientesReport(models.Model):
    _name ='metasventa.clientesreport'
    _auto = False

    id  = fields.Integer()    
    ano = fields.Integer()   
    name   = fields.Char(string="Cliente")
    montofacturado = fields.Float(string="Monto Facturado")
    montometa      = fields.Float(string="Monto Pronosticado")

    def init(self,cr):
        tools.drop_view_if_exists(cr,self._table)
        cr.execute("""
                    create or replace view %s as (                        
                        select u.id, 
                               u.name as name,
                               m.ano as ano,                               
                               m.monto as montometa,
                               sum(i.amount_untaxed) as montofacturado
                        from metasventa_metasclientes as m                        
                        join res_partner u 
                          on u.id = m.cliente
                        join account_invoice i 
                          on m.cliente = i.partner_id
                         and u.id  = i.partner_id
                         and m.ano = extract(year from  i.date_invoice)::int
                        group by u.id,u.name,m.ano,m.monto
                          )
                """ %(self._table))
