import glob

char_list = []
files_list = glob.glob("a.txt")
for file_elem in files_list:
    with open(file_elem, "r") as f:
        char_list.append(f.read())

print(*char_list)