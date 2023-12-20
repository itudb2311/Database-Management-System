

"""
table name: order_items

'id', 'order_id', 'user_id', 'product_id', 'inventory_item_id', 'status', 'created_at', 'shipped_at', 'delivered_at', 'returned_at', 'sale_price'

(64359, 44231, 35059, 13606, 173372, 'Shipped', '06.02.2022 22:19:16', '08.02.2022 12:06:00', '', '', '2,5')
(119595, 82306, 65637, 13606, 322704, 'Shipped', '10.01.2022 07:31:46', '12.01.2022 17:20:00', '', '', '2,5')
(126555, 87167, 69525, 13606, 341421, 'Returned', '18.04.2023 14:46:45', '21.04.2023 08:14:00', '21.04.2023 12:22:00', '24.04.2023 12:04:00', '2,5')
(180500, 124452, 99274, 28951, 486768, 'Shipped', '11.08.2023 05:38:40', '11.08.2023 10:54:00', '', '', '3')
(34799, 23912, 18858, 28951, 93988, 'Complete', '05.07.2022 01:08:20', '06.07.2022 01:03:00', '06.07.2022 16:11:00', '', '3')
(118879, 81823, 65238, 28951, 320760, 'Complete', '21.07.2023 05:44:24', '21.07.2023 12:36:00', '24.07.2023 15:07:00', '', '3')
"""



class OrderItems:
    def __init__(self, connection):
        self.columns = ['id', 'order_id', 'user_id', 'product_id', 'inventory_item_id', 'status', 'created_at', 'shipped_at', 'delivered_at', 'returned_at', 'sale_price']

    def insert_data(self, connection, data):
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO order_items VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
            connection.commit()
            cursor.close()
            print("Inserted", data)
        except Exception as e:
            print("Error while inserting into order_items", e)

    def update_data(self, connection, data, id):
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE order_items SET order_id=%s, user_id=%s, product_id=%s, inventory_item_id=%s, status=%s, created_at=%s, shipped_at=%s, delivered_at=%s, returned_at=%s, sale_price=%s WHERE id=%s" , (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], id))
            connection.commit()
            cursor.close()
            print("Updated", data)
        except Exception as e:
            print("Error while updating order_items", e)

    def delete_data(self, connection, id):
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM order_items WHERE id=%s", (id,))
            connection.commit()
            cursor.close()
            print("Deleted", id)
        except Exception as e:
            print("Error while deleting from order_items", e)

    def search(self, connection, data):
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM distribution_centers WHERE id={data} OR order_id={data} OR user_id={data} OR product_id={data} OR inventory_item_id={data} OR status={data} OR created_at={data} OR shipped_at={data} OR delivered_at={data} OR returned_at={data} OR sale_price={data}")
            centers = cursor.fetchall()
            cursor.close()
            return centers
        except Exception as e:
            print("Could not found any corresponding value")
            return "Could not found any corresponding value"