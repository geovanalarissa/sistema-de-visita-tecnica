--primeira table usuario--
CREATE TABLE usuario (
    id INT primary key,
    nome VARCHAR (100) NOT NULL,
    email VARCHAR (100) NOT NULL,
    senha VARCHAR (6) NOT NULL
);

--segunda table cliente--
CREATE TABLE cliente (
    id INT primary key,
    nome VARCHAR (100) NOT NULL,
    documento VARCHAR (14),
    telefone VARCHAR (11),
    email VARCHAR (100) NOT NULL,
    endereço VARCHAR (100) NOT NULL
);

--terceira table técnico--
CREATE TABLE tecnico (
    id INT primary key,
    nome VARCHAR (100) NOT NULL,
    telefone VARCHAR (11),
    especialidade VARCHAR (100) NOT NULL
);

--quarta table visita--
CREATE TABLE visita (
    id INT primary key,
    cliente_id VARCHAR (100) NOT NULL,
    tecnico_id VARCHAR (100) NOT NULL,
    data DATE,
    horario TIME,
    motivo VARCHAR (100) NOT NULL,
    observacoes VARCHAR (100), NOT NULL
);

--quinta table relatorio de visita--
CREATE TABLE relatorio_visita (
    id INT primary key,
    visita_id VARCHAR (100) NOT NULL,
    problema VARCHAR (100) NOT NULL,
    serviço_realizado VARCHAR (100) NOT NULL,
    materiais VARCHAR (100) NOT NULL,
    observacoes VARCHAR (100) NOT NULL,
    assinatura VARCHAR (100) NOT NULL
);
