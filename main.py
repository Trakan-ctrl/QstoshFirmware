import logging
from threading import Thread
import time
from collections import defaultdict
logging.basicConfig(level=logging.DEBUG)

#from src.bluetooth.connection_broker import ConnectionBroker
#from src.configs.config_parser import ConfigParser
#from src.robot_cordinator.cordinator import RobotCordinator
from src.robot_controler.robot_controler import RobotControler
from src.robot_controler.robot_database import RobotDatabase

logger = logging.getLogger("main")


def main():
    robot_controler = RobotControler()
    robot_database = RobotDatabase()
    robot_controler.reset_position()
    robot_sequence = dict()
    robot_movement = dict()
    
    while(1):
        order= int(input("""Choose one of three options: 
                    (1) one specified servo move, 
                    (2) move to specified point, 
                    (3) run sequence manager,
                    (4) reset position,
                    (5) show current position,
                    (6) save position,
                    (7) show json file
                    (8) close the programme"""))
        
        if order == 1 :
            chosen_servo = int(input("Choose which servo should move :"))
            angle = int(input("What angle the servo should rotate to? :"))
            robot_controler.move_chosen_servo(angle, chosen_servo)
        
        elif order == 2 :
            cor_x, cor_y, cor_z = input("Enter Euclidean space coordinates :").split()
            robot_controler.point_movement(int(cor_x), int(cor_y), int(cor_z))
            
        
        elif order == 3 :
            print("Moving concurrently")
            # servo = input("Which servo should move concurrently?").split()
            # servo = [eval(i) for i in servo]
            robot_controler.concurrent_movement( {1: 120, 4: 70})
        
        elif order == 4 :
            robot_controler.reset_position()
        
        elif order == 5 :
            print(robot_controler.current_position())
        
        elif order == 6:
            key_robot_sequence = 1
            while ('yes' ==  input("Do you want to write another sequence?")): 
                while ('yes' ==  input("Do you want to continue?")):
                    key_robot_movement = input("Which servo should move? :")
                    angle = input("What angle should servo turn to? :")
                    robot_movement[key_robot_movement] = angle
                
                robot_sequence[key_robot_sequence] = dict(robot_movement)
                key_robot_sequence = key_robot_sequence + 1
        
            name=input("Name of the sequence? :")  
            robot_sequence["name"] = name
            print(robot_sequence)
            robot_database.write_to_database(robot_sequence)
            robot_movement.clear() 
        elif order == 7:
            name = input("Give the name of the sequence: ")
            # robot_database.read_from_database(name)
            robot_controler.program_movement(name)
        else:
            break
   
        
    #config = ConfigParser("settings/settings.ini")
    #robot_cordinator=RobotCordinator(config)
    #robot_cordinator.run()
    #broker.init_config(config)
    

   # input("Press any key to end program...\n")
       


if __name__=="__main__":
    main()
            
        
        
          
    
    
    

