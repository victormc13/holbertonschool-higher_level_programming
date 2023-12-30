#!/usr/bin/python3

"""displays all values in the states table of hbtn_0e_0_usa
where name matches the argument"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

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
    cur.execute("SELECT * FROM states\
                WHERE BINARY name = '{}'\
                ORDER BY id ASC;".format(state_name))

    # Fetch all rows and display results
    results = cur.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
