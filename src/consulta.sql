select T.Nome, R.Recurso, T.TerminoReal, R.PerguntaDescricao, R.Conteudo as 'Resposta'
from DW_Vista.dbo.FT_TAREFA T
inner join DW_Vista.dbo.FT_CHECKLIST_RESPOSTA_FULL R on R.TarefaId = T.Id
where T.Id = '05528461-54c4-4b2d-af23-d89ed47dbb71'
or T.Id = '69fbdfc5-7642-4369-bd77-e873201545da'


