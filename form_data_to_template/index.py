from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def student():
    return render_template('student.html')


# Here /result/ won't work and this will cause an error -_-
# as you only mentioned "http://localhost:5000/result"
# and not "http://localhost:5000/result/" this probably has
# some significance which I might learn later. :)
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == "POST":
        result = request.form
        return render_template('result.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
