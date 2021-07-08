def f(a):
    def fu(b):
        nonlocal a
        a+=1
        return (a+b)
    return fu

func = f(4)
print(func(5))