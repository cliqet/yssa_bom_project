class Employee:
    def __init__(self, id: str, full_name: str, department: str, contact_number: str, email: str):
        self.id = id
        self.full_name = full_name
        self.department = department
        self.contact_number = contact_number
        self.email = email

    def __str__(self):
        return f'{self.id} - {self.full_name}'