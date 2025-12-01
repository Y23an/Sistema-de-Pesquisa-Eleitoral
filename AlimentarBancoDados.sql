-- =================================================================
-- 1. LIMPEZA TOTAL (Reinicia os IDs do 1)
-- =================================================================
TRUNCATE TABLE 
    resposta, 
    alternativa, 
    pergunta, 
    pesquisa, 
    entrevistado,
    candidato
RESTART IDENTITY CASCADE;

-- =================================================================
-- 2. INSERINDO 25 CANDIDATOS
-- Ajustado para: nome, partido, cargo
-- =================================================================

-- 5 Candidatos a Prefeito
INSERT INTO candidato (nome, partido, cargo) VALUES 
('Roberto Silva', 'MDB', 'Prefeito'),
('Ana Julia', 'PL', 'Prefeito'),
('Carlos Lupi', 'PT', 'Prefeito'),
('General Souza', 'REP', 'Prefeito'),
('Marina Verde', 'PV', 'Prefeito');

-- 20 Candidatos a Vereador
INSERT INTO candidato (nome, partido, cargo) VALUES 
('João do Caminhão', 'MDB', 'Vereador'), ('Maria da Saúde', 'MDB', 'Vereador'), ('Dr. Paulo', 'MDB', 'Vereador'),
('Sargento Rocha', 'PL', 'Vereador'), ('Pastora Sônia', 'PL', 'Vereador'), ('Kleber do Posto', 'PL', 'Vereador'),
('Professor Cláudio', 'PT', 'Vereador'), ('Lúcia Assistente', 'PT', 'Vereador'), ('Jovem Pedro', 'PT', 'Vereador'),
('Delegado Fonseca', 'REP', 'Vereador'), ('Irmã Dulce', 'REP', 'Vereador'), ('Empresário Beto', 'REP', 'Vereador'),
('Zé da Feira', 'PV', 'Vereador'), ('Bia dos Animais', 'PV', 'Vereador'), ('Ciclista André', 'PV', 'Vereador'),
('Dona Neide', 'PSD', 'Vereador'), ('Cantor Gil', 'PSD', 'Vereador'), ('Advogada Paula', 'PSDB', 'Vereador'),
('Médico Jorge', 'PSDB', 'Vereador'), ('Tiago do Esporte', 'PDT', 'Vereador');

-- =================================================================
-- 3. INSERINDO 25 ENTREVISTADOS
-- Ajustado para: nome, idade, genero, cidade
-- =================================================================
INSERT INTO entrevistado (nome, idade, genero, cidade) VALUES 
('Adriana Lima', 25, 'Feminino', 'Centro'), 
('Bernardo Alves', 34, 'Masculino', 'Zona Norte'), 
('Camila Rocha', 22, 'Feminino', 'Zona Sul'), 
('Diego Fernandes', 45, 'Masculino', 'Centro'), 
('Elaine Costa', 56, 'Feminino', 'Zona Leste'),
('Fabio Junior', 60, 'Masculino', 'Zona Oeste'), 
('Gustavo Mendes', 18, 'Masculino', 'Centro'), 
('Helena Martins', 29, 'Feminino', 'Zona Sul'), 
('Igor Santos', 31, 'Masculino', 'Zona Norte'), 
('Juliana Paes', 40, 'Feminino', 'Zona Oeste'),
('Kleber Machado', 55, 'Masculino', 'Centro'), 
('Larissa Manoela', 21, 'Feminino', 'Zona Sul'), 
('Marcos Mion', 42, 'Masculino', 'Zona Leste'), 
('Neymar Junior', 30, 'Masculino', 'Zona Norte'), 
('Olivia Palito', 33, 'Feminino', 'Centro'),
('Pedro Scooby', 35, 'Masculino', 'Zona Oeste'), 
('Quiteria Chagas', 38, 'Feminino', 'Zona Sul'), 
('Ronaldo Nazario', 44, 'Masculino', 'Zona Leste'), 
('Sabrina Sato', 41, 'Feminino', 'Centro'), 
('Thiago Leifert', 39, 'Masculino', 'Zona Norte'),
('Ursula Andress', 65, 'Feminino', 'Zona Oeste'), 
('Vinicius Junior', 23, 'Masculino', 'Centro'), 
('Wagner Moura', 46, 'Masculino', 'Zona Sul'), 
('Xuxa Meneghel', 59, 'Feminino', 'Zona Leste'), 
('Yasmin Brunet', 28, 'Feminino', 'Zona Norte');

-- =================================================================
-- 4. INSERINDO 2 PESQUISAS DISTINTAS
-- =================================================================
INSERT INTO pesquisa (titulo, data_inicio, data_fim, status, ativo) VALUES 
('Eleições 2025 - Intenção de Voto', '2025-09-01', '2025-10-01', 'aberta', TRUE), -- ID 1
('Avaliação da Gestão Municipal', '2025-08-01', '2025-12-31', 'aberta', TRUE);      -- ID 2

-- =================================================================
-- 5. INSERINDO 25 PERGUNTAS
-- =================================================================

-- --- PESQUISA 1: ELEIÇÕES (5 Perguntas) ---
INSERT INTO pergunta (pesquisa_id, texto, tipo) VALUES 
(1, 'Se a eleição fosse hoje, em quem você votaria para PREFEITO?', 'multipla_escolha'), -- ID 1
(1, 'E para VEREADOR, em quem você votaria?', 'multipla_escolha'),                      -- ID 2
(1, 'Em qual destes candidatos você JAMAIS votaria? (Rejeição)', 'multipla_escolha'),    -- ID 3
(1, 'Independente do seu voto, quem você acha que VAI ganhar?', 'multipla_escolha'),     -- ID 4
(1, 'Qual a principal qualidade que você busca num candidato?', 'aberta');               -- ID 5

-- --- PESQUISA 2: AVALIAÇÃO (20 Perguntas) ---
INSERT INTO pergunta (pesquisa_id, texto, tipo) VALUES 
(2, 'Como você avalia o serviço de SAÚDE pública?', 'multipla_escolha'),         -- ID 6
(2, 'Como você avalia a EDUCAÇÃO municipal?', 'multipla_escolha'),               -- ID 7
(2, 'Como você avalia a SEGURANÇA no seu bairro?', 'multipla_escolha'),          -- ID 8
(2, 'Como você avalia a LIMPEZA URBANA?', 'multipla_escolha'),                   -- ID 9
(2, 'Como você avalia a ILUMINAÇÃO PÚBLICA?', 'multipla_escolha'),               -- ID 10
(2, 'Como você avalia o TRANSPORTE PÚBLICO?', 'multipla_escolha'),               -- ID 11
(2, 'Como você avalia o estado do ASFALTO?', 'multipla_escolha'),                -- ID 12
(2, 'Como você avalia o TRÂNSITO na cidade?', 'multipla_escolha'),               -- ID 13
(2, 'Como você avalia as opções de LAZER?', 'multipla_escolha'),                 -- ID 14
(2, 'Como você avalia o incentivo ao ESPORTE?', 'multipla_escolha'),             -- ID 15
(2, 'Como você avalia o ATENDIMENTO na Prefeitura?', 'multipla_escolha'),        -- ID 16
(2, 'Como você avalia a TRANSPARÊNCIA dos gastos?', 'multipla_escolha'),         -- ID 17
(2, 'Como você avalia as OBRAS em andamento?', 'multipla_escolha'),              -- ID 18
(2, 'Como você avalia a GERAÇÃO DE EMPREGO?', 'multipla_escolha'),               -- ID 19
(2, 'Como você avalia o CUIDADO COM MEIO AMBIENTE?', 'multipla_escolha'),        -- ID 20
(2, 'Como você avalia a GESTÃO DA ÁGUA?', 'multipla_escolha'),                   -- ID 21
(2, 'Como você avalia o TURISMO na cidade?', 'multipla_escolha'),                -- ID 22
(2, 'Como você avalia o APOIO AO COMÉRCIO?', 'multipla_escolha'),                -- ID 23
(2, 'Você aprova a gestão do atual Prefeito?', 'multipla_escolha'),              -- ID 24
(2, 'Qual o maior problema do seu bairro hoje?', 'aberta');                      -- ID 25

-- =================================================================
-- 6. CRIANDO AS ALTERNATIVAS
-- =================================================================

-- Pergunta 1 (Prefeito)
INSERT INTO alternativa (pergunta_id, texto, candidato_id) 
SELECT 1, nome, id FROM candidato WHERE id BETWEEN 1 AND 5;
INSERT INTO alternativa (pergunta_id, texto, candidato_id) VALUES (1, 'Branco/Nulo', NULL), (1, 'Indeciso', NULL);

-- Pergunta 2 (Vereador)
INSERT INTO alternativa (pergunta_id, texto, candidato_id) 
SELECT 2, nome, id FROM candidato WHERE id BETWEEN 6 AND 25;
INSERT INTO alternativa (pergunta_id, texto, candidato_id) VALUES (2, 'Legenda', NULL);

-- Perguntas 6 a 23 (Avaliação Genérica)
INSERT INTO alternativa (pergunta_id, texto, candidato_id)
SELECT p.id, op.texto, NULL
FROM pergunta p
CROSS JOIN (VALUES ('Ótimo'), ('Bom'), ('Regular'), ('Ruim'), ('Péssimo')) AS op(texto)
WHERE p.id BETWEEN 6 AND 23;

-- Pergunta 24 (Aprovação)
INSERT INTO alternativa (pergunta_id, texto) VALUES (24, 'Aprovo'), (24, 'Desaprovo'), (24, 'Não sei opinar');

-- Pergunta 3 e 4 (Rejeição/Expectativa)
INSERT INTO alternativa (pergunta_id, texto, candidato_id) 
SELECT 3, nome, id FROM candidato WHERE id BETWEEN 1 AND 5;
INSERT INTO alternativa (pergunta_id, texto, candidato_id) 
SELECT 4, nome, id FROM candidato WHERE id BETWEEN 1 AND 5;

-- =================================================================
-- 7. GERANDO RESPOSTAS AUTOMÁTICAS
-- =================================================================

-- A) Prefeito (Pergunta 1)
INSERT INTO resposta (entrevistado_id, pergunta_id, alternativa_id, data_resposta, ativo)
SELECT 
    e.id, 
    1, 
    (SELECT id FROM alternativa WHERE pergunta_id = 1 ORDER BY RANDOM() LIMIT 1), 
    NOW(), 
    TRUE
FROM entrevistado e;

-- B) Vereador (Pergunta 2)
INSERT INTO resposta (entrevistado_id, pergunta_id, alternativa_id, data_resposta, ativo)
SELECT e.id, 2, (SELECT id FROM alternativa WHERE pergunta_id = 2 ORDER BY RANDOM() LIMIT 1), NOW(), TRUE
FROM entrevistado e;

-- C) Avaliação (Perguntas 6 a 23)
INSERT INTO resposta (entrevistado_id, pergunta_id, alternativa_id, data_resposta, ativo)
SELECT 
    e.id, 
    p.id, 
    (SELECT id FROM alternativa WHERE pergunta_id = p.id ORDER BY RANDOM() LIMIT 1), 
    NOW(), 
    TRUE
FROM entrevistado e
CROSS JOIN pergunta p
WHERE p.id BETWEEN 6 AND 23;

-- D) Respostas Abertas
INSERT INTO resposta (entrevistado_id, pergunta_id, texto_resposta, data_resposta, ativo)
SELECT e.id, 5, 'Melhorar a Saúde', NOW(), TRUE FROM entrevistado e WHERE e.id % 2 = 0;

INSERT INTO resposta (entrevistado_id, pergunta_id, texto_resposta, data_resposta, ativo)
SELECT e.id, 25, 'Buracos na rua', NOW(), TRUE FROM entrevistado e WHERE e.id % 3 = 0;