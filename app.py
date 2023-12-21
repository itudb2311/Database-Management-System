from flask import Flask, render_template, request
from settings import db_user,db_password,db_host,db_name  
import mysql.connector
from utils.table_operations import DistributionCenters


app = Flask(__name__)
connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)    

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
    for column in columns: # Sütunların tiplerini yazdırıyor
        column_name = column[0]
        column_type = column[1]
        mysql_data_type = get_mysql_data_types(column_type)
        print(f"{column_name}, {mysql_data_type}")
    return centers
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/distribution_centers')
def distribution_centers():
    centers = get_table_data('distribution_centers')
    return render_template('distribution_centers.html', centers=centers)

@app.route('/users')
def users():
    centers = get_table_data('users')
    return render_template('users.html', centers=centers)

@app.route('/events')
def events():
    centers = get_table_data('events')
    return render_template('events.html', centers=centers)

@app.route('/inventory_items')
def inventory_items():
    centers = get_table_data('inventory_items')
    return render_template('inventory_items.html', centers=centers)

@app.route('/products')
def products():
    centers = get_table_data('products')
    return render_template('products.html', centers=centers)

@app.route('/orders')
def orders():
    centers = get_table_data('orders')
    return render_template('orders.html', centers=centers)

@app.route('/order_items')
def order_items():
    centers = get_table_data('order_items')
    return render_template('order_items.html', centers=centers)

@app.route('/search', methods=['POST'])
def search():
    table_name = request.form['table_name']

    inputs = [request.form.get(f'input{i}', '').strip() for i in range(1, 30)]

    print(inputs)
    tables = {"distribution_centers": DistributionCenters(connection=connection),
              }
    table = tables[table_name]

    results = table.search(inputs)
    print(results)
    if not results:
        results = [['No Data Found!']]

    return render_template(f'{table_name}.html', centers=results)

if __name__ == '__main__':
    app.run(debug=True)