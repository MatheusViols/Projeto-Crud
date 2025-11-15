mysql -u root --password=root --execute="
CREATE DATABASE crud;

CREATE USER IF NOT EXISTS 'crud-user'@'localhost' IDENTIFIED BY 'crud-user';
GRANT ALL PRIVILEGES ON crud.* TO 'crud-user'@'localhost';
FLUSH PRIVILEGES;

USE crud;

CREATE TABLE IF NOT EXISTS usuario
(
	login varchar(20) not null primary key,
	senha varchar(20) not null,
	nome varchar(20) not null,
	sobrenome varchar(20) not null,
	endereco varchar(30) not null
);
"
