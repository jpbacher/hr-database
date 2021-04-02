# Create staging table for the current data
hr_staging_table_create = ("""
    CREATE TABLE IF NOT EXISTS hr_stage(
        emp_ID VARCHAR(8),
        emp_name VARCHAR(50),
        email VARCHAR(100),
        hire_dt DATE,
        job_title VARCHAR(100),
        salary INT,
        department_nm VARCHAR(50),
        manager VARCHAR(50),
        start_dt DATE,
        end_dt DATE,
        location VARCHAR(50),
        address VARCHAR(50),
        city VARCHAR(50),
        state vVARCHAR(2),
        education_lvl VARCHAR(50)
    );
""")

# create final database tables
manager_table_create = ("""
    CREATE TABLE IF NOT EXISTS manager(
        manager_id SERIAL PRIMARY KEY,
        manager VARCHAR(50)
    );
""")


department_table_create = ("""
    CREATE TABLE IF NOT EXISTS department(
        department_id SERIAL PRIMARY KEY,
        department_nm VARCHAR(50)
    );
""")


education_table_create = ("""
    CREATE TABLE IF NOT EXISTS education(
        education_lvl_id SERIAL PRIMARY KEY,
        education_lvl VARCHAR(50)
    );
""")


job_table_create = ("""
    CREATE TABLE IF NOT EXISTS job(
        job_title_id SERIAL PRIMARY KEY,
        job_title VARCHAR(100)
    );
""")


employee_table_create = ("""
    CREATE TABLE IF NOT EXISTS employee(
        emp_id SERIAL PRIMARY KEY,
        emp_name VARCHAR(100),
        email VARCHAR(100),
        hire_dt DATE
    );
""")


location_table_create = ("""
    CREATE TABLE IF NOT EXISTS location
        location_id SERIAL PRIMARY KEY,
        location VARCHAR(50)
    );
""")


address_table_create = ("""
    CREATE TABLE IF NOT EXISTS address(
        address_id SERIAL PRIMARY KEY,
        location_id INT REFERENCES location(location_id),
        city VARCHAR(2),
        state VARCHAR(50)
    );
""")


employment_history_table_create = ("""
    CREATE TABLE IF NOT EXISTS employment_history(
        emp_id INT REFERENCES employee(emp_id),
        job_title_id INT REFERENCES job(job_title_id),
        education_lvl_id INT REFERENCES education(education_lvl_id),
        manager_id INT REFERENCES manager(manager_id),
        department_id INT REFERENCES department(department_id),
        address_id INT REFERENCES address(address_id),
        start_dt DATE,
        end_dt DATE,
        PRIMARY KEY (emp_id, job_title_id)
    );
""")


# query list
create_table_queries = [hr_staging_table_create, manager_table_create, department_table_create,
                        education_table_create, job_table_create, employee_table_create,
                        location_table_create, address_table_create, employment_history_table_create]
