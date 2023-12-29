class Person:
    def __init__(self, newName="none", phone="999-999-9999"):
        self.name = newName
        self.phone = phone
        
    def setName(self, name):
        self.name = name
    def getName(self):
        return(self.name)
    def getPhone(self):
        return(self.phone)
    
    def __str__(self):
        stringtoReturn = "Name : " + self.name \
        + "\nphone : " + self.phone
        return(stringtoReturn)
    
    def __eq__(self, o):
        return(self.getName() == o.getName())
    
if __name__=="__main__":
    pass