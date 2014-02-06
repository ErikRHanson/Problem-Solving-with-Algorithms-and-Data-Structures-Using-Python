def modexp(x,n,p):
    if n == 0:
        return 1
    t = (x*x)%p
    tmp = modexp(t,n//2,p)
    if n%2 != 0:
        tmp = (tmp * x) % p
    return tmp
