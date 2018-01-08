import data_manager


def id_generator(filename):
    lines = data_manager.read_file(filename)

    for search in lines:
        new_id = search[0]

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
