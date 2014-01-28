
def squareroot(n):
    root = n/2.0   #initial guess will be 1/2 of n
    for k in range(20):
        root = (1.0/2.0) * (root + (n / root))

    return root

print squareroot(9)

print squareroot(4563)
