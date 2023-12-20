import random
import pandas as pd
# Read the CSV file
df = pd.read_csv('tables/thelook_ecommerce - orders.csv')

# Get the 'user_id' column
user_id_list = df['order_id'].tolist()

output = []
for i in range(500):
    random_element = random.choice(user_id_list)
    output.append(random_element)

df_events = pd.read_csv('tables/thelook_ecommerce - order_items.csv')
# Replace the column in the DataFrame
df_events['order_id'] = output 

# Save the modified DataFrame back to the CSV file
df_events.to_csv('tables/thelook_ecommerce - order_items.csv', index=False)











