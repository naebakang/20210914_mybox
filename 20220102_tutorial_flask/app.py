# File encoding: UTF-8

from flask import Flask, url_for, request, render_template
from markupsafe import escape  # <> 자를 &lt; 로 변환함


app = Flask(__name__)


# A Minimal Application
# @app.route('/')
# def hello_world():
#     return '<p>Hello, World!</p>'


# HTML Escaping
# @app.route('/<name>')
# def hello(name):
#     return f'Hello, {escape(name)}!'


# Rounting
# @app.route('/')
# def index():
#     return 'Index Page'
#
#
# @app.route('/hello')
# def hello():
#     return 'Hello, World!'
#

# Variable Rules
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User {}'.format(escape(username))
#
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'
#
#
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'
#

# Unique URLs / Redirection Behavior
# @app.route('/projects/')
# def projects():
#     return 'The project page'
#
#
# @app.route('/about')
# def about():
#     return 'The about page'


# URL Building
# @app.route('/')
# def index():
#     return 'index'
#
#
# @app.route('/login')
# def login():
#     return 'login'
#
#
# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'
#
#
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))


# HTTP Methods
def do_the_login():
    print('abcd')


def show_the_login_form():
    return 'abcd2'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
