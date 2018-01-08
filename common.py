import data_manager


def id_generator(filename):
    lines = data_manager.read_file(filename)

    for search in lines:
        new_id = search[0]

    new_id = int(new_id)
    new_id += 1
    return new_id


def id_generator_for_answers(filename):
    lines = data_manager.read_file_latin(filename)

    for search in lines:
        new_id = search[3]

    new_id = int(new_id)
    new_id += 1
    return new_id


def details_by_id(filename, id):
    lines = data_manager.read_file(filename)

    for data in lines:
        if data[0] == id:
            return data


def answer_by_question_id(filename_answer, id):
    lines = data_manager.read_file_latin(filename_answer)
    searched_answers = []

    for answer in lines:
        if answer[0] == id:
            searched_answers.append(answer)
    return searched_answers


def delete_question(filename_question, filename_answer, id):
    lines_question = data_manager.read_file(filename_question)
    lines_answer = data_manager.read_file_latin(filename_answer)

    edited_answers =[]
    for data in lines_answer:
        if id != data[0]:
            edited_answers.append(data)
            data_manager.write_in_file_latin('answer.csv', edited_answers)

    searched_id = int(id)
    lines_question.pop(searched_id)
    data_manager.write_in_file('question.csv', lines_question)

def delete_answer(filename, id):
    lines = data_manager.read_file_latin('answer.csv')

    edited_answers =[]
    for data in lines:
        if id != data[3]:
            edited_answers.append(data)
            data_manager.write_in_file_latin('answer.csv', edited_answers)

def find_answer_line(filename, id):
    lines = data_manager.read_file_latin('answer.csv')

    for data in lines:
        if id == data[3]:
            return data






