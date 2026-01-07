
from multiprocessing import Process, Value, Array
import sys

def fibonacci(n,a):
    if n==0 :
        a[0]=0
    elif n==1:
        a[0]=0
        a[1]=1
    else:
        a[0]=0
        a[1]=1
        for i in range (2, n+1):
             a[i] = a[i-1] + a[i-2]


if __name__ == "__main__":
    n = sys.argv[1]
    array = Array('i', int(n)+1)

    if int(n)<0:
        print("valeur négative")
        sys.exit()

    p = Process(target=fibonacci, args=(int(n),array))
    p.start()
    p.join()
    for i in array:
        print(i, end=" ")
 
 


