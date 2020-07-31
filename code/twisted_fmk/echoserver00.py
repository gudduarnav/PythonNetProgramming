# TCP Echo Server

from twisted.internet import reactor, protocol, endpoints  

class EchoProtocol(protocol.Protocol):
    def connectionMade(self):
        print("NOTE: An incoming connection")

    def dataReceived(self, data):
        self.transport.write(data)

class EchoFactory(protocol.ServerFactory):
    protocol = EchoProtocol


def main():
    fingerEP = endpoints.serverFromString(reactor,
        "tcp:1010")
    fingerEP.listen(EchoFactory())
    reactor.run()


if __name__=="__main__":
    main()

