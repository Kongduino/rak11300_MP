from pinout import *
import time
from machine import Pin, PWM

AIN1 = Pin(WB_A1, Pin.OUT)
ledb = Pin(PIN_LED2, Pin.OUT)
ledg = Pin(PIN_LED1, Pin.OUT)
pwm0 = PWM(AIN1)
pwm0.freq(500)
pwm1 = PWM(ledg)
pwm1.freq(500)
pwm2 = PWM(ledb)
pwm2.freq(500)
duty0 = 0
duty1 = 32768
duty2 = 65536
mult = 512
direction0 = 1
direction1 = 1
direction2 = 1
pwm0.duty_u16(duty0)
pwm1.duty_u16(duty1)
pwm1.duty_u16(duty2)
time.sleep(0.1)
while True:
    pwm0.duty_u16(duty0)
    pwm1.duty_u16(duty1)
    pwm2.duty_u16(duty2)
    duty0 += (mult*direction0)
    duty1 += (mult*direction1)
    duty2 += (mult*direction2)
    if duty0 > 65536:
        duty0 = 65536
        direction0 = -1
    elif duty0 < 0:
        duty0 = 0
        direction0 = 1
    if duty1 > 65536:
        duty1 = 65536
        direction1 = -1
    elif duty1 < 0:
        duty1 = 0
        direction1 = 1
    if duty2 > 65536:
        duty2 = 65536
        direction2 = -1
    elif duty2 < 0:
        duty2 = 0
        direction2 = 1
    time.sleep(0.01)