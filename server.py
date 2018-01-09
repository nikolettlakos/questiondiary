from flask import Flask, render_template, request, redirect
import data_manager
import time
import common
app = Flask(__name__)

@app.route('/')
def homepage():
    data = common.details_by_id('question.csv', id)
    lines = data_manager.read_file('question.csv')
    return render_template("homepage.html", lines=lines, data=data)

@app.route('/ask_question', methods=['POST', 'GET'])
def asking_question():
    if request.method == 'GET':
        return render_template('ask_a_question_form.html')
    elif request.method == 'POST':
        lines = data_manager.read_file('question.csv')
        data_dict = request.form.to_dict()
        data_list = [common.id_generator('question.csv'),data_dict['question_title'], data_dict['question_detail'], data_dict['category'], time.asctime(time.localtime(time.time()))]

        lines.append(data_list)

        data_manager.write_in_file('question.csv', lines)
        return redirect('/')

@app.route('/question/<id>/write_answer', methods=['POST', 'GET'])
def writing_answer(id):
    if request.method == 'GET':
        return render_template("write_an_answer_form.html")
    elif request.method == 'POST':
        lines = data_manager.read_file_latin('answer.csv')
        data_dict = request.form.to_dict()
        data_list = [id, data_dict['answer'], time.asctime(time.localtime(time.time())), common.id_generator_for_answers('answer.csv')]

        lines.append(data_list)

        data_manager.write_in_file_latin('answer.csv', lines)
        return redirect('/')

@app.route('/question/<id>', methods=['GET'])
def question_details(id):
    lines = data_manager.read_file('question.csv')

    data = common.details_by_id('question.csv', id)
    answer = common.answer_by_question_id('answer.csv', id)
    return render_template("question_details.html", id=id, lines=data, answer=answer)

@app.route('/question/<id>/delete', methods=['GET'])
def delete_question_with_answer(id):
    lines_question=data_manager.read_file('question.csv')
    lines_answer=data_manager.read_file_latin('answer.csv')

    common.delete_question('question.csv', 'answer.csv', id)
    return redirect('/')

@app.route('/question_edit/<id>', methods=['GET', 'POST'])
def edit_question(id):
    lines = data_manager.read_file('question.csv')
    found_lines = common.find_question_line('question.csv', id)

    if request.method == 'GET':
        return render_template('ask_a_question_form.html')
    elif request.method == 'POST':
        data_dict = request.form.to_dict()

        for data in lines:
            question_id = data[0]
            question_time= data[4]

        data_list = [question_id, data_dict['question_title'], data_dict['question_detail'], data_dict['category'], question_time]

        searched_id = int(id)
        lines[searched_id] = data_list

        data_manager.write_in_file('question.csv', lines)
        return redirect('/')

@app.route('/edit_answer/<id>', methods=['POST', 'GET'])
def edit_answer(id):
    lines = data_manager.read_file_latin('answer.csv')
    found_lines = common.find_answer_line('answer.csv,', id)

    if request.method == 'GET':
        return render_template('write_an_answer_form.html')
    elif request.method == 'POST':
        data_dict = request.form.to_dict()
        found_lines[1] = data_dict['answer']

        for data in lines:
            answer_id_by_question = data[0]
            answer_time = data[2]
            answer_id = data[3]

        data_list = [answer_id_by_question, data_dict['answer'], answer_time, answer_id]

        searched_id = int(id)
        lines[searched_id] = data_list

        data_manager.write_in_file_latin('answer.csv', lines)
        return redirect('/')

@app.route('/delete_answer/<id>', methods=['GET'])
def delete_answer(id):
    lines=data_manager.read_file_latin('answer.csv')

    common.delete_answer('answer.csv', id)
    common.answer_id_reduce('answer.csv', id)
    return redirect('/')

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
