from collections import defaultdict
import json

class RobotDatabase():
    
    def __init__(self):
        self.robot_sequence = list()
    
    def __dell__(self):
        pass
    
    def write_to_database(self, robot_sequence):
        
        json_string = json.dumps(robot_sequence)
        name = str(robot_sequence['name'])
        with open(f'{name}.json', 'w') as outfile:
            outfile.write(json_string)
        
        pass    
    
    
    def read_from_database(self, name):
        with open(f'{name}.json') as json_file:
            data = json.load(json_file)
        return data
        # for line in self.robot_database:
        #     print(line, end="")
        #     self.robot_position = line