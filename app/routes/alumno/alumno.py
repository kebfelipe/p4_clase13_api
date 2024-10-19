from flask import Blueprint, request
from controllers.estudiantes import obtener_estudiantes, obtener_estudiante, insertar_estudiante, modificar_estudiante

alumno_routes  = Blueprint('alumnos', __name__)

@alumno_routes.route('', methods=['GET'])
def obtrener_alumnos():
    return obtener_estudiantes()

@alumno_routes.route('/<id>', methods=['GET'])
def obtener_alumno(id):
    return obtener_estudiante(id)

@alumno_routes.route('', methods=['POST'])
def insertar_alumnos():
    data = request.get_json()
    return insertar_estudiante(data)

@alumno_routes.route('/<id>', methods=['PUT'])
def modificar_alumnos(id):
    data = request.get_json()
    return modificar_estudiante(id, data)