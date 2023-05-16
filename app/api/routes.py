import json

from flask import Flask, jsonify, request, Response
from app.domain.user.User import create_user
from app.domain.user.model.UserModel import User
from app.infrastructure.database.sqlite import db
from app.api.auth import encode_auth_token, token_required


def register_routes(app):

    @app.route('/api/v1/index', methods=['POST'])
    def index():
        return jsonify({'data': 'Hello API World!'}), 200
