# Create staging table for the current data
hr_staging_table_create = ("""
    CREATE TABLE IF NOT EXISTS HR_Stage(
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
    CREATE TABLE IF NOT EXISTS Manager(
        manager_id SERIAL PRIMARY KEY,
        manager VARCHAR(50)
    );
""")


department_table_create = ("""
    CREATE TABLE IF NOT EXISTS Department(
        dept_id SERIAL PRIMARY KEY,
        dept_nm VARCHAR(50)
    );
""")


education_table_create = ("""
    CREATE TABLE IF NOT EXISTS Education(
        education_lvl_id SERIAL PRIMARY KEY,
        education_lvl VARCHAR(50)
    );
""")


job_table_create = ("""
    CREATE TABLE IF NOT EXISTS Job(
        job_title_id SERIAL PRIMARY KEY,
        job_title VARCHAR(100)
    );
""")


employee_table_create = ("""
    CREATE TABLE IF NOT EXISTS Employee(
        emp_id SERIAL PRIMARY KEY,
        emp_name VARCHAR(100),
        email VARCHAR(100),
        hire_dt DATE
    );
""")


location_table_create = ("""
    CREATE TABLE IF NOT EXISTS Location
        location_id SERIAL PRIMARY KEY,
        location VARCHAR(50)
    );
""")


address_table_create = ("""
    CREATE TABLE IF NOT EXISTS Address(
        address_id SERIAL PRIMARY KEY,
        location_id INT REFERENCES location(location_id),
        city VARCHAR(2),
        state VARCHAR(50)
    );
""")


employment_history_table_create = ("""
    CREATE TABLE IF NOT EXISTS Employment_History(
        emp_id INT REFERENCES employee(emp_id),
        job_title_id INT REFERENCES job(job_title_id),
        education_lvl_id INT REFERENCES education(education_lvl_id),
        manager_id INT REFERENCES manager(manager_id),
        department_id INT REFERENCES department(department_id),
        address_id INT REFERENCES address(address_id),
        start_dt DATE,
        end_dt DATE,
        salary INT,
        PRIMARY KEY (emp_id, job_title_id)
    );
""")


manager_table_insert = ("""
    INSERT INTO Manager (manager)
        SELECT DISTINCT(manager)
        FROM HR_Stage
""")


department_table_insert = ("""
    INSERT INTO Department (dept_nm)
        SELECT DISTINCT(department_nm)
        FROM HR_Stage
""")


education_table_insert = ("""
    INSERT INTO Education (education_lvl)
        SELECT DISTINCT(education_lvl)
        FROM HR_Stage
""")


job_table_insert = ("""
    INSERT INTO Job (job_title)
        SELECT DISTINCT(job_title)
        FROM HR_Stage
""")


employee_table_insert = ("""
    INSERT INTO Employee (emp_name, email, hire_dt)
        SELECT DISTINCT(employee), email, hire_dt
        FROM HR_Stage
""")


location_table_insert = ("""
    INSERT INTO Location (location)
        SELECT DISTINCT(location)
        FROM HR_Stage
""")


address_table_insert = ("""
    INSERT INTO Address (address, location_id, city, state)
        SELECT DISTINCT(stg.address), l.location_id, stg.city, stg.state
        FROM HR_Stage stg
        JOIN Location l
        ON l.location_id = stg.location_id
""")


employment_history_table_insert = ("""
    INSERT INTO Employment_History (emp_id, job_title_id, education_lvl_id, manager_id, dept_id,
                                    address_id, start_dt, end_dt, salary)
        SELECT e.emp_id, j.job_title_id, edu.education_lvl_id, m.manager_id, d.dept_id, a.address_id, 
            start_dt, end_dt, salary
        FROM Employee e
        JOIN HR_Stage stg
        ON e.emp_name = stg.emp_name
        JOIN Job j
        ON j.job_tile = stg.job_title
        JOIN Education edu
        ON edu.education_lvl = stg.education_lvl
        JOIN Manager m
        ON m.manager = stg.manager
        JOIN Department d
        ON d.dept_nm = stg.department_nm
        JOIN ADDRESS a
        ON a.address = stg.address
""")


# query list
create_table_queries = [hr_staging_table_create, manager_table_create, department_table_create,
                        education_table_create, job_table_create, employee_table_create,
                        location_table_create, address_table_create, employment_history_table_create]
