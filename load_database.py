from psycopg2 import connect, sql
import configparser

import project
from queries import insert_table_queries


config = configparser.ConfigParser()
config.read_file(open('db.cfg'))
USER = config.get('USERNAME')
HOST = config.get('HOST')
DB_NAME = config.get('DB_NAME')


def load_data_into_tables(curr, conn, filename):
    """
    Load the given csv file into the staging table, and transfer records to appropriate tables.
    """

    conn = connect(f'host={HOST} dbname={DB_NAME} user={USER}')
    curr = conn.cursor()

    # load staging table
    curr.execute(sql.SQL(f'COPY hr_stage FROM {project.DATA_DIR/filename} DELIMITER "," CSV HEADER;'))
    conn.commit()

    # load all tables of the database
    for query in insert_table_queries:
        print(f'Running {query}...')
        curr.execute(query)
        conn.commit()
