
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

pwm=GPIO.PWM(11,50)


def AngleToPwm(angle):
        dc=1.5+angle*(10/180)
        return(dc)
 
answer='n'

 
while (answer=='y'):


    

    angle=input('Set the turn angle')

    dc=AngleToPwm(angle)


    pwm.start(1.5)
    sleep(2)

    pwm.ChangeDutyCycle(dc)
    sleep(2)
    
    answer=input('Do you want to close programme?(y,n)')


