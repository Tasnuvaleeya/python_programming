import threading


class MyMessenger(threading.Thread):
    def run(self):
        for _ in range(200):
            print(threading.current_thread().getName())

x = MyMessenger(name='Send Message')
y = MyMessenger(name='Receive Message')
x.start()
y.start()