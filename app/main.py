from flask import Flask, request, jsonify
from app.infrastructure.database.sqlite import db
from app.api.routes import register_routes as routes_base
from app.api.routes_v1 import register_routes as routes_v1
from app.api.routes_v2 import register_routes as routes_v2

from app.domain.user.User import create_user
from app.domain.user.model.UserModel import User

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    routes_base(app)
    routes_v1(app)
    routes_v2(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
