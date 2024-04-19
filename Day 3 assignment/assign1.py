import mysql.connector

connection = mysql.connector.connect(

    host ="localhost",
    port =3306,
    user="sunbeam",
    password="sunbeam",
    database="iotdb",

)

# create a query

empid = int(input("Enter Empid  :"))
name = (input("Enter the Name :"))
department = (input("Enter the department :"))
email = input("Enter Email :")
salary = int(input("Enter Salary : "))
doj =input("Enter Date of joining  :")

query= f"insert into employees values ({empid},'{name}','{department}','{email}','{salary}','{doj}');"

# create a cursor to execute the query
cursor = connection.cursor()

# execute query using cursor
cursor.execute(query)

# after execution of query commit your changes
connection.commit()

# close the cursor
cursor.close()

#close the connection with mysql server 
connection.close()






