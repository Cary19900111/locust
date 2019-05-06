import gevent
from gevent.event import Event,AsyncResult
from gevent.queue import Queue,Empty
 
tasks = Queue()

def Boss():
    for i in range(25):
        gevent.sleep(1)
        tasks.put(i)

def Worker(name):
    try:
        while True:
            task = tasks.get(timeout=3)
            print("worker %s got task %s"%(name,task))
            gevent.sleep(1)
    except Exception as e:
        print("Leave")
if __name__=="__main__":
    gevent.spawn(Boss).join()
    gevent.joinall([gevent.spawn(Worker,"keith"),gevent.spawn(Worker,"tony"),gevent.spawn(Worker,"Swaggie")])