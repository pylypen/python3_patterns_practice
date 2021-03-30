import threading


class SingletonDoubleChecked(object):
    __singleton_lock = threading.Lock()
    __singleton_instance = None

    @classmethod
    def instance(cls):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()

        return cls.__singleton_instance


if __name__ == "__main__":
    class X(SingletonDoubleChecked):
        pass

    class Y(SingletonDoubleChecked):
        pass

    A1, A2 = X.instance(), X.instance()
    B1, B2 = Y.instance(), Y.instance()

    assert A1 is not B1
    assert A1 is A2
    assert B1 is B2

    print('A1 : ', A1)
    print('A2 : ', A2)
    print('B1 : ', B1)
    print('B2 : ', B2)
