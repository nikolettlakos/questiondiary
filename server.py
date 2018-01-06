from flask import Flask, render_template, request, redirect
import data_manager
import time
app = Flask(__name__)

@app.route('/')
def homepage():
    lines = data_manager.read_file('question.csv')
    return render_template("homepage.html", lines=lines)

@app.route('/ask_question', methods=['POST', 'GET'])
def asking_question():
    if request.method == 'GET':
        return render_template('ask_a_question_form.html')
    elif request.method == 'POST':
        data_manager.write_in_file('answer.csv')
        return render_template('/')

@app.route('/write_answer', methods=['POST', 'GET'])
def writing_answer():
    return render_template("write_an_answer_form.html")

'''
@app.route('/question/<id>', methods=['GET'])
def question_details():
    id = data_manager.read_file('answer.csv'[])
    return render_template("question_details.html", id=id)
'''

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )