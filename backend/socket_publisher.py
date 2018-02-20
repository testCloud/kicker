import json, time, logging
#import websocket
from websocket import create_connection

class SocketPublisher:

    def __init__(self, port):
        #self.ws = websocket.Websocket()
        self.ws = create_connection("ws://kicker.local:" + str(port))
        #self.ws.connect("ws://kicker.local:15674")

    def publish(self, payload):
        self.ws.send(json.dumps(payload))
