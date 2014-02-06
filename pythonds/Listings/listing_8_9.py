def ext_gcd(x,y):
    if y == 0:
        return(x,1,0)
    else:
        (d,a,b) = ext_gcd(y, x%y)  
        return(d,b,a-(x//y)*b)           