
from threading import Thread
import time

class TaskClass(object):    
    
    @staticmethod
    def task_1():
        print("task_1 - start")
        time.sleep(5)
        print("task_1 - finish")    
    
    @staticmethod    
    def task_2():
        print("task_2 - start")
        time.sleep(10)
        print("task_2 - finish")
    
    @staticmethod
    def task_3():
        print("task_3 - start")
        time.sleep(5)
        print("task_3 - finish")
    
def main():
    thead1 = Thread(target=TaskClass.task_1()).start()
    thead2 = Thread(target=TaskClass.task_2()).start()
    thead3 = Thread(target=TaskClass.task_3()).start()
    
if __name__ == '__main__':
    main()