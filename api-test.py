from flask import Flask

app = Flask(__name__)


@app.route('/test/')
def sample():
    return 'Hello Word from the API :)'


if __name__ == '__main__':
    app.run()
