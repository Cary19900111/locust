import gevent
def test1():
    print("10")
    # gevent.sleep(0)
    print("11")
    # gevent.sleep(0)

def test2():
    print("20")
    # gevent.sleep(0)
    print("21")
    # gevent.sleep(0)

def test3():
    print("30")
    # gevent.sleep(0)
    print("31")
    # gevent.sleep(0)
if __name__=="__main__":
    # print(1)
    c = gevent.joinall([gevent.spawn(test1),gevent.spawn(test1),gevent.spawn(test1)])
    print(c)
