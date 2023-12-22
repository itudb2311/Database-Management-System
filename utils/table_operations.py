from settings import db_user,db_password,db_host,db_name  
import mysql.connector

class DistributionCenters:
    def __init__(self, connection):
        self.columns = ['id', 'name', 'latitude', 'longitude']
        self.connection = connection

    def generate_primary_key(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT MAX(id) FROM distribution_centers")
            max_id = cursor.fetchone()[0]
            cursor.close()
            if max_id is None:
                return 1
            return max_id + 1
        except Exception as e:
            print("Error while generating primary key for distribution_centers", e)
            return f"Error: {e}"
        
    def insert_data(self, data):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO distribution_centers VALUES (%s,%s,%s,%s)", (data[0], data[1], data[2], data[3]))
            self.connection.commit()
            cursor.close()
            print("Inserted", data)
        except Exception as e:
            print("Error while inserting into distribution_centers", e)
            return f"Error: {e}"

    def update_data(self,data, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE distribution_centers SET name=%s, latitude=%s, longitude=%s WHERE id=%s" , (data[0], data[1], data[2], id))
            self.connection.commit()
            cursor.close()
            print("Updated", data)
        except Exception as e:
            print("Error while updating distribution_centers", e)
            return f"Error: {e}"

    def delete_data(self, id):
        try:
            cursor = self.connection.cursor()
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
            query = "SELECT * FROM distribution_centers WHERE id LIKE %s AND name LIKE %s AND latitude LIKE %s AND longitude LIKE %s"
            parameters = (data[0] + '%', data[1] + '%', data[2] + '%', data[3] + '%')
            cursor.execute(query, parameters)
            centers = cursor.fetchall()
            cursor.close()
            return centers
        except Exception as e:
            print("Could not found any corresponding value")
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
            cursor.execute("INSERT INTO events VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
            self.connection.commit()
            cursor.close()
            print("Inserted", data)
        except Exception as e:
            print("Error while inserting into events", e)
            return f"Error: {e}"

    def update_data(self, data, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE events SET user_id=%s, sequence_number=%s, session_id=%s, created_at=%s, ip_address=%s, city=%s, state=%s, postal_code=%s, browser=%s, traffic_source=%s, uri=%s, event_type=%s WHERE id=%s" , (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], id))
            self.connection.commit()
            cursor.close()
            print("Updated", data)
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
            query = "SELECT * FROM events WHERE id LIKE %s AND user_id LIKE %s AND sequence_number LIKE %s AND session_id LIKE %s AND created_at LIKE %s AND ip_address LIKE %s AND city LIKE %s AND state LIKE %s AND postal_code LIKE %s AND browser LIKE %s AND traffic_source LIKE %s AND uri LIKE %s AND event_type LIKE %s"
            parameters = tuple(data[_] + '%' for _ in range(13))
            cursor.execute(query, parameters)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as e:
            print("Could not find any corresponding value")
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
            cursor.close()
            columns = cursor.description
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
            cursor.close()
            columns = cursor.description
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
            cursor.execute("INSERT INTO orders VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
            self.connection.commit()
            cursor.close()
            print("Inserted", data)
        except Exception as e:
            print("Error while inserting into orders", e)
            return f"Error: {e}"

    def update_data(self, data, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE orders SET order_id = %s, user_id = %s, status = %s, gender = %s, created_at = %s, returned_at = %s, shipped_at = %s, delivered_at = %s, num_of_item = %s WHERE order_id = %s", (*data, id))
            self.connection.commit()
            cursor.close()
            print("Updated data for order_id:", id)
        except Exception as e:
            print("Error while updating data for order_id:", id, e)
            return f"Error: {e}"

    def delete_data(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM orders WHERE order_id = %s", (id,))
            self.connection.commit()
            cursor.close()
            print("Deleted order_id:", id)
        except Exception as e:
            print("Error while deleting from orders", e)
            return f"Error: {e}"

    def search(self, data):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM orders WHERE order_id LIKE %s AND user_id LIKE %s AND status LIKE %s AND gender LIKE %s AND created_at LIKE %s AND returned_at LIKE %s AND shipped_at LIKE %s AND delivered_at LIKE %s AND num_of_item LIKE %s"
            parameters = tuple(data[_] + '%' for _ in range(9))
            cursor.execute(query, parameters)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as e:
            print("Could not find any corresponding value")
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
            cursor.execute("INSERT INTO products VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
            self.connection.commit()
            cursor.close()
            print("Inserted", data)
        except Exception as e:
            print("Error while inserting into products", e)
            return f"Error: {e}"

    def update_data(self, data, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE products SET id=%s, cost=%s, category=%s, name=%s, brand=%s, retail_price=%s, department=%s, sku=%s, distribution_center_id=%s WHERE id=%s", (*data, id))
            self.connection.commit()
            cursor.close()
            print("Updated", data)
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

    def search_products(self, data):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM products WHERE id LIKE %s AND cost LIKE %s AND category LIKE %s AND name LIKE %s AND brand LIKE %s AND retail_price LIKE %s AND department LIKE %s AND sku LIKE %s AND distribution_center_id LIKE %s"
            parameters = tuple(data[_] + '%' for _ in range(9))
            cursor.execute(query, parameters)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as e:
            print("Could not find any corresponding value")
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
            cursor.execute("INSERT INTO users VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
            self.connection.commit()
            cursor.close()
            print("Inserted", data)
        except Exception as e:
            print("Error while inserting into users", e)
            return f"Error: {e}"

    def update_data(self, data, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE users SET first_name = %s, last_name = %s, email = %s, age = %s, gender = %s, state = %s, street_address = %s, postal_code = %s, city = %s, country = %s, latitude = %s, longitude = %s, traffic_source = %s, created_at = %s WHERE id = %s", data + (id,))
            self.connection.commit()
            cursor.close()
            print("Updated data for id:", id)
        except Exception as e:
            print("Error while updating data for id:", id, e)
            return f"Error: {e}"

    def delete_data(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (id,))
            self.connection.commit()
            cursor.close()
            print("Deleted data for id:", id)
        except Exception as e:
            print("Error while deleting data for id:", id, e)
            return f"Error: {e}"

    def search(self, data):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM users WHERE id LIKE %s AND first_name LIKE %s AND last_name LIKE %s AND email LIKE %s AND age LIKE %s AND gender LIKE %s AND state LIKE %s AND street_address LIKE %s AND postal_code LIKE %s AND city LIKE %s AND country LIKE %s AND latitude LIKE %s AND longitude LIKE %s AND traffic_source LIKE %s AND created_at LIKE %s"
            parameters = tuple(data[_] + '%' for _ in range(15))
            cursor.execute(query, parameters)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as e:
            print("Could not find any corresponding value")
            return False


def get_mysql_data_types(column_type):
    # MySQL veri tipleri için eşleştirmeleri tanımla
    mysql_types = {
        246: 'DECIMAL',
        3: 'INT',
        12: 'DATETIME',
        253: 'VARCHAR'
        # Diğer veri tipleri için gerekli eşleştirmeleri ekle
    }
    
    # Veri tipini döndür
    return mysql_types.get(column_type, 'UNKNOWN')

def get_table_data(table_name):
    connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)    
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    columns = cursor.description  # Sütunların adları ve tipleri
    centers = cursor.fetchall()
    cursor.close()
    connection.close()
    column_types = []
    for column in columns: # Sütunların tiplerini yazdırıyor
        column_name = column[0]
        column_type = column[1]
        mysql_data_type = get_mysql_data_types(column_type)
        item = {'column_name': column_name, 'column_type': mysql_data_type}
        column_types.append(item)
    return centers, column_types
