import csv


def read_file(filename):
    lines = []
    with open(filename, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
                lines.append(row)
    return lines


def write_in_file(filename, new_data):
    with open(filename, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for row in new_data:
            writer.writerow(row)


def write_in_file_latin(filename, new_data):
    with open(filename, "w", encoding="latin-1", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for row in new_data:
            writer.writerow(row)


def read_file_latin(filename):
    lines = []
    with open(filename, "r", encoding="latin-1") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
                lines.append(row)
    return lines
