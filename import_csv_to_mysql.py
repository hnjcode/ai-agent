import csv
import pymysql

# MySQL server connection info (no database specified yet)
db_config = {
    "host": "localhost",
    "port": 3307,
    "user": "root",
    "password": "1111",
}

db = "ai_agent_db"

# Connect to MySQL server (without database)
connection = pymysql.connect(**db_config)
cursor = connection.cursor()

# Create new database if not exists
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db};")
print(f"Database '{db}' ensured to exist.")

# Close and reconnect to new database
cursor.close()
connection.close()

db_config["database"] = db
connection = pymysql.connect(**db_config)
cursor = connection.cursor()

# Create table if not exists
create_table_sql = """
CREATE TABLE IF NOT EXISTS salaries (
    Department VARCHAR(50),
    Department_Name VARCHAR(100),
    Division VARCHAR(100),
    Gender CHAR(1),
    Base_Salary FLOAT,
    Overtime_Pay FLOAT,
    Longevity_Pay FLOAT,
    Grade VARCHAR(10)
);
"""
cursor.execute(create_table_sql)

# Read CSV and insert data
with open("./data/salaries_2023.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("""
            INSERT INTO salaries (
                Department, Department_Name, Division, Gender,
                Base_Salary, Overtime_Pay, Longevity_Pay, Grade
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['Department'],
            row['Department_Name'],
            row['Division'],
            row['Gender'],
            float(row['Base_Salary']),
            float(row['Overtime_Pay']),
            float(row['Longevity_Pay']),
            row['Grade']
        ))

connection.commit()
cursor.close()
connection.close()

print("Data imported successfully into new database.")
