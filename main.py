from flask import Flask
from flask_cors import CORS


def main():
    app = Flask(__name__)
    CORS(app)


if __name__ == '__main__':
    main()
