from multiprocessing import Queue

colors = ['red', 'green','blue','black']
cnt = 1
#создание экземпляра очереди
queue = Queue()
print('Поместить элементы в очередь: ')
for color in colors:
    print('item no:', cnt, ' ', color)
    queue.put(color)
    cnt += 1

print('\nудаление элементов из очереди: ')
cnt = 0
while not queue.empty():
    print('item no:', cnt, ' ', queue.get())
    cnt += 1
