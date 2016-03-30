def arbitrary(*args):
    le= len(args)
    ar = float(sum(args)) / float(le)
    print le, ar

arbitrary(4, 5 ,6 ,3 ,2, 5, 2, 5, 9, 20, 1, 0)
