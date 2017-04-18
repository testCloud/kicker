#!/usr/bin/env python
import pigpio
from RPi import GPIO
from settings import Settings

class LEDController():
    PI = pigpio.pi()

    def __init__(self):
        self.led_off()

    def led_on(self):
        self.PI.set_PWM_dutycycle(Settings.LED_BLACK, 255)
        self.PI.set_PWM_dutycycle(Settings.LED_YELLOW, 255)
        self.status = 'on'

    def led_off(self):
        self.PI.set_PWM_dutycycle(Settings.LED_BLACK, 0)
        self.PI.set_PWM_dutycycle(Settings.LED_YELLOW, 0)
        self.status = 'off'
