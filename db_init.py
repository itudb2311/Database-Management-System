import mysql.connector
import pandas as pd
from table_definitions import (
    create_users_table, create_inventory_items_table, create_distribution_centers_table, create_events_table, create_products_table, create_order_items_table, create_orders_table
)
import numpy as np
from data_pipeline import PipeLine
from settings import db_user,db_password,db_host,db_name
def create_connection():
    try:
        # Connect to the MySQL Server
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            passwd=db_password
        )
        cursor = connection.cursor()

        # Create a new database, if it doesn't exist
        database_name = db_name  
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

        # Close the cursor & connection
        connection.close()

        # Connect to the new database
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            passwd=db_password,
            database=database_name
        )


        print(f"Connected to {database_name}")
        return connection

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return None

def create_table(cursor, query):
    try:
        cursor.execute(query)
        print(f"Table created successfully. {query.split()[5]}")
    except mysql.connector.Error as e:
        print(f"Table could not be created. {query.split()[5]}")
        print(f"create_table() error: {e}")

def insert_data(cursor, table, data):
    data = data.where(pd.notnull(data), None) 
    placeholders = ', '.join(['%s'] * len(data.columns))
    columns = ', '.join(data.columns)
    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    cursor.executemany(sql, [tuple(row) for row in data.to_numpy()])

def load_and_insert_data(cursor, table_name, data):
    insert_data(cursor, table_name, data)
    print(f"Data inserted successfully. {table_name}")
    
def delete_data(cursor, table_name):
    cursor.execute(f"DELETE FROM {table_name}")
    print(f"Data deleted successfully. {table_name}")

def main():
    db = create_connection()
    if db is None:
        print("Connection to the database could not be established!")
        return

    cursor = db.cursor()

    print("-"*10,"Creating tables...","-"*10)
    create_table_statements = [ create_distribution_centers_table,  #Common Table
                                create_inventory_items_table,       #M.Serdar NAZLI's table
                                create_users_table,                 #Common Table
                                create_events_table,                # Mehmet Umut Gokdag's table
                                create_products_table,              # Mehmet Ali Balıkçı's table
                                create_orders_table,                # HASAN TAHA BAGCI's table
                                create_order_items_table,           # Ömer Faruk AYDIN's table
                              ]

    for statement in create_table_statements:
        create_table(cursor, statement)

    pipeLine = PipeLine()
    print("-"*10,"Tables are created!","-"*10)

    print("\n","-"*10,"Data is being inserted...","-"*10)

    delete_data(cursor, 'order_items')
    delete_data(cursor, 'products')
    delete_data(cursor, 'orders')
    delete_data(cursor, 'events')
    delete_data(cursor, 'inventory_items')
    delete_data(cursor, 'distribution_centers')
    delete_data(cursor, 'users')
    
    load_and_insert_data(cursor, 'distribution_centers',pipeLine.distribution_centers)
    load_and_insert_data(cursor, 'users',pipeLine.users)
    load_and_insert_data(cursor, 'events',pipeLine.events)
    load_and_insert_data(cursor, 'inventory_items',pipeLine.inventory_items)
    load_and_insert_data(cursor, 'products',pipeLine.products)
    load_and_insert_data(cursor, 'orders',pipeLine.orders)
    load_and_insert_data(cursor, 'order_items',pipeLine.order_items)
    
    
    print("-"*10,"Data is inserted!","-"*10)

    db.commit()
    cursor.close()
    db.close()

if _name_ == '_main_':
    main()