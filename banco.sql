CREATE DATABASE IF NOT EXISTS sistema_visitas;
USE sistema_visitas;

CREATE TABLE visita (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cliente VARCHAR(100) NOT NULL,
    tecnico VARCHAR(100) NOT NULL,
    data DATE NOT NULL,
    horario TIME NOT NULL,
    motivo VARCHAR(100) NOT NULL,
    observacoes VARCHAR(100),
    turma VARCHAR(100),
    endereco VARCHAR(100)
);
