import mysql.connector
import dotenv
import os
import crud

dotenv.load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

connection = {
    # Nome do serviço do banco de dados no Docker Compose
    'host': os.getenv('HOST_DB', 'localhost1'),
    'user': os.getenv('USER_DB', 'root1'),  # Usuário
    'password': os.getenv('PASSWORD_DB', 'password1'),  # Senha
    # Nome do banco de dados que deseja se conectar
    'database': os.getenv('DATABASE_DB', 'dietas_bd1')
}

print("Valores connection", connection)

start = False
user_logged = {
    'id': 0,
    'nome': '',
    'sexo': '',
    'idade': 0,
}

# Conectar ao banco de dados
# Estabele a conexão do banco de dados baseado nas informações do dicionário criado acima
conexao = mysql.connector.connect(**connection)
cursor = conexao.cursor()  # Cria cursor

if start:
    with open('db/bd.sql', 'r') as file:
        with conexao.cursor() as cursor:
            cursor.execute(file.read(), multi=True)
        conexao.commit()
    print("Banco de dados criado com sucesso!")
    cursor.close()

try:
    # Menu Usuário
    while True:
        print("\nAUTENTICAÇÃO")
        print("\n1. Login")
        print("2. Cadastrar")
        print("3. Sair\n")

        opcao = int(input("Escolha a opção: "))

        if opcao == 1:  # LOGIN
            print("---LOGIN---")
            username = input("Nome de usuário: ")
            password = input("Senha: ")

            allowed = crud.login(conexao, username, password)

            if allowed:
                temp_user = crud.find_user(conexao, username)
                user_logged['id'] = temp_user[0][0]
                user_logged['nome'] = temp_user[0][1]
                user_logged['idade'] = temp_user[0][2]
                user_logged['sexo'] = temp_user[0][4]

                # Menu autenticação
                while True:
                    print("\nBem vindo (a), {}!".format(user_logged['nome']))
                    print("\nMenu:")
                    print("1. Dieta")
                    print("2. Alimento")
                    print("3. Sair\n")

                    escolha = int(input("Escolha a opção: "))

                    if escolha == 1:  # Dieta

                        print("Escolha a opção: ")
                        print("1. Inserir dieta")
                        print("2. Pesquisar dieta")
                        print("3. Exibir dieta")
                        print("4. Atualizar dieta")
                        print("5. Excluir dieta")
                        print("6. Sair")

                        opcao = int(input("Escolha sua opção: "))

                        while True:

                            if opcao == 1:  # Inserir
                                print("---Inserir dieta---")
                                name = input("Name: ")
                                date_init = input("Date init: ")
                                date_final = input("Date final: ")

                                crud.create_diet(
                                    conexao, name, date_init, date_final)

                            elif opcao == 2:  # Pesquisar
                                print("---Pesquisar dieta---")
                                name = input("Nome para buscar dieta: ")

                                diet = crud.find_diet(conexao, name)

                                if len(diet) > 0:
                                    print(
                                        'Dieta encontrada: {}'.format(diet[0][2]))

                                    print("1. Ver detalhes da dieta")
                                    print("2. Sair")
                                    opcao = int(input("Escolha a opção: "))

                                    if opcao == 1:
                                        print("Nome: ", diet[0][1])
                                        print("Data inicio: ", diet[0][2])
                                        print("Data fim: ", diet[0][3])

                                        all_food_diet = crud.find_food_diet(
                                            conexao, diet[0][0])
                                        print("Alimentos: ")
                                        for index, diet_id, food_id, quantity in all_food_diet:
                                            food = crud.find_food_id(
                                                conexao, food_id)[0][1]
                                            print('{}. {} - {}'.format(
                                                food_id, food, quantity))
                                        input('Pressione enter para continuar')
                                        break
                                    if opcao == 2:
                                        break
                                else:
                                    print('Dieta não encontrada, busque outra')

                            elif opcao == 3:  # Exibir
                                print("---Exibir dieta---")

                                diets = crud.all_diets(conexao)
                                for index, _, name, date_init, date_final, in diets:
                                    print('{}. {} ({} - {})'.format(index,
                                        name, date_init, date_final))
                                input('Pressione enter para continuar')
                                break

                            elif opcao == 4:  # Atualizar
                                print("---Atualizar dieta---")
                                name = input("Name: ")
                                date_init = input("Date init: ")
                                date_final = input("Date final: ")

                                crud.update_diet(
                                    conexao, name, date_init, date_final)

                            elif opcao == 5:  # Excluir
                                print("---Excluir dieta")
                                name = input("Name: ")

                                crud.remove_diet(conexao, name)

                            elif opcao == 7:  # Sair
                                print("SAINDO...")
                                break

                            else:
                                print("Opção inválida, tente novamente...")
                                break

                    if escolha == 2:  # Alimento

                        print("Escolha a opção: ")
                        print("1. Inserir alimento")
                        print("2. Exibir alimentos")
                        print("3. Excluir alimento")
                        print("4. Pesquisar alimento")
                        print("5. Sair")

                        opcao = int(input("Escolha sua opção: "))

                        while True:

                            if opcao == 1:  # Inserir
                                print("---Inserir alimento---")
                                name = input(("Name: "))

                                crud.create_food(conexao, name)

                                create_new = input(
                                    "Deseja cadastrar outro alimento? (S/N): ")
                                if create_new == 'N':
                                    break

                            elif opcao == 2:  # Exibir
                                print("---Exibir alimento---")

                                all_foods = crud.all_foods(conexao)
                                for index, food in all_foods:
                                    print('{}. {}'.format(index, food))
                                input('Pressione enter para continuar')
                                break
                            elif opcao == 3:  # Excluir
                                print("---Excluir alimento---")
                                all_foods = crud.all_foods(conexao)
                                for index, food in all_foods:
                                    print('{}. {}'.format(index, food))
                                name = input("Nome do alimento a ser excluído: ")

                                crud.remove_food(conexao, name)

                            elif opcao == 4:  # Pesquisar
                                print("---Pesquisar alimento---")
                                name = input("Nome do alimento a ser pesquisado: ")

                                foods = crud.find_food(conexao, name)
                                if len(foods) > 0:
                                    print('Alimento encontrado: {}'.format(
                                        foods[0][1]))
                                    break
                                print('Alimento não encontrado, busque outro')

                            elif opcao == 5:  # Sair
                                print("SAINDO...")

                            else:
                                print("Opção inválida, tente novamente...")
                    if escolha == 3:
                        print("SAINDO...")
                        break
                    else:
                        print("Opção inválida, tente novamente...")
        elif opcao == 2:  # CADASTRAR

            print("---CADASTRO---")
            username = input("Nome de Usuario: ")
            age = int(input("Idade: "))
            gender = input("Sexo: ")
            password = input("Senha: ")
            repassword = input("Repetir Senha: ")

            crud.signup(conexao, username, age, gender, password, repassword)

        elif opcao == 3:
            print("SAINDO...")
            exit()

        else:
            print("Opção inválida, tente novamente")
except KeyboardInterrupt as e:
    print("\nPrograma finalizado")
    # Fechar conexão
    cursor.close()  # Fecha o cursor
    conexao.close()  # Fecha conexão com o banco de

except Exception as e:
    print("Ocorreu um erro: ", e)
    # Fechar conexão
    cursor.close()  # Fecha o cursor
    conexao.close()  # Fecha conexão com o banco de
