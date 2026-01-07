from multiprocessing import Process, Value, Array
 
def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]
 
if __name__ == '__main__':
    number = Value('d', 0.0)
    vector = Array('i', range(10))
 
    p = Process(target=f, args=(number, vector))
    p.start()
    p.join()
 
    print(number.value)
    print(vector[:])

# %% 

from multiprocessing import Process, Manager
 
def f(d, l):
    d[1] = 'one'
    d['two'] = 2
    l.reverse()
 
if __name__ == '__main__':
    with Manager() as manager:
        dct = manager.dict()
        lst = manager.list(range(10))
 
        p = Process(target=f, args=(dct, lst))
        p.start()
        p.join()
 
        print(dct)
        print(lst)

