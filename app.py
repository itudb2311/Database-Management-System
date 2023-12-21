from flask import Flask, render_template, request
from settings import db_user,db_password,db_host,db_name  
import mysql.connector
from utils.table_operations import *

app = Flask(__name__)
connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)    

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
    results = [results]
    return render_template(f'{table_name}.html', centers=results)
                                        
if __name__ == '__main__':
    app.run(debug=True)