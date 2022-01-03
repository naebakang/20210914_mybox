# File encoding: UTF-8

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return '''
    <h1>dlrjs h1 wpahr</h1>
    <p>dlrjs p qhsans</p>
    <a href="https://google.com">google homepage</a>
    '''


@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'Hello, {user_name}({user_id})!'


if __name__ == '__main__':
    app.run(debug=True)
