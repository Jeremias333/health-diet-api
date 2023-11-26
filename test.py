import mysql.connector
import dotenv
import os
import crud

dotenv.load_dotenv() #Carrega as variáveis de ambiente do arquivo .env

connection = {
    'host': os.getenv('HOST_DB', 'localhost1'),  # Nome do serviço do banco de dados no Docker Compose
    'user': os.getenv('USER_DB', 'root1'), #Usuário
    'password': os.getenv('PASSWORD_DB', 'password1'), #Senha
    'database': os.getenv('DATABASE_DB', 'dietas_bd1') #Nome do banco de dados que deseja se conectar
}

print("Valores connection", connection)

start = True

# Conectar ao banco de dados
conexao = mysql.connector.connect(**connection) #Estabele a conexão do banco de dados baseado nas informações do dicionário criado acima
cursor = conexao.cursor() #Cria cursor

# crud.create_user(conexao, "João", 20, "M", "senha")
# print("criamos o usuário joão")

if start:
    with open('db/bd.sql', 'r') as file:
        with conexao.cursor() as cursor:
            cursor.execute(file.read(), multi=True)
        conexao.commit()
    print("Banco de dados criado com sucesso!")
    cursor.close()

# crud.find_user(conexao, "João")

# crud.create_food(conexao, "Arroz")
