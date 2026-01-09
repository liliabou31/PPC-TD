import time
import random
import multiprocessing
 
import math
import time


def is_prime(n):
    if n < 2:
        return (n, False)
    if n == 2:
        return (n, True)
    if n % 2 == 0:
        return (n, False)
 
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return (n, False)
    return (n, True)

 
if __name__ == "__main__":
    nb_nombre = 1000000
    nb_workers = 20
    indexes = [random.randint(1000, 1000000) for i in range(nb_nombre)]
    liste = []
    with multiprocessing.Pool(processes = nb_workers) as pool:
        start = time.time()
        print("*** Synchronous map")
        for x in pool.map(is_prime, indexes):
            liste.append(x)

        end = time.time()
        seconds = end - start
        print('temps asynchrone : ', seconds, ' pour ', nb_nombre, ' valeur', 'et ',nb_workers, ' workers')


        start = time.time()
        print("*** Asynchronous map")
        for x in pool.map_async(is_prime, indexes).get():
            liste.append(x)
 
        end = time.time()
        seconds = end - start
        print('temps synchrone : ', seconds)