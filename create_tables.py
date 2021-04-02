# Create staging table for the current data
hr_staging_table_create = ("""
    CREATE TABLE IF NOT EXISTS hr_stage(
        emp_ID varchar(8),
        emp_name varchar(50),
        email varchar(100),
        hire_dt date,
        job_title varchar(100),
        salary int,
        department_nm varchar(50),
        manager varchar(50),
        start_dt date,
        end_dt date,
        location varchar(50),
        address varchar(50),
        city varchar(50),
        state varchar(2),
        education_lvl varchar(50)
    );
""")


manager_table_create = ("""
    CREATE TABLE IF NOT EXISTS manager(
        manager_id SERIAL PRIMARY KEY,
        manager VARCHAR(50)
    );
""")
