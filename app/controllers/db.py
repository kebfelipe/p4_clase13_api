from mysql import connector
from mysql.connector import pooling
from config.config import Config

try:
    db_pool = pooling.MySQLConnectionPool(
        pool_name="mypool",
        pool_size=5,  # Número de conexiones en el pool
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB,
        port=int(Config.MYSQL_PORT)
    )
    print("Pool de conexiones creado exitosamente.")
except connector.Error as err:
    print(f"Error al crear el pool de conexiones: {err}")

def get_db_connection():
    return db_pool.get_connection()

def execute_sp(procedure_name, params=None):
    conn = None
    cursor = None
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        if params:
            cursor.callproc(procedure_name, params)
        else:
            cursor.callproc(procedure_name)
        
        results = []
        for result in cursor.stored_results():
            results.extend(result.fetchall())

        return results
    
    except connector.Error as err:
        print(f"Error: {err}")  # Manejo básico de errores
        return None
    
    finally:
        cursor.close()
        conn.close()