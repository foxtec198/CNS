-- select 
-- T.Id,
-- T.ChecklistId,
-- T.Nome,
-- T.Descricao,
-- T.Numero,
-- T.Escalonado,
-- T.Prazo,
-- T.Disponibilizacao,
-- T.InicioReal,
-- T.TerminoReal,
-- T.ServicoDescricao,
-- R.Nome as 'Colaborador',
-- Es.Descricao as 'Local',
-- Es.HierarquiaDescricao,
-- E.Longitude,
-- E.Latitude,
-- E.PerguntaDescricao as 'Pergunta',
-- E.Conteudo as 'Resposta'
-- from Tarefa T
-- inner join Execucao E
--     on E.TarefaId = T.Id
-- inner join Recurso R
--     on R.CodigoHash = T.FinalizadoPorHash
-- inner join Estrutura Es
--     on Es.Id = T.EstruturaId
-- where 
--     T.EstruturaNivel1 LIKE '%189535 -%'
-- and
--     T.ChecklistId IN (
--         'd93f3b97-e34b-4d6c-8912-64ea8c4f7856',
--         '3db0310c-7827-4fdc-ae74-751e5af7c6ac',
--         'ccba2b1e-5ab7-4ec9-9912-f0365b466203'
--     )


select top 1 T.EstruturaNivel1 from Tarefa T
where T.EstruturaNivel1 LIKE '%189535 -%'