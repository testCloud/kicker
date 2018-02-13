from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

clients = []
class EventBus(WebSocket):

    def handleMessage(self):
       print('message:', self.data)
       for client in clients:
          if client != self:
             client.sendMessage(self.data)

    def handleConnected(self):
       print(self.address, 'connected')
       clients.append(self)
       self.sendMessage('{ "kickerStatus": "playing", "score_black": 0, "score_yellow": 0 }')

    def handleClose(self):
       clients.remove(self)
       print(self.address, 'disconnected')

server = SimpleWebSocketServer('', 15675, EventBus)
server.serveforever()
