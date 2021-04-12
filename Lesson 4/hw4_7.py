def fact(num):
    f=1
    for el in range(1,num):
        f=f*el
        yield(f)
while True:
    try:
        g=fact(5)
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))
    except StopIteration:
        print('фсё')
        break
    
