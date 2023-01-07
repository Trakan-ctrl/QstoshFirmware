import logging
from threading import Thread
import time
logging.basicConfig(level=logging.DEBUG)

from src.bluetooth.connection_broker import ConnectionBroker
from src.configs.config_parser import ConfigParser

logger = logging.getLogger("main")

frame = {
    "type": "live_position",
    "position": {
        "base_horizontal_rotation": 0.,
        "base_vertical_rotation": 45.,
        "extension_rotation": -60.,
        "grabbed": False
    }
}

broker = ConnectionBroker()

status = {1: "idle"}

def res(bh, bv, e):
    print("msg from thread")
    status[1] = "running_command"
    bh /= 50
    bv /= 50
    e /= 50
    for _ in range(50):
        frame["position"]["base_horizontal_rotation"] += bh
        frame["position"]["base_vertical_rotation"] += bv
        frame["position"]["extension_rotation"] += e
        broker.send(str(frame))
        time.sleep(0.1)
    print("thread end")
    status[1] = "idle"
    cur_status(1)

def execute_mvmnt(msg: dict):
    print(msg)
    if msg["movement_type"] == "arm_position":    
        bh = msg["arm_position"]["base_horizontal_rotation"] - frame["position"]["base_horizontal_rotation"]
        bv = msg["arm_position"]["base_vertical_rotation"] - frame["position"]["base_vertical_rotation"]
        e = msg["arm_position"]["extension_rotation"] - frame["position"]["extension_rotation"]
        Thread(target=res, args=(bh, bv, e)).run()
    elif msg["movement_type"] == "grab_position":
        frame["position"]["grabbed"] = msg["grab_position"]["grabbed"]
        broker.send(str(frame))
        status[1] = "idle"
        cur_status(1)


def print_con():
    print("Client connected!")

def cur(msg):
    print("sending position")
    print(str(frame))
    broker.send(str(frame))

def cur_status(msg):
    broker.send(str({
        "type": "live_status",
        "status": status[1]
    }))


def main():
    config = ConfigParser("settings/settings.ini")
    broker.init_config(config)
    broker.add_callback_to_topic("execute_movement", execute_mvmnt)
    broker.add_callback_to_topic("ask_position", cur)
    broker.add_callback_to_topic("ask_status", cur_status)
    broker.on_client_connected = print_con
    broker.start_broker()
    input("Press any key to end program...\n")
    broker.stop_broker()


if __name__=="__main__":
    main()
            
        
        
          
    
    
    

