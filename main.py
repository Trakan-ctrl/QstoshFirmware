import logging
from threading import Thread
import time

logging.basicConfig(level=logging.DEBUG)

from src.bluetooth.connection_broker import ConnectionBroker
from src.configs.config_parser import ConfigParser
from src.robot_cordinator import RobotCordinator

logger = logging.getLogger("main")


def main():
    config = ConfigParser("settings/settings.ini")
    robot_cordinator=RobotCordinator()
    #broker.init_config(config)
    broker.start_broker()

    input("Press any key to end program...\n")
    broker.stop_broker()        


if __name__=="__main__":
    main()
            
        
        
          
    
    
    

