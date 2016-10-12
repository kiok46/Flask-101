'''
I am already falling in love with flask,
why didn't I do it before?
-_-
'''

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "<html><body><h1>Hello World</h1></body></html>"


@app.route('/render/')
def render():
    # Don't need to give a relative path, it automatically looks for
    # the file in templates folder.
    # that's awesome :D thanks to jinja2 template engine,
    return render_template("index.html")


@app.route('/play/<name>')
def render_name(name):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
