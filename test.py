from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, 夏瑞迪小可爱'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)