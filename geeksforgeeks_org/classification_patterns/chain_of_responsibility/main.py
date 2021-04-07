class AbstractHandler(object):
    def __init__(self, nxt):
        self._nxt = nxt

    def handle(self, request):
        handled = self.processRequest(request)

        if not handled:
            self._nxt.handle(request)

    def processRequest(self, request):
        raise NotImplementedError('First implement it !')


class FirstConcreteHandler(AbstractHandler):
    def processRequest(self, request):
        if 'a' < request <= 'e':
            print("This is {} handling request '{}'".format(self.__class__.__name__, request))
            return True


class SecondConcreteHandler(AbstractHandler):
    def processRequest(self, request):
        if 'e' < request <= 'l':
            print("This is {} handling request '{}'".format(self.__class__.__name__, request))
            return True


class ThirdConcreteHandler(AbstractHandler):
    def processRequest(self, request):
        if 'l' < request <= 'z':
            print("This is {} handling request '{}'".format(self.__class__.__name__, request))
            return True


class DefaultHandler(AbstractHandler):
    def processRequest(self, request):
        print("This is {} telling you that request '{}' has no handler right now.".format(self.__class__.__name__,
                                                                                          request))
        return True


class User:
    def __init__(self):
        initial = None
        self.handler = FirstConcreteHandler(SecondConcreteHandler(ThirdConcreteHandler(DefaultHandler(initial))))

    def agent(self, user_request):
        for request in user_request:
            self.handler.handle(request)


if __name__ == "__main__":
    user = User()

    string = "GeeksforGeeks"
    requests = list(string)

    user.agent(requests)
