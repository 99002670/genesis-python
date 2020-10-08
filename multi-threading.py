import threading
import time

'''
functions
callable classes
thread inheritance
'''

def my_task():
    print("child thread id:", threading.currentThread().ident)
    for i in range(2):
        print("my_task")
        time.sleep(1)

# print("main thread started")
# th1 = threading.Thread(target=my_task)
# th1.start()
# for i in range(2):
#     print("main thread id:", threading.currentThread().ident)
#     print("child thread id:", threading.currentThread().name)
#     print("main")
#     time.sleep(1)
#
# print("main ends")

class ChocolateBox():
    def __init__(self,):
        self.count = 0

        def take():
            print("cbox is modified by:", threading.currentThread().ident)

    def modify():
        self.count += 1

class Child(threading.Thread):
    def __init__(self, cbox, lock):
        super().__init__()
        pass
    def lock(self):
        print("Request lock by:", threading.currentThread().ident)
        self.lock.acquire_lock()
        print("Acquired lock by:", threading.currentThread().ident)

        for i in range(5):
            self.cbox.take()
            time.sleep(1)
        self.lock.release_lock()
        printf("Release lock by:", threading.currentThread().ident())


lock = threading.Lock()

cbox = ChocolateBox()
child1 = Child(cbox, lock);
child2 = Child(cbox, lock);
child3 = Child(cbox, lock);

child1.start()
child2.start()
child3.start()

child1.join()
child2.join()
