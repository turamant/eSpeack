import multiprocessing
from multiprocessing import Process


def print_func(continent='Asia'):
    print('The name of continent is: ', continent)

if __name__=='__main__':
    print("Количество ядер(процессоров)"
          " на этом компьютере", multiprocessing.cpu_count())
    names = ['America', 'Europe', 'Africa']
    procs = []
    proc = Process(target=print_func)
    procs.append(proc)
    proc.start()

    #создание экземпляра процесса с аргументами
    for name in names:
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()
        
    #Завершить все процессы
    for proc in procs:
        proc.join()
