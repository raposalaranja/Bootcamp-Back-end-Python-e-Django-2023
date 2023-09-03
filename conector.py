import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#1.Crie uma tabela chamada "alunos" com os seguintes campos:
#id(inteiro),nome(texto),idade(inteiro) e curso(texto).

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

#2.Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1001,"Snoopy",21,"Web para iniciantes")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1002,"Charlie",22,"Cloud Computing")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(10033,"Linus","20","Azure")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1004,"Lucy",24,"Banco de dados")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1005,"Schroeder",19,"Música")')

#3.Consultas Básicas Escreva consultas SQLpara realizar as seguintes tarefas:

#a)Selecionar todos os registros da tabela"alunos".
#dados = cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
    #print(alunos)

#b)Selecionar o nome e a idade dos alunos com mais de 20anos.
#dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>=20')
#for alunos in dados:
    #print(alunos)

#c)Selecionar os alunos do curso de"Engenharia"em ordem alfabética.
#dados = cursor.execute('SELECT * FROM alunos ORDER BY nome ASC')
#for alunos in dados:
    #print(alunos)
    
#d)Contar o número total de alunos na tabela
#dados = cursor.execute('SELECT COUNT(*) FROM alunos')
#for alunos in dados:
    #print(alunos)

#4.Atualização e Remoção 

#a)Atualize a idade de um aluno específico na tabela.

#cursor.execute('UPDATE alunos SET idade=16 WHERE nome="Schroeder"')

#b)Remova um aluno pelo seu ID.
#cursor.execute('DELETE FROM alunos WHERE id=1001')

#5.Criar uma Tabela e Inserir Dados Crie uma tabela chamada"clientes"com os campos:
#id(chaveprimária),nome(texto),idade(inteiro)e saldo(float).

#cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT);')

#Insira alguns registros de clientes na tabela.
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(200,"Jason",30,5000)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(300,"Carol","40",10000)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(400,"John",50,50000)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(500,"Paul",20,2000)')

#dados = cursor.execute('SELECT * FROM clientes')
#for clientes in dados:
    #print(clientes)

#6.Consultas e Funções Agregadas Escreva consultas SQL para realizar as seguintes tarefas:
#a)Selecione o nome e a idade dos clientes com idade superior a 30anos.
#dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>=30')
#for clientes in dados:
    #print(clientes)

#b)Calcule o saldo médio dos clientes.
#dados = cursor.execute('SELECT AVG(saldo) as SALDO_MEDIO FROM clientes')
#for clientes in dados:
    #print(clientes)

#c)Encontre o cliente como saldo máximo.
#dados = cursor.execute('SELECT MAX(saldo) as MAIOR_SALDO FROM clientes')
#for clientes in dados:
    #print(clientes)

#d)Conte quantos clientes têm saldo acima  de 1000.
#dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo>1000')
#for clientes in dados:
    #print(clientes)

#7.Atualização e Remoção com Condições 
#a)Atualize o saldo de um cliente específico.
#cursor.execute('UPDATE clientes SET saldo=1000 WHERE nome="Paul"')

#b)Remova um cliente pelo seu ID.
#cursor.execute('DELETE FROM clientes WHERE id=200')

#8.Junção de Tabelas Crie uma segunda tabela chamada "compras" com os campos:
# id(chaveprimária),cliente_id(chave estrangeira referenciando o id da tabela"clientes"),
# produto(texto) e valor(real).
#Insira algumas compras associadas a clientes existentes na tabela"clientes". 
#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id CONSTRAINT fk_ComprasCliente FOREIGN KEY (cliente_id) REFERENCES clientes (cliente_id), produto VARCHAR, valor FLOAT);')


conexao.commit()
conexao.close

