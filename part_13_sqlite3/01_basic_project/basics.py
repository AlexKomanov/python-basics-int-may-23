import sqlite3

# Create a connection to the DB
connection_manager = sqlite3.connect("gta.db")

# Create a cursor object
my_cursor = connection_manager.cursor()

# Create a new table
my_cursor.execute(
    "CREATE TABLE IF NOT EXISTS gta (release_date INTEGER, release_name TEXT, release_city TEXT)")

query_string = """
INSERT INTO gta VALUES (?,?,?)
"""

query_param = (1997, "Grand Theft Auto", "state of New Guernsey")

# my_cursor.execute(query_string, query_param)

release_list = [
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

# my_cursor.executemany(query_string, release_list)

# release_date = int(input("Release Date: "))
# release_name = input("Release Name: ")
# release_city = input("Release City: ")
#
# tuple_of_data = (release_date, release_name, release_city)
#
# my_cursor.execute(query_string, tuple_of_data)

connection_manager.commit()

for row in my_cursor.execute("SELECT * FROM gta WHERE release_date = 1997"):
    print(row)

connection_manager.close()
