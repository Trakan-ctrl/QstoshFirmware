import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

pwm=GPIO.PWM(11,50)


dc=AngleToPwm(angle)


pwm.start(1.5)
sleep(2)

pwm.ChangeDutyCycle(dc)
sleep(2)
