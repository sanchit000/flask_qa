from flask import Flask
from .extensions import db,login_manager
from .commands import create_tables
from .routes.auth import auth
from .routes.main import main
from .models import User

"""
This function will create a main flask app and configuration setup from setting.py file
"""
def create_app(config_file='settings.py'):
    app=Flask(__name__)   #creates the Flask instance.

    app.config.from_pyfile(config_file)
    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'

    # Given method with the user_loader decorator so that flask_login can find a current_user

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    #Register blueprint application to the main flask app

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.cli.add_command(create_tables)


    return app