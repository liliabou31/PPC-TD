import sys
import threading
import random

def pi(n, liste):
    print("Starting thread:", threading.current_thread().name)
    for i in range(0, n):
        x = random.uniform(-1,1)
        y= random.uniform(-1,1)
        res = 0
        if x**2+y**2<=1:
            liste.append('bite')
    print("Ending thread:", threading.current_thread().name)

if __name__ == "__main__":
    print("Starting thread:", threading.current_thread().name)
    nb_points = int(sys.argv[1])
    liste = []
    thread = threading.Thread(target=pi, args=(nb_points,liste))
    thread.start()
    thread.join()
    print('valeur de pi = ',(4*len(liste))/nb_points )
    
    print("Ending thread:", threading.current_thread().name)