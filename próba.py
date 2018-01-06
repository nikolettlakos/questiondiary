import data_manager
import csv

def read_file(filename):
    lines = []
    with open(filename, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
                lines.append(row)

    print(lines)


read_file("question.csv")


def write_file(filename):
    with open(filename, encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

write_file("answer.csv")
