from twisted.internet import reactor, protocol, endpoints
from datetime import datetime

class PrintTimeProtocol(protocol.Protocol):
    def connectionMade(self):
        tm = datetime.now()
        s_tm = tm.strftime("%a %d-%m-%Y %H:%M:%S") + "\r\b"
        self.transport.write(bytes(s_tm, "utf-8"))
        self.transport.loseConnection()

class PrintTimeFactory(protocol.ServerFactory):
    protocol = PrintTimeProtocol


# main
ep = endpoints.serverFromString(reactor, "tcp:1010")
ep.listen(PrintTimeFactory())
reactor.run()

