select R.Nome as Sup, COUNT(R.Nome)  as Realizado, DAY(TerminoReal) as Dia
from Tarefa T
inner join Recurso R on R.CodigoHash = T.FinalizadoPorHash
inner join dw_vista.dbo.DM_Estrutura Es on Es.Id_Estrutura = T.EstruturaId
inner join dw_vista.dbo.DM_CR c on c.Id_cr = Es.Id_cr
where c.Gerente = 'DENISE DOS SANTOS DIAS SILVA'
and T.Nome LIKE '%Visita %' 
and month(Disponibilizacao) = 01
and YEAR(T.Disponibilizacao) = 2024
GROUP BY R.Nome, DAY(TerminoReal)
ORDER BY DAY(TerminoReal)