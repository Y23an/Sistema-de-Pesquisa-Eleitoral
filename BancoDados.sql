DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'status_enum') THEN
        CREATE TYPE status_enum AS ENUM ('aberta', 'encerrada');
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'tipo_enum') THEN
        CREATE TYPE tipo_enum AS ENUM ('multipla_escolha', 'aberta');
    END IF;
END
$$;


CREATE TABLE IF NOT EXISTS Pesquisa (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    status status_enum NOT NULL,
    ativo BOOLEAN DEFAULT TRUE
);


CREATE TABLE IF NOT EXISTS Candidato (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    partido VARCHAR(20) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    ativo BOOLEAN DEFAULT TRUE
);


CREATE TABLE IF NOT EXISTS Entrevistado (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    genero VARCHAR(20) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    ativo BOOLEAN DEFAULT TRUE
);


CREATE TABLE IF NOT EXISTS Pergunta (
    id SERIAL PRIMARY KEY,
    texto TEXT NOT NULL,
    tipo tipo_enum NOT NULL,
    pesquisa_id INT NOT NULL,
    ativo BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (pesquisa_id) REFERENCES Pesquisa(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Alternativa (
    id SERIAL PRIMARY KEY,
    texto TEXT NOT NULL,
    pergunta_id INT NOT NULL,
    candidato_id INT NULL,
    ativo BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (pergunta_id) REFERENCES Pergunta(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (candidato_id) REFERENCES Candidato(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Resposta (
    id SERIAL PRIMARY KEY,
    entrevistado_id INT NOT NULL,
    pergunta_id INT NOT NULL,
    alternativa_id INT NULL,
    texto_resposta TEXT NULL,
    data_resposta TIMESTAMP NOT NULL,
    ativo BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (entrevistado_id) REFERENCES Entrevistado(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (pergunta_id) REFERENCES Pergunta(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (alternativa_id) REFERENCES Alternativa(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);
