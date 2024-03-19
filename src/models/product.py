class Product:
    def __init__(self, 
                 product_id: int, 
                 setup_type: str, 
                 name: str, 
                 description: str):
        self.product_id = product_id
        self.setup_type = setup_type
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.product_id} - {self.setup_type} - {self.name}'