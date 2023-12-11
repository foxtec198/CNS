use dw_vista
SELECT T.[Status], T.Nome, T.TerminoReal, R.Recurso as Supervisor, Es.Descricao as 'Local' 
from FT_TAREFA T
inner join DM_ESTRUTURA Es on Es.Id_Estrutura = T.Id_Estrutura
inner join FT_CHECKLIST_RESPOSTA_FULL R on R.TarefaId = T.Id
inner join DM_SERVICO Sv on Sv.Id_Servico = T.Id_Servico
where Es.CRno = 42636
and Sv.Servico LIKE '%VISITA%'
and MONTH(TerminoReal) >= 8
and MONTH(TerminoReal) <= 10
ORDER BY TerminoReal DESC
