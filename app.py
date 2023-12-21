from flask import Flask, render_template
from settings import db_user,db_password,db_host,db_name  
import mysql.connector


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

def get_distribution_centers():
    connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM distribution_centers")
    centers = cursor.fetchall()
    cursor.close()
    connection.close()
    return centers

@app.route('/distribution-centers')
def distribution_centers():
    centers = get_distribution_centers()
    return render_template('distribution_centers.html', centers=centers)

def get_users():
    connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    centers = cursor.fetchall()
    cursor.close()
    connection.close()
    return centers


@app.route('/users')
def users():
    centers = get_users()
    return render_template('users.html', centers=centers)

def get_events():
    connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events")
    centers = cursor.fetchall()
    cursor.close()
    connection.close()
    return centers


@app.route('/events')
def events():
    centers = get_events()
    return render_template('events.html', centers=centers)

def get_inventory_items():
    connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM inventory_items")
    centers = cursor.fetchall()
    cursor.close()
    connection.close()
    return centers


@app.route('/inventory_items')
def inventory_items():
    centers = get_inventory_items()
    return render_template('inventory_items.html', centers=centers)

def get_products():
    connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    centers = cursor.fetchall()
    cursor.close()
    connection.close()
    return centers


@app.route('/products')
def products():
    centers = get_products()
    return render_template('products.html', centers=centers)

def get_orders():
    connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orders")
    centers = cursor.fetchall()
    cursor.close()
    connection.close()
    return centers


@app.route('/orders')
def orders():
    centers = get_orders()
    return render_template('orders.html', centers=centers)

def get_order_items():
    connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM order_items")
    centers = cursor.fetchall()
    cursor.close()
    connection.close()
    return centers


@app.route('/order_items')
def order_items():
    centers = get_order_items()
    return render_template('order_items.html', centers=centers)

if __name__ == '__main__':
    app.run(debug=True)