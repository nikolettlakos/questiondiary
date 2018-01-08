from flask import Flask, render_template, request, redirect
import data_manager
import time
import common
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
        lines = data_manager.read_file('question.csv')
        data_dict = request.form.to_dict()
        data_list = [common.id_generator('question.csv'),data_dict['question_title'], data_dict['question_detail'], data_dict['category'], time.time()]

        lines.append(data_list)

        data_manager.write_in_file('question.csv', lines)
        return redirect('/')


@app.route('/write_answer', methods=['POST', 'GET'])
def writing_answer():
    if request.method == 'GET':
        return render_template("write_an_answer_form.html")
    elif request.method == 'POST':
        lines = data_manager.read_file('answer.csv')
        data_dict = request.form.to_dict()
        data_list = [data_dict['answer'], time.time()]

        lines.append(data_list)

        data_manager.write_in_file('answer.csv', lines)
        return redirect('/')


@app.route('/question/<id>', methods=['GET'])
def question_details(id):
    lines = data_manager.read_file('question.csv')
    data = common.details_by_id('question.csv', id)
    return render_template("question_details.html", id=id, lines=data)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    lines = data_manager.read_file('question.csv')
    if request.method == 'GET':
        render_template('edit_form.html', id=id, lines=lines)
    elif request.method == 'POST':
        data_dict = request.form.to_dict()
        lines[1] = data_dict['question_title']
        lines[2] = data_dict['question_detail']
        lines[3] = data_dict['category']

        return redirect('/')

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )