def fibonacci(n):
    """Return the nth fibonacci  number for positive 'n'"""
    if 0<=n<=1:
        return n
    a,b=0,1 #to store the vales of 1,0
    for f in range(n-1):
        result=a+b
        a=b
        b=result

    return result


for i in range(36):
    print(i,fibonacci(i))

