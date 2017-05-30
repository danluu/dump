def fib(n):
    if n == 0:
        return (0,0)
    elif n == 1:
        return (1,0)
    else:
        cdr, cddr = fib(n-1)
        return (cdr + cddr, cdr)

print(fib(22))
