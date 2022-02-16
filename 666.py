


class Fan(object):
    def __init__(self,radius, on=False, speed=1):
       self.radius=radius
       self.on=on
       self.speed=speed
    


    def __str__(self):
        string = "Fan with radius "+str(self.radius) + "\n"
        if self.on is False:
            
            string = string + "The fan is currently off"
            
            return string
        else:
            string = string +"The fan is currently on and is running at speed " + str(self.speed)
           
            return string
            

    def getRadius(self):
        return self.radius
        

    def getOn(self):
        return self.on

    
    def getSpeed(self):
        return self.speed

    def setOn(self, state):
        if state is False or state is True:
            self._on = state
        else:
            print("The value " + str(state) + " is invalid. Value must be either True or False")


    def setSpeed(self,num):
        if num not in [1, 2, 3]:
            print("The value " +str(num) + " is invalid. A valid speed must be 1, 2, or 3")

        else:
            
            self.speed=num
            self.on=True
        

    



def main():
        fan1 = Fan(5)
        print(fan1)
        
        print()
        fan2 = Fan(12.5, True, 2)
        print(fan2)

        print("\nTesting the accessor methods on fan2")
        print(fan2.getRadius())
        print(fan2.getOn())
        print(fan2.getSpeed())
        

        print("\nTesting the mutator methods on fan2")
        fan2.setOn("off")
        fan2.setOn(False)
        fan2.setSpeed(5)
        fan2.setSpeed(3)

        print()
        print(fan2)
main()
