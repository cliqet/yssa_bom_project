class Client:
    def __init__(self, id: str, company_name: str, contact_person: str, contact_number: str, email: str):
        self.id = id
        self.company_name = company_name
        self.contact_person = contact_person
        self.contact_number = contact_number
        self.email = email

    def __str__(self):
        return f'{self.id} - {self.company_name}'