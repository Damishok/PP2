def file_size(f_name):
    import os
    stat_info = os.stat(f_name)
    return stat_info.st_size


def file_len(f_name):
    with open(f_name, 'r') as infile:
        words = infile.read()
    return words


print("File size in bytes of a plain file: " + str(file_size("d.txt")))

print(len(file_len('d.txt')))