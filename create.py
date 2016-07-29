import sqlite3
conn = sqlite3.connect('user.db')
cursor = conn.cursor()
cursor.execute('create table user(name varchar(20) primary key,password varchar(20))')
cursor.execute('insert into user(name,password)values("admin","password")')
cursor.execute('insert into user(name,password)values("chaos","chaos")')

cursor.close()
conn.commit()
conn.close()
