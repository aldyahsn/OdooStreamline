import xmlrpc.client

class OdooStreamline:
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
    
    # =================================
    # PRODUCT
    # =================================
    
    def create_product(self, product_data):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.template', 'create', [product_data])

    def read_product(self, product_id):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.template', 'read', [[product_id]])

    def update_product(self, product_id, update_data):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.template', 'write', [[product_id], update_data])

    def delete_product(self, product_id):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.template', 'unlink', [[product_id]])

    def search_products(self, domain=[], fields=['name', 'list_price', 'default_code']):
        """
        Search for products based on specific criteria.
        :param domain: A list of tuples specifying the search criteria.
        :param fields: A list of strings specifying which fields to fetch for each matching product.
        :return: A list of dictionaries, where each dictionary contains data for a product matching the search criteria.
        """
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.template', 'search_read', [domain], {'fields': fields})


    # =================================
    # ATTRIBUTE
    # =================================
    
    # Attribute CRUD
    def create_attribute(self, attribute_data):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.attribute', 'create', [attribute_data])

    def read_attribute(self, attribute_id):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.attribute', 'read', [[attribute_id]])

    def update_attribute(self, attribute_id, update_data):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.attribute', 'write', [[attribute_id], update_data])

    def delete_attribute(self, attribute_id):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.attribute', 'unlink', [[attribute_id]])

    # Variant CRUD
    def create_variant(self, variant_data):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.product', 'create', [variant_data])

    def read_variant(self, variant_id):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.product', 'read', [[variant_id]])

    def update_variant(self, variant_id, update_data):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.product', 'write', [[variant_id], update_data])

    def delete_variant(self, variant_id):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.product', 'unlink', [[variant_id]])