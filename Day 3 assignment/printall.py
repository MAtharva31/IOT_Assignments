# import mysql connector
import mysql.connector

# create connection with mysql server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb" 
)


# form a qery
query1 = "select * from employees order by salary DESC;"
query2 = "select Name from employees;"
query3 = "select Department from employees;"


cursor = connection.cursor()

cursor.execute(query1)

records = cursor.fetchall() 
    
print(records)


cursor.execute(query2)

records = cursor.fetchall() 
    
print(records)


cursor.execute(query3)

records = cursor.fetchall() 
    
print(records)


# close the cursor
cursor.close()

# close the connection
connection.close()

