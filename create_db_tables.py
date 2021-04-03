from psycopg2 import connect, sql
import configparser

from queries import create_table_queries


config = configparser.ConfigParser()
config.read_file(open('db.cfg'))
USER = config.get('USERNAME')
HOST = config.get('HOST')
DB_NAME = config.get('DB_NAME')


def create_database():
    """
    Creates and connects to the HR database; returns the connection and cursor to HR database
    """

    # connect to the default database
    conn = connect(f'host={HOST} dbname=postgres user={USER}')
    curr = conn.cursor()

    # create database
    curr.execute(sql.SQL(f'CREATE DATABASE {DB_NAME};'))

    # close connection to default
    curr.close()

    # connect to newly created database
    conn = connect(f'host={HOST} dbname={DB_NAME} user={USER}')
    curr = conn.cursor()

    return curr, conn


def create_tables(curr, conn):
    '''
    Create tables using queries in 'create_tables' module
    '''

    for query in create_table_queries:
        print(f'Running {query}...')
        curr.execute(query)
        conn.commit()


def main():
    """
    Establishes connection to hr_tech_abc database & gets the cursor to it.
    Creates all tables needed & closes connection.
    """

    curr, conn = create_database()
    create_tables(curr, conn)

    conn.close()


if __name__ == "__main__":
    main()
