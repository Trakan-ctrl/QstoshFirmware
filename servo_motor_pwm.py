import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(03, GPIO.OUT)

pwm=GPIO.PWM(03,50)

pwm.start(0)

pwm.ChangeDutyCycle(3.5)
