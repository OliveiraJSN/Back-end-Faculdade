drop database clinicamedica; -- derruba o banco de dados clinicamedica
create database clinicamedica; -- cria o banco de dados clinicamedica

use clinicamedica; -- usa o banco de dados clinicamedica

create table consultas( -- cria a tabela consultas
id int auto_increment primary key, -- id (auto_increment pois cada novo registro ele acrecenta 1 automanticamento)
nome_paciente varchar(50), -- nome_paciente varchar = "string" com 50 caracteres
nome_medico varchar(50), -- nome_medico varchar = "string" com 50 caracteres
especialidade varchar(30), -- especialidade varchar = "string" com 30 caracteres
data_consulta datetime -- data consulta como data
);
	