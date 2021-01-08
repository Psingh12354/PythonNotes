class Quadrilateral:
    def __init__(self,a,b,c,d):
        self.side1=a
        self.side2=b
        self.side3=c
        self.side4=d
    def Perimeter(self):
        p=self.side1+self.side2+self.side3+self.side4
        print("Perimeter is ",p)
class Rectangle(Quadrilateral): #inherit previous class
    def __init__(self,a,b,c=None,d=None):
        super().__init__(a,b,c,d)
        self.length=self.side1
        self.breadth=self.side2
    def Area(self):
        Ar=self.length*self.breadth
        print("Area is ",Ar)
class Square(Quadrilateral):
    def __init__(self,a,b=None,c=None,d=None):
        super().__init__(a,b,c,d)
        self.side=seld.side1A
    def square(self):
        Sq=self.side**2
        print("Sqare Area is ",Sq)

"""
Output-:
>>> q1=Quadrilateral(4,5,6,7)
>>> q1.Perimeter()
"""
"""
>>> q1=Rectangle(5,6)
>>> q1.Area()
"""

"""
>>> q1=Square(5)
>>> q1.square()
"""
