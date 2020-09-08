import pytds
import json
import pandas as pd

with open('config.JSON') as config_file:
    data = json.load(config_file)
    pass

SQLserver = data['SQLserver']
Temperatura = data['Temperatura']
Mensaje = data['Mensaje']
Telegran = Mensaje['Telegran']

conn = pytds.connect(SQLserver['direccion_IP_servidor'], SQLserver['nombre_de_Base_de_dato'],SQLserver['nombre_de_usuario'], SQLserver['password'])
cursor = conn.cursor()
cursor.execute('SELECT * FROM temperaturas')


try:
    with conn.cursor() as cursor:
        # En este caso no necesitamos limpiar ningún dato
        cursor.execute("SELECT TOP (1)  updated_at  FROM temperaturas ORDER by Id DESC;")
        # Hacer un while, mientras fetchone no regrese None
        Tem = cursor.fetchone()
        while Tem:
            
            hola = (Tem[2])
            print(hola)
            Tem = cursor.fetchone()
except Exception as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conn.close()

