class Employee:
    def __init__(self, 
                 employee_id: int, 
                 first_name: str,
                 last_name: str, 
                 department_name: str, 
                 employee_position_title: str,
                 contact_no: str, 
                 email_address: str):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.department_name = department_name
        self.employee_position_title = employee_position_title
        self.contact_no = contact_no
        self.email_address = email_address

    def __str__(self):
        return f'{self.id} - {self.first_name} {self.last_name}'