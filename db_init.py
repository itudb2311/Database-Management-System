import mysql.connector
import pandas as pd
from table_definitions import (
    create_users_table, create_inventory_items_table, create_distribution_centers_table, create_events_table, create_products_table, create_order_items_table
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


    create_table_statements = [ create_inventory_items_table,       #M.Serdar NAZLI's table
                                create_users_table,                 #Common Table
                                create_distribution_centers_table,  #Common Table
                                create_events_table,                # Mehmet Umut Gokdag's table
                                create_products_table,              # Mehmet Ali Balıkçı's table
                                create_order_items_table,           # Ömer Faruk AYDIN's table
                              ]

    for statement in create_table_statements:
        create_table(cursor, statement)

    #Load and insert data from CSV files
#<<<<<<< HEAD
#    load_and_insert_data(cursor, 'tables/inventory_items.csv', 'events')
#    load_and_insert_data(cursor, 'tables/users.csv', 'users')
#    load_and_insert_data(cursor, 'tables/distribution_centers.csv', 'users')
#    load_and_insert_data(cursor, 'tables/products.csv', 'products')
#=======
#    load_and_insert_data(cursor, 'tables/thelook_ecommerce - inventory_items.csv', 'inventory_items')
#    load_and_insert_data(cursor, 'tables/thelook_ecommerce - users.csv', 'users')
#    load_and_insert_data(cursor, 'tables/thelook_ecommerce - distribution_centers.csv', 'distribution_centers')
#    load_and_insert_data(cursor, 'tables/thelook_ecommerce - events.csv', 'events')
#    load_and_insert_data(cursor, 'tables/thelook_ecommerce - products.csv', 'products')
#    load_and_insert_data(cursor, 'tables/thelook_ecommerce - order_items.csv', 'order_items')
#>>>>>>> f7881ae541f8cf4851b1cbbf7c6a420fedfe5b45


    db.commit()
    cursor.close()
    db.close()

if __name__ == '__main__':
    main()
