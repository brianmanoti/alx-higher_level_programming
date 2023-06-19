import MySQLdb

def list_states(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to fetch all the states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the states
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

# Provide your MySQL credentials and the database name
username = "your_username"
password = "your_password"
database = "hbtn_0e_0_usa"

# Call the function to list the states
list_states(username, password, database)

