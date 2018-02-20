import time
from settings import Settings
from RPi import GPIO
from socket_publisher import SocketPublisher

if __name__ == '__main__':
    state_bus_publisher = SocketPublisher(15674)

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(Settings.IR_BLACK, GPIO.IN)
    GPIO.setup(Settings.IR_YELLOW, GPIO.IN)

    timer_in_seconds = 1200
    stop_after = time.time()
    ready_for_new_goal = True

    while True:
        if ready_for_new_goal:
            if GPIO.input(Settings.IR_BLACK) == 1:
                stop_after = time.time() + timer_in_seconds
                ready_for_new_goal = False
                state_bus_publisher.publish({ 'message': 'goal', 'payload': { 'team': 'black' } })

            if GPIO.input(Settings.IR_YELLOW) == 1 :
                stop_after = time.time() + timer_in_seconds
                ready_for_new_goal = False
                state_bus_publisher.publish({ 'message': 'goal', 'payload': { 'team': 'yellow' } })

        if time.time() - stop_after + timer_in_seconds > 1:
            ready_for_new_goal = True
        time.sleep(.01)
