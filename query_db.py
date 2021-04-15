import sqlite3

# connecting to db
con = sqlite3.connect('technical_test.db')
cur = con.cursor()

# printing each row in the db
for row in cur.execute('select * from famous_people;'):
    print(row)
    print('')

# closing connection to db
con.close()