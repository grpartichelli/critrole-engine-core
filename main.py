from flask import Flask
from flask_cors import CORS

from controllers.api_example import app_example

app = Flask(__name__)
app.register_blueprint(app_example)


def main():
    CORS(app)
    app.run()


if __name__ == '__main__':
    main()
