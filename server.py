from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
def index():
    pass


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8000,
        host='0.0.0.0'
    )