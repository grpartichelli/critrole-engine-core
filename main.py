from flask import Flask
from flask_cors import CORS

from controllers.controller_example import app_example
from controllers.character_controller import character_controller

app = Flask(__name__)
app.register_blueprint(app_example)
app.register_blueprint(character_controller)


def main():
    CORS(app)
    app.run()


if __name__ == '__main__':
    main()
