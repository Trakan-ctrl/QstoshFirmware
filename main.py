import logging
from threading import Thread
import time

logging.basicConfig(level=logging.DEBUG)

#from src.bluetooth.connection_broker import ConnectionBroker
#from src.configs.config_parser import ConfigParser
#from src.robot_cordinator.cordinator import RobotCordinator
from src.robot_controler.robot_controler import RobotControler

logger = logging.getLogger("main")


def main():
    robot_controler = RobotControler()
    
    while(1):
        order= int(input("""Choose one of three options: 
                    (1) one specified servo move, 
                    (2) move to specified point, 
                    (3) run sequence manager
                    (4) close the programme"""))
        
        if order == 1:
            chosen_servo = int(input("Choose which servo should move :"))
            angle = int(input("What angle the servo should rotate to? :"))
            robot_controler.move_chosen_servo(angle, chosen_servo)
        
        elif order == 2:
            pass
        
        elif order == 3:
            pass
        
        else:
            break
   
        
    #config = ConfigParser("settings/settings.ini")
    #robot_cordinator=RobotCordinator(config)
    #robot_cordinator.run()
    #broker.init_config(config)
    

   # input("Press any key to end program...\n")
       


if __name__=="__main__":
    main()
            
        
        
          
    
    
    

