import sqlite3
conn = sqlite3.connect('user.db')
cursor = conn.cursor()
cursor.execute('select * from user where name=?',('chao',))
values = cursor.fetchall()
if len(values)==0:
    print('null')
else:
    print(values[0][0]+values[0][1])
#print(values[0][0]+values[0][1])
