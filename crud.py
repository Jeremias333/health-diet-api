def create_user(conn, username, age, gender, password):
    cursor = conn.cursor()
    sql = "INSERT INTO usuario (nome, idade, senha, sexo) VALUES (%s, %s, %s, %s)"
    val = (username, age, password, gender)
    cursor.execute(sql, val)
    conn.commit()
    print("Usuário cadastrado com sucesso!")
    cursor.close()
    return True


def find_user(conn, username):
    cursor = conn.cursor()
    sql = "SELECT * FROM usuario WHERE BINARY nome = %s"
    val = (username, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    # print("Achamos este usuário: ", result)
    cursor.close()
    return result


def user_exists(conn, username):
    user_list = find_user(conn, username)
    if len(user_list) > 0:
        return True
    return False


def signup(conn, username, age, gender, password, repassword):
    if user_exists(conn, username):
        print("O usuário já existe!")
        return False

    if password == repassword:
        print("Usuário cadastrado com sucesso!")
        create_user(conn, username, age, gender, password)
        return True
    else:
        print("As senhas não coincidem!")
        return False


def login(conn, username, password):
    if user_exists(conn, username):
        user_selected = find_user(conn, username)
        if password == user_selected[0][3]:
            print("Usuário logado com sucesso!")
            return True
        else:
            print("Senha incorreta!")
            return False
    else:
        print("Usuário não existe!")
        return False

def create_food(conn, name):
    cursor = conn.cursor()
    sql = "INSERT INTO alimentos (nome) VALUES (%s)"
    val = (name, )
    cursor.execute(sql, val)
    conn.commit()
    print("Alimento: ", name, " cadastrado com sucesso!")
    cursor.close()
    return True

def find_food(conn, name):
    cursor = conn.cursor()
    sql = "SELECT * FROM alimentos WHERE BINARY nome = %s"
    val = (name, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    cursor.close()
    return result

def all_foods(conn):
    cursor = conn.cursor()
    sql = "SELECT * FROM alimentos"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result

def remove_food(conn, name):
    cursor = conn.cursor()
    sql = "DELETE FROM alimentos WHERE BINARY nome = %s"
    val = (name, )
    cursor.execute(sql, val)
    conn.commit()
    print("Alimento: ", name, " removido com sucesso!")
    cursor.close()
    return True

def find_diet(conn, name):
    cursor = conn.cursor()
    sql = "SELECT * FROM dietas WHERE BINARY nome = %s"
    val = (name, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    cursor.close()
    return result

def all_diets(conn):
    cursor = conn.cursor()
    sql = "SELECT * FROM dietas"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result

def create_diet(conn, name, date_init, date_final):
    cursor = conn.cursor()
    sql = "INSERT INTO dietas (nome, data_inicio, data_fim) VALUES (%s, %s, %s)"
    val = (name, date_init, date_final)
    cursor.execute(sql, val)
    conn.commit()
    print("Dieta: ", name, " cadastrada com sucesso!")
    cursor.close()
    return True

def remove_diet(conn, name):
    cursor = conn.cursor()
    sql = "DELETE FROM dietas WHERE BINARY nome = %s"
    val = (name, )
    cursor.execute(sql, val)
    conn.commit()
    print("Dieta: ", name, " removida com sucesso!")
    cursor.close()
    return True

def update_diet(conn, name, date_init, date_final):
    cursor = conn.cursor()
    sql = "UPDATE dietas SET data_inicio = %s, data_fim = %s WHERE BINARY nome = %s"
    val = (date_init, date_final, name)
    cursor.execute(sql, val)
    conn.commit()
    print("Dieta: ", name, " atualizada com sucesso!")
    cursor.close()
    return True

def add_food_diet(conn, food_id, diet_id):
    cursor = conn.cursor()
    sql = "INSERT INTO dieta_alimento (alimento_id, dieta_id) VALUES (%s, %s)"
    val = (food_id, diet_id)
    cursor.execute(sql, val)
    conn.commit()
    print("Alimento: ", food_id, " adicionado na dieta: ", diet_id, " com sucesso!")
    cursor.close()
    return True

def find_food_diet(conn, diet_id):
    cursor = conn.cursor()
    sql = "SELECT * FROM dieta_alimento WHERE dieta_id = %s"
    val = (diet_id, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    cursor.close()
    return result
