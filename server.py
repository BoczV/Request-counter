from flask import Flask, render_template, request, redirect
import database_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/request-counter', methods=['GET', 'POST', 'DELETE', 'PUT'])
def request_counter():
    database_manager.insert_new_request_method(request.method)
    return render_template('request_counter.html')


@app.route('/statistics')
def statistics():
    all_data_from_http = database_manager.get_all_data_from_http()
    return render_template('statistics.html', all_data_from_http=all_data_from_http)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8000,
        host='0.0.0.0'
    )