import gevent
from gevent.event import Event, AsyncResult
evt = AsyncResult() #可以带数据，Event不行
def setter():
    print("好好听课")
    gevent.sleep(5) #持续时间为5
    print("好的 ,下课")
    global evt
    evt.set( 'Done' )
 
def waiter(): #等待下课
    print ("听课 ")
    global  evt, is_ok
    data = evt.get()
    print(data)
    print ("哈哈 , 终于下课了")
def main():
    gevent.joinall( [
        gevent.spawn( setter )
        , gevent.spawn( waiter )
        , gevent.spawn( waiter) 
    ] )
if __name__ == '__main__':
    main()