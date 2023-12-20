

"""
table name: events

'id', 'user_id', 'sequence_number', 'session_id', 'created_at', 'ip_address', 'city', 'state', 'postal_code', 'browser', 'traffic_source', 'uri', 'event_type'

(1437378, '', 3, '1fa8f43a-da87-426d-bacf-cc33d17049bb', '03.08.2020 00:31:00', '92.208.191.197', 'Bogatynia', 'Dolnoslaskie', 59, 'Chrome', 'YouTube', '/cart', 'cart')
(1511836, '', 2, 'c3657070-848b-4c15-a07b-1041e23e96c1', '22.09.2022 12:40:00', '203.170.182.131', 'Bogatynia', 'Dolnoslaskie', 59, 'Safari', 'Organic', '/cart', 'cart')
(160346, '11997', 3, '8d15c1e1-0a90-4ca4-bea6-8ba4480e8d30', '04.01.2023 12:46:25', '128.63.210.181', 'Bogatynia', 'Dolnoslaskie', 59, 'Chrome', 'Organic', '/cart', 'cart')
(1156916, '88696', 6, '6db2513c-6fc7-40ac-b338-a0e6fbc53f5c', '23.09.2023 02:11:59', '186.76.72.140', 'Bogatynia', 'Dolnoslaskie', 59, 'Safari', 'Email', '/cart', 'cart')
(1438095, '', 3, '55148874-96da-4573-97cb-18313f88d717', '22.07.2023 03:05:00', '36.20.249.25', 'Bogatynia', 'Dolnoslaskie', 59, 'Safari', 'Email', '/cart', 'cart')
(1774602, '', 3, '56dd7b67-ee23-407d-b93d-a8cd59bdd3cf', '22.06.2021 08:45:00', '76.234.17.165', 'Bogatynia', 'Dolnoslaskie', 59, 'Firefox', 'Email', '/cart', 'cart')
(12653, '872', 6, 'fb08ef1e-5bd1-4988-9eff-b4da7ad0c6c5', '03.11.2020 00:04:20', '223.114.184.120', 'Bogatynia', 'Dolnoslaskie', 59, 'Chrome', 'Email', '/cart', 'cart')
"""



class Events:
    def __init__(self, connection):
        self.columns = ['id', 'user_id', 'sequence_number', 'session_id', 'created_at', 'ip_address', 'city', 'state', 'postal_code', 'browser', 'traffic_source', 'uri', 'event_type']

    def insert_data(self, connection, data):
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO events VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)
            connection.commit()
            cursor.close()
            print("Inserted", data)
        except Exception as e:
            print("Error while inserting into events", e)

    def update_data(self, connection, data, id):
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE events SET user_id=%s, sequence_number=%s, session_id=%s, created_at=%s, ip_address=%s, city=%s, state=%s, postal_code=%s, browser=%s, traffic_source=%s, uri=%s, event_type=%s WHERE id=%s" , (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], id))
            connection.commit()
            cursor.close()
            print("Updated", data)
        except Exception as e:
            print("Error while updating events", e)

    def delete_data(self, connection, id):
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM events WHERE id=%s", (id,))
            connection.commit()
            cursor.close()
            print("Deleted", id)
        except Exception as e:
            print("Error while deleting from events", e)

    def search(self, connection, data):
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM distribution_centers WHERE id={data} OR user_id={data} OR sequence_number={data} OR session_id={data} OR created_at={data} OR ip_address={data} OR city={data} OR state={data} OR postal_code={data} OR browser={data} OR traffic_source={data} OR uri={data} OR event_type={data}")
            centers = cursor.fetchall()
            cursor.close()
            return centers
        except Exception as e:
            print("Could not find any corresponding value")
            return "Could not find any corresponding value"
        