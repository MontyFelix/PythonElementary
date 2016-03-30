def fac(a):
    if a == 1:
        return a
    else:
        return a*fac(a-1)

fac(4)
