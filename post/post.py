'''
Run: python post.py
Open: login.html from ./templates in any browser
In the Browser:
    - Type a name and click submit button/ press enter.
    - login method in post.py class will be called.s
'''

from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return "welcome " + name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == "__main__":
    app.run(debug=True)
