def count_words(filepath):
   with open(filepath) as f:
       dat = f.read()
       dat.replace(",", " ")
       return len(dat.split("."))


print(count_words("e.txt"))