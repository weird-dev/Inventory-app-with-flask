from flask import Flask, render_template, request, redirect
from database import create_table, add_product, get_product_by_id, delete_product, update_product, get_products

app = Flask(__name__)

@app.route('/')
def index():
    product = get_products()
    return render_template('index.html', product=product)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/add_product', methods=['POST'])
def add():
    name = request.form['name']
    quantity = request.form['quantity']
    price = request.form['price']
    add_product(name, quantity, price)
    return redirect('/')

@app.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edit(product_id):
    if request.method == 'GET':
        product = get_product_by_id(product_id)
        return render_template('edit.html', product=product)
    elif request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']
        update_product(product_id, name, quantity, price)
        return redirect('/')

@app.route('/delete_product/<int:product_id>')
def delete(product_id):
    delete_product(product_id)
    return redirect('/')

if __name__ == "__main__":
    create_table()
    app.run(debug=True, port=5001)