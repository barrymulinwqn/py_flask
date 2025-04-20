from flask import Flask

app = Flask(__name__)
app.config.update(DEBUG=True)


@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)