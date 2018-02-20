drop view metasventa_vendedoresreport;


create or replace function trg_metas_vendedores_stat() 
returns trigger as $trg_metas_vendedores_stat$
declare
    cc record;
begin

  execute 'truncate table metasventa_vendedoresreport';

  for cc in  select u.id, 
                    u.login as name,
                    m.ano as ano,
                    m.mes as mes,
                    m.monto as montometa,
                    sum(i.amount_untaxed) as montofacturado,                              
                    sum((i.amount_untaxed/m.monto) * 100) as logro
               from metasventa_metasvendedores as m                        
                    join res_users u on u.id = m.vendedor
                    join account_invoice i on m.vendedor = i.user_id
                and u.id  = i.user_id
                and i.state in ('paid','open')
                and m.ano = extract(year from  i.date_invoice)::int
                and m.mes = extract(month from  i.date_invoice)::int
              group by u.id,u.login,m.ano,m.mes,m.monto  loop
			  
			 insert into metasventa_vendedoresreport
			            (name,ano,mes,montometa, montofacturado,logro)
			      values(cc.name,cc.ano,cc.mes,cc.montometa,cc.montofacturado,cc.logro);	   
			 
   end loop;

   return null;
   
 end;
$trg_metas_vendedores_stat$ language plpgsql;


create trigger trg_metas_vendedores_stat after insert or update or delete on account_invoice
  for each row execute procedure trg_metas_vendedores_stat();




