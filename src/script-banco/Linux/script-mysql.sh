mysql -u root --password=root --execute="
CREATE DATABASE IF NOT EXISTS crud;

CREATE USER IF NOT EXISTS 'crud-user'@'localhost' IDENTIFIED BY 'crud-user';
GRANT ALL PRIVILEGES ON crud.* TO 'crud-user'@'localhost';
FLUSH PRIVILEGES;

USE crud;

CREATE TABLE IF NOT EXISTS usuario
(
	CPF varchar(11) not null unique primary key,
	senha varchar(11) not null,
	nome_comp varchar(50) not null,
	data_nasc date not null,
	telefone varchar(11) not null,
	endereco varchar(30) not null,
	
	desc_user varchar(100),

	cod_area int not null,
	cod_bairro int not null

);

CREATE TABLE IF NOT EXISTS empresa
(
	CNPJ varchar(14) not null unique primary key,
	senha varchar(11) not null,
	nome_emp varchar(30) not null,
	endereco varchar(30) not null,

	desc_emp varchar(100),

	cod_bairro int not null
);

CREATE TABLE IF NOT EXISTS instituicao
(
	CNPJ varchar(14) not null unique primary key,
	senha  varchar(11) not null,
	nome_inst varchar(30) not null,
	endereco varchar(30) not null,

	desc_inst varchar(100),

	cod_bairro int not null
);

CREATE TABLE IF NOT EXISTS curso
(
	cod_curso int not null unique primary key AUTO_INCREMENT,
	nome_curso varchar(20) not null,
	quant_vagas int not null,

	desc_curso varchar(100),

	cod_area int not null,
	cod_turno int not null,

	CNPJ varchar(14) not null,
	cod_bairro int not null
);

CREATE TABLE IF NOT EXISTS vaga
(
	cod_vaga int not null unique primary key AUTO_INCREMENT,
	nome_vaga varchar(20) not null,
	quant_vagas int not null,

	desc_vaga varchar(100),

	cod_area int not null,
	cod_turno int not null,

	CNPJ varchar(14) not null,
	cod_bairro int not null
);

CREATE TABLE IF NOT EXISTS area
(
	cod_area int not null unique primary key,
	nome_area varchar(20) not null
);

CREATE TABLE IF NOT EXISTS bairro
(
	cod_bairro int not null unique primary key,
	nome_bairro varchar(40) not null
);

CREATE TABLE IF NOT EXISTS turno
(
	cod_turno int not null unique primary key,
	nome_turno varchar(20) not null
);

CREATE TABLE IF NOT EXISTS matricula 
(
	CPF varchar(11) not null,
	cod_curso int not null,

	status_mat boolean not null DEFAULT False

);

CREATE TABLE IF NOT EXISTS aplica
(
	CPF varchar(11) not null,
	cod_vaga int not null,
	
	status_apli boolean not null DEFAULT False

);

ALTER TABLE usuario
ADD CONSTRAINT fk_area_usr FOREIGN KEY (cod_area)  REFERENCES area(cod_area),
ADD CONSTRAINT fk_bairro_usr FOREIGN KEY (cod_bairro) REFERENCES bairro(cod_bairro);

ALTER TABLE empresa
ADD CONSTRAINT fk_bairro_emp FOREIGN KEY (cod_bairro) REFERENCES bairro(cod_bairro);

ALTER TABLE instituicao
ADD CONSTRAINT fk_bairro_inst FOREIGN KEY (cod_bairro) REFERENCES bairro(cod_bairro);

ALTER TABLE curso
ADD CONSTRAINT fk_area_curso FOREIGN KEY (cod_area)  REFERENCES area(cod_area),
ADD CONSTRAINT fk_turno_curso FOREIGN KEY (cod_turno) REFERENCES turno(cod_turno),

ADD CONSTRAINT fk_CNPJ_curso FOREIGN KEY (CNPJ) REFERENCES instituicao(CNPJ),
ADD CONSTRAINT fk_bairro_curso FOREIGN KEY (cod_bairro) REFERENCES instituicao(cod_bairro);

ALTER TABLE vaga
ADD CONSTRAINT fk_area_vaga FOREIGN KEY (cod_area) REFERENCES area(cod_area),
ADD CONSTRAINT fk_turno_vaga FOREIGN KEY (cod_turno) REFERENCES turno(cod_turno),

ADD CONSTRAINT fk_CNPJ_vaga FOREIGN KEY (CNPJ) REFERENCES empresa(CNPJ),
ADD CONSTRAINT fk_bairro_vaga FOREIGN KEY (cod_bairro) REFERENCES empresa(cod_bairro);

ALTER TABLE matricula
ADD CONSTRAINT fk_CPF_mat FOREIGN KEY (CPF) REFERENCES usuario(CPF),
ADD CONSTRAINT fk_curso_mat FOREIGN KEY (cod_curso)  REFERENCES curso(cod_curso),
ADD CONSTRAINT pk_matricula PRIMARY KEY (CPF, cod_curso);

ALTER TABLE aplica
ADD CONSTRAINT fk_CPF_apli FOREIGN KEY (CPF) REFERENCES usuario(CPF),
ADD CONSTRAINT fk_vaga_apli FOREIGN KEY (cod_vaga) REFERENCES vaga(cod_vaga),
ADD CONSTRAINT pk_aplica PRIMARY KEY (CPF, cod_vaga);


INSERT INTO turno(cod_turno, nome_turno) VALUES(1, 'Manhã');
INSERT INTO turno(cod_turno, nome_turno) VALUES(2, 'Tarde');
INSERT INTO turno(cod_turno, nome_turno) VALUES(3, 'Noite');

INSERT INTO area(cod_area, nome_area) VALUES(1, 'TI');
INSERT INTO area(cod_area, nome_area) VALUES(2, 'Saúde');
INSERT INTO area(cod_area, nome_area) VALUES(3, 'Design');
INSERT INTO area(cod_area, nome_area) VALUES(4, 'Marketing');
INSERT INTO area(cod_area, nome_area) VALUES(5, 'Industrial');
INSERT INTO area(cod_area, nome_area) VALUES(6, 'Administração');
INSERT INTO area(cod_area, nome_area) VALUES(7, 'Setor Público');

INSERT INTO bairro(cod_bairro, nome_bairro) VALUES  
(1,'Agamenon Magalhães'),  
(2,'Alto do Céu'),  
(3,'Ana de Albuquerque'),  
(4,'Arassoiaba'),  
(5,'Área Rural de Igarassu'),  
(6,'Bela Vista'),  
(7,'Bonfim'),  
(8,'Campina de Feira'),  
(9,'Centro'),  
(10,'Cruz de Reboucas'),  
(11,'Distrito de Três Ladeiras'),  
(12,'Distrito Industrial'),  
(13,'Distrito Nova Cruz'),  
(14,'Encanto Igarassu'),  
(15,'Inhamã'),  
(16,'Jabacó'),  
(17,'Jardim Boa Sorte'),  
(18,'Monjope'),  
(19,'Pancó'),  
(20,'Vila Rural'),  
(21,'Posto de Monta'),  
(22,'Rubina'),  
(23,'Santa Luzia'),  
(24,'Santa Rita'),  
(25,'Santo Antônio'),  
(26,'Saramandaia'),  
(27,'Sítio dos Marcos'),  
(28,'Tabatinga'),  
(29,'Triunfo'),  
(30,'Umbura'),  
(31,'Cuieiras');

INSERT INTO usuario(CPF, senha, nome_comp, data_nasc, telefone, endereco, desc_user, cod_area, cod_bairro) VALUES('18196112320', 'manga', 'George Alberto', '1987-06-12', '81997141562', 'Rua Camboiá', 'Professor de Front End Rapaz!', 1, 7);

INSERT INTO empresa(CNPJ, senha, nome_emp, endereco, desc_emp, cod_bairro) VALUES('12345678912345', 'sarahbonito', 'Bonito Generation', 'Rua Padre Canhão', 'Empresa do ramo criativo', 19);

INSERT INTO instituicao(CNPJ, senha, nome_inst, endereco, desc_inst, cod_bairro) VALUES('12345678912345', 'janeremover', 'Unesp', 'Avenida fim do mundo', 'Universidade com mais de 90 anos de história em pernambuco', 22);

INSERT INTO vaga(nome_vaga, quant_vagas, desc_vaga, cod_area, cod_turno, CNPJ, cod_bairro) VALUES('Dev BackEnd', 1, 'Desenvolvedor BackEnd RAPAZ!', 1, 3, '12345678912345', 19);
"
