create database if not exists produto;
use produto;

CREATE table IF NOT EXISTS itens(
codigo int NOT NULL PRIMARY KEY,
produto varchar(50),
descricao varchar(50),
destaque bool,
preco float,
url_imagem varchar(300),
disponibilidade bool default 1
);