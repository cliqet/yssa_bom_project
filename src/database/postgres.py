from typing import List, Any

import psycopg

from config.configuration import config


__conn: psycopg.Connection = None


def initialize_sql_database():
    global __conn

    __conn = psycopg.connect(config.database.psql.connection_string)
    with __conn.cursor() as cur:
        cur.execute('SELECT VERSION()')
        result = cur.fetchone()
        if result is not None:
            print("Database connection successful!")
            print("PostgreSQL version:", result[0])
        else:
            print("Failed to establish database connection.")


def execute_raw_query(query: str, params: List[Any] | None = None) -> list[dict] | None:
    global __conn
    
    try:
        with __conn.cursor() as cursor:
            cursor.execute(query, params if params else None)

            if cursor.description:  # Check if the query has a result set
                columns = [desc[0] for desc in cursor.description]
                rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
            else:
                rows = None
            
            __conn.commit()
            return rows

    except (psycopg.ProgrammingError, psycopg.DatabaseError) as error:
        __conn.rollback()
        print('internal server error, rolling back..')
        raise error
