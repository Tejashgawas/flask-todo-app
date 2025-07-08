# app package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#create db instance global variable
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration from a config file
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the database with the app
    db.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp, url_prefix='/tasks')

    return app
