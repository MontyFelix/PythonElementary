import threading
import math
from sys import argv
import Exercise2

class f(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        global result
        #or math.factorial(self.num)
        temp = Exercise2.fac(self.num)
        print temp
        print "%s: calculate %d's factorial is %d" %(self.name,self.num,temp)
        result = temp

result = 0
threads = []
global qr
ar, fa = argv
def test():
    for i in range(0, int(fa)+1):
        t = f(i)
        threads.append(t)
    for i in range(1, len(threads)):
        threads[i].start()
        threads[i].join()

if __name__ == '__main__':
    test()

    print 'The result is %d' %result
