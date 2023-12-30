#!/usr/bin/python3

"""filter and display states based on the provided state name,
safe from SQL injection"""


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
    cur.execute("SELECT * FROM states\
                WHERE name = %s\
                ORDER BY id ASC;", (state_name,))

    # Fetch all rows and display results
    results = cur.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
