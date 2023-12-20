

"""
table name: orders

'order_id', 'user_id', 'status', 'gender', 'created_at', 'returned_at', 'shipped_at', 'delivered_at', 'num_of_item'

(1, 1, 'Shipped', 'F', '20.10.2023 18:23:21', '', '22.10.2023 04:43:21', '', 1)
(2, 2, 'Shipped', 'F', '22.08.2023 12:22:00', '', '24.08.2023 06:59:00', '', 2)
(3, 3, 'Shipped', 'F', '21.10.2023 06:05:21', '', '23.10.2023 16:16:21', '', 1)
(7, 5, 'Shipped', 'F', '29.07.2022 05:26:00', '', '29.07.2022 07:52:00', '', 1)
(9, 6, 'Shipped', 'F', '13.09.2023 09:19:00', '', '16.09.2023 00:03:00', '', 1)
(14, 9, 'Shipped', 'F', '03.07.2023 02:10:00', '', '04.07.2023 07:28:00', '', 1)
(22, 13, 'Shipped', 'F', '02.07.2022 07:08:00', '', '02.07.2022 18:38:00', '', 1)
"""



class Orders:
    def __init__(self):
        self.columns = ['order_id', 'user_id', 'status', 'gender', 'created_at', 'returned_at', 'shipped_at', 'delivered_at', 'num_of_item']

    def insert_data(self, connection, data):
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO orders VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
            connection.commit()
            cursor.close()
            print("Inserted", data)
        except Exception as e:
            print("Error while inserting into orders", e)

    def update_data(self, connection, data, id):
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE orders SET order_id = %s, user_id = %s, status = %s, gender = %s, created_at = %s, returned_at = %s, shipped_at = %s, delivered_at = %s, num_of_item = %s WHERE order_id = %s", (*data, id))
            connection.commit()
            cursor.close()
            print("Updated data for order_id:", id)
        except Exception as e:
            print("Error while updating data for order_id:", id, e)

    def delete_data(self, connection, id):
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM orders WHERE order_id = %s", (id,))
            connection.commit()
            cursor.close()
            print("Deleted order_id:", id)
        except Exception as e:
            print("Error while deleting from orders", e)

    def search(self, connection, data):
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM orders WHERE order_id={data} OR user_id={data} OR status={data} OR gender={data} OR created_at={data} OR returned_at={data} OR shipped_at={data} OR delivered_at={data} OR num_of_item={data}")
            orders = cursor.fetchall()
            cursor.close()
            return orders
        except Exception as e:
            print("Could not find any corresponding value")
            return "Could not find any corresponding value"

            
