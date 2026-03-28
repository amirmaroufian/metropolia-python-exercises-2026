import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='newuser',
         user='newuser',
         password='12345',
         autocommit=True
         )

def get_airport_data(icao_code):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{icao_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Airport name: {row[0]}\nAirport location: {row[1]}")


icao_code = input("Enter ICAO code: ")
get_airport_data(icao_code)

