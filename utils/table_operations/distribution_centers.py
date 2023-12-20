

"""
table name: distribution_centers

'id', 'name', 'latitude', 'longitude'

(1, 'Memphis TN', '35,1174', '-89,9711')
(2, 'Chicago IL', '41,8369', '-87,6847')
(3, 'Houston TX', '29,7604', '-95,3698')
"""



class DistributionCenters:
    def __init__(self, connection):
        self.columns = ['id', 'name', 'latitude', 'longitude']
        self.max_id = self.get_max_id(connection)

    def get_max_id(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT MAX(id) FROM distribution_centers")
            max_id = cursor.fetchone()[0]
            cursor.close()
            return max_id
        except Exception as e:
            print("Error while getting max id from distribution_centers", e)
            return 0

    def insert_data(self, connection, data):
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO distribution_centers VALUES (%s,%s,%s,%s)", (self.max_id+1, data[0], data[1], data[2]))
            connection.commit()
            cursor.close()
            print("Inserted", data)
        except Exception as e:
            print("Error while inserting into distribution_centers", e)

    def update_data(self, connection, data, id):
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE distribution_centers SET name=%s, latitude=%s, longitude=%s WHERE id=%s" , (data[0], data[1], data[2], id))
            connection.commit()
            cursor.close()
            print("Updated", data)
        except Exception as e:
            print("Error while updating distribution_centers", e)

    def delete_data(self, connection, id):
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM distribution_centers WHERE id=%s", (id,))
            connection.commit()
            cursor.close()
            print("Deleted", id)
        except Exception as e:
            print("Error while deleting from distribution_centers", e)

    def search(self, connection, data):
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM distribution_centers WHERE id={data} OR name={data} OR latitude={data} OR longitude={data}")
            centers = cursor.fetchall()
            cursor.close()
            return centers
        except Exception as e:
            print("Could not found any corresponding value")
            return "Could not found any corresponding value"
