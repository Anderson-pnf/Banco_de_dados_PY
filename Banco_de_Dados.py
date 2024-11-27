import sqlite3

conexao = sqlite3.connect('Banco_de_dados.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        cidade TEXT NOT NULL
)
''')

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
cidade = input('Digite sua cidade: ')

cursor.execute('''
    INSERT INTO pessoas (nome, idadem cidade)
    VALUES (?, ?, ?)
''', (nome, idade, cidade))

conexao.commit()

cursor.execute('SELECT * FROM pessoas')

pessoas = cursor.fetchall()

for pessoa in pessoas:
    print(f''' ID: {pessoa[0]}, Nome: {pessoa[1]}, Idade: {pessoa[2]} Cidade: {pessoa[3]}''')

conexao.close()