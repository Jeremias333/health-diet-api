import mysql.connector

# Configurações do banco de dados para conseguir se conectar
connection = {
    'host': 'db',  # Nome do serviço do banco de dados no Docker Compose
    'user': 'root', #Usuário
    'password': 'senha_do_banco', #Senha
    'database': 'dietas_db' #Nome do banco de dados que deseja se conectar
}

# Conectar ao banco de dados
conexao = mysql.connector.connect(**db_config) #Estabele a conexão do banco de dados baseado nas informações do dicionário criado acima
cursor = conexao.cursor() #Cria cursor

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
