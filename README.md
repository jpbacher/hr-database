# hr-database
Converting HR data into a database using PostgreSQL


Tech ABC Inc. has been experiencing rapid growth. The company has grown from 10 employees
to 200 in only 6 months. Thus, HR is experiencing difficulty maintaining simple 
employee information in an Excel spreadsheet.
 

#### Files used for creating database
* *project.py*: displays project structure
* *clean_staging_data.py*: script that removes commas from salary column
* *queries.py*: contains all sql queries, imported into various scripts
* *create_db_tables.py*: creates the HR database, and adds the tables
* *load_database.py*: reads data into the staging table, then loads records into database tables;
creates a view and procedure
* *read_queries.ipynb*: displays output of various questions
* *hrERDPhysical.pdf*: shows the Physical ERD of the database


#### Data that will be stored
* *emp_name* 
* *email*
* *hire_dt*
* *address*
* *city*
* *state*
* *location*
* *manager*
* *dept_nm*
* *education_lvl*
* *job_title*
* *start_dt*
* *end_dt*
* *salary*


#### Owners/Mangers of the data
The HR team will be the owners of the data; they will input and edit information in the 
database.
 

#### User access
* User types: employees
* Restrictions to access: employees will not have access to salary information


#### Access to the data
Any employee with a domain login will be able to access the database. Salary information is
restricted to HR and management only.
 

#### Estimated growth & size of the database
The company is expecting a 20% growth rate per year over the next 5 years - from 200 employees now
to close to 500 employees.
 

#### Data sensitive/restrictions
Salary information restricted to the HR team and management. 
 

#### Data retention/backup & storage
Federal regulation requires employee data be retained for at least 7 years.
 

#### Justification of a database
It is necessary to implement a database over a spreadsheet - one spreadsheet document is 
currently being shared, and thus, data integrity and data security are of great concern to the company.

It is necessary to design an OLTP for Tech ABC's HR department; the data will constantly be updated and added - 
we want this data refreshed quickly.
 

#### Database objects (tables, views, procedures)
- The database consists of 8 tables: **Employment_History**, **Employee**, **Address**,
**Location**, **Manager**, **Department**, **Education**, **Job**
- The database has 1 view: **employee_attribute** - lists all the employee attributes,
*emp_id*, *emp_name*, *email*, *hire_dt*, *start_dt*, *job_title*, *dept_nm*, *education_lvl*
- The database has 1 procedure: **retrieve_employee_job_history**


#### Data ingestion (ingestion method)
The ingestion method will be a simple ETL:

1. Extract data from the Excel file and load into staging table
2. Transform the data to meet requirements of the designed database
3. Load the records from staging table into appropriate database tables


#### Scalability & Flexibility Considerations
Because we expect the employee count to rapidly increase over the next 5 years (20% per year), we will
use a *sharded database*. This approach will allow the HR team to easily 'write' in more data. The downside
to this method is 'reading' times will be slower for users; however, Tech ABC is more concerned
about keeping the HR database up-to-date.
