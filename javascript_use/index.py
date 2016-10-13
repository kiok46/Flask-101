'''
Important attributes of request object are listed below −

Form − It is a dictionary object containing key and value pairs of form
parameters and their values.

args − parsed contents of query string which is part of URL after question
mark (?).

Cookies − dictionary object holding Cookie names and values.

files − data pertaining to uploaded file.

method − current request method.
'''

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
