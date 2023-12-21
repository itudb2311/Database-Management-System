import mysql.connector
from settings import db_host, db_password, db_user, db_name


mydb = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute(f"CREATE DATABASE {db_name}")

# close the connection to the database.
if (mydb.is_connected()):
    mycursor.close()
    mydb.close()
    print("MySQL connection is closed")

cnx = mysql.connector.connect(
   user=db_user, 
   password=db_password, 
   host=db_host, 
   database=db_name, 
   auth_plugin='mysql_native_password')

cursor = cnx.cursor()

def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
          if command.rstrip() != '':
            cursor.execute(command)
        except ValueError as msg:
            print("Command skipped: ", msg)


executeScriptsFromFile('./database/schema.sql')
cnx.commit()