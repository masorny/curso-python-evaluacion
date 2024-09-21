import mysql.connector
from time import strftime

DB_CONFIG = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'loginlog'
}

def insertarlog(url: str, matricula: str):
    '''
    Inserta el registro en la base de datos.
    '''
    
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)

        query = "INSERT INTO registrologin(urlvisitada, matricula, fechaingreso) values(%s, %s, %s)"
        cursor.execute(query, (url, matricula, strftime('%Y-%m-%d %H:%M:%S')))

        conn.commit()
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
        pass