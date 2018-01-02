from openerp import tools
from openerp import models,fields,api

class MetasventaDataReport(models.Model):
    _name ='metasventa.vendedoresreport'
    _auto = False

    id = fields.Integer()
    ano = fields.Integer()
    vendedor = fields.Char()

    
    def init(self,cr):
        tools.drop_view_if_exists(cr,self._table)
        cr.execute("""
                    create or replace view %s as (
                        select o.id,
                               29 as ano,
                               5 as vendedor 
                        from sale_order as o
                    )
                """ %(self._table))
