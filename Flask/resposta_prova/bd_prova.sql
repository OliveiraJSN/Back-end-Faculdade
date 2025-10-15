
create database cinema;

CREATE TABLE cinema.cinema_ingressos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_filme VARCHAR(50) NOT NULL,
    genero VARCHAR(20) NOT NULL,
    sessoes VARCHAR(10) NOT NULL,
    nome_cliente VARCHAR(50) NOT NULL,
    assento VARCHAR(10),
    data_filme DATE
);


select * from cinema.cinema_ingressos;