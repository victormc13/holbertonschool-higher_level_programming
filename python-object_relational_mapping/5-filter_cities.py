#!/usr/bin/python3

"""list all cities of a given state from the database hbtn_0e_4_usa"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    state_name = sys.argv[4]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
               host='localhost',
               port=3306,
               user=username,
               passwd=password,
               db=database
        )
    except Exception:
        print("Could not connect to database")
        sys.exit(1)

    # Create cursor object
    cur = db.cursor()

    # Execute query with user input
    cur.execute("SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')\
                FROM cities\
                JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC;", (state_name,))

    # Fetch all rows and display results
    result = cur.fetchone()
    if result:
        print(result[0])

    # Close the cursor and database connection
    cur.close()
    db.close()
