from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Define the WSGI application object
app = Flask(__name__)
app.url_map.strict_slashes = False

# Configurations
app.config.from_object("app.config")

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return "This page does not exist!"


# Import a module / component using its blueprint handler variable (mod_auth)
from app.controllers import mod_asset as asset_module

# Register blueprint(s)
app.register_blueprint(asset_module)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

from app.models import seed_db
seed_db()