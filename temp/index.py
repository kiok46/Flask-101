'''
By now I am seriously falling in love with flask,
why didn't I do it before??
-_-
'''

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "<html><body><h1>Hello World</h1></body></html>"


@app.route('/render/')
def render():
    # Here you do not need to give the proper path i.e templates/index.html
    # seems like it automatically looks for a folder named "templates"
    # that's awesome :D thanks to jinja2 template engine.
    return render_template('index.html')


@app.route('/play/<name>')
def hello_play(name):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)
