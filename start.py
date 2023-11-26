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

start = False

# Conectar ao banco de dados
conexao = mysql.connector.connect(**connection) #Estabele a conexão do banco de dados baseado nas informações do dicionário criado acima
cursor = conexao.cursor() #Cria cursor

if start:
    with open('db/bd.sql', 'r') as file:
        with conexao.cursor() as cursor:
            cursor.execute(file.read(), multi=True)
        conexao.commit()
    print("Banco de dados criado com sucesso!")
    cursor.close()


# Menu CRUD
while True:
    print("\nMenu:")
    print("1. Inserir dieta saudável")
    print("2. Atualizar dieta saudável")
    print("3. Recuperar dietas saudáveis")
    print("4. Excluir dieta saudável")
    print("5. Sair")

    escolha = int(input("Escolha a opção: "))

    if escolha == 1:
        print("INSERIR\n")
        continue

    if escolha == 2:
        print("ATUALIZAR\n")
        continue

    elif escolha == 3:
        print("RECUPERAR\n")
        continue

    elif escolha == 4:
        print("EXCLUIR\n")
        continue

    elif escolha == 5:
        print("SAINDO...")
        break

    else:
        print("OPÇÃO INVÁLIDA")
        continue

# Fechar conexão
cursor.close() #Fecha o cursor
conexao.close() #Fecha conexão com o banco de 
