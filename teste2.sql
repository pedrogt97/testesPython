create table usuarios(
	id INTEGER PRIMARY KEY,
	nome TEXT NOT NULL,
	email TEXT NOT NULL);

insert into usuarios(nome,email) values ('Joao','joao@email.com.br');
insert into usuarios(nome,email) values ('Pedro','pedro@email.com.br');
insert into usuarios(nome,email) values ('Maria','maria@email.com.br');

create table compras(
	id INTEGER PRIMARY KEY,
	id_usuarios INTEGER,
	valor REAL NOT NULL,
	item TEXT NOT NULL,
	FOREIGN KEY(id_usuarios) REFERENCES usuarios(id));

insert into compras (id_usuarios,valor,item) VALUES (1,500,'Colchao');
insert into compras (id_usuarios,valor,item) VALUES (2,250,'Jogo de Pratos');
insert into compras (id_usuarios,valor,item) VALUES (2,1000,'Celular');

select c.id_usuarios,
	u.nome,
	c.id as id_compra,
	c.valor as valor_compra,
	c.item as item_compra
FROM usuarios u INNER JOIN compras c ON c.id_usuarios = u.id;


select c.id_usuarios,
	u.nome,
	c.id as id_compra,
	c.valor as valor_compra,
	c.item as item_compra
FROM usuarios u LEFT JOIN compras c ON c.id_usuarios = u.id;
