from settings import db_user,db_password,db_host,db_name  
import mysql.connector
import hashlib
import numpy as np


class Admins:
    def __init__(self, connection):
        self.columns = ['id', 'name','email','password']    # Columns
        self.connection = connection                        # Connection
    def check_admin(self, email, password):                 # Check if the admin exists
        # Encrpyt the password to SHA256
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            cursor = self.connection.cursor()              # Create a cursor
            cursor.execute("SELECT * FROM admins WHERE email = %s AND password = %s", (email, hashed_password)) # Execute the query
            result = cursor.fetchone()                      # Fetch the result
            cursor.close()                                  # Close the cursor
            if result is None:
                return False
            return True
        except Exception as e:
            print("Error while checking admin", e)
            return f"Error: {e}"
    
class DistributionCenters:
    def __init__(self, connection):
        self.columns = ['id', 'name', 'latitude', 'longitude']  # Columns
        self.connection = connection                            # Connection

    def generate_primary_key(self):
        try:
            cursor = self.connection.cursor()                           # Create a cursor
            cursor.execute("SELECT MAX(id) FROM distribution_centers")  # Get the max id
            max_id = cursor.fetchone()[0]                               # Fetch the result
            cursor.close()                                              # Close the cursor
            if max_id is None:                                          # If there is no max id, return 1
                return 1
            return max_id + 1                                           # Otherwise, return the max id + 1
        except Exception as e:
            print("Error while generating primary key for distribution_centers", e)
            return f"Error: {e}"

    def insert_data(self, data):
        try:
            cursor = self.connection.cursor()               # Create a cursor
            data['id'] = self.generate_primary_key()        # Generate a primary key

            # Convert 'None' strings to Python None and format dates
            for key, value in data.items():
                if value == 'None' or value == '':
                    data[key] = None

            # Prepare the insert statement
            insert_fields = ', '.join(self.columns)                 # Get the columns
            placeholders = ', '.join(['%s' for _ in self.columns])  # Get the placeholders
            insert_query = f"INSERT INTO distribution_centers ({insert_fields}) VALUES ({placeholders})"    # Create the query

            # Extract the values in the order of self.columns
            insert_values = [data.get(col) for col in self.columns]

            # Execute the query
            cursor.execute(insert_query, tuple(insert_values))
            self.connection.commit()
            cursor.close()
            print("Inserted", insert_values)
        except Exception as e:
            print("Error while inserting into distribution_centers", e)
            return f"Error: {e}"

    def update_data(self, data, id):
        try:
            cursor = self.connection.cursor()               # Create a cursor
            # Convert 'None' strings to Python None and format dates
            processed_data = [
                None if data[field] == 'None' else data[field] for field in self.columns if field in data
            ]

            # Prepare the update statement
            update_fields = ', '.join([f"{field} = %s" for field in self.columns if field in data])

            # Create the query
            update_query = f"UPDATE distribution_centers SET {update_fields} WHERE id = %s"

            # Execute the query
            cursor.execute(update_query, processed_data + [id])

            # Commit the changes
            self.connection.commit()
            cursor.close()
            print("Updated", processed_data)
        except Exception as e:
            print("Error while updating distribution_centers", e)
            return f"Error: {e}"

    def delete_data(self, id):
        try:
            cursor = self.connection.cursor()

            # Prepare the delete statement
            cursor.execute("DELETE FROM distribution_centers WHERE id=%s", (id,))
            self.connection.commit()
            cursor.close()
            print("Deleted", id)
        except Exception as e:
            print("Error while deleting from distribution_centers", e)
            return f"Error: {e}"

    def search(self, data):
        try:
            cursor = self.connection.cursor()

            # Prepare the search statement
            query_parts = []
            parameters = []
            # Iterate over the columns
            for column in self.columns:
                # Get the value from the form data
                value = data.get(column, '') + '%'

                # If the value is '%', append the query part
                if value == '%':
                    query_parts.append(f"({column} LIKE %s OR {column} IS NULL)")

                # Otherwise,
                else:
                    query_parts.append(f"{column} LIKE %s")
                parameters.append(value)
            
            # Create the query
            query = "SELECT * FROM distribution_centers WHERE " + " AND ".join(query_parts)
            cursor.execute(query, tuple(parameters))
            results = cursor.fetchall()
            columns = cursor.description # Get the columns
            cursor.close()
            column_types = []
            for column in columns:
                column_name = column[0]
                column_type = column[1]
                mysql_data_type = get_mysql_data_types(column_type)
                item = {'column_name': column_name, 'column_type': mysql_data_type}
                column_types.append(item)
            return results, column_types
        
        except Exception as e:
            print("Could not find any corresponding value", e)
            return False



class Events:
    def __init__(self, connection):
        self.columns = ['id', 'user_id', 'sequence_number', 'session_id', 'created_at', 'ip_address', 'city', 'state', 'postal_code', 'browser', 'traffic_source', 'uri', 'event_type']
        self.connection = connection

    def generate_primary_key(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT MAX(id) FROM events")
            max_id = cursor.fetchone()[0]
            cursor.close()
            if max_id is None:
                return 1
            return max_id + 1
        except Exception as e:
            print("Error while generating primary key for events", e)
            return f"Error: {e}"

    def insert_data(self, data):
        try:
            cursor = self.connection.cursor()

            data['id'] = self.generate_primary_key()

            # Convert 'None' strings to Python None and format dates
            for key, value in data.items():
                if value == 'None' or value == '':
                    data[key] = None
                # Add additional formatting as necessary, e.g., for dates

            # Prepare the insert statement
            insert_fields = ', '.join(self.columns)
            placeholders = ', '.join(['%s' for _ in self.columns])
            insert_query = f"INSERT INTO events ({insert_fields}) VALUES ({placeholders})"

            # Extract the values in the order of self.columns
            insert_values = [data.get(col) for col in self.columns]

            # Execute the query
            cursor.execute(insert_query, tuple(insert_values))
            self.connection.commit()
            cursor.close()
            print("Inserted", insert_values)
        except Exception as e:
            print("Error while inserting into events", e)
            return f"Error: {e}"

    def update_data(self, data, id):
        try:
            cursor = self.connection.cursor()
            processed_data = [
                None if data[field] == 'None' else data[field] for field in self.columns if field in data
            ]
            update_fields = ', '.join([f"{field} = %s" for field in self.columns if field in data])
            update_query = f"UPDATE events SET {update_fields} WHERE id = %s"
            cursor.execute(update_query, processed_data + [id])
            self.connection.commit()
            cursor.close()
            print("Updated", processed_data)
        except Exception as e:
            print("Error while updating events", e)
            return f"Error: {e}"

    def delete_data(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM events WHERE id=%s", (id,))
            self.connection.commit()
            cursor.close()
            print("Deleted", id)
        except Exception as e:
            print("Error while deleting from events", e)
            return f"Error: {e}"

    def search(self, data):
        try:
            cursor = self.connection.cursor()
            query_parts = []
            parameters = []
            for column in self.columns:
                value = data.get(column, '') + '%'
                if value == '%':
                    query_parts.append(f"({column} LIKE %s OR {column} IS NULL)")
                else:
                    query_parts.append(f"{column} LIKE %s")
                parameters.append(value)
            query = "SELECT * FROM events WHERE " + " AND ".join(query_parts)
            cursor.execute(query, tuple(parameters))
            results = cursor.fetchall()
            columns = cursor.description # Get the columns
            cursor.close()
            column_types = []
            for column in columns:
                column_name = column[0]
                column_type = column[1]
                mysql_data_type = get_mysql_data_types(column_type)
                item = {'column_name': column_name, 'column_type': mysql_data_type}
                column_types.append(item)
            return results, column_types
        
        except Exception as e:
            print("Could not find any corresponding value", e)
            return False

class InventoryItems:
    def __init__(self, connection):
        self.columns = ['id', 'product_id', 'created_at', 'sold_at', 'cost', 'product_category', 'product_name', 'product_brand', 'product_retail_price', 'product_department', 'product_sku', 'product_distribution_center_id']
        self.connection = connection
    
    def generate_primary_key(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT MAX(id) FROM inventory_items")
            max_id = cursor.fetchone()[0]
            cursor.close()
            if max_id is None:
                return 1
            return max_id + 1
        except Exception as e:
            print("Error while generating primary key for inventory_items", e)
            return f"Error: {e}"
    
    def insert_data(self, data):
        try:
            cursor = self.connection.cursor()


            data['id'] = self.generate_primary_key()

            # Convert 'None' strings to Python None and format dates
            for key, value in data.items():
                if value == 'None' or value == '':
                    data[key] = None
                # Add additional formatting as necessary, e.g., for dates

            # Prepare the insert statement
            insert_fields = ', '.join(self.columns)
            placeholders = ', '.join(['%s' for _ in self.columns])
            insert_query = f"INSERT INTO inventory_items ({insert_fields}) VALUES ({placeholders})"

            # Extract the values in the order of self.columns
            insert_values = [data.get(col) for col in self.columns]

            # Execute the query
            cursor.execute(insert_query, tuple(insert_values))
            self.connection.commit()
            cursor.close()
            print("Inserted", insert_values)
        except Exception as e:
            print("Error while inserting into inventory_items", e)
            return f"Error: {e}"
    
    def update_data(self, data, id):
        try:
            cursor = self.connection.cursor()
            processed_data = [
                None if data[field] == 'None' else data[field] for field in self.columns if field in data
            ]
            update_fields = ', '.join([f"{field} = %s" for field in self.columns if field in data])
            update_query = f"UPDATE inventory_items SET {update_fields} WHERE id = %s"
            cursor.execute(update_query, processed_data + [id])
            self.connection.commit()
            cursor.close()
            print("Updated", processed_data)
        except Exception as e:
            print("Error while updating inventory_items", e)
            return f"Error: {e}"
    
    def delete_data(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM inventory_items WHERE id=%s", (id,))
            self.connection.commit()
            cursor.close()
            print("Deleted", id)
        except Exception as e:
            print("Error while deleting from inventory_items", e)
            return f"Error: {e}"
        
    def search(self, data):
        try:
            cursor = self.connection.cursor()
            query_parts = []
            parameters = []
            for column in self.columns:
                value = data.get(column, '') + '%'
                if value == '%':
                    query_parts.append(f"({column} LIKE %s OR {column} IS NULL)")
                else:
                    query_parts.append(f"{column} LIKE %s")
                parameters.append(value)
            query = "SELECT * FROM inventory_items WHERE " + " AND ".join(query_parts)
            cursor.execute(query, tuple(parameters))
            results = cursor.fetchall()
            columns = cursor.description # Get the columns
            cursor.close()
            column_types = []
            for column in columns:
                column_name = column[0]
                column_type = column[1]
                mysql_data_type = get_mysql_data_types(column_type)
                item = {'column_name': column_name, 'column_type': mysql_data_type}
                column_types.append(item)
            return results, column_types
        
        except Exception as e:
            print("Could not find any corresponding value", e)
            return False
        


class OrderItems:
    def __init__(self, connection):
        self.columns = ['id', 'order_id', 'user_id', 'product_id', 'inventory_item_id', 'status', 'created_at', 'shipped_at', 'delivered_at', 'returned_at', 'sale_price']
        self.connection = connection

    def generate_primary_key(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT MAX(id) FROM order_items")
            max_id = cursor.fetchone()[0]
            cursor.close()
            if max_id is None:
                return 1
            return max_id + 1
        except Exception as e:
            print("Error while generating primary key for order_items", e)
            return f"Error: {e}"
        
    def insert_data(self, data):
        try:
            cursor = self.connection.cursor()


            data['id'] = self.generate_primary_key()

            # Convert 'None' strings to Python None and format dates
            for key, value in data.items():
                if value == 'None' or value == '':
                    data[key] = None
                # Add additional formatting as necessary, e.g., for dates

            # Prepare the insert statement
            insert_fields = ', '.join(self.columns)
            placeholders = ', '.join(['%s' for _ in self.columns])
            insert_query = f"INSERT INTO order_items ({insert_fields}) VALUES ({placeholders})"

            # Extract the values in the order of self.columns
            insert_values = [data.get(col) for col in self.columns]

            # Execute the query
            cursor.execute(insert_query, tuple(insert_values))
            self.connection.commit()
            cursor.close()
            print("Inserted", insert_values)
        except Exception as e:
            print("Error while inserting into order_items", e)
            return f"Error: {e}"
        
    def update_data(self, data, id):
        try:
            cursor = self.connection.cursor()
            processed_data = [
                None if data[field] == 'None' else data[field] for field in self.columns if field in data
            ]
            update_fields = ', '.join([f"{field} = %s" for field in self.columns if field in data])
            update_query = f"UPDATE order_items SET {update_fields} WHERE id = %s"
            cursor.execute(update_query, processed_data + [id])
            self.connection.commit()
            cursor.close()
            print("Updated", processed_data)
        except Exception as e:
            print("Error while updating order_items", e)
            return f"Error: {e}"

    def delete_data(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM order_items WHERE id=%s", (id,))
            self.connection.commit()
            cursor.close()
            print("Deleted", id)
        except Exception as e:
            print("Error while deleting from order_items", e)
            return f"Error: {e}"

    def search(self, data):
        try:
            cursor = self.connection.cursor()
            query_parts = []
            parameters = []
            for column in self.columns:
                value = data.get(column, '') + '%'
                if value == '%':
                    query_parts.append(f"({column} LIKE %s OR {column} IS NULL)")
                else:
                    query_parts.append(f"{column} LIKE %s")
                parameters.append(value)
            query = "SELECT * FROM order_items WHERE " + " AND ".join(query_parts)
            cursor.execute(query, tuple(parameters))
            results = cursor.fetchall()
            columns = cursor.description # Get the columns
            cursor.close()
            column_types = []
            for column in columns:
                column_name = column[0]
                column_type = column[1]
                mysql_data_type = get_mysql_data_types(column_type)
                item = {'column_name': column_name, 'column_type': mysql_data_type}
                column_types.append(item)
            return results, column_types
        
        except Exception as e:
            print("Could not find any corresponding value", e)
            return False

class Orders:
    def __init__(self, connection):
        self.columns = ['order_id', 'user_id', 'status', 'gender', 'created_at', 'returned_at', 'shipped_at', 'delivered_at', 'num_of_item']
        self.connection = connection

    def generate_primary_key(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT MAX(order_id) FROM orders")
            max_id = cursor.fetchone()[0]
            cursor.close()
            if max_id is None:
                return 1
            return max_id + 1
        except Exception as e:
            print("Error while generating primary key for orders", e)
            return f"Error: {e}"


    def insert_data(self, data):
        try:
            cursor = self.connection.cursor()

            data['order_id'] = self.generate_primary_key()

            # Convert 'None' strings to Python None and format dates
            for key, value in data.items():
                if value == 'None' or value == '':
                    data[key] = None

            # Prepare the insert statement
            insert_fields = ', '.join(self.columns)
            placeholders = ', '.join(['%s' for _ in self.columns])
            insert_query = f"INSERT INTO orders ({insert_fields}) VALUES ({placeholders})"

            # Extract the values in the order of self.columns
            insert_values = [data.get(col) for col in self.columns]

            # Execute the query
            cursor.execute(insert_query, tuple(insert_values))
            self.connection.commit()
            cursor.close()
            print("Inserted", insert_values)
        except Exception as e:
            print("Error while inserting into orders", e)
            return f"Error: {e}"
        
    def update_data(self, data, id):
        try:
            cursor = self.connection.cursor()
            processed_data = [
                None if data[field] == 'None' else data[field] for field in self.columns if field in data
            ]
            update_fields = ', '.join([f"{field} = %s" for field in self.columns if field in data])
            update_query = f"UPDATE orders SET {update_fields} WHERE order_id = %s"
            cursor.execute(update_query, processed_data + [id])
            self.connection.commit()
            cursor.close()
            print("Updated", processed_data)
        except Exception as e:
            print("Error while updating orders", e)
            return f"Error: {e}"
        
    def delete_data(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM orders WHERE order_id=%s", (id,))
            self.connection.commit()
            cursor.close()
            print("Deleted", id)
        except Exception as e:
            print("Error while deleting from orders", e)
            return f"Error: {e}"
        
    def search(self, data):
        try:
            cursor = self.connection.cursor()
            query_parts = []
            parameters = []
            for column in self.columns:
                value = data.get(column, '') + '%'
                if value == '%':
                    query_parts.append(f"({column} LIKE %s OR {column} IS NULL)")
                else:
                    query_parts.append(f"{column} LIKE %s")
                parameters.append(value)
            query = "SELECT * FROM orders WHERE " + " AND ".join(query_parts)
            cursor.execute(query, tuple(parameters))
            results = cursor.fetchall()
            columns = cursor.description # Get the columns
            cursor.close()
            column_types = []
            for column in columns:
                column_name = column[0]
                column_type = column[1]
                mysql_data_type = get_mysql_data_types(column_type)
                item = {'column_name': column_name, 'column_type': mysql_data_type}
                column_types.append(item)
            return results, column_types
        
        except Exception as e:
            print("Could not find any corresponding value", e)
            return False



class Products:
    def __init__(self, connection):
        self.columns = ['id', 'cost', 'category', 'name', 'brand', 'retail_price', 'department', 'sku', 'distribution_center_id']
        self.connection = connection

    def generate_primary_key(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT MAX(id) FROM products")
            max_id = cursor.fetchone()[0]
            cursor.close()
            if max_id is None:
                return 1
            return max_id + 1
        except Exception as e:
            print("Error while generating primary key for products", e)
            return f"Error: {e}"

    def insert_data(self, data):
        try:
            cursor = self.connection.cursor()

            data['id'] = self.generate_primary_key()

            # Convert 'None' strings to Python None and format dates
            for key, value in data.items():
                if value == 'None' or value == '':
                    data[key] = None
                # Add additional formatting as necessary, e.g., for dates

            # Prepare the insert statement
            insert_fields = ', '.join(self.columns)
            placeholders = ', '.join(['%s' for _ in self.columns])
            insert_query = f"INSERT INTO products ({insert_fields}) VALUES ({placeholders})"

            # Extract the values in the order of self.columns
            insert_values = [data.get(col) for col in self.columns]

            # Execute the query
            cursor.execute(insert_query, tuple(insert_values))
            self.connection.commit()
            cursor.close()
            print("Inserted", insert_values)
        except Exception as e:
            print("Error while inserting into products", e)
            return f"Error: {e}"

    def update_data(self, data, id):
        try:
            cursor = self.connection.cursor()
            processed_data = [
                None if data[field] == 'None' else data[field] for field in self.columns if field in data
            ]
            update_fields = ', '.join([f"{field} = %s" for field in self.columns if field in data])
            update_query = f"UPDATE products SET {update_fields} WHERE id = %s"
            cursor.execute(update_query, processed_data + [id])
            self.connection.commit()
            cursor.close()
            print("Updated", processed_data)
        except Exception as e:
            print("Error while updating products", e)
            return f"Error: {e}"

    def delete_data(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM products WHERE id=%s", (id,))
            self.connection.commit()
            cursor.close()
            print("Deleted", id)
        except Exception as e:
            print("Error while deleting from products", e)
            return f"Error: {e}"

    def search(self, data):
        try:
            cursor = self.connection.cursor()
            query_parts = []
            parameters = []
            for column in self.columns:
                value = data.get(column, '') + '%'
                if value == '%':
                    query_parts.append(f"({column} LIKE %s OR {column} IS NULL)")
                else:
                    query_parts.append(f"{column} LIKE %s")
                parameters.append(value)
            query = "SELECT * FROM products WHERE " + " AND ".join(query_parts)
            cursor.execute(query, tuple(parameters))
            results = cursor.fetchall()
            columns = cursor.description # Get the columns
            cursor.close()
            column_types = []
            for column in columns:
                column_name = column[0]
                column_type = column[1]
                mysql_data_type = get_mysql_data_types(column_type)
                item = {'column_name': column_name, 'column_type': mysql_data_type}
                column_types.append(item)
            return results, column_types
        
        except Exception as e:
            print("Could not find any corresponding value", e)
            return False



class Users:
    def __init__(self, connection):
        self.columns = ['id', 'first_name', 'last_name', 'email', 'age', 'gender', 'state', 'street_address', 'postal_code', 'city', 'country', 'latitude', 'longitude', 'traffic_source', 'created_at']
        self.connection = connection

    def generate_primary_key(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT MAX(id) FROM users")
            max_id = cursor.fetchone()[0]
            cursor.close()
            if max_id is None:
                return 1
            return max_id + 1
        except Exception as e:
            print("Error while generating primary key for users", e)
            return f"Error: {e}"

    def insert_data(self, data):
        try:
            cursor = self.connection.cursor()

            data['id'] = self.generate_primary_key()

            # Convert 'None' strings to Python None and format dates
            for key, value in data.items():
                if value == 'None' or value == '':
                    data[key] = None
                # Add additional formatting as necessary, e.g., for dates

            # Prepare the insert statement
            insert_fields = ', '.join(self.columns)
            placeholders = ', '.join(['%s' for _ in self.columns])
            insert_query = f"INSERT INTO users ({insert_fields}) VALUES ({placeholders})"

            # Extract the values in the order of self.columns
            insert_values = [data.get(col) for col in self.columns]

            # Execute the query
            cursor.execute(insert_query, tuple(insert_values))
            self.connection.commit()
            cursor.close()
            print("Inserted", insert_values)
        except Exception as e:
            print("Error while inserting into users", e)
            return f"Error: {e}"

    def update_data(self, data, id):
        try:
            cursor = self.connection.cursor()
            processed_data = [
                None if data[field] == 'None' else data[field] for field in self.columns if field in data
            ]
            update_fields = ', '.join([f"{field} = %s" for field in self.columns if field in data])
            update_query = f"UPDATE users SET {update_fields} WHERE id = %s"
            cursor.execute(update_query, processed_data + [id])
            self.connection.commit()
            cursor.close()
            print("Updated", processed_data)
        except Exception as e:
            print("Error while updating users", e)
            return f"Error: {e}"

    def delete_data(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM users WHERE id=%s", (id,))
            self.connection.commit()
            cursor.close()
            print("Deleted", id)
        except Exception as e:
            print("Error while deleting from users", e)
            return f"Error: {e}"

    def search(self, data):
        try:
            cursor = self.connection.cursor()
            query_parts = []
            parameters = []
            for column in self.columns:
                value = data.get(column, '') + '%'
                if value == '%':
                    query_parts.append(f"({column} LIKE %s OR {column} IS NULL)")
                else:
                    query_parts.append(f"{column} LIKE %s")
                parameters.append(value)
            query = "SELECT * FROM users WHERE " + " AND ".join(query_parts)
            cursor.execute(query, tuple(parameters))
            results = cursor.fetchall()
            columns = cursor.description # Get the columns
            cursor.close()
            column_types = []
            for column in columns:
                column_name = column[0]
                column_type = column[1]
                mysql_data_type = get_mysql_data_types(column_type)
                item = {'column_name': column_name, 'column_type': mysql_data_type}
                column_types.append(item)
            return results, column_types
        
        except Exception as e:
            print("Could not find any corresponding value", e)
            return False


def get_mysql_data_types(column_type):
    mysql_types = {
        246: 'DECIMAL',
        3: 'INT',
        12: 'DATETIME',
        253: 'VARCHAR'
    }
    
    return mysql_types.get(column_type, 'UNKNOWN')

def get_table_data(table_name):
    connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)    
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    columns = cursor.description
    centers = cursor.fetchall()
    cursor.close()
    connection.close()
    column_types = []
    for column in columns: 
        column_name = column[0]
        column_type = column[1]
        mysql_data_type = get_mysql_data_types(column_type)
        item = {'column_name': column_name, 'column_type': mysql_data_type}
        column_types.append(item)
    return centers, column_types 
