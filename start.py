import mysql.connector
import dotenv
import os
import crud

dotenv.load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

connection = {
    # Nome do serviço do banco de dados no Docker Compose
    'host': os.getenv('HOST_DB', 'localhost'),
    'user': os.getenv('USER_DB', 'user'),  # Usuário
    'password': os.getenv('PASSWORD_DB', 'password'),  # Senha
    # Nome do banco de dados que deseja se conectar
    'database': os.getenv('DATABASE_DB', 'db')
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
                print(temp_user)
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
                                name = input("Nome: ")
                                date_init = input("Data inicio: ")
                                date_final = input("Data fim: ")

                                crud.create_diet(conexao, user_logged['id'], name, date_init, date_final)
                                
                                create_new = input(
                                    "Deseja inserir outra dieta? (S/N): ").lower()
                                if create_new == 's':
                                    continue
                                else:
                                    break

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
                                        print("Nome: ", diet[0][2])
                                        print("Data inicio: ", diet[0][3])
                                        print("Data fim: ", diet[0][4])

                                        all_food_diet = crud.find_food_diet(
                                            conexao, diet[0][1])
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
                                print("---Exibir dietas---")

                                diets = crud.all_diets(conexao, user_logged['id'])
                                for index, _, name, date_init, date_final, in diets:
                                    print('{}. {} ({} - {})'.format(index,
                                                                    name, date_init, date_final))
                                input('Pressione enter para continuar')
                                break

                            elif opcao == 4:  # Atualizar
                                print("---Dietas Existentes---")
                                print("DIGITE SAIR para voltar ao menu anterior")
                                diet = []
                                diets = crud.all_diets(conexao, user_logged['id'])
                                for index, _, name, date_init, date_final, in diets:
                                    print('{}. {} ({} - {})'.format(index,
                                                                    name, date_init, date_final))
                                while True:
                                    choice_diet = input("Escolha a dieta pelo nome: ")
                                    if choice_diet == 'SAIR':
                                        break
                                    diet = [list(crud.find_diet(conexao, choice_diet)[0])]
                                    print("Dieta: ", diet, type(diet))
                                    if len(diet) > 0:
                                        while True:
                                            print("---Atualizar dieta---")
                                            print("Nome: ", diet[0][2])
                                            print("Data inicio: ", diet[0][3])
                                            print("Data fim: ", diet[0][4])
                                            print("1. Atualizar nome")
                                            print("2. Atualizar data inicio")
                                            print("3. Atualizar data final")
                                            print("4. Adicionar comida")
                                            print("5. Remover comida")
                                            print("6. Sair")
                                            
                                            option = int(input("Escolha a opção: "))
                                            
                                            if option == 1:
                                                new_name = input("Novo nome: ")
                                                crud.update_diet_name(conexao, diet[0][2], new_name)
                                                diet[0][2] = new_name
                                                continue
                                            elif option == 2:
                                                new_date_init = input("Nova data inicio: ")
                                                crud.update_diet_date_init(conexao, diet[0][2], new_date_init)
                                                diet[0][3] = new_date_init
                                                continue
                                            elif option == 3:
                                                new_date_final = input("Nova data final: ")
                                                crud.update_diet_date_final(conexao, diet[0][2], new_date_final)
                                                diet[0][4] = new_date_final
                                                continue
                                            elif option == 4:
                                                all_foods = crud.all_foods(conexao)
                                                for index, food in all_foods:
                                                    print('{}. {}'.format(index, food))
                                                food_id = int(input("ID do alimento: "))
                                                quantity = input("Quantidade: ")
                                                crud.add_food_diet(conexao, food_id, diet[0][1], quantity)
                                                continue
                                            elif option == 5:
                                                all_food_diet = crud.find_food_diet(
                                                    conexao, diet[0][1])
                                                for index, diet_id, food_id, quantity in all_food_diet:
                                                    food = crud.find_food_id(
                                                        conexao, food_id)[0][1]
                                                    print('{}. {} - {}'.format(
                                                        food_id, food, quantity))
                                                food_id = int(input("ID do alimento: "))
                                                crud.remove_food_diet(conexao, food_id, diet[0][1])
                                                continue
                                            elif option == 6:
                                                break
                                    else:
                                        print("Dieta não encontrada, tente novamente")
                                        continue

                                

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
                                    "Deseja cadastrar outro alimento? (S/N): ").lower()
                                if create_new == 's':
                                    continue
                                else:
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
                                name = input(
                                    "Nome do alimento a ser excluído: ")

                                crud.remove_food(conexao, name)

                                remove_new = input(
                                    "Deseja excluir outro alimento? (S/N): ").lower()
                                if remove_new == 's':
                                    continue
                                else:
                                    break

                            elif opcao == 4:  # Pesquisar
                                print("---Pesquisar alimento---")
                                name = input(
                                    "Nome do alimento a ser pesquisado: ")

                                foods = crud.find_food(conexao, name)
                                if len(foods) > 0:
                                    print('Alimento encontrado: {}'.format(
                                        foods[0][1]))
                                    search_new = input(
                                        "Deseja pesquisar outro alimento? (S/N): ").lower()
                                    if search_new == 's':
                                        continue
                                    else:
                                        break
                                else:
                                    print('Alimento não encontrado, busque outro')
                                    search_new = input(
                                        "Deseja pesquisar outro alimento? (S/N): ").lower()
                                    if search_new == 's':
                                        continue
                                    else:
                                        break

                            elif opcao == 5:  # Sair
                                break

                            else:
                                print("Opção inválida, tente novamente...")
                                continue
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
