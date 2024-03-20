from models.client import Client
from database.postgres import execute_raw_query

query = """
    SELECT c.client_id, c.company_name, c.contact_person, c.contact_no, c.email_address
    FROM msdbom.client c
    ORDER BY c.client_id;
"""

def get_clients() -> list[Client]:
    results = execute_raw_query(query)
    if not results:
        return []
    
    return [Client(**result) for result in results]