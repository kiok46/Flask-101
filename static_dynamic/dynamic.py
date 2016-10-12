'''
I am too lazy to document this but I think you should read static.py first
then you won't need any documentation for this file.

but then I accept pull requests.

Thank you.
'''

from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/admin/')
def admin():
    return "hello admin"


@app.route('/guest/<name>')
def guest(name):
    return "hello guest: " + name


@app.route('/user/<name>')
def guess_who(name):
    if name == "admin":
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', name=name))


if __name__ == "__main__":
    app.run(debug=True)
