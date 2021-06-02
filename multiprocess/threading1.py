'''
>> lscpu - информация об системе , потоках!!!
'''

import time
import threading
from threading import Thread

def sleepMe(i):
    print("Thread %s going to sleep for 5 seconds" % threading.current_thread())
    time.sleep(5)
    print("Thread %s is awake now." % threading.current_thread())



for i in range(4):
    th = Thread(target=sleepMe, args=(i,))
    th.start()

for thread in threading.enumerate():
    print("Все активные потоки %s." % thread.getName())
print("Главный поток: ", threading.main_thread())
