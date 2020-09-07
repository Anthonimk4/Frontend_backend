import pytds
from flask import Flask, jsonify
import socket
from temperatura import temp
import json
app = Flask(__name__)

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


@app.route('/ping', methods=['GET'])
def ping():
    
    return jsonify({"luis": 1})


@app.route('/products')
def getproducts():

    return jsonify(products)



@app.route('/temperatura')
def Temperatura():
    Temperatura = int (27)
    return jsonify({"Temp": temp})





if __name__ == "__main__":
    app.run(socket.gethostname(), port=80)
