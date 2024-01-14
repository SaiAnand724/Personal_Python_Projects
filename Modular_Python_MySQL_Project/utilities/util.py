"""
Working with MySQL Workbench
- Set up SQL server with credentials

Either command line should work:
pip3 install mysql-connector-python
pip3 install mysql-connector-python-rf
"""
# Import mysql-connector module 
import mysql.connector

# Import json module for storing and fetching information
import json

# Connecting to/Setting up database
"""
Basic Doc Source: https://www.psycopg.org/docs/module.html#psycopg2.connect
MySQL Doc Source: https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
Create a new database session and return a new connection object.

The basic connection parameters are:

dbname – the database name (database is a deprecated alias)

user – user name used to authenticate

password – password used to authenticate

host – database host address (defaults to UNIX socket if not provided)

port – connection port number (defaults to 5432 if not provided)
"""

mydb = mysql.connector.connect(
    host = "localhost",
    # Username for connection - default (root)
    user = "root", 
    # Password for connection - User generated password
    password = "User-Password",
    # Create a database first, then fill field with info
    # Field to determine which database to start/work with
    database = "Any_Database"
)

# print(mydb) - Lets you know the connection works
# Output should look like: <mysql.connector.connection.MySQLConnection object at 0x00000**********0>

# Create SQL database in python
# Initialize cursor
"""columns_to_str
Doc Source: https://www.psycopg.org/docs/cursor.html
Cursors are created by the connection. cursor() method: 
    they are bound to the connection for the entire lifetime and all the commands 
    are executed in the context of the database session wrapped by the connection.

"""
# Create cursor object using the mydb connection
mycursor = mydb.cursor()

# Formatting columns into a string
def columns_to_str(column_names):
    count = 0
    columns_array_str = ""
    for name in column_names:
        if count != (len(column_names) - 1):
            columns_array_str += name + ", "
        else:
            columns_array_str += name
                
        count += 1
    
    return columns_array_str

class Utilities:
    def __init__(self):
        self
        
    # Manual execute function for MySQL
    def mysql_execute():
        return
    
    
    # Database commands for MySQL
    # Show database command for MySQL
    def mysql_show_db():
        show_db_form = "SHOW DATABASES"
        return show_db_form
    
    # Create database command for MySQL
    def mysql_create_db(database_name):
        create_db_form = "CREATE DATABASE IF NOT EXISTS " + database_name
        # mycursor.execute(create_db_form)
        return create_db_form
    
    # Drop database command for MySQL
    def mysql_drop_db(database_name):
        drop_db_form = "DROP IF EXISTS " + database_name
        # mycursor.execute(drop_db_form)
        return drop_db_form
    
    # Table commands for MySQL
    # Show tables command for MySQL
    def mysql_show_tb():
        show_tb_form = "SHOW TABLES"
        # cursor = mycursor.execute(show_db_form)
        return show_tb_form
    
    # Create table command for MySQL
    def mysql_create_tb(table_name, column_names):
        columns_array_str = columns_to_str(column_names)
        
        create_tb_form = "CREATE TABLE IF NOT EXISTS " + table_name + " (" + columns_array_str + ")"
        # mycursor.execute(create_tb_form)
        return create_tb_form
    
    # Drop table command for MySQL
    def mysql_drop_tb(table_name):
        drop_tb_form = "DROP TABLE IF EXISTS " + table_name 
        # mycursor.execute(drop_tb_form)
        return drop_tb_form
    
    # Adding an element to a table command for MySQL
    def mysql_addto_tb(table_name, values_array):
        values_array_str = ""
        count = 0
        for value in values_array:
            if count != (len(values_array) - 1): 
                print(type(value))
                if type(value) != str:
                    values_array_str += str(value) + ", "
                else:
                    values_array_str += "'" + str(value) + "', "
            else:
                print(type(value))
                if type(value) != str:
                    values_array_str += str(value)
                else:
                    values_array_str += "'" + str(value) + "'"
                
            count += 1
        
        insert_tb_form = "INSERT INTO " + table_name + " VALUES (" + values_array_str + ")"
        # mycursor.excecute(insert_tb_form)
        # mycursor.executemany(insert_tb_form, values_dict)
        return insert_tb_form
    
    # Removing a specific element from a table for MySQL
    def mysql_rmfrm_tb(table_name, column_name, value):
        print(type(value))
        if type(value) != str:
            del_frmtb_form = "DELETE FROM " + table_name + " WHERE " + column_name + " = " + str(value)
        else:
            str_value = "'" + value + "'"
            del_frmtb_form = "DELETE FROM " + table_name + " WHERE " + column_name + " = " + str_value
        # mycursor.execute(del_form_temp) # - remove comment when running initially
        return del_frmtb_form
    
    # Updating a specific element from a table for MySQL
    def mysql_upd_tb(table_name, upd_column_name, upd_row_value, loc_column_name, loc_row_value):
        print(type(upd_row_value))
        print(type(loc_row_value))
        if (type(upd_row_value) == str and type(loc_row_value) == str):
            upd_row_value = "'" + upd_row_value + "'"
            loc_row_value = "'" + loc_row_value + "'"
        elif (type(upd_row_value) == str):
            upd_row_value = "'" + upd_row_value + "'"
            loc_row_value = str(loc_row_value)
        elif (type(loc_row_value) == str):
            upd_row_value = str(upd_row_value)
            loc_row_value = "'" + loc_row_value + "'"
        else:
            upd_row_value = str(upd_row_value)
            loc_row_value = str(loc_row_value)
        
        upd_statement = upd_column_name + " = " + upd_row_value
        loc_statement = loc_column_name + " = " + loc_row_value
            
        upd_form_temp = "UPDATE " + table_name + " SET " + upd_statement + " WHERE " + loc_statement
        # mycursor.execute(upd_form_temp)
        return upd_form_temp
    
    
    # Select statement for a table for MySQL
    def mysql_slfrm_tb(table_name, column_names):
        columns_array_str = columns_to_str(column_names)
        
        select_tb_form = "SELECT " + columns_array_str + " FROM " + table_name
        # mycursor.execute(select_tb_form)

        # Using .fectchall() function to get data from previous execute statement to store table
        myresult_table = "" # mycursor.fetchall()
        
        for row in myresult_table:
            print(row)
            
        return select_tb_form
    
    # Where select statement for a table in MySQL
    def mysql_whrin_tb(table_name, column_names, loc_column_name, loc_row_value):
        columns_array_str = columns_to_str(column_names)
            
        if (type(loc_row_value) == str):
            loc_row_value = "'" + loc_row_value + "'"
        else:
            loc_row_value = str(loc_row_value)
            
        loc_statement = loc_column_name + " = " + loc_row_value
        
        whr_tb_form = "SELECT " + columns_array_str + " FROM " + table_name + " WHERE " + loc_statement
        return whr_tb_form
    
    # Order by (sort) select statement for a table for MySQL
    def mysql_ordby_tb(table_name, column_names, ord_column_name, direction):
        columns_array_str = columns_to_str(column_names)

        ord_tb_form = "SELECT " + columns_array_str + " FROM " + table_name + " ORDER BY " + ord_column_name + " " + direction
        # mycursor.execute(ord_tb_form)
        return ord_tb_form
    
   
"""
database_name = "django_db"

table_name = "Table_1"
columns_tb = ["play_id INTEGER(10) PRIMARY KEY, name VARCHAR(50), age INTEGER(10), pwr_lvl INTEGER(10), gender VARCHAR(1)"]
column_names = ["play_id", "name", "age", "pwr_lvl", "gender"]

index = 0
all_columns = ["*"]
column_name = column_names[index]

values_arr = (1, "He-mothy", 18, 7, "M")
value = values_arr[index]

index_2 = 1
upd_column = column_names[index_2]
upd_value = values_arr[index_2]

ord_column_name = column_names[2]
ord_dir_arr = ["", "ASC", "DESC"]
ord_direction = ord_dir_arr[2]


# Testing functions

query_formula_1 = Utilities.mysql_create_db(database_name) 
# query_formula_1 = Utilities.mysql_drop_db(database_name) 
print(query_formula_1)

query_formula_2 = Utilities.mysql_create_tb(table_name, columns_tb) 
# query_formula_2 = Utilities.mysql_drop_tb(table_name)
print(query_formula_2)

# query_formula_3 = Utilities.mysql_addto_tb(table_name, values_arr)
query_formula_3 = Utilities.mysql_rmfrm_tb(table_name, column_name, value)
# query_formula_3 = Utilities.mysql_upd_tb(table_name, upd_column, upd_value, column_name, value)
print(query_formula_3)

# query_formula_4 = Utilities.mysql_slfrm_tb(table_name, column_names)
query_formula_4 = Utilities.mysql_slfrm_tb(table_name, all_columns)
print(query_formula_4)

query_formula_5 = Utilities.mysql_ordby_tb(table_name, column_names, ord_column_name, ord_direction)
# query_formula_5 = Utilities.mysql_ordby_tb(table_name, all_columns, ord_column_name, ord_direction)
print(query_formula_5)

query_formula_6 = Utilities.mysql_whrin_tb(table_name, column_names, column_name, value)
# query_formula_6 = Utilities.mysql_whrin_tb(table_name, all_columns, column_name, value)
print(query_formula_6)

query_formula_7 = Utilities.mysql_show_db()
query_formula_7 = Utilities.mysql_show_tb()
"""
# Testing variables
