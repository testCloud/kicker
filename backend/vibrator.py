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

    #GPIO SETUP
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    channel_black = 17
    channel_yellow = 27
    GPIO.setup(channel_black, GPIO.IN)
    GPIO.setup(channel_yellow, GPIO.IN)

    timer_in_seconds = 1200

    def callback(channel):
        print(GPIO.input(channel))
        if GPIO.input(channel) == 0:
            if channel == channel_black:
                print("Goal for black!")
                event_publisher.publish('goal', { 'team': 'black' })
                led_controller.led_on()
            else:
                print("Goal for yellow!")
                event_publisher.publish('goal', { 'team': 'black' })

            led_controller.led_on()
            stop_after = time.time() + timer_in_seconds
        else:
            print("Movement FALLING!")

    GPIO.add_event_detect(channel_black, GPIO.FALLING, bouncetime=500)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(channel_black, callback)  # assign function to GPIO PIN, Run function on change
    GPIO.add_event_detect(channel_yellow, GPIO.FALLING, bouncetime=500)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(channel_yellow, callback)  # assign function to GPIO PIN, Run function on change

    # infinite loop
    while True:
        time.sleep(.5)
