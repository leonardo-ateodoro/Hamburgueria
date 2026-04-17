create database if not exists produto;
use produto;

CREATE table IF NOT EXISTS itens(
codigo int NOT NULL PRIMARY KEY auto_increment,
produto varchar(50),
descricao varchar(50),
destaque bool,
preco float,
url_imagem varchar(300),
disponibilidade bool default 1
);

create table if not exists usuarios(
	usuario varchar(20) primary key,
    senha varchar(200) not null,
    nome varchar(100) DEFAULT "ANONIMO" 
    );