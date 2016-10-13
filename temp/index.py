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


'''
The Jinga2 template engine uses the following delimiters for escaping from
HTML.
    - {% ... %} for Statements
    - {{ ... }} for Expressions to print to the template output
    - {# ... #} for Comments not included in the template output
    - # ... ## for Line Statements
'''


@app.route('/play/<name>')
def render_name(name):
    return render_template('hello.html', name=name)


@app.route('/marks/<int:score>')
def result(score):
    '''
    In this method we use conditioning(if else) in jinja2.
    '''
    return render_template('hello.html', marks=score)


@app.route('/multival/')
def multi_val():
    '''
    how to send multiple values and also deal with dictionary.
    '''
    dict_ = {"phy": 23, "chem": 34, "math": 45}
    if sum(dict_.values())/3. < 33:
        anc = "failed"
    else:
        anc = "passed"
    return render_template("multi_vale.html", result=dict_, announcement=anc)


if __name__ == '__main__':
    app.run(debug=True)
