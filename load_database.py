from psycopg2 import connect, sql
from create_tables import create_table_queries


def create_database(db_name):
    """
    Creates and connects to the HR database; returns the connection and cursor to HR database
    """

    # connect to the default database
    conn = connect("host=127.0.0.1 dbname=postgres user=joshbacher")
    curr = connect.cursor()

    # create database
    curr.execute(sql.SQL(f'CREATE DATABASE {db_name}'))

    # close connection to default
    curr.close()

    # connect to newly created database
    conn = connect("host=127.0.0.1 dbname=db_name user=joshbacher")
    curr = conn.cursor()

    return curr, conn
