import os
import sys
from config.configuration import ROOT_DIR
from database.postgres import initialize_sql_database, execute_raw_query

"""
cd to src directory
Run python -m scripts.create_db
"""

def main():
    while True:
        response = input('Do you have an empty database setup? Press y to continue: ')
        if response == 'y':
            break
        else:
            print('\nSetup empty database first')
            sys.exit(0)


    initialize_sql_database()
    print('Initializing sql database')

    with open(os.path.join(ROOT_DIR, 'database', 'sql_files', 'init.sql'), 'r') as sql_file:
        sql_contents = sql_file.read()
        execute_raw_query(sql_contents)

    print('Database created')

if __name__ == '__main__':
    main()