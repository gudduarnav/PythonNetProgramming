# Echo Line Server
from twisted.internet import reactor, protocol, endpoints 
from twisted.protocols import basic 

class EchoProtocol(basic.LineReceiver):
    def lineReceived(self, data):
        self.transport.write(data + b"\r\n")

class EchoFactory(protocol.ServerFactory):
    protocol = EchoProtocol


# main
ep = endpoints.serverFromString(reactor, "tcp:1010")
ep.listen(EchoFactory())
reactor.run()
