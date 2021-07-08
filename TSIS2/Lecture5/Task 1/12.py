color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as my_file:
    for c in color:
        my_file.write("%s\n" % c)

content = open('b.txt')
print(content.read())