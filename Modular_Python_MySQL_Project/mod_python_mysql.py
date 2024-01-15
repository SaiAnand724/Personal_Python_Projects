"""
Working with MySQL Workbench
- Set up SQL server with credentials

Either command line should work:
pip3 install mysql-connector-python
pip3 install mysql-connector-python-rf
"""
import os, sys

# Import mysql-connector module 
import mysql.connector

# Import Utilities module from util.py
from utilities.util import Utilities as mysql_util

# Global variables
database_name = "python_test_db"
table_name1 = "python_students_table"
column_names = ["stud_id", "name", "age", "gender"]


def connect_to_db():
    global mycursor
    global mydb
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

    print("Database connection point: ", mydb) # - Lets you know the connection works
    # Output should look like: <mysql.connector.connection.MySQLConnection object at 0x00000**********0>
    return mydb


def create_database(mycursor):
        global database_name
        # Create MySQL database in python
        # Manual name input to make database
        # References mydb object for database name
        # database_name = mydb._database # - Uncommented once field is filled
        create_db_form = mysql_util.mysql_create_db(database_name)
        print(create_db_form)
        mycursor.execute(create_db_form)

        # Show MySQL databases in python
        show_db_form = mysql_util.mysql_show_db()
        mycursor.execute(show_db_form)

        print("\nDatabases: ")
        for db in mycursor:
            print(db)

def use_database(mycursor):
    global database_name
    # Use MySQL database in python
    use_db_form = mysql_util.mysql_use_db(database_name)
    mycursor.execute(use_db_form)

def create_table(mycursor):
    # Create MySQL table in python
    columns_tb = ["stud_id INTEGER(10) PRIMARY KEY", "name VARCHAR(50)", "age INTEGER(10)", "gender VARCHAR(1)"]
    create_tb_form = mysql_util.mysql_create_tb(table_name1, columns_tb)
    mycursor.execute(create_tb_form)

    # Show MySQL tables in python
    show_tb_form = mysql_util.mysql_show_tb()
    mycursor.execute(show_tb_form)

    print("\nTables: ")
    for tb in mycursor:
        print(tb)
        
def populate_tb(mycursor):
    # Add values to MySQL table in python
    values_arr = (1, "He-mothy", 18, "M")
    addto_tb_form = mysql_util.mysql_addto_tb(table_name1, values_arr)
    mycursor.execute(addto_tb_form) # needs to get commented once it is run, should fix in util.py later
    
def show_tb(mycursor):
    all_columns = ["*"]
    # Select all columns to see new input
    sel_allcol_form = mysql_util.mysql_slfrm_tb(table_name1, all_columns)
    mycursor.execute(sel_allcol_form)

    # Using .fectchall() function to get data from previous execute statement to store table
    myresult_table = mycursor.fetchall()

    # Print table
    print("\nTable [all columns (*)]: ")
    for row in myresult_table:
        print(row)
    
    # Turn each column name into an array within the field_list
    field_list = [[i] for i in column_names]
    print(str(field_list))

    # Temp random module import for randint() function
    from random import randint
    rand_index = randint(0, len(column_names) - 1)

    # Select only specified columns to see new input
    sel_col_form = mysql_util.mysql_slfrm_tb(table_name1, field_list[rand_index])
    mycursor.execute(sel_col_form)

    # Using .fectchall() function to get data from previous execute statement to store table
    myresult_table_1 = mycursor.fetchall()

    # Print table
    print("\nTable " + str(field_list[rand_index]) + ": ")
    for row in myresult_table_1:
        print(row)
        
def drop_db(mycursor):
    global database_name
    # Drop database from MySQL using Python
    drop_db_form = mysql_util.mysql_drop_db(database_name)
    print(drop_db_form)
    mycursor.execute(drop_db_form)
    
    
def db_commit(mydb):
    """
    Doc Source: https://www.psycopg.org/docs/connection.html#connection.commit
    Sends inserted data to database using .commit()
    Commit any pending transaction to the database.

    Note: Ideally this would be the next to last line
    """
    mydb.commit()
    
def create_cursor(mydb):
    # Initialize cursor
    """
    Doc Source: https://www.psycopg.org/docs/cursor.html
    Cursors are created by the connection. cursor() method: 
        they are bound to the connection for the entire lifetime and all the commands 
        are executed in the context of the database session wrapped by the connection.

    """
    # Create cursor object using the mydb connection
    mycursor = mydb.cursor()
    return mycursor
    
def cursor_close(mycursor):
    """
    Doc Source: https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-close.htm
    Use close() when you are done using a cursor. This method closes the cursor, resets all results, 
        and ensures that the cursor object has no reference to its original connection object.
    """
    mycursor.close()


if __name__ == "__main__":
    mydb = connect_to_db()
    mycursor = create_cursor(mydb)
    create_database(mycursor)
    use_database(mycursor)
    create_table(mycursor)
    populate_tb(mycursor) # - comment after adding to table
    db_commit(mydb)
    show_tb(mycursor)
    # drop_db(mycursor) # - uncomment when dropping table
    cursor_close(mycursor)