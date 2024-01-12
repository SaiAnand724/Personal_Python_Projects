"""
Working with MySQL Workbench
- Set up SQL server with credentials

Either command line should work:
pip3 install mysql-connector-python
pip3 install mysql-connector-python-rf
"""
# Import mysql-connector module 
import mysql.connector

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
    # user = "root"
    user = "saiSQL", 
    # Password for connection - User generated password
    # passwd = "User-Password"
    password = "saibabaSQL724",
    # Field to determine which database to start/work with
    database = "temp_db"
)

# print(mydb) - Lets you know the connection works
# Output should look like: <mysql.connector.connection.MySQLConnection object at 0x00000**********0>

# Create SQL database in python
# Initialize cursor
"""
Doc Source: https://www.psycopg.org/docs/cursor.html
Cursors are created by the connection. cursor() method: 
    they are bound to the connection for the entire lifetime and all the commands 
    are executed in the context of the database session wrapped by the connection.

"""
# Create cursor object using the mydb connection
mycursor = mydb.cursor()

# SQL Query Code Log
"""
1. mycursor.execute("CREATE DATABASE temp_db")
2. mycursor.execute("SHOW DATABASES")
3. mycursor.execute("CREATE TABLE players (play_id INTEGER(10) PRIMARY KEY, name VARCHAR(50), age INTEGER(10), pwr_lvl INTEGER(10))")
4. mycursor.execute("SHOW TABLES")
5. mycursor.execute(sql_formula, player1), mycursor.execute(sql_formula, player2), mycursor.execute(sql_formula, player3)
    sql_formula = "INSERT INTO players (play_id, name, age, pwr_lvl) VALUES (%s, %s, %s, %s)"
    player1 = (1, "He-mothy", 18, 6)
    player2 = (2, "She-mothy", 18, 8)
    player3 = (3, "Jee-mothy", 15, 4)
6. mycursor.executemany(sql_formula, xtra_player_array)
    xtra_player_array = [(4, "They-mothy", 22, 2), 
                         (5, "Darrel", 20, 10), 
                         (6, "We-mothy", 12, 7)]
7. mycursor.execute(sql_form_temp_1)
    sql_form_temp_1 = "UPDATE players_temp SET age = 15 WHERE name = 'We-mothy'"
n. mydb.commit()
n + 1. mycursor.close()


"""
# Base statement used to interact with MySQL in python
# mycursor.execute("")

"""
Created database temp_db
Show the databases listed
Must first run: mycursor.execute("SHOW DATABASES")

Then print the list of databases into terminal:
for db in mycursor:
    print(db)
"""
# mycursor.execute("CREATE DATABASE temp_db")

"""
Created table players
Template view (for writing in MySQL Workbench): 
    CREATE TABLE players 
    (play_id INTEGER(10) PRIMARY KEY, 
    name VARCHAR(50), 
    age INTEGER(10), 
    pwr_lvl INTEGER(10))
    );

Show the tables within database
Must first run: mycursor.execute("SHOW TABLES")

Then print the list of tables into terminal:
for tb in mycursor:
    print(tb)

""" 
# mycursor.execute("CREATE TABLE players (play_id INTEGER(10) PRIMARY KEY, name VARCHAR(50), age INTEGER(10), pwr_lvl INTEGER(10))")


"""
Populate table in python using "formula" and element object
Using ("%s") as a placeholder for the values in the table 
    such that the element values can be inserted using the parameter format

sql_formula = "INSERT INTO [table_name] (field_1, field_2, ... field_n) VALUES (%s, %s, ... %s)"
element_object_1 = (val_1, val_2, ... val_n)
element_object_2 = (val_1, val_2, ... val_n)
element_object_n = (val_1, val_2, ... val_n)
...

To fill up table: mycursor.execute(sql_formula, element_object_n)

Can be run as many times as needed for as many elements present

"""

sql_formula = "INSERT INTO players (play_id, name, age, pwr_lvl) VALUES (%s, %s, %s, %s)"
player1 = (1, "He-mothy", 18, 6)
player2 = (2, "She-mothy", 18, 8)
player3 = (3, "Jee-mothy", 15, 4)

# Excecuting insert statement for created player elements:
# mycursor.execute(sql_formula, player1) # - remove comments when running initially
# mycursor.execute(sql_formula, player2)
# mycursor.execute(sql_formula, player3)

"""
Populate table in python using "formula" and element object array
Using ("%s") as a placeholder for the values in the table 
    such that the element values can be inserted using the parameter format

sql_formula = "INSERT INTO [table_name] (field_1, field_2, ... field_n) VALUES (%s, %s, ... %s)"
element_object_array = [(val_1, val_2, ... val_n), 
                        (val_1, val_2, ... val_n), 
                        (val_1, val_2, ... val_n), 
                        ...]
                        
Doc Source: https://www.psycopg.org/docs/cursor.html#cursor.executemany

Format: executemany(query, vars_list)
Execute a database operation (query or command) against all parameter 
    tuples or mappings found in the sequence vars_list.

To populate as table values: mycursor.executemany(sql_formula, element_object_array)

Need only run once as all elements requiring insert should be in the array


"""
extra_player_array = [(4, "They-mothy", 22, 2), 
                      (5, "Darrel", 20, 10), 
                      (6, "We-mothy", 12, 7)]

# mycursor.executemany(sql_formula, extra_player_array) # - remove comment when running initially


"""
Doc Source: https://www.psycopg.org/docs/connection.html#connection.commit
Sends inserted data to database using .commit()
Commit any pending transaction to the database.

Note: Ideally this would be the last line
"""
mydb.commit()

"""
Doc Source: https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-close.htm
Use close() when you are done using a cursor. This method closes the cursor, resets all results, 
    and ensures that the cursor object has no reference to its original connection object.
"""
mycursor.close()