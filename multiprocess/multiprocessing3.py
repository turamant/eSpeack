import multiprocessing

def worker(x):
    name_proc = multiprocessing.current_process().name
    res = x*x
    print(name_proc, res)
    return res

data = range(3, 7)

with multiprocessing.Pool(2) as pool:
    print('Результаты:')
    print(pool.map(worker, data))