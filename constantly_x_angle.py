
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

robot_position = {
                "position": {
                "base_vertical_rotation": 0.,
                "base_horizontal_rotation": 90.,
                "extension_rotation": 50.,
                "grabbed": False
                }}

pwm=GPIO.PWM(11,50)


def angle_to_pwm(angle):
    dc=2.5+float(angle)*(10/180)
    return(dc)
 
    
def step_movement(angle, robot_position):
    delta = angle - robot_position["position"]["base_horizontal_rotation"]
    print("Pozycja silnika 1:", robot_position["position"]["base_horizontal_rotation"])
    
    if delta > 0 :
        
        for step in range(int(delta/10)):
            dc = angle_to_pwm(angle + 10*(step+1))
            print("Ruszam sie co 10 stopni!")
            pwm.ChangeDutyCycle(dc)
            sleep(2)
            
    else :
    
        for step in range(int(-(delta/10))):
            dc = angle_to_pwm(angle - 10*(step+1))
            print("Ruszam sie co 10 stopni!!")
            pwm.ChangeDutyCycle(dc)
            sleep(2)
    
    robot_position["position"]["base_horizontal_rotation"] = angle
    
        
    
    
 
answer='n'

 
while (answer=='n'):


    

    angle=float(input('Set the turn angle'))
    
    step_movement(angle, robot_position)
    
    answer=input('Do you want to close programme?(y,n)')


