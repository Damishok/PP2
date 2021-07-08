def is_pangram(s):
    alphabet = set()
    for i in s:
        if i == ' ': continue
        else: alphabet.add(i.lower())
    return len(alphabet) == 26

print(is_pangram(input()))