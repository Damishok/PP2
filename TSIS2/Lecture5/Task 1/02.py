def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as file:
        for line in islice(file, nlines):
            print(line)
file_read_from_head('a.txt', 3)