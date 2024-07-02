import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('EXAMPLE.db')
c = conn.cursor()

# Define the table creation statement with IF NOT EXISTS
table_info = '''CREATE TABLE IF NOT EXISTS STUDENTS (
    id INT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    age INT NOT NULL, 
    marks INT NOT NULL
)'''

# Create table if it doesn't exist
c.execute(table_info)

# Insert a row of data (optional)
c.execute("INSERT INTO STUDENTS (id, name, age, marks) VALUES (1, 'Alice', 21, 100 )")
c.execute("INSERT INTO STUDENTS (id, name, age, marks) VALUES (2, 'Alica', 21, 200 )")
c.execute("INSERT INTO STUDENTS (id, name, age, marks) VALUES (3, 'Ali', 20, 300 )")
c.execute("INSERT INTO STUDENTS (id, name, age, marks) VALUES (4, 'Maat', 18, 100 )")

# Commit the changes
conn.commit()

# Fetch data
data = c.execute("SELECT * FROM STUDENTS")
for row in data:
    print(row)

# Close the connection
conn.close()


