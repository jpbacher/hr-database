from psycopg2 import connect, sql
import configparser

import project
from queries import insert_table_queries


config = configparser.ConfigParser()
config.read_file(open('db.cfg'))
USER = config.get('DATABASE', 'USERNAME')
HOST = config.get('DATABASE', 'HOST')
DB_NAME = config.get('DATABASE', 'DB_NAME')


def load_data_into_tables(curr, conn):
    """
    Load the given csv file into the staging table, and transfer records to appropriate tables.
    """

    # load staging table
    print(f'Loading staging table...')
    curr.execute(sql.SQL(f"COPY HR_Stage "
                         f"FROM '{project.DATA_DIR/'clean_hr_data.csv'}'"
                         f"DELIMITER ',' "
                         f"CSV HEADER;"))
    conn.commit()

    # load records of all the database tables
    for query in insert_table_queries:
        print(f'Running {query}...')
        curr.execute(query)
        conn.commit()


def main():

    conn = connect(f'host={HOST} dbname={DB_NAME} user={USER}')
    curr = conn.cursor()

    load_data_into_tables(curr, conn)


if __name__ == "__main__":
    main()
