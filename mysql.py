import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",   # change this
    database="startersql"
)

# Step 2: Query the data
query = "SELECT name, gender, salary FROM users"
df = pd.read_sql(query, conn)

# Step 3: Display data
print("User Data:\n", df)

# Step 4: Analyze data
avg_salary = df.groupby('gender')['salary'].mean()
print("\nAverage Salary by Gender:\n", avg_salary)

# Step 5: Visualize
avg_salary.plot(kind='bar', color=['skyblue', 'pink'])
plt.title('Average Salary by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Salary')
plt.show()

# Step 6: Close connection
conn.close()
