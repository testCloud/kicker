from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

clients = []
class Broadcaster(WebSocket):

    def handleMessage(self):
       for client in clients:
          if client != self:
             client.sendMessage(self.data)

    def handleConnected(self):
       clients.append(self)

    def handleClose(self):
       clients.remove(self)

server = SimpleWebSocketServer('', 8000, Broadcaster)
server.serveforever()
