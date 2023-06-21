from flask import Blueprint, jsonify, request
from api.user.serializers import UserSerializer
from api.user.services import UserService

user = Blueprint('user', __name__)


# Create new User

@user.route('/create', methods=['POST'])
def create():
    req = UserSerializer().load(request.json)
    data = UserService.create(**req)
    return jsonify(data)


# get User

@user.route('/<username>', methods=['GET'])
def get_by_username(username):
    user_info = UserService.get(username)
    return jsonify(user_info)


# delete User

@user.route('/<username>', methods=['DELETE'])
def delete(username):
    user_info = UserService.delete(username)
    return jsonify(user_info)


# update User

@user.route('/<username>', methods=['PUT'])
def update(username):
    req = UserSerializer().load(request.json)
    user_info = UserService.update(username, **req)
    return jsonify(user_info)
