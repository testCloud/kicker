import json
import websocket
from socket_publisher import SocketPublisher

def on_message(ws, message):
    state_bus_publisher = SocketPublisher(15674)
    state_bus_publisher.publish(json.loads(message))
    print(message)

def on_error(ws, error):
    print("### errored ###")
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("### opened ###")

if __name__ == '__main__':

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp('ws://kicker.local:15675',
            on_message = on_message,
            on_error = on_error,
            on_close = on_close)

    ws.run_forever()
