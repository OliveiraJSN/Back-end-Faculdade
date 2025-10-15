drop database login_usuarios;

	create database login_usuarios;

	create table login_usuarios.usuarios(
	id int auto_increment not null primary key,
	nome varchar(100) not null,
	email varchar(50) unique not null,
	senha varchar(50) not null
	);

	select * from login_usuarios.usuarios;
