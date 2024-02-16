from odoostreamline import OdooStreamline
import json

odoo_url = 'https://hamesha-dev1.odoo.com'
db = 'hamesha-dev1'
username = 'aldy.ahsandin@gmail.com'
password = '6bfefd69991c74ed1c12969fc1fc23a747af5f38'

odoo = OdooStreamline(odoo_url, db,username, password)

# CREATE PRODUCT
# -------------------
# product_id = odoo.create_product({'name': 'New Product', 'list_price': 100.00})
# print(f'Product created with ID: {product_id}')

# GET PRODUCT WITH ID 15
# -------------------
# product = odoo.read_product(15)
# print(json.dumps(product, indent=4))

# UPDATE PRODUCT WITH ID (15)
# -------------------
# update_data = {
#     'name': 'Updated Product Name',
#     'list_price': 999,
# }
# odoo.update_product(15, update_data)


all_products = odoo.search_products()
print(json.dumps(all_products, indent=4))