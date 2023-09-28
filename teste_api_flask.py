#pip install flask

from flask import Flask, request
import db

app = Flask(__name__)

@app.route('/hello')
def hello():
    return {"msg" : "Hello World!"}

@app.route('/carros', methods=['GET'])
def get_all():
    return db.carros

@app.route('/carros/<int:id>', methods=['GET'])
def get_id(id):
    for car in db.carros:
        if car ['id'] == id:
            return car, 200
        
    info ={'msg': "nao encontrado"}
    return info, 404

@app.route('/carros', methods=['POST'])
def insere():
    dado = request.json
    db.carros.append(dado)
    info = {"url": f"/carros/{dado['id']}"}
    return info, 200
    

app.run(debug=True)



#postman e insomnia (teste de api)

# {"id" : 7,
# "montadora" : "BYD",
# "modelo" : "CR300",
# "ano" : 2023,
# "placa" : "EWD-7629"}