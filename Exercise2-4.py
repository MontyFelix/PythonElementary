    import time


def timeit(method):
    def timed(*args, **kw):
        start = time.time()
        result = method(*args, **kw)
        ed = time.time()

        print "%r, %5.2f sec" % (method.__name__, ed-start)
        return result
    return timed

@timeit
def fac(a):
    if a == 1:
        return a
    else:
        return a*fac(a-1)

fac(4)
@timeit
def arbitrary(*args):
    le= len(args)
    ar = float(sum(args)) / float(le)
    print le, ar
    time.sleep(2)
    return le, ar

arbitrary(4, 5 ,6 ,3 ,2, 5, 2, 5, 9, 20, 1, 0)
