import sqlite3
MySchool=sqlite3.connect('MyCricke1.db')
curschool=MySchool.cursor()
curschool.execute('''CREATE TABLE student (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT (20) NOT NULL,
    age INTEGER,
    marks REAL);''')
MySchool.close() 

"""
There are 4 method define in connection close
1> cursor() - cursor enables python object to work with db it allow retrival
2> commit() - Explicit commits any pending transaction
3> rollback() - undo the 
4> close - closes the connection through db
""""

