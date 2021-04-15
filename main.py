import wikipedia
import sqlite3

# creating the database
con = sqlite3.connect('technical_test.db')
cur = con.cursor()

try:
    cur.execute('select * from famous_people;')
except sqlite3.OperationalError: 
    cur.execute('CREATE TABLE famous_people (id integer primary key, name text, summary text)')
else:
    pass

# user input a name
print(".:: Which famous people are you looking for ? ::.")
user_input = input("name of the famous person: ")


try:
    summary = wikipedia.summary(user_input)

# make suggestion if there's similar name
except wikipedia.exceptions.DisambiguationError as e:
    print(f"Did you mean {str(e.options[0])} ?")

# if no match at all
except wikipedia.exceptions.PageError:
     print("I do not know this person")

else:

    # getting the full name of the famous person from the summary
    name = []
    for el in summary.split():
        if '(' in el:
            break
        else:
            name.append(f'{el} ')

    # pushing informations in the database 
    cur.execute('insert into famous_people (name, summary) values (?,?)', (''.join(name).rstrip(), summary))
    # commiting changes in the database
    con.commit()
    # closing connection to db
    con.close()