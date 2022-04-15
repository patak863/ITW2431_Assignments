# Name: Mike Patak
# ITW 2431
# Project 12 Prob. 1
# File name: ITW2431_P12_P1_mpatak.py
# MODIFIED: 4/14/22
# PURPOSE:  Create a database named 'company.sqlite' and within the
#           database define four tables: department, employee, project, and
#           works_on. The program will then execute three SQL queries.
# ASSUMPTIONS: database 'company.sqlite' does not already exist
###########################################################################

# import the sqlite3 module
import sqlite3

conn = sqlite3.connect(r'world_updated.db')
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

for y in cur.fetchall():
    print(y)

print('\nColumns in \'city\' table')
data=cur.execute("SELECT * FROM city LIMIT 5")
for column in data.description:
    print(column[0])

for row in data:
    print(row)
city_name = "King's Landing"
#cur.execute("INSERT INTO city (ID, cityName, CountryCode, District, Population_City) "
#            "VALUES(?, ?, ?, ?, ?)", (5000, city_name, 'WTO', '', 5000000000))

cur.execute("SELECT * FROM city WHERE ID=5000 ")
print(cur.fetchall())

print('\nColumns in \'country\' table')
data=cur.execute("SELECT * FROM country ")
for column in data.description:
    print(column[0])

data=cur.execute("SELECT cityName FROM city WHERE Population_City=1000000 ") # WHERE Code='WTO' ")
#data=cur.execute("SELECT countryName, Continent, Region, Population_country FROM country WHERE Population_country > 1000000000 ")
print(cur.fetchall())

