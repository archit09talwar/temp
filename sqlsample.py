import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database="archit"
)
cursor = connection.cursor()

# Step 3: Write and execute the SQL query
query = "SELECT * FROM hospital"
cursor.execute(query)

# Step 4: Fetch the results
results = cursor.fetchall()

# Step 5: Display the results
for row in results:
    print(row)

# Step 6: Close the connection
cursor.close()
connection.close()
