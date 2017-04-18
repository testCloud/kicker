import RPi.GPIO as GPIO
import pigpio
from requests_futures.sessions import FuturesSession
import json, time

IR_PIN = 17
IR_PIN2 = 27
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
PI = pigpio.pi()
PI.set_PWM_dutycycle(16, 0)
PI.set_PWM_dutycycle(26, 0)

if __name__ == '__main__':
    GPIO.setup(IR_PIN, GPIO.IN)
    GPIO.setup(IR_PIN2, GPIO.IN)
    session = FuturesSession()

    previous_state1 = 0
    previous_state2 = 0

    while True:
        current_state1 = GPIO.input(IR_PIN)
        current_state2 = GPIO.input(IR_PIN2)
        if current_state1 > previous_state1:
            PI.set_PWM_dutycycle(16, 255)
            PI.set_PWM_dutycycle(26, 0)
            print("GOOOOAAAAL for team Yellow!!!")
            session.post('http://kraken.test.io/events', data=json.dumps({ 'event': { 'name': 'goal', 'payload': { 'team': 'yellow' } } }))
        previous_state1 = current_state1
        if current_state2 > previous_state2:
            PI.set_PWM_dutycycle(26, 255)
            PI.set_PWM_dutycycle(16, 0)
            print("GOOOOAAAAL for team BLACK!!!")
            session.post('http://kraken.test.io/events', data=json.dumps({ 'event': { 'name': 'goal', 'payload': { 'team': 'black' } } }))
        previous_state2 = current_state2
        time.sleep(0.01)

