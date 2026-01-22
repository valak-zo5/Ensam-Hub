
from flask import Flask, render_template



app = Flask(__name__)







@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route("/pomodoro")
def pomodoro():
    return render_template("pomodoro.html")

@app.route("/drives")
def drives():
    return render_template("drives.html")

@app.route("/notes")
def notes():
    return render_template("notes.html")

@app.route("/focus")
def focus():
    return render_template("focus.html")

@app.route("/other")
def other():
    return render_template("other.html")



if __name__ == '__main__':
    app.run(debug=True,port=8000)