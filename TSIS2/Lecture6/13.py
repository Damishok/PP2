def pascal(x):
    lst = [1]
    n = [0]
    for i in range(max(x, 0)):
        print(lst)
        lst = [l+r for l, r in zip(lst+n, n+lst)]
    return x>=1

pascal(int(input()))