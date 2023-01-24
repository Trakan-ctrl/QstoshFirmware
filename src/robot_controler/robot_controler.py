from typing import Callable
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)


class RobotControler:

    def __init__(self):
        self.robot_position = {
                            "type": "live_position",
                            "position": {
                                "base_vertical_rotation": 0.,
                                "base_horizontal_rotation": 20.,
                                "extension_rotation": 50.,
                                "grabbed": False
                            }}
    def __del__(self):
        GPIO.clenaup()
        
        
    def move_chosen_servo(self, chosen_servo: int):      # chosen_servo -> pin number on board   
        if chosen_servo == 1:
            print("Servo 1 wykonuje ruch!")    
        elif chosen_servo == 2:
            print("Servo 2 wykonuje ruch!")
        elif chosen_servo == 3:
            print("Servo 3 wykonuje ruch!")
        elif chosen_servo == 4:
            print("Servo 4 wykonuje ruch!")
    
    def move(self, chosen_servo: int):
        
       

        pwm=GPIO.PWM(11,50)


        def AngleToPwm(angle):
                dc=1.5+angle*(10/180)
                return(dc)
        
        answer='n'

        
        while (answer=='y'):


            

            angle=input('Set the turn angle')

            dc=AngleToPwm(angle)


            pwm.start(1.5)
            sleep(3)

            pwm.ChangeDutyCycle(dc)
            sleep(2)
            
            answer=input('Do you want to close programme?(y,n)')

                
                
                
            
            
            
        
        