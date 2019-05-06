from contextlib import contextmanager

@contextmanager
def test():
    a = 1
    c = 3
    print(a)
    yield
    print(c)

if __name__=='__main__':
    with test():
        print(4)