# importing the required module
import sqlite3

#use the database if it pre-exists or create it otherwise
try:
    connection = sqlite3.connect("myemp.db")
    print("Connected with the database successfully .....")
except:
    print("Database creation ERROR !!!")

# create employee table as employee (emp_id,emp_name, emp_city, emp_salary)
# sqlStr = '''
#         CREATE TABLE employee(
#         emp_id INTEGER PRIMARY KEY,
#         emp_name TEXT,
#         emp_city TEXT,
#         emp_salary REAL
#         );
#         '''
# try:
#     connection.execute(sqlStr)
#     print("Database table has been created successfully....")
# except:
#     print("Error occurred while creating the datbase ")

print(connection.execute('pragma table_info(employee)'))
print(list(connection.execute('pragma table_info(employee)'))) # return list of tuples
for each_row in list (connection.execute('pragma table_info(employee)')):
    print(each_row)

# reading data from the csv file
import csv
sqlStr = "INSERT INTO employee VALUES('{e_id}','{e_name}','{e_city}','{e_salary}');"



# read lines from the csv file and store them into the table
# with open('emp_data.csv') as data_file:
#     csv_reader = csv.reader(data_file)
#     # reader to read from the data file with ',' as a delimiter/separator
#     for each_row in csv_reader:
#         # print(each_row)
#       connection.execute(sqlStr.format(e_id=each_row[0], e_name=each_row[1], e_city=each_row[2], e_salary=each_row[3]))
# connection.commit()   # to make the change permanent
# print ("All records got inserted successfully...")
   
   # retrieving records from the database table
# SQL for fetching all records from the table
# sqlStr = "SELECT * FROM employee;"
# # read from the table and point the cursor to the variable cur_table
# cur_table = connection.execute(sqlStr)
# # print (list(cur_table))
# for row in list(cur_table):
#     print(f"Emp-ID: {row[0]}, Emp-Name: {row[1]}, Emp-City: {row[2]}, Emp-Salary: {row[3]}")
#--------------------------------------------------------------------------------------------
# sqlStr = "SELECT emp_name, AVG(emp_salary) FROM employee GROUP BY emp_city  ;"
# cur_table = connection.execute(sqlStr)
# for row in list(cur_table):
#     print(f"Emp-City: {row[0]} and Avg-Emp-Salary: {row[1]}")

# sqlStr = "UPDATE employee set emp_salary=30000 where emp_city='Chennai' ;"
# table = connection.execute(sqlStr)
# for row in list(table):
#     print(f"Emp-city: {row[0]} UPdated Salary: {row[1]}")



# sqlStr = "DELETE FROM employee where emp_city='Kolkata' ;"
# table = connection.execute(sqlStr)
# for row in list(table):
#     print(f"Emp-city: {row[0]} UPdated Salary: {row[1]}")



# sqlStr = "SELECT * FROM employee;"
# # read from the table and point the cursor to the variable cur_table
# cur_table = connection.execute(sqlStr)
# # print (list(cur_table))
# for row in list(cur_table):
#     print(f"Emp-ID: {row[0]}, Emp-Name: {row[1]}, Emp-City: {row[2]}, Emp-Salary: {row[3]}")


n = int(input("Enter the no of records to input : "))
for i in range(n):
    code = int(input("Enter Employee ID : "))
    name = input("Enter Employee name : ")
    city = input("Enter city name : ")
    salary = int(input("Enter Employee salary : "))

    # sqlStr = "INSERT INTO employee VALUES('{e_id}','{e_name}','{e_city}','{e_salary}');"
    sqlStr = "INSERT INTO employee VALUES('{e_id}','{e_name}','{e_city}','{e_salary}');"
    connection.execute(sqlStr.format(e_id=code, e_name=name, e_city=city, e_salary=salary))


sqlStr = "SELECT * FROM employee;"
# read from the table and point the cursor to the variable cur_table
cur_table = connection.execute(sqlStr)
# print (list(cur_table))
for row in list(cur_table):
    print(f"Emp-ID: {row[0]}, Emp-Name: {row[1]}, Emp-City: {row[2]}, Emp-Salary: {row[3]}")