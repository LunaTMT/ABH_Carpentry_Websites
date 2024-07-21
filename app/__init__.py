# yourapp/__init__.py
import os
from flask import Flask

def create_app(config_filename='config.py'):
    app = Flask(__name__)

    # Load the default configuration
    app.config.from_object('config.default')

    # Load the instance configuration, if it exists, when not testing
    app.config.from_pyfile(config_filename, silent=True)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Import and register blueprints
    from . import AHB
    app.register_blueprint(AHB.bp)

    return app
