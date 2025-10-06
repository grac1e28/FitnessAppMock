from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/tutoring")
def tutoring():
    return render_template('tutoring.html')

@app.route("/quizzes")
def quizzes():
    return render_template('quizzes.html')

@app.route("/study")
def study():
    return render_template('study.html')

if __name__ == "__main__":
    app.run(debug = True)