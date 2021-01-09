class book:
    def __init__(self):
        self.title=input("Enter book Title : ")
        self.author=input("Enter book Author name : ")
        self.publisher=input("Enter book Publisher name : ")
        self.price=int(input("Enter book Price : "))       
    def setter(self):
        self.title=input("Enter book Title : ")
        self.author=input("Enter book Author name : ")
        self.publisher=input("Enter book Publisher name : ")
        self.price=int(input("Enter book Price : "))
        return
    def getter(self):
        print("Book Title : {}\nBook Author : {}\nBook Publisher : {}\nBook Price : {}".format(self.title,self.autor,self.publisher,self.price))
        return
    def royality(self,sold):
        if(sold<=500):
            self.royality=self.price*(10/100)
            return self.royality
        if(sold<=1000):
            self.royality=self.price*((12+(1/2))/100)
            return self.royality
        if(sold<=500):
            self.royality=self.price*(15/100)
            return self.royality
class ebook(book):
    def __init__(self):
        super().__init__()
        self.format=input("Enter format (EPUB, PDF,MOBI etc) : ")
    def royality(self,sold):
        if(sold<=500):
            self.royality=(self.price-self.price*0.12)*(10/100)
            return self.royality
        if(sold<=1000):
            self.royality=(self.price-self.price*0.12)*((12+(1/2))/100)
            return self.royality
        if(sold<=500):
            self.royality=(self.price-self.price*0.12)*(15/100)
            return self.royality

e1=book()
sold=int(input("Enter total number of sales of book : "))
print("Royality amount on Book is : ",e1.royality(sold))

e2=ebook()
sold=int(input("Enter total number of sales of ebook : "))
print("Royality amount on eBook is : ",e2.royality(sold))
