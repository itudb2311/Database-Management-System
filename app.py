from flask import Flask, render_template
from settings import db_user,db_password,db_host,db_name  
import mysql.connector


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')



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

if __name__ == '__main__':
    app.run(debug=True)