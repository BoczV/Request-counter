from flask import Flask, render_template, request, redirect

app = Flask(__name__)

counter_dict = {'POST': 0, 'GET': 0, 'DELETE': 0, 'PUT': 0}


@app.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def index():
    counter_dict[request.method] += 1
    return render_template('index.html')


@app.route('/request-counter')
def request_counter():
    return render_template('request_counter.html', counter_dict=counter_dict)


@app.route('/statistics')
def statistics():
    return render_template('statistics.html', counter_dict=counter_dict)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8000,
        host='0.0.0.0'
    )