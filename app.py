import pytds
from flask import Flask, jsonify, request
import socket
from temperatura import temp
import json
from products import products
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
    print(request.json)
    return "res"
    
@app.route('/tres', methods=['POST'])
def tres():
    print(request.json)
    return "res"


@app.route('/id')
def id():
    cursor.execute("SELECT TOP (1) id FROM temperaturas ORDER by Id DESC;")
    Tem = cursor.fetchone()
    Tmp = (Tem[0])
    return Tmp
        
   
                 
@app.route('/zona')
def zona():
    cursor.execute("SELECT TOP (1) zona_id FROM temperaturas ORDER by Id DESC;")
    Tem = cursor.fetchone()
        
    return Tem 

@app.route('/temp')
def temp():
    cursor.execute("SELECT TOP (1) id, valor  FROM temperaturas ORDER by Id DESC;")
    Tem = cursor.fetchone()
    Tmp = (Tem[1])    
    return jsonify({"name": Tmp})      


@app.route('/fecha')
def fecha():
    cursor.execute("SELECT TOP (1) created_at  FROM temperaturas ORDER by Id DESC;")
    Tem = cursor.fetchone()
        

    return jsonify(Tem)   

@app.route('/temperatura')
def temperatura():

    return jsonify(

        {"id": id()},
        {"zona": zona()}
    
    
    
    )  



    
    






if __name__ == "__main__":
    app.run(socket.gethostname(), port=80)
