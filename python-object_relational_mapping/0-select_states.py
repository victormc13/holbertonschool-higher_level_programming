#!/usr/bin/python3

"""list all states from the database hbtn_0e_0e_usa."""


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
    cursor = db.cursor()

    # Execute query
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    # Fetch all rows and display results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
