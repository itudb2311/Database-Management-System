from flask import Flask, render_template, request, redirect, jsonify, json, session
from settings import db_user,db_password,db_host,db_name  
import mysql.connector
from utils.table_operations import *

app = Flask(__name__)
app.secret_key = 'a_secret_key_that_is_super_hard_to_find_i_believe..//!?=)'

connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)    
tables = {"distribution_centers": DistributionCenters(connection=connection),
              "events": Events(connection=connection),
              "inventory_items": InventoryItems(connection=connection),
              "order_items":OrderItems(connection=connection),
              "orders":Orders(connection=connection),
              "products":Products(connection=connection),
              "users":Users(connection=connection)}

@app.route('/login', methods=['GET', 'POST'])
def login():
    admin_table = Admins(connection=connection)  # Initialize with the connection
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']

        if admin_table.check_admin(username, password):
            session['logged_in'] = True  # Set session variable
            return redirect('/')
        else:
            # Handle login failure
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')

@app.route('/')
def index():
    if not session.get('logged_in'):    # If user is not logged in, redirect to login page
        return redirect('/login')       # Otherwise, show the index page
    return render_template('index.html')    # If user is logged in, show the index page

@app.route('/about')                    # If user is logged in, show the about page 
def about():                            # Otherwise, redirect to login page
    if not session.get('logged_in'):    # If user is not logged in, redirect to login page
        return redirect('/login')       
    return render_template('about.html')# If user is logged in, show the about page

@app.route('/distribution_centers')
def distribution_centers():
    if not session.get('logged_in'):    
        return redirect('/login')
    centers = get_table_data('distribution_centers')                        # Get distribution centers data from the database
    return render_template('distribution_centers.html', centers=centers)    # Pass the data to the template

@app.route('/users')
def users():
    if not session.get('logged_in'):
        return redirect('/login')
    centers = get_table_data('users')                       # Get users data from the database
    return render_template('users.html', centers=centers)   # Pass the data to the template

@app.route('/events')
def events():
    if not session.get('logged_in'):
        return redirect('/login')
    centers = get_table_data('events')                      # Get events data from the database
    return render_template('events.html', centers=centers)  # Pass the data to the template

@app.route('/inventory_items')
def inventory_items():
    if not session.get('logged_in'):
        return redirect('/login')
    centers = get_table_data('inventory_items')                     # Get inventory items data from the database
    return render_template('inventory_items.html', centers=centers) # Pass the data to the template

@app.route('/products')
def products():
    if not session.get('logged_in'):
        return redirect('/login')
    centers = get_table_data('products')                        # Get products data from the database
    return render_template('products.html', centers=centers)    # Pass the data to the template    

@app.route('/orders')
def orders():
    if not session.get('logged_in'):
        return redirect('/login')
    centers = get_table_data('orders')                          # Get orders data from the database
    return render_template('orders.html', centers=centers)      # Pass the data to the template

@app.route('/order_items')
def order_items():
    if not session.get('logged_in'):
        return redirect('/login')
    centers = get_table_data('order_items')                     # Get order items data from the database
    return render_template('order_items.html', centers=centers) # Pass the data to the template


@app.route('/search', methods=['POST'])
def search():
    if not session.get('logged_in'):
        return redirect('/login')
    table_name = request.form['table_name'] # Get the table name from the form data
    table = tables[table_name]              # Get the table handler from the dictionary
    form_data = request.form.to_dict()      # Convert the form data to a dictionary
    results = table.search(form_data)       # Searching operation call with the form data
    if not results:                         # If no results found, show a message
        results = [['No Data Found!']]      
    return render_template(f'{table_name}.html', centers=results)   # Pass the data to the template

@app.route('/delete', methods=['POST'])
def delete():
    if not session.get('logged_in'):
        return redirect('/login')
    data = request.form                         # Get the form data
    table_name = data['table_name']             # Get the table name from the form data
    items_to_delete = json.loads(data['data'])  # Get the items to delete from the form data
    handler = tables[table_name]                # Get the table handler from the dictionary
    for item in items_to_delete:                # Iterate over the items to delete
        handler.delete_data(item["id"])         # Delete the item from the database

    results = get_table_data(table_name)        # Get the updated data from the database

    if not results:
        results = [['No Data Found!']]

    return render_template(f'{table_name}.html', centers=results)   # Pass the data to the template

@app.route('/update', methods=['POST'])
def update():
    if not session.get('logged_in'):
        return redirect('/login')
    data = request.form                 # Get the form data
    table_name = data['table_name']     # Get the table name from the form data
    if table_name == 'orders':           # If the table is users, hash the password
        id = data['order_id']                 # Get the id from the form data
    else:
        id = data['id']                     
    tables[table_name].update_data(data,id) # Update the data in the database
    results = get_table_data(table_name)    # Get the updated data from the database
    if not results:
        results = [['No Data Found!']]

    return render_template(f'{table_name}.html', centers=results)       # Pass the data to the template


@app.route('/insert', methods=['POST'])
def insert():
    if not session.get('logged_in'):
        return redirect('/login')
    data = request.form.to_dict()               # Get the form data
    table_name = request.form['table_name']     # Get the table name from the form data
    tables[table_name].insert_data(data)        # Insert the data into the database
    results = get_table_data(table_name)        # Get the updated data from the database
    if not results:     
        return jsonify({"success": False}), 500

    return render_template(f'{table_name}.html', centers=results)  # Pass the data to the template

@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Remove the logged_in session variable
    return redirect('/login')       # Redirect to login page

if __name__ == '__main__':
    app.run(debug=True)             # Run the app in debug mode