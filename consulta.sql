select
T.Nome, R.nome, T.TerminoReal as "Horario", Es.Descricao as 'local', EstruturaHierarquiaDescricao as 'Local completo'
from Tarefa T
join Estrutura Es on T.EstruturaId = Es.Id
join Recurso R on R.CodigoHash = T.FinalizadoPorHash
where EstruturaHierarquiaDescricao LIKE '%42610 %'
and T.Nome LIKE '%RONDA %'
and MONTH(TerminoReal) >= 01 
and MONTH(TerminoReal) <= 02 
and YEAR(TerminoReal) = 2024 
