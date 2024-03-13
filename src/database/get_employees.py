from models.employee import Employee


def get_employee_names() -> list[dict]:
    """ Use to get employee names for dropdown """
    return [
        {'label': 'Employee 1', 'value': 'employee1'},
        {'label': 'Employee 2', 'value': 'employee2'},
        {'label': 'Employee 3', 'value': 'employee3'}
    ]