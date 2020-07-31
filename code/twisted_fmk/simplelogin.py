# Simple Login 
from twisted.internet import reactor, protocol, endpoints
from twisted.protocols import basic

class SimpleLoginProtocol(basic.LineReceiver):
    C_PROMPT = 0    # Display Prompt
    C_USERNAME = 1  # User replies with name
    
    def connectionMade(self):
        self.state = self.C_PROMPT
        self.processState(None)
    
    def lineReceived(self, data):
        self.processState(data)

    def processState(self, data):
        if(self.state == self.C_PROMPT):
            self.transport.write(bytes("Who are you ? \r\n","utf-8"))
            self.state = self.C_USERNAME
        elif(self.state == self.C_USERNAME):
            s = str(data, "utf-8")
            if s.strip().lower() == "quit":
                self.transport.write(bytes("Bye Bye!!!\r\n", "utf-8"))
                self.transport.loseConnection()
            else:
                sr = "Hello {0}. Welcome to Python.\r\n".format(s)
                self.transport.write(bytes(sr, "utf-8"))
                self.state = self.C_PROMPT
                self.processState(data)


class SimpleLoginFactory(protocol.ServerFactory):
    protocol = SimpleLoginProtocol


# main
ep = endpoints.serverFromString(reactor, "tcp:1010")
ep.listen(SimpleLoginFactory())
reactor.run()