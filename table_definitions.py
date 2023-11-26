create_inventory_items_table = """
CREATE TABLE IF NOT EXISTS inventory_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    created_at DATETIME,
    sold_at DATETIME,
    cost DECIMAL(10, 2),
    product_category VARCHAR(255),
    product_name VARCHAR(255),
    product_brand VARCHAR(255),
    product_retail_price DECIMAL(10, 2),
    product_department VARCHAR(255),
    product_sku VARCHAR(255),
    product_distribution_center_id INT,
    FOREIGN KEY (product_id) REFERENCES products(id)
)
"""

create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        email VARCHAR(255),
        age INT,
        gender VARCHAR(50),
        state VARCHAR(255),
        street_address VARCHAR(255),
        postal_code VARCHAR(255),
        city VARCHAR(255),
        country VARCHAR(255),
        latitude DECIMAL(10, 8)
        longitude DECIMAL(11, 8),
        traffic_source VARCHAR(255),
        created_at DATETIME
    )
    """


create_distribution_centers_table = """
CREATE TABLE IF NOT EXISTS distribution_centers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    postal_code VARCHAR(255),
    country VARCHAR(255),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8)
)
"""








