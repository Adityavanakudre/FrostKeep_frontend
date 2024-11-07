from flask import Flask, render_template, redirect, url_for, request
import requests
from datetime import datetime

app = Flask(__name__)
API_URL = "https://inventory-fulfillment.up.railway.app/api/products"

# Route to get and display all products
@app.route('/products', methods=['GET'])
def get_all_products():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        products = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching products: {e}")
        products = []
    return render_template('products.html', products=products)

# Route to delete a product
@app.route('/products/<int:id>/delete', methods=['POST'])
def delete_product(id):
    try:
        response = requests.delete(f"{API_URL}/{id}")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error deleting product: {e}")
    return redirect(url_for('get_all_products'))

# Route to update a product
@app.route('/products/<int:id>/update', methods=['POST'])
def update_product(id):
    product_data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "price": request.form['price'],
        "quantity": request.form['quantity']
    }
    try:
        response = requests.put(f"{API_URL}/{id}", json=product_data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error updating product: {e}")
    return redirect(url_for('get_all_products'))

# Route to create a new product
@app.route('/products/create', methods=['POST'])
def create_product():
    new_product_data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "price": request.form['price'],
        "quantity": request.form['quantity']
    }
    try:
        response = requests.post(API_URL, json=new_product_data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error creating product: {e}")
    return redirect(url_for('get_all_products'))

# Route to get deleted products
@app.route('/products/deleted', methods=['GET'])
def get_deleted_products():
    try:
        response = requests.get(f"{API_URL}/deleted")
        response.raise_for_status()
        deleted_products = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching deleted products: {e}")
        deleted_products = []
    return render_template('deleted_products.html', deleted_products=deleted_products)

# Route to restore a deleted product
@app.route('/products/restore/<int:id>', methods=['POST'])
def restore_product(id):
    try:
        response = requests.put(f"{API_URL}/restore/{id}")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error restoring product: {e}")
    return redirect(url_for('get_deleted_products'))

# Route to fetch product history
@app.route('/products/<int:id>/history', methods=['GET'])
def product_history(id):
    try:
        response = requests.get(f"{API_URL}/{id}/history")
        response.raise_for_status()
        history = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching product history: {e}")
        history = []
    return render_template('product_history.html', history=history, product_id=id)

# Route to revert product to a specific version
@app.route('/products/<int:id>/revert/<int:version_id>', methods=['POST'])
def revert_product_version(id, version_id):
    try:
        response = requests.put(f"{API_URL}/{id}/revert/{version_id}")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error reverting product: {e}")
    return redirect(url_for('get_all_products'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Pass current year to home page
@app.route('/')
def home():
    return render_template('index.html', year=datetime.now().year)    

# Custom Jinja filter to format dates
@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y-%m-%d %H:%M:%S'):
    if isinstance(value, str):
        # Parse the string into a datetime object
        value = datetime.fromisoformat(value)
    return value.strftime(format)    

# # Home route to redirect to products page
# @app.route('/')
# def home():
#     return redirect(url_for('get_all_products'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
