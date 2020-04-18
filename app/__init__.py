from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
import os

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)  
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # app.config.from_object(config[config_name])    
    # config[config_name].init_app(app)
    # #db.init_app(app)    
    
    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    return app