import RPi.GPIO as GPIO
from time import sleep

def AngleToPwm(angle):
    dc=1.5+angle*(10/180)
    return(dc)
    
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

pwm=GPIO.PWM(11,50)


angle=input('Set the turn angle')

dc=AngleToPwm(angle)


pwm.start(1.5)
sleep(2)

pwm.ChangeDutyCycle(dc)
sleep(2)


