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
            cor_x, cor_y, cor_z = input("Enter Euclidean space coordinates :").split()
            robot_controler.point_movement(int(cor_x), int(cor_y), int(cor_z))
            
        
        elif order == 3:
            print("Moving concurrently")
            # servo = input("Which servo should move concurrently?").split()
            # servo = [eval(i) for i in servo]
            robot_controler.concurrent_movement( {1: 120, 4: 70})
        
        else:
            break
   
        
    #config = ConfigParser("settings/settings.ini")
    #robot_cordinator=RobotCordinator(config)
    #robot_cordinator.run()
    #broker.init_config(config)
    

   # input("Press any key to end program...\n")
       


if __name__=="__main__":
    main()
            
        
        
          
    
    
    

