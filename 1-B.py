def f(x):
    a=True
    for i in range(2,x):
        if x%i==0:
            a=False
            break
    if a:
        return x
    else:
        return 0
L=[f(x) for x in range(1,1000) if f(x)!=0]
print(L)
