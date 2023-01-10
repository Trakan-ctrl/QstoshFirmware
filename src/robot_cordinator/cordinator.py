import logging
from threading import Thread
import time
from calculations.inv_kinematics_two_links import inverse_kinematics
from calculations.recasting import recasting_coordinates
import RPi.GPIO as GPIO
from time import sleep

logging.basicConfig(level=logging.DEBUG)

from bluetooth.connection_broker import ConnectionBroker
from src.configs.config_parser import ConfigParser


class RobotCordinator:

    status = {1: "idle"}

    def __init__(self):
        self.config = None
        self.broker = ConnectionBroker()
        self.robot_state = {
                        "type": "live_position",
                        "position": {
                            "base_vertical_rotation": 0.,
                            "base_horizontal_rotation": 20.,
                            "extension_rotation": 50.,
                            "grabbed": False
                        }
                     }

       
        self.broker.add_callback_to_topic("execute_movement", self.execute_movement)
        self.broker.add_callback_to_topic("calculate_pbm", self.calculate_points_based_movement)
        # dodanie callbacks
        # ustawienie parametrow poczatkowych
        #
        #
        #
        #
        #
        

    def configure(self, configs):
        pass

    def run(self):
        self.execute_movement
        self.broker.start_broker()
        
        

        while(1):
            sleep(2)
            print('Wykonuje sie w nieskonczonosc!!!')
            pass    

 

    def move(self):
        
        #Thread(target=self.live_position).run()

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(11, GPIO.OUT)

        pwm_bh=GPIO.PWM(11,50)
    #   pwm_bv=GPIO.PWM(11,50)
    #   pwm_e=GPIO.PWM(11,50)
                    

    #   pwm.start(1.5) ustawienie poczatkowej pozycji
    #   pwm.start(1.5) 
    #   pwm.start(1.5)
    #   sleep(2)

    #    pwm_bh.ChangeDutyCycle(AngleToPwm(bh))
    #    pwm_bv.ChangeDutyCycle(AngleToPwm(bv))
    #    pwm_e.ChangeDutyCycle(AngleToPwm(e))
    #    sleep(2)

    def grap(self):
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(11, GPIO.OUT)


    def execute_movement(self, msg: dict):
        if msg["movement_type"] == "arm_position":
            self.robot_state["position"]["base_vertical_rotation"] = msg["arm_position"]["base_vertical_rotation"] 
            self.robot_state["position"]["base_horizontal_rotation"] = msg["arm_position"]["base_horizontal_rotation"] 
            self.robot_state["position"]["extension_rotation"] = msg["arm_position"]["extension_rotation"] 
            self.move()
            #Thread(target=self.res, args=(bh, bv, e)).run()
        
        #elif msg["movement_type"] == "point_based_position":
        #    inverse_kinematics(msg["point_based_position"]["x"], msg["point_based_position"]["x"], msg["point_based_position"]["x"])
        
        elif msg["movement_type"] == "grab_position":
            self.robot_state["position"]["grabbed"] = msg["grab_position"]["grabbed"]
            self.grap()
            #self.broker.send(str(self.robot_state))
        #status[1] = "idle"
        #cur_status(1)
        
    

    def live_position(self):
        print("sending position")
        #print(str(robot_state))
        self.broker.send(str(self.robot_state))

    def cur_position(self):
        self.broker.send(str(self.robot_state))

    def live_status(self):
        pass

    def cur_status(self, msg):
        self.broker.send(str({
            "type": "live_status",
            "status": 2
        }))

    def calculate_points_based_movement(self, msg: dict): #converts points in Euclideas space to manipulator joints angles
        x, y, delta_base = recasting_coordinates(msg["point_based_position"]["x"], msg["point_based_position"]["y"], msg["point_based_position"]["z"])
        delta2, delta3 = inverse_kinematics(x, y)
        self.broker.send(str({
            "type": "position_calculation_result",
            "data": {
                    "base_horizontal_rotation": delta2,
                    "base_vertical_rotation": delta_base,
                    "extension_rotation": delta3,
	}

        }))

    def get_program_list(self):
        pass

    def print_con(self):
        print("Client connected!")