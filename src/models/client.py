class Client:
    def __init__(self, 
                 client_id: str, 
                 company_name: str, 
                 contact_person: str, 
                 contact_no: str, 
                 email_address: str):
        self.client_id = client_id
        self.company_name = company_name
        self.contact_person = contact_person
        self.contact_no = contact_no
        self.email_address = email_address

    def __str__(self):
        return f'{self.id} - {self.company_name}'