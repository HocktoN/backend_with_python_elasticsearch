from marshmallow import Schema, fields, validates
from api.user.exceptions import WrongEmailException, WrongPasswordException


class UserSerializer(Schema):
    username = fields.String()
    email = fields.String()
    password = fields.String()

    @validates('email')
    def validate_email(self, email):
        if not email.endswith('@gmail.com'):
            raise WrongEmailException('Wrong email')

    @validates('password')
    def validate_password(self, password):
        if len(password) < 8:
            raise WrongPasswordException('Wrong password')
