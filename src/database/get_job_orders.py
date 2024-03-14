from models.job_order import JobOrder

def get_job_order_numbers() -> list[dict]:
    """ Gets job order numbers for dropdown list """
    return [
        {'label': 'ABC123', 'value': 'ABC123'},
        {'label': 'DEF456', 'value': 'DEF456'},
        {'label': 'GHI789', 'value': 'GHI789'}
    ]