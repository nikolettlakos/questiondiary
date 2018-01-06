import data_manager


def id_generator(filename):
    lines = data_manager.read_file(filename)

    new_id = 0
    for id in lines:
        new_id = id[0]
    new_id = int(new_id)
    new_id = new_id + 1