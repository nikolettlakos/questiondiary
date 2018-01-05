from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/ask_question', methods=['POST', 'GET'])
def asking_question():
    return render_template("ask_a_question_form.html")

@app.route('/write_answer', methods=['POST', 'GET'])
def writing_answer():
    return render_template("write_an_answer_form.html")

@app.route('/question/<id>', methods=['GET'])
def question_details():
    return render_template("question_details.html")

if __name__ == "__main__":
    app.run(
        debug=True, # Allow verbose error reports
        port=5000 # Set custom port
    )