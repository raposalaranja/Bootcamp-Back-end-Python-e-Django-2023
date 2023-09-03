import sqlite3

conexao = sqlite3.connect('BancodeDados')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')


#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

#cursor.execute('DROP TABLE produtos')

#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(1,"Chris","RJ","chr@gmail.com", 123456789)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(2,"Marcia","SP","mar@gmail.com", 234567891)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(3,"Paulo","RS","paulo@gmail.com", 345678912)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(4,"Joao","MG","joao@gmail.com", 456789123)')
#cursor.execute('INSERT INTO gerentes(id,nome,endereco,email) VALUES(4,"Elis","RJ","elis@gmail.com")')
#cursor.execute('INSERT INTO gerentes(id,nome,endereco,email) VALUES(4,"Jose","SP","jose@gmail.com")')
#cursor.execute('INSERT INTO gerentes(id,nome,endereco,email) VALUES(8,"Cintia","BR","cintia@gmail.com")')
#cursor.execute('DELETE FROM usuario where id=1')

#cursor.execute('UPDATE usuario SET endereco="Minas Gerais" WHERE nome="Joao"')

#ORDER BY e DESC
#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')

#LIMIT e DISTINCT
#dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 3')

#GROUP BY E HAVING
#dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3')

# JOIN RIGHT, LEFT, FULL, INNER

# INNER JOIN
#dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')

# LEFT JOIN
#dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.nome = gerentes.nome')

# RIGHT JOIN
#dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.nome = gerentes.nome')

# FULL JOIN
#dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.nome = gerentes.nome')

#SUBCONSULTAS
dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes)')
for usuario in dados:
    print(usuario)

conexao.commit()
conexao.close