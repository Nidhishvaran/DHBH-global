from flask import Flask
from flask_cors import CORS
from config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
