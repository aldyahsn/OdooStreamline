import xmlrpc.client
import json

class API:
    
    def __init__(self, url, db, username, password):
        self.url = url
        self.db = db
        self.username = username
        self.password = password
        self.uid = self._authenticate()
        self.models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

    def _authenticate(self):
        common = xmlrpc.client.ServerProxy(f'{self.url}/xmlrpc/2/common')
        return common.authenticate(self.db, self.username, self.password, {})
   
    # ====================
    # CREATE 
    # ====================
    
    def create_product(self, product_data):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.template', 'create', [product_data])

    def create_attribute(self, name):
        attribute_id = self.models.execute_kw(self.db, self.uid, self.password, 'product.attribute', 'create', [{'name': name}])
        print(f'Attribute "{name}" created with ID: {attribute_id}')
        return attribute_id

    def create_attribute_value(self, attribute_id, value):
        value_id = self.models.execute_kw(self.db, self.uid, self.password, 'product.attribute.value', 'create', [{
            'name': value,
            'attribute_id': attribute_id,
        }])
        print(f'Value "{value}" created with ID: {value_id}')
        return value_id

    def link_attribute_values_to_product(self, product_template_id, attribute_id, value_ids):
        self.models.execute_kw(self.db, self.uid, self.password, 'product.template.attribute.line', 'create', [{
            'product_tmpl_id': product_template_id,
            'attribute_id': attribute_id,
            'value_ids': [(6, 0, value_ids)],
        }])
        print(f'Linked attribute values {value_ids} to product template ID: {product_template_id}')
    
    def create_product_with_variant(self):
        # Create a Product Variable
        # ===============================
        '''
        product_template_data = {
            'name': 'Chair',
            'type': 'product',
        }

        product_template_id = odoo_crud.create_product(product_template_data)

        # Create or find the "Material" attribute
        material_attribute_id = odoo_crud.create_attribute('Size')

        # Create the "OAK" and "TEAK" attribute values
        oak_value_id = odoo_crud.create_attribute_value(material_attribute_id, 'Small')
        teak_value_id = odoo_crud.create_attribute_value(material_attribute_id, 'Large')

        # Link the attribute values to the product template
        odoo_crud.link_attribute_values_to_product(product_template_id, material_attribute_id, [oak_value_id, teak_value_id])

        '''
        pass
    # ====================
    # SEARCHING 
    # ====================
    
    def get_productlist(self, domain=[], fields=['name', 'list_price', 'default_code', 'description']):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.template', 'search_read', [domain], {'fields': fields})

    def get_productlist_ID(self, domain=[]):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.template', 'search', [domain])

    
    def get_variantlist(self, domain=[], fields=['name', 'default_code', 'product_tmpl_id']):
        return  self.models.execute_kw(self.db, self.uid, self.password, 'product.product', 'search_read', [domain], {'fields':fields})
    
    def get_variantlist_ID(self, domain=[]):
        return  self.models.execute_kw(self.db, self.uid, self.password, 'product.product', 'search', [domain],)
    
    
    def get_product(self, product_id):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.template', 'read', [[product_id]])
    
    def get_variant(self, variant_id):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.product', 'read', [[variant_id]])

    
    
# Set variable
odoo_url = 'https://hamesha-dev2.odoo.com'
db = 'hamesha-dev2'
username = 'aldy.ahsandin@gmail.com'
password = '114b2a139c7b22b425ba9564f0b300c9837decd6'

odoo_crud = API(odoo_url, db, username, password)

print(json.dumps(odoo_crud.get_variantlist(), indent=4))




