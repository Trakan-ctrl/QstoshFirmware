import math


def recasting_coordinates(cor_x, cor_y, cor_z):
    delta_base = math.atan(cor_y/cor_x)*(180/math.pi)
    x = math.sqrt(pow(cor_x, 2) + pow(cor_y, 2))

    return x, cor_z, delta_base

def angle_to_pwm(angle, server_version: int):
        
        if server_version == 1 or server_version == 2:
                dc = 2.5+float(angle)*(10/180)
        elif server_version == 3:
                dc = 3.5+float(angle)*(10/180)
        elif server_version == 4:
                dc = 2+float(angle)*(10/180)

        else:
                print("Specified servo doesn't exist!!!")
                dc = 0
        
        return(dc)

        
