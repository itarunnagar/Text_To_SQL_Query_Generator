import sqlite3
import os

# Check if the database file exists and delete it if it does
db_file = "company.db"
if os.path.exists(db_file):
    os.remove(db_file)
    print(f"Database '{db_file}' has been deleted.")
else:
    print(f"Database '{db_file}' does not exist.")

# Connect to SQLite database (it will be created again if deleted)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create Employee table with hire_date in DATE format (without time)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        salary INTEGER NOT NULL,
        hire_date DATE NOT NULL  -- Store only the date part
    )
''')

# Insert multiple entries into Employee table with proper date format (without time)
employee_data = [
    (1, "Alice", "Sales", 50000, "2021-01-15"),
    (2, "Bob", "Engineering", 70000, "2020-06-10"),
    (3, "Marlie", "Marketing", 60000, "2022-03-20"),
    (4, "John", "Engineering", 72000, "2019-11-25"),
    (5, "Emma", "Sales", 55000, "2020-08-14"),
    (6, "Liam", "Marketing", 62000, "2021-09-30"),
    (7, "Sophia", "HR", 58000, "2022-01-05"),
    (8, "William", "Engineering", 75000, "2018-07-19"),
    (9, "Olivia", "Sales", 51000, "2021-06-21"),
    (10, "Noah", "Finance", 68000, "2020-04-15")
]

cursor.executemany("INSERT OR IGNORE INTO Employees (id, name, department, salary, hire_date) VALUES (?, ?, ?, ?, ?)", employee_data)

# Create Departments table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        manager TEXT NOT NULL
    )
''')

# Insert multiple entries into Departments table
department_data = [
    (1, "Sales", "Alice"),
    (2, "Engineering", "Bob"),
    (3, "Marketing", "Marlie"),
    (4, "HR", "Sophia"),
    (5, "Finance", "Noah"),
    (6, "Operations", "William"),
    (7, "Customer Support", "Emma"),
    (8, "IT", "John")
]

cursor.executemany("INSERT OR IGNORE INTO Departments (id, name, manager) VALUES (?, ?, ?)", department_data)

# Showing That Records Was Inserted Succesfully.
print("Tables created with multiple entries successfully!")



# Commit changes and close the connection
conn.commit()
conn.close()
