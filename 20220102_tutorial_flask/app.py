# File encoding: UTF-8

from flask import Flask, url_for, request, render_template, make_response, abort, redirect, jsonify, session
from markupsafe import escape  # <> 자를 &lt; 로 변환함
from werkzeug.utils import secure_filename
from werkzeug.middleware.proxy_fix import ProxyFix

"""
20220111, 보아하니, url, upload file name 등과 같은 입력 받을 때 보안에 신경써야 한다.
"""


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


# # HTTP Methods
# def do_the_login():
#     print('abcd')
#
#
# def show_the_login_form():
#     return 'abcd2'
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# # Rendering Templates
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
#
# Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
# Markup.escape('<blink>hacker</blink>')
# Markup('<em>Marked up</em> &raquo; HTML').striptags()

# Accessing Request Data
with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

# with app.request_context(environ):
#     assert request.method == 'POST'


# # The Request Object
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)
#
#
# searchword = request.args.get('key', '')


# # File Uploads
# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['the_file']
#         file.save(f'/var/www/uploads/{secure_filename(file.filename)}')

# # Cookies
# @app.route('/')
# def index():
#     # username = request.cookies.get('username')
#     # # use cookies.get(key) instead of cookies[key] to not get a
#     # # KeyError if the cookie is missing.
#     # return str(username)
#
#     resp = make_response(render_template('hello.html'))
#     resp.set_cookie('username', 'the username')
#     return resp


# # Redirects and Errors
# @app.route('/')
# def index():
#     return redirect(url_for('login'))
#
#
# @app.route('/login')
# def login():
#     abort(401)
#     # this_is_never_executed()
#
#
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404


# # About Responses
# @app.errorhandler(404)
# def not_found(error):
#     resp = make_response(render_template('error.html'), 404)
#     resp.headers['X-Something'] = 'A value'
#     return resp


# # APIs with JSON
# @app.route("/me")
# def me_api():
#     user = get_current_user()
#     return {
#         "username": user.username,
#         "theme": user.theme,
#         "image": url_for("user_image", filename=user.image),
#     }
#
#
# @app.route("/users")
# def users_api():
#     users = get_all_users()
#     return jsonify([user.to_json() for user in users])

# Sessions
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# Message Flashing


# Logging
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')

# Hooking in WSGI Middleware
app.wsgi_app = ProxyFix(app.wsgi_app)

# Using Flask Extensions

# Deploying to a Web Server
