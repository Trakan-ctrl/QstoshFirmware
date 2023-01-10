
from math import *
import matplotlib.pyplot as plt


def inverse_kinematics(x, y):

        
        link1_length=20
        link2_length=20


        #('Wspolrzedna na y ostatniego zgiecia:',y)
        #print('Wspolrzedna na x ostatniego zgiecia',x)

        delta3 = -acos((pow(x,2)+pow(y,2)-(pow(link1_length,2)+pow(link2_length,2)))/(2*link1_length*link2_length))
        delta2 = atan(y/x) - atan(link2_length*sin(delta3)/(link1_length + link2_length*cos(delta3)))


        p1x = link1_length*cos(delta2)
        p1y = link1_length*sin(delta2)


        #print('delta2:',delta2)
        #print('delta3',delta3)
        #print('delta3',delta3)
        #print('p1x, p1y',p1x,p1y)
        #print('p2x, p2y',p2x,p2y)


        #plt.xlim(-50,50)
        ##plt.ylim(-50,50)
        #plt.plot([-5,5],[0,0])
        #plt.plot([0, p1x],[0, p1y],[p1x, x],[p1y, y], marker = 'o' )
        #plt.show()
        return delta2, delta3
