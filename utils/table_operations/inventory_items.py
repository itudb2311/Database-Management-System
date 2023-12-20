

"""
table name: inventory_items

'id', 'product_id', 'created_at', 'sold_at', 'cost', 'product_category', 'product_name', 'product_brand', 'product_retail_price', 'product_department', 'product_sku', 'product_distribution_center_id'

(29853, 16898, '12.03.2023 05:29:50', '26.04.2023 03:49:50', '13,92499997', 'Tops & Tees', "Quiksilver Waterman Men's On The Rise", '', 25, 'Men', '22811EE19846217512507785E74D12CC', 3)
(29854, 16898, '14.04.2023 15:55:00', '', '13,92499997', 'Tops & Tees', "Quiksilver Waterman Men's On The Rise", '', 25, 'Men', '22811EE19846217512507785E74D12CC', 3)
(140712, 16898, '18.07.2023 02:18:19', '18.08.2023 23:46:19', '13,92499997', 'Tops & Tees', "Quiksilver Waterman Men's On The Rise", '', 25, 'Men', '22811EE19846217512507785E74D12CC', 3)
(140713, 16898, '27.01.2022 16:40:00', '', '13,92499997', 'Tops & Tees', "Quiksilver Waterman Men's On The Rise", '', 25, 'Men', '22811EE19846217512507785E74D12CC', 3)
(140714, 16898, '04.05.2020 07:20:00', '', '13,92499997', 'Tops & Tees', "Quiksilver Waterman Men's On The Rise", '', 25, 'Men', '22811EE19846217512507785E74D12CC', 3)
"""



class InventoryItems:
    def __init__(self, connection):
        self.columns = ['id', 'product_id', 'created_at', 'sold_at', 'cost', 'product_category', 'product_name', 'product_brand', 'product_retail_price', 'product_department', 'product_sku', 'product_distribution_center_id']

    def insert_data(self, connection, data):
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO inventory_items VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
            connection.commit()
            cursor.close()
            print("Inserted", data)
        except Exception as e:
            print("Error while inserting into inventory_items", e)

    def update_data(self, connection, data, id):
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE inventory_items SET product_id=%s, created_at=%s, sold_at=%s, cost=%s, product_category=%s, product_name=%s, product_brand=%s, product_retail_price=%s, product_department=%s, product_sku=%s, product_distribution_center_id=%s WHERE id=%s" , (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], id))
            connection.commit()
            cursor.close()
            print("Updated", data)
        except Exception as e:
            print("Error while updating inventory_items", e)

    def delete_data(self, connection, id):
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM inventory_items WHERE id=%s", (id,))
            connection.commit()
            cursor.close()
            print("Deleted", id)
        except Exception as e:
            print("Error while deleting from inventory_items", e)

    def search(self, connection, data):
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM distribution_centers WHERE id={data} OR product_id={data} OR created_at={data} OR sold_at={data} OR cost={data} OR product_category={data} OR product_name={data} OR product_brand={data} OR product_retail_price={data} OR product_department={data} OR product_sku={data} OR product_distribution_center_id={data}")
            centers = cursor.fetchall()
            cursor.close()
            return centers
        except Exception as e:
            print("Could not found any corresponding value")
            return "Could not found any corresponding value"