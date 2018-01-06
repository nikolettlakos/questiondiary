import csv


def read_file(filename):
    lines = []
    with open(filename, encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
                lines.append(row)
    return lines


def write_in_file(filename):
    with open(filename, "w") as file:
        writer = file.read()
