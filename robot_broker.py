import logging
from threading import Thread
import time
from collections import defaultdict
from typing import Callable


logging.basicConfig(level=logging.DEBUG)

from src.bluetooth.connection_broker import ConnectionBroker
from src.configs.config_parser import ConfigParser
from src.robot_cordinator.cordinator import RobotCordinator

logger = logging.getLogger("main")

def __init__(self):
        self.callbacks = defaultdict(list)
        self.on_client_connected: Callable = None
        self._broker_thread: Thread = Thread(target=self._broker_thread_method)
        self._running = True

def main():
    while(1):
        config = ConfigParser("settings/settings.ini")
        robot_cordinator=RobotCordinator(config)
        robot_command=input('Podaj co ma zrobic robot: \n Podanie swojej aktualnej pozycji: p ')
        robot_cordinator.callback_handler(robot_command)
        
        
        #robot_cordinator.run()
        #broker.init_config(config)
    

   # input("Press any key to end program...\n")
       


if __name__=="__main__":
    main()
            
        
        
          
    
    
    

