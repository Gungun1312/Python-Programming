#import the sql
import sqlite3

# use the database if it pre exist or create it otherwise 
try :
    connection = sqlite3.connect("myemp.db")
    print("connected with the database successfully..")
except : 
    print("database connection Error...")
    
    
sqlStr = '''
         CREATE TABLE employee (
             emp_id INTEGER PRIMARY KEY,
             emp_name TEXT,
             emp_city TEXT,
             emp_salary REAL
         );
         '''
try:    # create the employee table if it does not pre-exist
    connection.execute(sqlStr)
    print ("Database table has been created successfully...")
except:
    print ("Error occurred while creating the database table...")
    

