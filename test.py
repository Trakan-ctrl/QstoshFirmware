import math 

def main():
    servo = input("Which servo should move concurrently?").split()
    servo = [eval(i) for i in servo]
    
    print(servo)
    test(servo)


def test(servo):
    print(servo)
    for x in servo:
        print(x)
        
    print("Sum :", sum(servo))
    
if __name__=="__main__":
    main()
