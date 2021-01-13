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
def update(name1):
    sql="SELECT * from hello WHERE name='"+name1+"';"
    c.execute(sql)
    record=c.fetchone()
    print(record)
    n=int(input("Enter new age"))
    sql="UPDATE hello set age='"+str(n)+"' WHERE name='"+name1+"';"
    try:
        c.execute(sql)
        print("Record Update")
    except:
        print("Error in updation")
        conn.rollback()
name=input("Enter name : ")
age=int(input("Enter age : "))
name1=input("Enter name to update : ")
create_table()
data_entry(name,age)
select()
print("\n")
select2()
print('\n')
update(name)
c.close()
conn.close()
