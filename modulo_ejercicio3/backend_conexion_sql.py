import sqlite3

#creamos la base de datos local con un usuario
def inicializar_base():
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    #creamos la tabla de usuarios si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            username TEXT,
            password TEXT
        )
    ''')
    #agregamos un usuario para realizar el ejemplo
    cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", ("santiago", "12345"))
    conexion.commit()
    #cierra la conexion a la base de datos
    conexion.close()

# Validar login
def validar_usuario(username, password):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    #consulta de sql para la validacion del usuario
    cursor.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, password))
    result = cursor.fetchone() #si no encuentra datos similares devuelve none 
    #cierra la conexion a la base de datos
    conn.close()
    return result is not None






    
    