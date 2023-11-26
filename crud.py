
def start_db(conn):
    cursor = conn.cursor()
    with open('bd.sql', 'r') as file:
        with cursor.cursor() as cursor:
            cursor.execute(file.read(), multi=True)
        cursor.commit()
    print("Banco de dados criado com sucesso!")
    cursor.close()

def user_exists(username):
    #procurar username no banco de dados
    return False

def signup(username, password, repassword):
    if user_exists(username):
        print("O usuário já existe!")
        return False
    
    if password == repassword:
        print("Usuário cadastrado com sucesso!")
        return True
    else:
        print("As senhas não coincidem!")
        return False


def login(username, password):
    if user_exists(username):
        # verificar se senha passada é igual do usuário
        if password == "senha":
            print("Usuário logado com sucesso!")
            return True
        else:
            print("Senha incorreta!")
            return False
    else:
        print("Usuário não existe!")
        return False

