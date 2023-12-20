

"""
table name: products

'id', 'cost', 'category', 'name', 'brand', 'retail_price', 'department', 'sku', 'distribution_center_id'

(27569, '92,65256259', 'Swim', "2XU Men's Swimmers Compression Long Sleeve Top", '2XU', '150,4100037', 'Men', 'B23C5765E165D83AA924FA8F13C05F25', 1)
(27445, '24,71966119', 'Swim', "TYR Sport Men's Square Leg Short Swim Suit", 'TYR', '38,99000168', 'Men', '2AB7D3B23574C3DEA2BD278AFD0939AB', 1)
(27457, '15,89760026', 'Swim', "TYR Sport Men's Solid Durafast Jammer Swim Suit", 'TYR', '27,60000038', 'Men', '8F831227B0EB6C6D09A0555531365933', 1)
(27466, '17,85000005', 'Swim', "TYR Sport Men's Swim Short/Resistance Short Swim Suit", 'TYR', '30', 'Men', '67317D6DCC4CB778AEB9219565F5456B', 1)
(27481, '29,40800052', 'Swim', 'TYR Alliance Team Splice Jammer', 'TYR', '45,95000076', 'Men', '213C888198806EF1A0E2BBF2F4855C6C', 1)
(27487, '15,65558991', 'Swim', "TYR Sport Men's 4-Inch Nylon Trainer-A Swim Suit", 'TYR', '26,48999977', 'Men', '978F39314267ADC0E1C50DB2615B467C', 1)
(27510, '22,57175048', 'Swim', "TYR Sport Men's Solid Jammer Swim Suit", 'TYR', '39,95000076', 'Men', '4ECBB790F241666326D31F799EB85D1E', 1)
"""



class Products:
    def __init__(self):
        self.columns = ['id', 'cost', 'category', 'name', 'brand', 'retail_price', 'department', 'sku', 'distribution_center_id']

    def insert_data(self, connection, data):
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO products VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
            connection.commit()
            cursor.close()
            print("Inserted", data)
        except Exception as e:
            print("Error while inserting into products", e)

    def update_data(self, connection, data, id):
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE products SET id=%s, cost=%s, category=%s, name=%s, brand=%s, retail_price=%s, department=%s, sku=%s, distribution_center_id=%s WHERE id=%s", (*data, id))
            connection.commit()
            cursor.close()
            print("Updated", data)
        except Exception as e:
            print("Error while updating products", e)

    def delete_data(self, connection, id):
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM products WHERE id=%s", (id,))
            connection.commit()
            cursor.close()
            print("Deleted", id)
        except Exception as e:
            print("Error while deleting from products", e)

    def search(self, connection, data):
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM products WHERE id={data} OR cost={data} OR category={data} OR name={data} OR brand={data} OR retail_price={data} OR department={data} OR sku={data} OR distribution_center_id={data}")
            products = cursor.fetchall()
            cursor.close()
            return products
        except Exception as e:
            print("Could not found any corresponding value")