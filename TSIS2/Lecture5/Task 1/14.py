with open('b.txt') as fh1, open('a.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        # line1 from b.txt, line2 from a.txt
        print(line1+line2)