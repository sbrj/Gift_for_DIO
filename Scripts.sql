SELECT nome, cidade, estado, usuario
FROM devs_csv;

SELECT count(*) qnt, cidade, estado 
from devs_csv dc 
WHERE cidade != ''
group by cidade, estado 
order by qnt desc

SELECT count(*) qnt, estado 
from devs_csv dc 
WHERE estado != ''
group by estado 
order by qnt desc

SELECT dc.*, pc.pontos 
from devs_csv dc 
left join pontos_csv pc 
	on dc.usuario = pc.nome 
order by pontos ASC 

select dc.*, pc.pontos 
from devs_csv dc 
left join pontos_csv pc 
	on dc.usuario = pc.nome 
WHERE cidade = 'Ipatinga'
order by pontos DESC 

select dc.*, pc.pontos 
from devs_csv dc 
left join pontos_csv pc 
	on dc.usuario = pc.nome 
WHERE cidade = 'Rio de Janeiro'
order by pontos DESC 

with qt as (
	SELECT dc.nome, COUNT(*) quantidade 
	from devs_csv dc 
	left join pontos_csv pc on dc.usuario = pc.nome 
	where pc.pontos > 1200
)
select quantidade, sum(pc.pontos)/quantidade media 
from devs_csv dc 
left join qt on qt.nome = dc.nome 
left join pontos_csv pc on dc.usuario = pc.nome

select count(*) Qnt, cidade, estado, sum(pc.pontos) soma_pontos 
from devs_csv dc 
left join pontos_csv pc on dc.usuario = pc.nome 
where cidade != ''
group by cidade, estado 
ORDER by soma_pontos desc 