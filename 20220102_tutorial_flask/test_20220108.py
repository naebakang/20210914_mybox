# File encoding: UTF-8

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def test_add():
    return jsonify({'ip': request.remote_addr}), 200


@app.route('/test/')
def test_test():
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)


@app.route('/test2/')
def test_test2():
    return request.environ['REMOTE_ADDR']


@app.route('/test3/')
def test_test3():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200  # private ip
    else:
        return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200  # public ip


@app.route('/test4/')
def test_test4():
    return jsonify(origin=request.headers.get('X-Forwarded-For', request.remote_addr))


@app.route('/test5/')
def test_test5():
    return '<p>abcd{}</p>, <p>\n{}</p>, <p>\n{}</p>, <p>\n{}</p>, <p>\n{}</p>'.format(
        request.remote_addr, request.remote_user, request.environ, request.endpoint, request.method
    )


@app.route('/test6/')
def test_test6():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        if request.environ.get('HTTP_X_REAL_IP') is None:
            return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200  # private ip
        else:
            request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  # public ip
    else:
        return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200  # public ip


if __name__ == '__main__':
    app.run(debug=True, port=5000)
