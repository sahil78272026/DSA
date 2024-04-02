from apscheduler.schedulers.background import BackgroundScheduler
import time
import atexit

def my_task1():
    print("Task 1")
def ny_task2():
    print("Task 2")
if __name__=='__main__':
     scheduler = BackgroundScheduler()
     scheduler.configure({'apscheduler.daemon': False})
     scheduler.add_job(my_task1, 'interval', minutes=1)
     scheduler.start()
     while True:
         time.sleep(1)