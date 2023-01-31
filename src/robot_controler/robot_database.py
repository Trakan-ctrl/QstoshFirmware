from collections import defaultdict

class RobotDatabase():
    
    def __init__(self):
        self.robot_position = defaultdict(list)
        self.robot_database =  open('robot_database.txt', 'a')
    
    def __dell__(self):
        self.robot_database.close()
    
    def write_to_database(self, robot_position):
        self.robot_database.writelines("Hello!!!")
        pass
    
    
    def read_from_database(self):
        for line in self.robot_database:
            print(line, end="")
        