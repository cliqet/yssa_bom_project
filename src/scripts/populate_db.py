import csv
import os
from database.postgres import initialize_sql_database, execute_raw_query
from config.configuration import ROOT_DIR

"""
cd to src directory
Run python -m scripts.populate_db
"""

def main():
    initialize_sql_database()
    print('Initializing sql database')

    print('Inserting records into client table...')
    # populate client table
    with open(os.path.join(ROOT_DIR, 'database', 'csv_files', 'clienttable.csv'), 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')

        for row in reader:
            id = row[0]
            company_name = row[1]
            contact_person = row[2]
            contact_no = row[3]
            email = row[4]

            execute_raw_query(
                f"""
                    INSERT INTO msdbom.client (company_name, contact_person, contact_no, email_address) 
                    VALUES (%s, %s, %s, %s);
                """,
                [company_name, contact_person, contact_no, email]
            )
            print(f'Inserting record {id}')

    print('Inserting records into product table...')
    # populate product table
    with open(os.path.join(ROOT_DIR, 'database', 'csv_files', 'producttable.csv'), 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')

        for row in reader:
            id = row[0]
            setup_type = row[1]
            name = row[2]
            description = row[3]

            execute_raw_query(
                f"""
                    INSERT INTO msdbom.product (setup_type, name, description) 
                    VALUES (%s, %s, %s);
                """,
                [setup_type, name, description]
            )
            print(f'Inserting record {id}')

    print('Inserting records into department table...')
    # populate department table
    with open(os.path.join(ROOT_DIR, 'database', 'csv_files', 'department.csv'), 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')

        for row in reader:
            id = row[0]
            department_name = row[1]

            execute_raw_query(
                f"""
                    INSERT INTO msdbom.department (department_name) 
                    VALUES (%s);
                """,
                [department_name]
            )
            print(f'Inserting record {id}')

    print('Inserting records into employee_position table...')
    # populate employee_position table
    with open(os.path.join(ROOT_DIR, 'database', 'csv_files', 'employeeposition.csv'), 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')

        for row in reader:
            id = row[0]
            employee_position_title = row[1]

            execute_raw_query(
                f"""
                    INSERT INTO msdbom.employee_position (employee_position_title) 
                    VALUES (%s);
                """,
                [employee_position_title]
            )
            print(f'Inserting record {id}')

    print('Inserting records into employee table...')
    # populate employee table
    with open(os.path.join(ROOT_DIR, 'database', 'csv_files', 'employeetable.csv'), 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')

        for row in reader:
            id = row[0]
            first_name = row[1]
            last_name = row[2]
            department = row[3] if row[3] else None
            position_title = row[4] if row[4] else None
            contact_no = row[5]
            email = row[6]

            execute_raw_query(
                f"""
                    INSERT INTO msdbom.employee (first_name, last_name, department_id, employee_position_id, contact_no, email_address) 
                    VALUES (%s, %s, %s, %s, %s, %s);
                """,
                [first_name, last_name, department, position_title, contact_no, email]
            )
            print(f'Inserting record {id}')

    print('Finished inserting records')

    # populate job order table
    # with open(os.path.join(ROOT_DIR, 'database', 'csv_files', 'jobomlisttable.csv'), 'r') as csv_file:
    #     reader = csv.reader(csv_file, delimiter=';')

    #     for row in reader:
    #         jo_no = row[0]
    #         sales_executive = row[1]
    #         date_created = row[2]
    #         event_name = row[3]
    #         venue = row[4]
    #         event_start_date = row[5]
    #         event_end_date = row[6]
    #         company_name = row[7]
    #         contact_person = row[8]
    #         contact_no = row[9]
    #         email = row[10]
    #         ingress_date = row[11]
    #         ingress_time = row[12]
    #         egress_date = row[13]
    #         egress_time = row[14]
    #         prepared_by = row[15]
    #         reviewed_by = row[16]
    #         approved_by = row[17]

if __name__ == '__main__':
    main()