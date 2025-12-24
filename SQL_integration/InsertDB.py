import sqlite3
conn=sqlite3.connect('test.db')
print("Opened database successfull")
conn.execute("DROP TABLE Student")
conn.execute("CREATE TABLE Student(ID INT,NAME TEXT)")
print("Table created successfully")
conn.execute("INSERT INTO Student(ID,NAME)\
                    VALUES(1,'AAA')")
conn.execute("INSERT INTO Student(ID,NAME)\
                    VALUES(2,'BBB')")
conn.execute("INSERT INTO Student(ID,NAME)\
                    VALUES(3,'CCC')")
conn.execute("INSERT INTO Student(ID,NAME)\
                    VALUES(4,'DDD')")
conn.execute("INSERT INTO Student(ID,NAME)\
                    VALUES(5,'EEE')")
conn.commit()
s=conn.execute("SELECT * FROM Student")
for i in s:
  print(i[0]," ",i[1])
conn.close()
