from psycopg2 import connect, sql
import configparser

from create_tables import create_table_queries
import project


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


def load_stage_table(curr, conn, filename):
    conn = connect(f'host={HOST} dbname={DB_NAME} user={USER}')
    curr = conn.cursor()

    curr.execute(sql.SQL(f'COPY hr_stage FROM {project.DATA_DIR/filename} DELIMITER "," CSV HEADER;'))





