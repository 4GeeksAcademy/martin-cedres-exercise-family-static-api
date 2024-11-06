"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
Este módulo se encarga de iniciar el servidor API, cargar la base de datos y agregar los puntos finales.
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person


# Crea la aplicación Flask
app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Crea el objeto 'jackson_family' utilizando la estructura de datos definida en 'datastructures'
jackson_family = FamilyStructure("Jackson")

# Maneja errores globalmente y devolverlos como JSON
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

#  Endpoint para generar el mapa del sitio con todos los endpoints disponibles
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():

    # así es como puedes usar la estructura de datos de la Familia llamando a sus métodos
    members = jackson_family.get_all_members()
   
    return jsonify(members), 200

# Verifica si los campos obligatorios existen en el cuerpo de la solicitud
@app.route('/member', methods=['POST'])
def post_member(): 
    body = request.get_json(silent = True)  
    if body is None: 
        return jsonify({'msg': 'No fue enviada informacion en el body'}), 400 
    if 'first_name' not in body: 
        return jsonify({'msg': 'El campo first_name es obligatorio'}), 400
    if 'age' not in body: 
        return jsonify({'msg': 'El campo age es obligatorio'}), 400
    if 'lucky_numbers' not in body: 
        return jsonify({'msg': 'El campo lucky_numbers es obligatorio'}), 400
    
    # Crear un nuevo miembro usando la información recibida en el cuerpo de la solicitud    
    new_member =  {
            'first_name': body ['first_name'], 
            'last_name': jackson_family.last_name,
            'age': body['age'],
            'lucky_numbers': body['lucky_numbers']
             }
    if 'id' in body:
        new_member['id']=body['id'] #Si me envian un id a traves del json que me lo agrege
   
   # Llamar al método 'add_member' de la estructura de datos para agregar el nuevo miembro
    member = jackson_family.add_member(new_member)
    return jsonify({'msg': 'Ok', 'member': member }), 200

# Endpoint para obtener un miembro específico por su ID
@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    member=jackson_family.get_member(id) # Buscar al miembro con el ID dado
    if not member: 
        return jsonify({'msg': 'No existe miembro con el ID indicado'}), 400 # Si no se encuentra al miembro, devolver un error
    return jsonify(member), 200 # Si se encuentra, devolver los datos del miembro

# Endpoint para eliminar un miembro específico por su ID
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    member=jackson_family.delete_member(id)
    if not member['done']: 
        return jsonify({'msg': 'No existe miembro con el ID indicado'}), 400
    return jsonify(member), 200 # Si se eliminó correctamente, devolver una confirmación


    

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
