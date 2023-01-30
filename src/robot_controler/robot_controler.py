from typing import Callable
from src.robot_controler.calculations import angle_to_pwm, recasting_coordinates
from src.robot_controler.inverse_kinematics import inverse_kinematics
import RPi.GPIO as GPIO
import concurrent.futures
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
# GPIO.setup(12, GPIO.OUT)
# GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
class RobotControler:

    def __init__(self):
        self.robot_position = {
                            "type": "live_position",
                            "position": {
                                "base_vertical_rotation": 0.,
                                "base_horizontal_rotation": 90.,
                                "extension_rotation": 50.,
                                "grabbed": False
                            }}
        self.pwm_1 = GPIO.PWM(11,50)
        # self.pwm_2 = GPIO.PWM(12,50)
        # self.pwm_3 = GPIO.PWM(13,50)
        self.pwm_4 = GPIO.PWM(15,50)
        self.pwm_1.start(0)
        # self.pwm_2.start(0)
        # self.pwm_3.start(0)
        self.pwm_4.start(0)
        
        
    def __del__(self):
        self.pwm_1.stop()
        # self.pwm_2.stop()
        # self.pwm_3.stop()
        self.pwm_4.stop()
        GPIO.cleanup()
        
    def move_chosen_servo(self, angle: int, chosen_servo: int):      # chosen_servo -> pin number on board   
        if chosen_servo == 1:
            print("Servo 1 wykonuje ruch!") 
            self.step_movement(angle, self.robot_position, self.pwm_1, chosen_servo)
        elif chosen_servo == 2:
            print("Servo 2 wykonuje ruch!")
            # self.step_movement(angle, self.robot_position, self.pwm_2, chosen_servo)
        elif chosen_servo == 3:
            print("Servo 3 wykonuje ruch!")
            # self.step_movement(angle, self.robot_position, self.pwm_3, chosen_servo)
        elif chosen_servo == 4:
            print("Servo 4 wykonuje ruch!")
            self.step_movement(angle, self.robot_position, self.pwm_4, chosen_servo)
    
    def move(self, chosen_servo: int):
        pass
        
    def step_movement(self, angle, robot_position, pwm, chosen_servo: int):
        delta = angle - robot_position["position"]["base_horizontal_rotation"]
        print("Pozycja silnika:", robot_position["position"]["base_horizontal_rotation"])
        
        if delta > 0 :
            
            for step in range(int(delta/10)):
                dc = angle_to_pwm(robot_position["position"]["base_horizontal_rotation"] + 10*(step+1), chosen_servo)
                print("Ruszam sie co 10 stopni!")
                pwm.ChangeDutyCycle(dc)
                sleep(0.5)
                
        else :
        
            for step in range(int(-(delta/10))):
                dc = angle_to_pwm(robot_position["position"]["base_horizontal_rotation"] - 10*(step+1), chosen_servo)
                print("Ruszam sie co 10 stopni!!")
                pwm.ChangeDutyCycle(dc)
                sleep(0.5)
        print(dc)
        robot_position["position"]["base_horizontal_rotation"] = angle
        
    def point_movement(self, cor_x, cor_y, cor_z):
        cor_x, cor_z, delta_base = recasting_coordinates(cor_x, cor_y, cor_z)
        print(delta_base)
        delta_horizontal, delta_extension = inverse_kinematics(cor_x, cor_z)
        self.step_movement(delta_base, self.robot_position, self.pwm_1, 1)
        # self.step_movement(delta_horizontal, self.robot_position, self.pwm_2, 2)
        # self.step_movement(delta_extension, self.robot_position, self.pwm_3, 3)
        
    def concurrent_movement(self, servo_engines: dict):
        print("Concurrent movement of servos: ", servo_engines)
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            for engine in servo_engines:
                print("Starting thread: ", engine)
                # executor.submit(self.hello_thread)
                executor.submit(self.move_chosen_servo, servo_engines[engine], engine)

    def hello_thread(self):
        print("Hello!!!")
        


