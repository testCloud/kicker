import time
from heartbeat import Heartbeat
from event_publisher import EventPublisher
from led_controller import LEDController
from settings import Settings
from RPi import GPIO
from game import Game
from socket_publisher import SocketPublisher

if __name__ == '__main__':
    event_publisher = EventPublisher()
    socket_publisher = SocketPublisher()
    Heartbeat('kicker', event_publisher)

    led_controller = LEDController()
    led_controller.led_off()

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(Settings.IR_BLACK, GPIO.IN)
    GPIO.setup(Settings.IR_YELLOW, GPIO.IN)

    timer_in_seconds = 1200
    stop_after = time.time()
    ready_for_new_goal = True
    the_game = Game(socket_publisher, event_publisher)
    while True:
        if led_controller.status == 'on' and time.time() > stop_after:
            led_controller.led_off()

        if ready_for_new_goal:
            if GPIO.input(Settings.IR_BLACK) == 1:
                led_controller.led_on()
                the_game.goal_for_black()
                stop_after = time.time() + timer_in_seconds
                ready_for_new_goal = False

            if GPIO.input(Settings.IR_YELLOW) == 1 :
                led_controller.led_on()
                the_game.goal_for_yellow()
                stop_after = time.time() + timer_in_seconds
                ready_for_new_goal = False

        if time.time() - stop_after + timer_in_seconds > 1:
            ready_for_new_goal = True
        time.sleep(.01)
