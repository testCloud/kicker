import time
from heartbeat import Heartbeat
from event_publisher import EventPublisher
from led_controller import LEDController

if __name__ == '__main__':
    event_publisher = EventPublisher()

    Heartbeat('kicker', event_publisher)

    led_controller = LEDController()
    led_controller.led_on()

    while True:
        time.sleep(.001)
