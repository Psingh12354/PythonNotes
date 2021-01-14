import sqlite3
BookDB=sqlite3.connect("Assignment5.db")
c=BookDB.cursor()
total=0
while True:
    title=input("Book title: ")
    sql1="SELECT * FROM books WHERE title='"+title+"'"
    sql2="SELECT Price FROM books WHERE title='"+title+"'"
    c.execute(sql1)
    record=c.fetchone()
    if record!=None:
        print(record)
        c.execute(sql2)
        price=record[2]
        print(price)
        quantity=int(input("No. of copies: "))
        cost=price*quantity
        total+=cost
        print("Total Cost ",total)
    else:
        print("Book title not found!")
        choice=input("Press [y/n] to continue?")
        choice.lower()
        if choice=='n':
            break
BookDB.close()
