from flask import Flask, render_template, request, redirect, json
from settings import db_user,db_password,db_host,db_name  
import mysql.connector
from utils.table_operations import *

app = Flask(__name__)
connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)    
tables = {"distribution_centers": DistributionCenters(connection=connection),
              "events": Events(connection=connection),
              "inventory_items": InventoryItems(connection=connection),
              "order_items":OrderItems(connection=connection),
              "orders":Orders(connection=connection),
              "products":Products(connection=connection),
              "users":Users(connection=connection)}

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
    print("searched",request.form.get)
    inputs = [request.form.get(f'input{i}', '').strip() for i in range(1, 30)]
    print("inputs",inputs)
    table = tables[table_name]
    
    form_data = request.form.to_dict()
    results = table.search(form_data)

    if not results:
        results = [['No Data Found!']]
    print(results)
    return render_template(f'{table_name}.html', centers=[results])

@app.route('/delete', methods=['POST'])
def delete():
    data = request.form
    table_name = data['table_name']
    items_to_delete = json.loads(data['data'])
    handler = tables[table_name]
    for item in items_to_delete:
        handler.delete_data(item["id"])

    results = get_table_data(table_name)

    if not results:
        results = [['No Data Found!']]

    return render_template(f'{table_name}.html', centers=results)

@app.route('/update', methods=['POST'])
def update():
    data = request.form
    table_name = data['table_name']
    id = data['id']
    tables[table_name].update_data(data,id)
    results = get_table_data(table_name)
    
    if not results:
        results = [['No Data Found!']]

    return render_template(f'{table_name}.html', centers=results)

if __name__ == '__main__':
    app.run(debug=True)