import  dbUtils as db

def exite_usuario(user_name):
    query = "SELECT * FROM user WHERE name='%s';" % user_name
    return len(db.get(query)) > 0

def agregar_usuario(user_name):
    query = "INSERT INTO user (name) VALUES ('%s');" % user_name
    return db.insert(query)
    
def agregar_deuda(deudor_name, prestador_name, monto):
    query = "INSERT INTO deuda (prestadorName, deudorName, monto) VALUES ('%s', '%s', %d)" % pretador_name, deudor_name, monto
    return db.insert(query)
    
def consultar_deuda(deudor_name):
    query = "SELECT * FROM deuda WHERE deudorName='%s'" % deudor_name
    return db.get(query)
    
def consultar_deudores(prestador_name):
    query = "SELECT * FROM deuda WHERE prestadorName='%s'" % prestador_name
    return db.get(query)

def obtener_usuarios():
    query = "SELECT * from user;"
    return db.get(query)
    
