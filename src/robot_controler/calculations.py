
    
def angle_to_pwm(angle, server_version):
        
        if server_version == 1 or server_version == 2:
                dc = 2.5+float(angle)*(10/180)
        elif server_version == 3:
                dc = 3.5+float(angle)*(10/180)
        elif server_version == 4:
                dc = 5+float(angle)*(5/180)

        else:
                print("Specified servo doesn't exist!!!")
                dc=0
        
        return(dc)

        
