import flask_cors

from flask import Flask
from user.views import user

app = Flask(__name__)
flask_cors.CORS(app)

app.register_blueprint(user, url_prefix='/user')


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
