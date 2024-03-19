from typing import Callable
from models.employee import Employee
from database.postgres import execute_raw_query

all_employees_query = """
    SELECT e.employee_id, e.first_name, e.last_name, d.department_name, p.employee_position_title,
        e.contact_no, e.email_address
    FROM msdbom.employee e
    LEFT JOIN msdbom.department d ON e.department_id = d.department_id
    LEFT JOIN msdbom.employee_position p ON e.employee_position_id = p.employee_position_id;
"""

all_sales_executives_query = """
    SELECT e.employee_id, e.first_name, e.last_name, d.department_name, p.employee_position_title,
        e.contact_no, e.email_address
    FROM msdbom.employee e
    LEFT JOIN msdbom.department d ON e.department_id = d.department_id
    LEFT JOIN msdbom.employee_position p ON e.employee_position_id = p.employee_position_id
    WHERE p.employee_position_title = 'Sales Executive';
"""

def get_employees() -> list[Employee]:
    results = execute_raw_query(all_employees_query)
    if not results:
        return []
    
    return [Employee(**result) for result in results]

def get_sales_executives() -> list[Employee]:
    results = execute_raw_query(all_sales_executives_query)
    if not results:
        return []
    
    return [Employee(**result) for result in results]

def get_employee_names(db_func: Callable) -> list[dict]:
    """ Use to get employee names for dropdown """
    employees = db_func()

    return [
        {'label': f'{employee.first_name} {employee.last_name}', 'value': employee.employee_id}
        for employee in employees
    ]