#!/usr/bin/python3

"""list all cities from the database hbtn_0e_4_usa"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

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
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC;")

    # Fetch all rows and display results
    results = cur.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
