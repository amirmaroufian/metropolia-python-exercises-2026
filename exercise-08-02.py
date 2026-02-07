import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='newuser',
         user='newuser',
         password='12345',
         autocommit=True
         )

def get_airport_type(area_code):
    sql = f"SELECT type FROM airport WHERE iso_country='{area_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    airport_counts = {}

    if cursor.rowcount > 0:
        for row in result:
            airport_type = row[0]
            if airport_type in airport_counts:
                airport_counts[airport_type] += 1
            else:
                airport_counts[airport_type] = 1

    for airport_type in sorted(airport_counts):
        print(f"{airport_type}: {airport_counts[airport_type]}")


area_code = input("Enter Area Code: ")
get_airport_type(area_code)
