import mysql.connector
from settings import db_host, db_password, db_user, db_name

try:
    mydb = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()

    mycursor.execute(f"CREATE DATABASE {db_name}")
    print(f"Database {db_name} created")
    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()

    cnx = mysql.connector.connect(
    user=db_user, 
    password=db_password, 
    host=db_host, 
    database=db_name, 
    auth_plugin='mysql_native_password')

    cursor = cnx.cursor()

    def executeScriptsFromFile(filename):
        fd = open(filename, 'r')
        sqlFile = fd.read()
        fd.close()

        sqlCommands = sqlFile.split(';')

        for command in sqlCommands:
            try:
                if command.rstrip() != '':
                    cursor.execute(command)
            except ValueError as msg:
                print("Command skipped: ", msg)


    executeScriptsFromFile('./database/schema.sql')
    cnx.commit()

    print(f"Database {db_name} created")
except Exception as err:
    print("There was an error creating the database: ", err)