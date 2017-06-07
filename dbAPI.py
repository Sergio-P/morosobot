import  dbUtils as db

def existe_usuario(user_name):
    query = "SELECT * FROM user WHERE name='%s';" % user_name
    return len(db.get(query)) > 0

def agregar_usuario(user_name):
    query = "INSERT INTO user (name) VALUES ('%s');" % user_name
    return db.insert(query)
    
def agregar_deuda(deudor_name, prestador_name, monto):
    deuda = obtener_deuda(prestador_name, deudor_name)
    if len(deuda) == 1:
        nueva_deuda = deuda[0] + monto
        query = "UPDATE deuda SET monto=%d WHERE prestadorName='%s' AND deudorName='%s';" %(nueva_deuda, prestador_name, deudor_name)
        return db.insert(query)
    else:
        query = "INSERT INTO deuda (prestadorName, deudorName, monto) VALUES ('%s', '%s', %d);" % (prestador_name, deudor_name, monto)
        return db.insert(query)
        
def pagar_deuda(deudor_name, prestador_name, monto):
    deuda = obtener_deuda(prestador_name, deudor_name)
    if len(deuda) == 1:
        nueva_deuda = deuda[0] - monto
        if (nueva_deuda <= 0):
            query = "DELETE FROM deuda WHERE prestadorName='%s' AND deudorName='%s';" % (prestador_name, deudor_name)
        else:
            query = "UPDATE deuda SET monto=%d WHERE prestadorName='%s' AND deudorName='%s';" %(nueva_deuda, prestador_name, deudor_name)
        return db.insert(query)
    else: #No habia deuda, error
        return -1
        
def obtener_deuda(prestador_name, deudor_name):
    query = "SELECT monto FROM deuda WHERE prestadorName='%s' AND deudorName='%s';" % (prestador_name, deudor_name)
    return db.get(query)
    
def consultar_deuda(deudor_name):
    query = "SELECT * FROM deuda WHERE deudorName='%s';" % deudor_name
    return db.get(query)
    
def consultar_deudores(prestador_name):
    query = "SELECT * FROM deuda WHERE prestadorName='%s';" % prestador_name
    return db.get(query)

def obtener_usuarios():
    query = "SELECT * from user;"
    return db.get(query)
    
