import random


def random_line(f_name):
    lines = open(f_name).read().splitlines()
    return random.choice(lines)


print(random_line('a.txt'))