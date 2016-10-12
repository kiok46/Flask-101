from flask import Flask
app = Flask(__name__)
# taking the name of the module.


# route is a decorator which tells the application URL should call the
# associated function.
# @app.route(rule, options)
@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/hello/<name>')
def test_name(name):
    return 'hello! ' + name


# Shows that we have the power to only accept integers.
@app.route('/blog/<int:post_id>')
def show_blog(post_id):
    return 'Blog Number %d' % post_id


# Shows that we have the power to only accept floats.
@app.route('/rev/<float:rev_no>')
def revision(rev_no):
    return 'Revision Number %f' % rev_no


# Here if we use flask/ as the url then it will show error but
@app.route('/flask')
def flask_print():
    return "flask"


# Here if we use python/as the url then we won't get any error.
@app.route('/python/')
def python_print():
    return "python"

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host, port, debug, options)
