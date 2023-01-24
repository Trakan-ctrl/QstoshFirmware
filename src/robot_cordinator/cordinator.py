import logging
from threading import Thread
import time
from src.calculations.inv_kinematics_two_links import inverse_kinematics
from src.calculations.recasting import recasting_coordinates
#import RPi.GPIO as GPIO
from time import sleep
from typing import Callable
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG)

from src.bluetooth.connection_broker import ConnectionBroker
from src.configs.config_parser import ConfigParser


class RobotCordinator:

    status = {1: "idle"}

    def __init__(self, config):
        self.config = config
        self.broker = ConnectionBroker()
        self.callbacks = defaultdict(list)
        self.robot_state = {
                        "type": "live_position",
                        "position": {
                            "base_vertical_rotation": 0.,
                            "base_horizontal_rotation": 20.,
                            "extension_rotation": 50.,
                            "grabbed": False
                        }
                     }
        self._callback_handler: Thread = Thread(target=self.callback_handler)
        

        self.add_callback("p", self.cur_position)
        #self.broker.add_callback_to_topic("execute_movement", self.execute_movement)
        #self.broker.add_callback_to_topic("calculate_pbm", self.calculate_points_based_movement)
        #self.broker.add_callback_to_topic("live_position,", self.cur_position)
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
        
        
        
        #self.broker.start_broker()
        #self.broker.init_config(self.config)
        #print(self.broker.dane())
        

        while(1):
            print("Serwer dziala!!!")
            
            sleep(2)   

 

    def move(self):
        pass
        #Thread(target=self.live_position).run()

    #    GPIO.setmode(GPIO.BOARD)

    #    GPIO.setup(11, GPIO.OUT)

    #    pwm_bh=GPIO.PWM(11,50)
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
        pass
    #    GPIO.setmode(GPIO.BOARD)

     #   GPIO.setup(11, GPIO.OUT)


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
        print(str(self.robot_state))
        self.broker.send(str(self.robot_state))

    def cur_position(self):
        print("sending position")
        print(self.robot_state)
        #self.broker.send(str(self.robot_state))

    def live_status(self):
        pass

    def cur_status(self):
        print(self.robot_state)
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
        
    def add_callback(self,topic: str ,callback: Callable[[dict], None]):
        self.callbacks[topic].append(callback) 
    
    def callback_handler(self, command: str):
        print("robot_handler, komenda:")
        print(command)
        for callback in self.callbacks[command]:
                            callback()
        
            
            
        
        
    
   # def start_callback_handler(self):
   #     self._callback_handler.start()