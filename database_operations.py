import mysql.connector
from mysql.connector import Error
import pandas as pd



class DatabaseOpeartions:
    def __init__(self, host_name, user_name, user_password, db_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.db_name = db_name

    
    def create_connection(self, host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.db_name,
                auth_plugin='mysql_native_password'
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return connection
    

    def insert_data(self, connection, table_name:str, data):
        try:
            cursor = connection.cursor()

            columns = self.get_columns(connection, table_name)
            column_names = [column[0] for column in columns]
            query = f"INSERT INTO {table_name} ({','.join(column_names)}) VALUES ({','.join(['%s' for _ in column_names])})"
            cursor.execute(query, data)
            connection.commit()
            print("Data inserted successfully")
        except Exception as err:
            print(f"Error: '{err}'")

    def get_columns(self, connection, table_name:str):
        try:
            cursor = connection.cursor()
            cursor.execute(f"SHOW COLUMNS FROM {table_name}")
            columns = cursor.fetchall()
            return columns
        except Exception as err:
            print(f"Error: '{err}'")

    def update_data(self):
        pass

    def delete_data(self):
        pass

    def select_data(self):
        pass

    def select_all_data(self):
        pass

    def close_connection(self):
        pass