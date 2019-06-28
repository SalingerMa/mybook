# -*- coding: utf-8 -*-
from flask import Flask
from flask_login import LoginManager


login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprint(app)
    register_plugin(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)

def register_plugin(app):
    from app.model.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()