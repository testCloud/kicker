import time
from heartbeat import Heartbeat
from event_publisher import EventPublisher
from led_controller import LEDController
from settings import Settings
from RPi import GPIO

if __name__ == '__main__':
    event_publisher = EventPublisher()
    Heartbeat('kicker', event_publisher)

    led_controller = LEDController()
    led_controller.led_off()

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(Settings.IR_BLACK, GPIO.IN)
    GPIO.setup(Settings.IR_YELLOW, GPIO.IN)

    timer_in_seconds = 1200
    stop_after = time.time()
    while True:
        if led_controller.status == 'on' and time.time() > stop_after:
            led_controller.led_off()
        if GPIO.input(Settings.IR_BLACK) == 1 or GPIO.input(Settings.IR_YELLOW) == 1:
            led_controller.led_on()
            stop_after = time.time() + timer_in_seconds
        time.sleep(.001)
