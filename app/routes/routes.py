from flask import Flask
from config.config import Config
from routes.alumno.alumno import alumno_routes

def run_app():

    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(alumno_routes, url_prefix='/api/alumno')

    return app
