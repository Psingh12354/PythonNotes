"""
- Static method knows nothing about the class and just deals with the parameters
- Class method works with the class since its parameter is always the class itself.
"""
class person:
    counter=0
    def __init__(self,a,b):
        self.name=a
        self.gender=b   #Attributes or instance variable
        person.counter+=1
    def ShowInfo(self): #self is necessay here
        print('Name : ',self.name) #to call you need to use self.
        print('Gender : ',self.gender)
    @classmethod
    def ShowCount(cls): #class method call by class not by individual
        print('Number of object created show far : ',cls.counter)

# In output or shell you need type the following command
# p1=person()
# p1.ShowInfo()
