import sqlite3
BookDB=sqlite3.connect("Assignment5.db")
c=BookDB.cursor()
c.execute("Create TABLE books(title TEXT (50) NOT NULL,Author TEXT (50) NOT NULL,Price REAL NOT NULL);")
while True:
    title=input("Book Title: ")
    author=input("Enter Author: ")
    price=eval(input("Price: "))
    sql="INSERT INTO books(title,Author,Price) VALUES('"+title+"','"+author+"','"+str(price)+"');"
    try:
        c.execute(sql)
        BookDB.commit()
        print("Changes successfully done!")
    except:
        print("Error occured...")
        BookDB.rollback()
BookDB.close()

