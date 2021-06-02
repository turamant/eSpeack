import threading

def delayed():
    print("I am printed after 5 seconds!")

print("Hello")
thread = threading.Timer(5, delayed)
thread.start()
print("Bye bye!")


