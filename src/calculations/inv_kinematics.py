
from math import *
import matplotlib.pyplot as plt

a1=20
a2=20
x=10
y=20
psi=80

psi=radians(psi)



# p2x=x-a3*cos(psi)
# p2y=y-a3*sin(psi)

print('Wspolrzedna na y ostatniego zgiecia:',y)
print('Wspolrzedna na x ostatniego zgiecia',x)

#print((pow(p2x,2)+pow(p2y,2)-(pow(a1,2)+pow(a2,2)))/(2*a1*a2))

delta2= -acos((pow(x,2)+pow(y,2)-(pow(a1,2)+pow(a2,2)))/(2*a1*a2))

delta1=atan(y/x) - atan(a2*sin(delta2)/(a1 + a2*cos(delta2)))

delta3=psi-(delta1+delta2)

p1x=a1*cos(delta1)
p1y=a1*sin(delta1)


print('delta1:',delta1)
#print('delta2',delta2)
#print('delta3',delta3)
#print('p1x, p1y',p1x,p1y)
#print('p2x, p2y',p2x,p2y)
print('Dlugosc pierwszego czlonu: ',sqrt(pow(p1x,2)+pow(p1y,2)))
print('Dlugosc drugiego czlonu: ',sqrt(pow(p1x - x,2)+pow(p1y - y,2)))



plt.xlim(-50,50)
plt.ylim(-50,50)
plt.plot([-5,5],[0,0])
plt.plot([0, p1x],[0, p1y],[p1x, x],[p1y, y], marker = 'o' )
plt.show()



