import mysql.connector
import pandas as pd
from table_definitions import (
    create_users_table, create_inventory_items_table, create_distribution_centers_table, create_events_table
)

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="",
            user="",  
            passwd="",  
            database=""  
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return None

def create_table(cursor, query):
    try:
        cursor.execute(query)
    except mysql.connector.Error as e:
        print(f"create_table() error: {e}")

def insert_data(cursor, table, data):
    placeholders = ', '.join(['%s'] * len(data.columns))
    columns = ', '.join(data.columns)
    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    cursor.executemany(sql, [tuple(row) for row in data.to_numpy()])

def load_and_insert_data(cursor, filepath, table_name):
    data = pd.read_csv(filepath)
    insert_data(cursor, table_name, data)

def main():
    db = create_connection()
    if db is None:
        return

    cursor = db.cursor()


    create_table_statements = [create_inventory_items_table,        #M.Serdar NAZLI's table
                                create_users_table,                 #Common Table
                                create_distribution_centers_table,   #Common Table
                                create_events_table                 # Mehmet Umut Gokdag's table
                              ]

    for statement in create_table_statements:
        create_table(cursor, statement)

    #Load and insert data from CSV files
    load_and_insert_data(cursor, 'tables/inventory_items.csv', 'events')
    load_and_insert_data(cursor, 'tables/users.csv', 'users')
    load_and_insert_data(cursor, 'tables/distribution_centers.csv', 'users')



    db.commit()
    cursor.close()
    db.close()

if __name__ == '__main__':
    main()
