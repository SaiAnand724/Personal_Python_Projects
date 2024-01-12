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
    user = "root", 
    # Password for connection - User generated password
    password = "User-Password",
    # Field to determine which database to start/work with
    database = "Any_Database"
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

# Base statement used to interact with MySQL in python
# mycursor.execute("")

# SQL Query Code Log
"""
1. mycursor.execute("SELECT * FROM players")
2. mycursor.fetchall()
3. mycursor.fetchone() - better to not use
4. mycursor.execute(query_formula)
    query_formula = "SELECT [columns] FROM [table] WHERE [column name = value]"
5. mycursor.execute(upd_form_temp)
    upd_form_temp = "UPDATE [table] SET [column name = value] WHERE [column name = value]"
6. mycursor.execute(ord_form_temp)
    ord_form_temp = "SELECT [columns] FROM [table] ORDER BY [column name]"
7. mycursor.execute(del_form_temp)
    del_form_temp = "DELETE FROM [table] WHERE [column name = value]"
8. mycursor.executemany(sql_formula_temp_1, dupl_entry)
    sql_formula_temp_1 = "INSERT INTO players_temp (play_id, name, age, pwr_lvl) VALUES (%s, %s, %s, %s)"
    dupl_entry = [(7, "Ree-mothy", 16, 6), (8, "Ree-mothy", 16, 6)]
9. mycursor.execute(drop_form_temp)
    drop_form_temp = "DROP TABLE IF EXISTS [table]"
10. mydp.commit()
11. mycursor.close()
"""

# Player Table Column Formats: (play_id, name, age, pwr_lvl)

# Excecuting select statement for all columns in MySQL
mycursor.execute("SELECT * FROM players")

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table = mycursor.fetchall()

# Print in python terminal
print("Players Table [all columns]: ")
for row in myresult_table:
    print(row)
    
print("\n") # spacing

# Excecuting select statement for name and age columns in MySQL
mycursor.execute("SELECT name, age FROM players")

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table_1 = mycursor.fetchall()

# Print in python terminal
print("Players Table [name, age]: ")
for row in myresult_table_1:
    print(row)
    
print("\n") # spacing

# Excecuting select statement for play_id and pwr_lvl columns in MySQL
mycursor.execute("SELECT play_id, pwr_lvl FROM players")

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table_2 = mycursor.fetchall()

# Print in python terminal
print("Players Table [play_id, pwr_lvl]: ")
for row in myresult_table_2:
    print(row)
    
print("\n") # spacing

# Excecuting select statement for play_id and pwr_lvl columns in MySQL
mycursor.execute("SELECT * FROM players WHERE name LIKE '%-mothy'")

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table_3 = mycursor.fetchall()

# Print in python terminal
print("Players Table [names with %-mothy]: ")
for row in myresult_table_3:
    print(row)
    
print("\n") # spacing

# Excecuting select statement for play_id and pwr_lvl columns in MySQL
mycursor.execute("SELECT * FROM players WHERE name NOT LIKE '%-mothy'")

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table_4 = mycursor.fetchall()

# Print in python terminal
print("Players Table [names without %-mothy]: ")
for row in myresult_table_4:
    print(row)
    
print("\n") # spacing



"""
Create "formula" for specific queries:
query_formula = "SELECT [columns] FROM [table] WHERE [column name w/ conditional]"
"""
query_formula = "SELECT * FROM players WHERE age = 18"

mycursor.execute(query_formula)

# Using .fectchall() function to get data from previous execute statement to store table
myformula_table_1 = mycursor.fetchall()

# print(myformula_table) - debug print

# Print in python terminal
print("Players Table [all columns, age = 18]: ")
for result in myformula_table_1:
    print(result)

print("\n") # spacing

# Excecuting select statement for all columns in MySQL
mycursor.execute("SELECT * FROM players LIMIT 1")

"""
Using .fectchone() function to get one row (first) of 
data from previous execute statement to store table

Note: .fetchone() function should probably not be used, LIMIT works better
    Error traceback log will start with this line: 
        mycursor.execute("SELECT [columns] FROM [table_name]")
"""

# using .fetchall() to .fetchone() issue
myresult_table_fone = mycursor.fetchall()
# myresult_table_fone = mycursor.fetchone()

# Print in python terminal
print("Players Table [all columns, first row]: ")
for row in myresult_table_fone:
    print(row)

print("\n") # spacing


"""
Created table players_temp
Template view (for writing in MySQL Workbench): 
    CREATE TABLE players_temp
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
# INSERT INTO formula
sql_formula_temp = "INSERT INTO players_temp (play_id, name, age, pwr_lvl) VALUES (%s, %s, %s, %s)"

# mycursor.execute("CREATE TABLE players_temp (play_id INTEGER(10) PRIMARY KEY, name VARCHAR(50), age INTEGER(10), pwr_lvl INTEGER(10))")

copy_player_array =  [(1, "He-mothy", 18, 6), 
                     (2, "She-mothy", 18, 8), 
                     (3, "Jee-mothy", 15, 4), 
                     (4, "They-mothy", 22, 2), 
                     (5, "Darrel", 20, 10), 
                     (6, "We-mothy", 12, 7)]

# mycursor.executemany(sql_formula_temp, copy_player_array) # - remove comment when running initially

mycursor.execute("SHOW TABLES")

# Print the list of tables into terminal
print("Tables in Database: ")
for tb in mycursor:
    print(tb)

print("\n") # spacing 

# Player_temp Table Column Formats: (play_id, name, age, pwr_lvl)

# Excecuting select statement for all columns in MySQL
mycursor.execute("SELECT * FROM players")

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table = mycursor.fetchall()

# Print in python terminal
print("Players_temp init Table [all columns]: ")
for row in myresult_table:
    print(row)
    
print("\n") # spacing


"""
Updating players_temp table with "formula"
upd_form_temp = "UPDATE [table_name] SET [column_name = value] WHERE [conditional]"
"""
# UPDATE formula
upd_form_temp = "UPDATE players_temp SET age = 15 WHERE name = 'We-mothy'"

# mycursor.execute(upd_form_temp)

# Excecuting select statement using UPDATE formula
mycursor.execute("SELECT * FROM players_temp")

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table = mycursor.fetchall()

# Print in python terminal
print("Players_temp Table after UPDATE [all columns]: ")
for row in myresult_table:
    print(row)
    
print("\n") # spacing

# Excecuting select statement for all columns in MySQL, limiting to top 5 rows
mycursor.execute("SELECT * FROM players_temp LIMIT 3")

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table = mycursor.fetchall()

# Print in python terminal
print("Players_temp Table [top 3 rows]: ")
for row in myresult_table:
    print(row)
    
print("\n") # spacing

# Excecuting select statement for all columns in MySQL, limiting to top 5 rows, offset by 2
mycursor.execute("SELECT * FROM players_temp LIMIT 3 OFFSET 2")

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table = mycursor.fetchall()

# Print in python terminal
print("Players_temp Table [top 3 rows, 2 row offset]: ")
for row in myresult_table:
    print(row)
    
print("\n") # spacing

"""
Updating players_temp table with "formula"
ord_form_temp = "SELECT [columns] FROM [table] ORDER BY [column name]"
"""

# ORDER BY formula
ord_form_temp = "SELECT * FROM players_temp ORDER BY name"

# Excecuting select statement using ORDER BY formula
mycursor.execute(ord_form_temp)

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table = mycursor.fetchall()

# Print in python terminal
print("Players_temp Table after ORDER BY [name]: ")
for row in myresult_table:
    print(row)
    
print("\n") # spacing

# ORDER BY age ascending
ord_form_temp_1 = "SELECT * FROM players_temp ORDER BY age ASC"

# Excecuting select statement using ORDER BY formula
mycursor.execute(ord_form_temp_1)

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table = mycursor.fetchall()

# Print in python terminal
print("Players_temp Table after ORDER BY [age ASC]: ")
for row in myresult_table:
    print(row)
    
print("\n") # spacing

# ORDER BY age desc
ord_form_temp_2 = "SELECT * FROM players_temp ORDER BY age DESC"

# Excecuting select statement using ORDER BY formula
mycursor.execute(ord_form_temp_2)

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table = mycursor.fetchall()

# Print in python terminal
print("Players_temp Table after ORDER BY [age DESC]: ")
for row in myresult_table:
    print(row)
    
print("\n") # spacing

# ORDER BY power level - default ascending, keep it at descending
ord_form_temp_3 = "SELECT * FROM players_temp ORDER BY pwr_lvl DESC"

# Excecuting select statement using ORDER BY formula
mycursor.execute(ord_form_temp_3)

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table = mycursor.fetchall()

# Print in python terminal
print("Players_temp Table after ORDER BY [pwr_lvl DESC]: ")
for row in myresult_table:
    print(row)
    
print("\n") # spacing

# INSERT INTO formula for duplicate entries
sql_formula_temp_1 = "INSERT INTO players_temp (play_id, name, age, pwr_lvl) VALUES (%s, %s, %s, %s)"

# Creating duplicate entry
dupl_entry = [(7, "Ree-mothy", 16, 6), (8, "Ree-mothy", 16, 6)]

# Execute statement for adding duplicate entries
# mycursor.executemany(sql_formula_temp_1, dupl_entry) # - remove comment when running initially

# Execute select statement for all columns in MySQL
mycursor.execute("SELECT * FROM players_temp")

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table = mycursor.fetchall()

# Print in python terminal
print("Players_temp Table after entering duplicates: ")
for row in myresult_table:
    print(row)
    
print("\n") # spacing

"""
Deleting from players_temp table with "formula"
del_form_temp = "DELETE FROM [table] WHERE [column name = value]"
"""
# DELETE "formula", finds first instance of "Ree-mothy" and deletes it
del_form_temp = "DELETE FROM players_temp WHERE name = 'Ree-mothy'"

# Executing statement for DELETE formula 
# mycursor.execute(del_form_temp) # - remove comment when running initially

# Execute select statement for all columns in MySQL
mycursor.execute("SELECT * FROM players_temp")

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table = mycursor.fetchall()

# Print in python terminal
print("Players_temp Table after DELETE duplicates: ")
for row in myresult_table:
    print(row)

"""
Code snippet below can be used after entries and after deleting to see difference:

# Execute select statement for all columns in MySQL
mycursor.execute("SELECT * FROM players_temp")

# Using .fectchall() function to get data from previous execute statement to store table
myresult_table = mycursor.fetchall()

# Print in python terminal
print("Players_temp Table after entering duplicates: ")
for row in myresult_table:
    print(row)

# Print in python terminal
print("Players_temp Table after DELETE duplicates: ")
for row in myresult_table:
    print(row)

"""

print("\n") # spacing

"""
Dropping players_temp table from database with "formula"
drop_form_temp = "DROP TABLE [table]"

Dropping temp_db database from schema
drop_form_temp_db = "DROP [database]"
"""
# DROP players_temp table
drop_form_temp = "DROP TABLE IF EXISTS players_temp"

# Executing statement for DROP formula 
# mycursor.execute(drop_form_temp) # - remove comment when running initially

# Excecutes command to show the tables within database in MySQL
mycursor.execute("SHOW TABLES")

# Print the list of tables into terminal:
print("Tables in Database: ")
for tb in mycursor:
    print(tb)


"""
Doc Source: https://www.psycopg.org/docs/connection.html#connection.commit
Sends inserted data to database using .commit()
Commit any pending transaction to the database.

Note: Ideally this would be the last line in code after modifying data
"""
mydb.commit()

"""
Doc Source: https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-close.htm
Use close() when you are done using a cursor. This method closes the cursor, resets all results, 
    and ensures that the cursor object has no reference to its original connection object.
"""
mycursor.close()
