import sqlite3

# Function to create the table if it doesn't exist
def create_table():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, price REAL)''')
    conn.commit()
    conn.close()

# Function to add a new product to the database
def add_product(name, quantity, price):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''INSERT INTO products (name, quantity, price)
                 VALUES (?, ?, ?)''', (name, quantity, price))
    conn.commit()
    conn.close()

    # Function to retrieve all products from the database
def get_products():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM products''')
    products = c.fetchall()
    conn.close()
    return products

# Function to retrieve a single product by ID from the database
def get_product_by_id(product_id):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM products WHERE id = ?''', (product_id,))
    product = c.fetchone()
    conn.close()
    return product

# Function to update a product in the database
def update_product(product_id, name, quantity, price):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''UPDATE products SET name=?, quantity=?, price=? WHERE id=?''', (name, quantity, price, product_id))
    conn.commit()
    conn.close()

# Function to delete a product from the database
def delete_product(product_id):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''DELETE FROM products WHERE id = ?''', (product_id,))
    conn.commit()
    conn.close()
