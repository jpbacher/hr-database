from psycopg2 import connect, sql
import configparser

import project
from queries import (manager_table_insert, department_table_insert, education_table_insert,
                     job_table_insert, employee_table_insert, location_table_insert,
                     address_table_insert, employment_history_table_insert)


config = configparser.ConfigParser()
config.read_file(open('db.cfg'))
USER = config.get('USERNAME')
HOST = config.get('HOST')
DB_NAME = config.get('DB_NAME')


def load_stage_table(curr, conn, filename):
    conn = connect(f'host={HOST} dbname={DB_NAME} user={USER}')
    curr = conn.cursor()
    hr_stage = curr.execute(sql.SQL(f'COPY hr_stage FROM {project.DATA_DIR/filename} DELIMITER "," CSV HEADER;'))
    return curr, conn, hr_stage


def load_data_into_hr_tables(curr, conn, stage_table):
