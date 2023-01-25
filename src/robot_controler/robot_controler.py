from typing import Callable
from src.robot_controler.calculations import angle_to_pwm
#import RPi.GPIO as GPIO
from time import sleep
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(11, GPIO.OUT)


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
        # self.pwm_1 = GPIO.PWM(11,50)
        # self.pwm_2 = GPIO.PWM(11,50)
        # self.pwm_3 = GPIO.PWM(11,50)
        # self.pwm_4 = GPIO.PWM(11,50)
        # self.pwm_1.start(0)
        
        
    def __del__(self):
        # GPIO.clenaup()
        # self.pwm_1.stop()
        pass
        
    def move_chosen_servo(self, angle: int, chosen_servo: int):      # chosen_servo -> pin number on board   
        if chosen_servo == 1:
            print("Servo 1 wykonuje ruch!") 
            # self.step_movement(angle, self.robot_position, self.pwm_1)
        elif chosen_servo == 2:
            print("Servo 2 wykonuje ruch!")
        elif chosen_servo == 3:
            print("Servo 3 wykonuje ruch!")
        elif chosen_servo == 4:
            print("Servo 4 wykonuje ruch!")
    
    def move(self, chosen_servo: int):
        pass
        
    def step_movement(self, angle, robot_position, pwm):
        delta = angle - robot_position["position"]["base_horizontal_rotation"]
        print("Pozycja silnika:", robot_position["position"]["base_horizontal_rotation"])
        
        if delta > 0 :
            
            for step in range(int(delta/10)):
                dc = angle_to_pwm(robot_position["position"]["base_horizontal_rotation"] + 10*(step+1))
                print("Ruszam sie co 10 stopni!")
                pwm.ChangeDutyCycle(dc)
                sleep(0.5)
                
        else :
        
            for step in range(int(-(delta/10))):
                dc = angle_to_pwm(robot_position["position"]["base_horizontal_rotation"] - 10*(step+1))
                print("Ruszam sie co 10 stopni!!")
                pwm.ChangeDutyCycle(dc)
                sleep(0.5)
        
        robot_position["position"]["base_horizontal_rotation"] = angle
        

                
                
                
            
            
            
        
        