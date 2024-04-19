
# import mysql connector
import mysql.connector

# function to create a connection
def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "sunbeam",
        password = "sunbeam",
        database = "iotdb"
    )

def update_person(empid, email):
    # get connection
    conn = get_connection()

    # form a query
    query = f"update employees SET email= %s where empid = %s;"
    val = (email, empid)

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()



update_person(25, "kartikgophane@gmail.com")