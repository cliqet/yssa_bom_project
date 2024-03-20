from models.product import Product
from database.postgres import execute_raw_query

query = """
    SELECT p.product_id, p.setup_type, p.name, p.description
    FROM msdbom.product p
    ORDER BY p.product_id;
"""

def get_products() -> list[Product]:
    results = execute_raw_query(query)
    if not results:
        return []
    
    return [Product(**result) for result in results]