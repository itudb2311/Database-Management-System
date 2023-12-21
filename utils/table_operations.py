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
            cursor.execute(f"SELECT * FROM distribution_centers WHERE LIKE id='%{data}%' OR name='%{data}%' OR latitude='%{data}%' OR longitude='%{data}%'")
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
            cursor.execute(f"SELECT * FROM distribution_centers WHERE id={data} OR user_id={data} OR sequence_number={data} OR session_id={data} OR created_at={data} OR ip_address={data} OR city={data} OR state={data} OR postal_code={data} OR browser={data} OR traffic_source={data} OR uri={data} OR event_type={data}")
            centers = cursor.fetchall()
            cursor.close()
            return centers
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
            cursor.execute(f"SELECT * FROM distribution_centers WHERE id={data} OR product_id={data} OR created_at={data} OR sold_at={data} OR cost={data} OR product_category={data} OR product_name={data} OR product_brand={data} OR product_retail_price={data} OR product_department={data} OR product_sku={data} OR product_distribution_center_id={data}")
            centers = cursor.fetchall()
            cursor.close()
            return centers
        except Exception as e:
            print("Could not found any corresponding value")
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
            cursor.execute(f"SELECT * FROM distribution_centers WHERE id={data} OR order_id={data} OR user_id={data} OR product_id={data} OR inventory_item_id={data} OR status={data} OR created_at={data} OR shipped_at={data} OR delivered_at={data} OR returned_at={data} OR sale_price={data}")
            centers = cursor.fetchall()
            cursor.close()
            return centers
        except Exception as e:
            print("Could not found any corresponding value")
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
            cursor.execute(f"SELECT * FROM orders WHERE order_id={data} OR user_id={data} OR status={data} OR gender={data} OR created_at={data} OR returned_at={data} OR shipped_at={data} OR delivered_at={data} OR num_of_item={data}")
            orders = cursor.fetchall()
            cursor.close()
            return orders
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

    def search(self, data):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM products WHERE id={data} OR cost={data} OR category={data} OR name={data} OR brand={data} OR retail_price={data} OR department={data} OR sku={data} OR distribution_center_id={data}")
            products = cursor.fetchall()
            cursor.close()
            return products
        except Exception as e:
            print("Could not found any corresponding value")
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
            cursor.execute("SELECT * FROM users WHERE id=%s OR first_name=%s OR last_name=%s OR email=%s OR age=%s OR gender=%s OR state=%s OR street_address=%s OR postal_code=%s OR city=%s OR country=%s OR latitude=%s OR longitude=%s OR traffic_source=%s OR created_at=%s", (data, data, data, data, data, data, data, data, data, data, data, data, data, data, data))
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print("Could not find any corresponding value")
            return False
