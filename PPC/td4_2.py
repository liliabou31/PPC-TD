import threading
from queue import Queue
import statistics
import sys
import time

def worker(queue, data):
    while True:
        print("Starting thread:", threading.current_thread().name)    
        task = queue.get()  # Récupère une tâche
        print(f"{threading.current_thread().name} a reçu la tâche : {task}")

        if task is None:
            queue.task_done()
            break  # Permet d'arrêter le thread proprement

        elif task == 'min':
            print('min :', min(data))
            time.sleep(0.5)

        elif task == 'max':
            print('max :', max(data))
            time.sleep(0.5)

        elif task == 'median':
            print('median :', statistics.median(data))
            time.sleep(0.5)

        elif task == 'mean':
            print('mean :', statistics.mean(data))
            time.sleep(0.5)

        elif task == 'ecart type':
            if len(data) > 1:
                print('ecart type :', statistics.stdev(data))
            else:
                print('ecart type : impossible (pas assez de données)')
            time.sleep(0.5)

        queue.task_done()


if __name__ == "__main__": 
    liste_tache = ["min", "max", "median", "mean", "ecart type"]  
    print("Starting thread:", threading.current_thread().name)

    data = []
    input_str = sys.stdin.read().split()

    for s in input_str:
        try:
            x = float(s)
        except ValueError:
            print("bad number", s)
        else:
            data.append(x) #plus cmd d 

    threads = []
    queue = Queue()

    for i in liste_tache:
        queue.put(i)
    
    for i in liste_tache:
        queue.put(None)

    for i in range(len(liste_tache)):
        t = threading.Thread(target=worker, args=(queue,data))
        t.start()
        threads.append(t)


    for t in threads:
        t.join()

    print("Ending thread:", threading.current_thread().name)