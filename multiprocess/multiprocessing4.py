import multiprocessing


def worker(rear, write):
    while not read.empty():
        name_proc = multiprocessing.current_process().name
        x = read.get()
        res = x * x
        print(name_proc, res)
        write.put(res)
    else:
        read.close()
        write.close()


write = multiprocessing.Queue()
read = multiprocessing.Queue()
[read.put(x) for x in range(3, 7)]

NUM_CORE = 2
procs = []
for i in range(NUM_CORE):
    p = multiprocessing.Process(target=worker, args=(read, write,))
    procs.append(p)
    p.start()

[proc.join() for proc in procs]
print([write.get() for _ in range(write.qsize())])