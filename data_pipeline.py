import numpy as np 
import pandas as pd 


"""
    This class is used to read the csv files and return the dataframes
    The dataframes are then used to insert the data into the database
"""
class PipeLine():
    def __init__(self, dir = 'tables/'):
        self.dir = dir
        self.get_data()

    def read_csv(self, file_name, dropna=False, datetime_cols=None, replace_comma=True):
        dataset = pd.read_csv(self.dir + file_name)

        if dropna:
            dataset = dataset.dropna()

        if replace_comma:
            dataset = dataset.replace({',': '.'}, regex=True)

        if datetime_cols is not None:
            for col in datetime_cols:
                # Attempt to parse the datetime with a specified format
                try:
                    dataset[col] = pd.to_datetime(dataset[col], format='%d.%m.%Y %H:%M:%S', errors='coerce')
                except ValueError:
                    # Fallback to default parser if the format is incorrect
                    dataset[col] = pd.to_datetime(dataset[col], errors='coerce')

                # Format to MySQL datetime format
                dataset[col] = dataset[col].dt.strftime('%Y-%m-%d %H:%M:%S')
        return dataset
    def get_data(self):
        #datetime_cols_users = ['created_at'] 
        datetime_cols_events = ['created_at']  
        datetime_cols_orders = ['created_at','returned_at','shipped_at','delivered_at'] 
        datetime_cols_order_items = ['created_at','shipped_at','delivered_at','returned_at']
        datetime_cols_inventory_items = ['created_at', 'sold_at']  


        self.users = self.read_csv('thelook_ecommerce - users.csv')
        self.inventory_items = self.read_csv('thelook_ecommerce - inventory_items.csv', datetime_cols=datetime_cols_inventory_items)
        self.distribution_centers = self.read_csv('thelook_ecommerce - distribution_centers.csv')
        self.events = self.read_csv('thelook_ecommerce - events.csv', dropna=True, datetime_cols=datetime_cols_events)
        self.products = self.read_csv('thelook_ecommerce - products.csv')
        self.orders = self.read_csv('thelook_ecommerce - orders.csv',datetime_cols=datetime_cols_orders)
        self.order_items = self.read_csv('thelook_ecommerce - order_items.csv',datetime_cols=datetime_cols_order_items)
