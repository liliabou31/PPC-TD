from multiprocessing import Process
import os 
import time
import sys
 
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def fibonacci(n):
    info('function fibonacci')
    n = int(n)
    if n==0 :
        print(0)
    elif n==1:
        print (0, end = " ")
        print (1, end = " ")
    else:
        print (0, end = " ")
        print (1, end = " ")
        print (1, end = " ")
        if n > 2:
            res1 = 1
            res2 = 1 
            p = 0
            for i in range (3, n+1):
                p = res1
                res1 += res2
                res2 = p
                print(res1, end = " ")

 
if __name__ == "__main__":
    n = sys.argv[1]
    if int(n)<0:
        print("valeur négative")
        sys.exit()
    info('main line')
    p = Process(target=fibonacci, args=(n,))
    p.start()
    time.sleep(10)
    p.join()