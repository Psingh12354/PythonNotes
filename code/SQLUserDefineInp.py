import sqlite3
conn=sqlite3.connect('tutorial.db')
c=conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS hello(NAME TEXT, AGE INT)')
def data_entry(name,age):
    c.execute("INSERT INTO hello (NAME,AGE) VALUES(?,?);",(name,age))
    conn.commit()
    
def select(): #Use of select command fetchone()
    sql="SELECT * from hello;"
    c.execute(sql)
    while True:
        record=c.fetchone()
        if record==None:
            break
        print(record)
def select2(): #use of select command to fetchall()
    sql="SELECT * from hello;"
    c.execute(sql)
    result=c.fetchall()
    for record in result:
        print(record)
name=input("Enter name : ")
age=int(input("Enter age : "))
create_table()
data_entry(name,age)
select()
print("\n")
select2()
c.close()
conn.close()
