from flask import jsonify, request
from controllers.db import execute_sp

def obtener_estudiantes():
    alumnos = execute_sp('sp_obtener_estudiantes')
    if alumnos:
        return jsonify(alumnos), 200
    else:
        return jsonify({"message": "No se encontraron alumnos"}), 404

def obtener_estudiante(id):
    alumno = execute_sp('sp_obtener_estudiante', (id,))
    if alumno:
        return jsonify(alumno), 200
    else:
        return jsonify({"message": "No se encontró el alumno"}), 404
    
def insertar_estudiante(data):
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    edad = data.get('edad')
    if nombre and apellido and edad:
        alumno = execute_sp('sp_insertar_estudiante', (nombre, apellido, edad))
        return jsonify({"message": "Estudiante insertado", "data": alumno}), 201
    else:
        return jsonify({"message": "Faltan datos"}), 400
    
def modificar_estudiante(id, data):
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    edad = data.get('edad')
    if nombre and apellido and edad:
        execute_sp('sp_modificar_estudiante', (id, nombre, apellido, edad))
        return jsonify({"message": "Estudiante modificado"}), 200
    else:
        return jsonify({"message": "Faltan datos"}), 400