# Drop tables if exist
hr_staging_table_drop = "DROP TABLE IF EXISTS HR_Stage"
manager_table_drop = "DROP TABLE IF EXISTS Manager"
department_table_drop = "DROP TABLE IF EXISTS Department"
education_table_drop = "DROP TABLE IF EXISTS Education"
job_table_drop = "DROP TABLE IF EXISTS Job"
employee_table_drop = "DROP TABLE IF EXISTS Employee"
location_table_drop = "DROP TABLE IF EXISTS Location"
address_table_drop = "DROP TABLE IF EXISTS Address"
employment_history_table_drop = "DROP TABLE IF EXISTS Employment_History"


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
        state VARCHAR(2),
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
    CREATE TABLE IF NOT EXISTS Location(
        location_id SERIAL PRIMARY KEY,
        location VARCHAR(50)
    );
""")


address_table_create = ("""
    CREATE TABLE IF NOT EXISTS Address(
        address_id SERIAL PRIMARY KEY,
        address VARCHAR(50),
        location_id INT REFERENCES Location(location_id),
        city VARCHAR(50),
        state VARCHAR(2)
    );
""")


employment_history_table_create = ("""
    CREATE TABLE IF NOT EXISTS Employment_History(
        emp_id INT REFERENCES Employee(emp_id),
        job_title_id INT REFERENCES Job(job_title_id),
        education_lvl_id INT REFERENCES Education(education_lvl_id),
        manager_id INT REFERENCES Manager(manager_id),
        dept_id INT REFERENCES Department(dept_id),
        address_id INT REFERENCES Address(address_id),
        start_dt DATE,
        end_dt DATE,
        salary INT,
        PRIMARY KEY (emp_id, job_title_id)
    );
""")


manager_table_insert = ("""
    INSERT INTO Manager (manager)
        SELECT DISTINCT(manager)
        FROM HR_Stage;
""")


department_table_insert = ("""
    INSERT INTO Department (dept_nm)
        SELECT DISTINCT(department_nm)
        FROM HR_Stage;
""")


education_table_insert = ("""
    INSERT INTO Education (education_lvl)
        SELECT DISTINCT(education_lvl)
        FROM HR_Stage;
""")


job_table_insert = ("""
    INSERT INTO Job (job_title)
        SELECT DISTINCT(job_title)
        FROM HR_Stage;
""")


employee_table_insert = ("""
    INSERT INTO Employee (emp_name, email, hire_dt)
        SELECT DISTINCT(emp_name), email, hire_dt 
        FROM HR_Stage;
""")


location_table_insert = ("""
    INSERT INTO Location (location)
        SELECT DISTINCT(location)
        FROM HR_Stage;
""")


address_table_insert = ("""
    INSERT INTO Address (address, location_id, city, state)
        SELECT DISTINCT(stg.address), l.location_id, stg.city, stg.state
        FROM HR_Stage stg
        JOIN Location l
        ON l.location = stg.location;
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
        ON j.job_title = stg.job_title
        JOIN Education edu
        ON edu.education_lvl = stg.education_lvl
        JOIN Manager m
        ON m.manager = stg.manager
        JOIN Department d
        ON d.dept_nm = stg.department_nm
        JOIN ADDRESS a
        ON a.address = stg.address;
""")


# query list
create_table_queries = [hr_staging_table_create, manager_table_create, department_table_create,
                        education_table_create, job_table_create, employee_table_create,
                        location_table_create, address_table_create, employment_history_table_create]


drop_table_queries = [hr_staging_table_drop, manager_table_drop, department_table_drop,
                      education_table_drop, job_table_drop, employee_table_drop,
                      location_table_drop, address_table_drop, employment_history_table_drop]


insert_table_queries = [manager_table_insert, department_table_insert, education_table_insert,
                        job_table_insert, employee_table_insert, location_table_insert,
                        address_table_insert, employment_history_table_insert]


# CRUD queries
web_programmer_job_insert = ("""
    INSERT INTO Job (job_title)
    VALUES ('Web Programmer');
""")


web_programmer_to_web_developer_job = ("""
    INSERT INTO Job (job_title)
    VALUES ('Web Developer')
    WHERE job_title = 'Web Programmer'
""")


web_developer_job_delete = ("""
    DELETE FROM Job
    WHERE job_title = 'Web Developer'
""")


create_employee_attributes_view = ("""
    CREATE VIEW employee_attributes AS
      SELECT e.emp_id, e.emp_name, e.email, e.hire_dt, ehist.start_dt, j.job_title,
        d.dept_nm, edu.education_lvl
      FROM Employee e
      JOIN Employment_History ehist
      ON e.emp_id = ehist.emp_id
      JOIN Job j
      ON ehist.job_title_id = j.job_title_id
      JOIN Department d
      ON ehist.dept_id = d.dept_id
      JOIN Education edu
      ON ehist.education_lvl_id = edu.education_lvl_id
      WHERE end_dt IS NULL;
""")


get_employee_job_history_procedure = ("""
    CREATE FUNCTION retrieve_employee_job_history(emp_name VARCHAR(100)
    BEGIN
        SELECT e.emp_name, j.job_title, d.dept_nm, m.manager, start_dt, end_dt
        FROM Employee e
        JOIN Employee_History ehist
        ON e.emp_id = ehist.emp_id
        JOIN Job j
        ON ehist.job_title_id = j.job_title_id
        JOIN Department d
        ON ehist.dept_id = d.dept_id 
        JOIN Manager m
        ON ehist.manager_id = m.manager_id;
    END;
    LANGUAGE 'plpgsql';
""")
