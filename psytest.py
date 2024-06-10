import psycopg2

# connect to "chinook" database

connection = psycopg2.connect(database="chinook")

#build a cursor-object ( a list)

cursor = connection.cursor()

#execute a query and retrieve everything from "Artist" column

cursor.execute('SELECT * FROM "Artist"')

# fetch the results     multiple

results = cursor.fetchall()

# fetch the results        single
#results = cursor.fetchone()

#close connection to DB

connection.close()

#print result

for result in results:
    print(results)