class DistributionCenters:
    def __init__(self, connection):
        self.columns = ['id', 'name', 'latitude', 'longitude']
        self.connection = connection


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

    def insert_data(self, data):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO inventory_items VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
            self.connection.commit()
            cursor.close()
            print("Inserted", data)
        except Exception as e:
            print("Error while inserting into inventory_items", e)
            return f"Error: {e}"

    def update_data(self, data, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE inventory_items SET product_id=%s, created_at=%s, sold_at=%s, cost=%s, product_category=%s, product_name=%s, product_brand=%s, product_retail_price=%s, product_department=%s, product_sku=%s, product_distribution_center_id=%s WHERE id=%s" , (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], id))
            self.connection.commit()
            cursor.close()
            print("Updated", data)
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
            query = "SELECT * FROM inventory_items WHERE id LIKE %s AND product_id LIKE %s AND created_at LIKE %s AND sold_at LIKE %s AND cost LIKE %s AND product_category LIKE %s AND product_name LIKE %s AND product_brand LIKE %s AND product_retail_price LIKE %s AND product_department LIKE %s AND product_sku LIKE %s AND product_distribution_center_id LIKE %s"
            parameters = tuple(data[_] + '%' for _ in range(12))
            cursor.execute(query, parameters)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as e:
            print("Could not find any corresponding value")
            return False

        


class OrderItems:
    def __init__(self, connection):
        self.columns = ['id', 'order_id', 'user_id', 'product_id', 'inventory_item_id', 'status', 'created_at', 'shipped_at', 'delivered_at', 'returned_at', 'sale_price']
        self.connection = connection

    def insert_data(self, data):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO order_items VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
            self.connection.commit()
            cursor.close()
            print("Inserted", data)
        except Exception as e:
            print("Error while inserting into order_items", e)
            return f"Error: {e}"

    def update_data(self, data, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE order_items SET order_id=%s, user_id=%s, product_id=%s, inventory_item_id=%s, status=%s, created_at=%s, shipped_at=%s, delivered_at=%s, returned_at=%s, sale_price=%s WHERE id=%s" , (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], id))
            self.connection.commit()
            cursor.close()
            print("Updated", data)
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
            query = "SELECT * FROM order_items WHERE id LIKE %s AND order_id LIKE %s AND user_id LIKE %s AND product_id LIKE %s AND inventory_item_id LIKE %s AND status LIKE %s AND created_at LIKE %s AND shipped_at LIKE %s AND delivered_at LIKE %s AND returned_at LIKE %s AND sale_price LIKE %s"
            parameters = tuple(data[_] + '%' for _ in range(11))
            cursor.execute(query, parameters)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as e:
            print("Could not find any corresponding value")
            return False




class Orders:
    def __init__(self, connection):
        self.columns = ['order_id', 'user_id', 'status', 'gender', 'created_at', 'returned_at', 'shipped_at', 'delivered_at', 'num_of_item']
        self.connection = connection

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
