import tkinter as tk
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
def get_data():
    # Fetch the data from both entry widgets
    data1 = entry1.get()
    data2 = entry2.get()
    
    # Print the data to the console
    print(f"Data from Entry 1: {data1}")
    print(f"Data from Entry 2: {data2}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Data Entry Example")

# Create two labels
label1 = tk.Label(root, text="Enter First Data:")
label1.pack(pady=5)  # Add some padding for better spacing

label2 = tk.Label(root, text="Enter Second Data:")
label2.pack(pady=5)

# Create two entry widgets
entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Create a button that will fetch and print data when clicked
button = tk.Button(root, text="Get Data", command=get_data)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
