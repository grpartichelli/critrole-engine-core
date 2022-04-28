from flask import Flask
from flask_cors import CORS

from controllers.character_controller import character_controller
from controllers.transcript_controller import transcript_controller
from controllers.dice_roll_controller import dice_roll_controller

app = Flask(__name__)
app.register_blueprint(character_controller)
app.register_blueprint(transcript_controller)
app.register_blueprint(dice_roll_controller)


def main():
    CORS(app)
    app.run()


if __name__ == '__main__':
    main()
