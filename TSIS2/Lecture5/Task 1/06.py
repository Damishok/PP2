def file_read(fname):
    with open(fname, "r") as my_file:
        data = my_file.readlines()
        print(data)
file_read('a.txt')