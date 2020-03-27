def f(n):
    for i in range(1,n):
        print ('* '*i)
    for i in range(1,n+1):
        print ('* '*(n+1-i))
    return n
z=f(6)
print(z)