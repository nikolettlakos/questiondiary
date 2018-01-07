import data_manager
import csv


def details_by_id(filename, id):
    lines = data_manager.read_file(filename)

    for data in lines:
        if data[0] == id:
            print(data)



details_by_id('question.csv', "1")