# Name: Mike Patak
# ITW 2431
# Lab 12 Prob. 1
# File name: ITW2431_L12_P1_mpatak.py
# MODIFIED: 4/10/22
# PURPOSE:  Create a database named 'company.sqlite' and within the
#           database define four tables: department, employee, project, and
#           works_on. The program will then execute three SQL queries.
# ASSUMPTIONS: database 'company.sqlite' does not already exist
###########################################################################

# import the sqlite3 module
import sqlite3
# create a connection to the database 'company.sqlite'
conn = sqlite3.connect('company.sqlite')
# initialize a cursor to the database for executing commands
cur = conn.cursor()
# check if the table already exists, if it does it will be dropped/deleted
cur.execute('DROP TABLE IF EXISTS department')
# create the table 'department' in the database
cur.execute('CREATE TABLE department ('
                'dept_no TEXT NOT NULL, '
                'dept_name TEXT NOT NULL, '
                'location TEXT NULL, '
                'PRIMARY KEY (dept_no))')

# check if the table already exists, if it does it will be dropped/deleted
cur.execute('DROP TABLE IF EXISTS employee')
# create the table 'employee' in the database
cur.execute('CREATE TABLE employee ('
                'emp_no INTEGER NOT NULL, '
                'emp_fname TEXT NOT NULL, '
                'emp_lname TEXT NOT NULL, '
                'dept_no TEXT NOT NULL, '
                'PRIMARY KEY (emp_no), '
                'FOREIGN KEY (dept_no) REFERENCES department (dept_no))')

# check if the table already exists, if it does it will be dropped/deleted
cur.execute('DROP TABLE IF EXISTS project')
# create the table 'project' in the database
cur.execute('CREATE TABLE project ('
                'project_no TEXT NOT NULL, '
                'project_name TEXT NOT NULL, '
                'budget INTEGER NULL,'
                'PRIMARY KEY (project_no))')

cur.execute('DROP TABLE IF EXISTS works_on')
# create the table 'works_on' in the database
cur.execute('CREATE TABLE works_on ('
                'emp_no INTEGER NOT NULL, '
                'project_no TEXT NOT NULL, '
                'job TEXT NULL, '
                'enter_date TEXT NULL, '
                'PRIMARY KEY (emp_no, project_no), '
                'FOREIGN KEY (emp_no) REFERENCES employee(emp_no), '
                'FOREIGN KEY (project_no) REFERENCES project(project_no))')

# Load data into 'department' table
cur.execute('INSERT INTO department (dept_no, dept_name, location) VALUES (?, ?, ?)', ('d1', 'Research', 'Dallas'))
cur.execute('INSERT INTO department (dept_no, dept_name, location) VALUES (?, ?, ?)', ('d2', 'Accounting', 'Seattle'))
cur.execute('INSERT INTO department (dept_no, dept_name, location) VALUES (?, ?, ?)', ('d3', 'Marketing', 'Atlanta'))
# Load data into 'employee' table
cur.execute('INSERT INTO employee (emp_no, emp_fname, emp_lname, dept_no) VALUES (?, ?, ?, ?)', (25348, 'Matthew', 'Smith', 'd3'))
cur.execute('INSERT INTO employee (emp_no, emp_fname, emp_lname, dept_no) VALUES (?, ?, ?, ?)', (10102, 'Ann', 'Jones', 'd3'))
cur.execute('INSERT INTO employee (emp_no, emp_fname, emp_lname, dept_no) VALUES (?, ?, ?, ?)', (18316, 'John', 'Barrimore', 'd1'))
cur.execute('INSERT INTO employee (emp_no, emp_fname, emp_lname, dept_no) VALUES (?, ?, ?, ?)', (29346, 'James', 'James', 'd2'))
cur.execute('INSERT INTO employee (emp_no, emp_fname, emp_lname, dept_no) VALUES (?, ?, ?, ?)', (9031, 'Elke', 'Hansel', 'd2'))
cur.execute('INSERT INTO employee (emp_no, emp_fname, emp_lname, dept_no) VALUES (?, ?, ?, ?)', (28559, 'Sybill', 'Moser', 'd1'))
# Load data into 'project' table
cur.execute('INSERT INTO project (project_no, project_name, budget) VALUES (?, ?, ?)', ('p1', 'Apollo', 1200000))
cur.execute('INSERT INTO project (project_no, project_name, budget) VALUES (?, ?, ?)', ('p2', 'Gemini', 95000))
cur.execute('INSERT INTO project (project_no, project_name, budget) VALUES (?, ?, ?)', ('p3', 'Mercury', 186500))
# Load data into 'works_on' table
cur.execute('INSERT INTO works_on (emp_no, project_no, job, enter_date) VALUES (?, ?, ?, ?)', (10102, 'p1', 'Analyst', '2006.10.1'))
cur.execute('INSERT INTO works_on (emp_no, project_no, job, enter_date) VALUES (?, ?, ?, ?)', (10102, 'p3', 'Manager', '2008.1.1'))
cur.execute('INSERT INTO works_on (emp_no, project_no, job, enter_date) VALUES (?, ?, ?, ?)', (25348, 'p2', 'Clerk', '2007.2.15'))
cur.execute('INSERT INTO works_on (emp_no, project_no, job, enter_date) VALUES (?, ?, ?, ?)', (18316, 'p2', '', '2007.6.1'))
cur.execute('INSERT INTO works_on (emp_no, project_no, job, enter_date) VALUES (?, ?, ?, ?)', (29346, 'p2', '', '2006.12.15'))
cur.execute('INSERT INTO works_on (emp_no, project_no, job, enter_date) VALUES (?, ?, ?, ?)', (9031, 'p1', 'Manager', '2007.4.15'))
cur.execute('INSERT INTO works_on (emp_no, project_no, job, enter_date) VALUES (?, ?, ?, ?)', (28559, 'p1', '', '2007.8.1'))
cur.execute('INSERT INTO works_on (emp_no, project_no, job, enter_date) VALUES (?, ?, ?, ?)', (28559, 'p2', 'Clerk', '2008.2.1'))
cur.execute('INSERT INTO works_on (emp_no, project_no, job, enter_date) VALUES (?, ?, ?, ?)', (9031, 'p3', 'Clerk', '2006.11.15'))
cur.execute('INSERT INTO works_on (emp_no, project_no, job, enter_date) VALUES (?, ?, ?, ?)', (29346, 'p1', 'Clerk', '2077.1.4'))
# commit the changes to the database
conn.commit()
print()
print('-- All employee information in the employee table --')
# SQL to return all the information from the 'employee' table
cur.execute('SELECT * FROM employee')
# fetch all the result from the executed SQL query
print(cur.fetchall())
print()
print('-- All departments in the department table --')
# SQL to return all the department names from the 'department' table
cur.execute('SELECT dept_name FROM department')
# fetch all the result from the executed SQL query
print(cur.fetchall())
print()
print('-- Employee names with department names and locations working on project Gemini--')
# initialize string for project name
str_project_name = 'Gemini'
# SQL multi table join, we specifically want to know who worked on project Gemini so the first join needs
# to be the 'project' table and the 'works_on' table. This will get the emp_no from 'works_on' associated with
# project Gemini. Then need to join with 'employee' and then join with 'department'
cur.execute('SELECT employee.emp_fname, employee.emp_lname, department.dept_name, department.location, project.project_name FROM project '
            'JOIN works_on ON project.project_no = works_on.project_no '
            'JOIN employee ON employee.emp_no = works_on.emp_no '
            'JOIN department ON department.dept_no = employee.dept_no '
            'WHERE project.project_name=?', [str_project_name])
# fetch all the result from the executed SQL query
print(cur.fetchall())
print()
# close the connection to database
conn.close()
