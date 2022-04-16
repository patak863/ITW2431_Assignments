# Name: Mike Patak
# ITW 2431
# Project 12 Prob. 1
# File name: ITW2431_P12_P1_mpatak.py
# MODIFIED: 4/14/22
# PURPOSE:  Update a database named 'world_updated.db' by adding a new city.
#       Then execute queries to do the following:
#       - Show the city that was added
#       - countries that have a population > 1,000,000
#       - cities in the USA with a poulation > 1,000,000
#       - count the cities in the USA with a poulation > 1,000,000
#       - average population of cities in the USA with a poulation > 1,000,000
#       Print out the results from all these queries.
# ASSUMPTIONS: database 'company.sqlite' does not already exist
###############################################################################

# import the sqlite3 module
import sqlite3

# create a connection to the database 'world_updated.db'
conn = sqlite3.connect(r'world_updated.db')
cur = conn.cursor()

# query to show all the table in the database 'world_updated.db'
#cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
#for y in cur.fetchall():
#    print(y)

# code to print out all the tables in the database
#print('\nColumns in \'city\' table')
#for row in data:
#   print(row)

# code to insert 'King's Landing' into world_updated.db
city_name = "King's Landing"
#cur.execute("INSERT INTO city (ID, cityName, CountryCode, District, Population_City) "
#            "VALUES(?, ?, ?, ?, ?)", (5000, city_name, 'WTO', '', 5000000000))
print("\nQuestion (a)")
cur.execute("SELECT * FROM city WHERE ID=5000 ")
print(cur.fetchall())

# Code to print out the columns in the 'country' table
#print('\nColumns in \'country\' table')
#data=cur.execute("SELECT * FROM country ")
#for column in data.description:
#    print(column[0])

print("\nQuestion (b)")
# query to find all countries whose population is greater than 1,000,000
data=cur.execute("SELECT countryName, Continent, Region, Population_country FROM country WHERE Population_country > 1000000000 ")
# loop through and print out the results
for country in data:
    print(country)

print("Westero did not show up in (b) because we added King's Landing in Westero to the 'city' table.\n"
      "Westero does not exist in the 'country' table so the query would not have found it, and if it was\n"
      "in the country table the population of King's Landing would not have been added to it yet.")

print("\nQuestion (c)")
# query to find all the cities with a population greater than 1,000,000 and in the USA
data=cur.execute("SELECT * FROM city WHERE CountryCode='USA' and Population_City>1000000  ")
# loop through and print out the results
for city in data:
    print(city)

# query to count the number of cities in the USA with a population greater than 1,000,000
data=cur.execute("SELECT COUNT(*) FROM city WHERE CountryCode='USA' and Population_City>1000000 ")
# fetch one object and return the item in the first position
int_num = data.fetchone()[0]
print("\nThe count of cities in the USA with population greater that 1,000,000 is: " + str(int_num))

# query the average population of cities in the USA with a population greater than 1,000,000
data=cur.execute("SELECT AVG(Population_City) FROM city WHERE CountryCode='USA' and Population_City>1000000 ")
# fetch one object and return the item in the first position
int_num = data.fetchone()[0]
print("\nThe average population of cities in the USA with population greater that 1,000,000 is: " + str(int_num))
