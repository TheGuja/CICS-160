class Person:
    def __init__(self, newName="none", address="none", phone="999-999-9999"):
        self.name = newName
        self.address = address
        self.phone = phone
        self.previous = None
        self.next = None

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return(self.name)
    
    def getPhone(self):
        return(self.phone)
    
    def getNext(self):
        return(self.next)

    def setNext(self, p):
        self.next = p

    def getPrevious(self):
        return(self.previous)

    def setPrevious(self, p):
        self.previous = p
    
    def __str__(self):
        stringtoReturn = "Name : " + self.name \
                       + "\naddress : " + self.address \
                       + "\nphone : " + self.phone
        return(stringtoReturn)

    def __eq__(self, s):
        return(self.getName() == s)

    def __ne__(self, o: object) -> bool:
        return(not(self==o))

if __name__=="__main__":
    pass
