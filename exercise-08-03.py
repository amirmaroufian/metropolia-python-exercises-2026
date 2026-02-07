import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='newuser',
         user='newuser',
         password='12345',
         autocommit=True
         )


def get_two_airports_distance(first_airport, second_airport):
    sql = F"SELECT ident, latitude_deg, longitude_deg FROM airport WHERE ident='{first_airport}' OR ident='{second_airport}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()



    if cursor.rowcount > 0:
        # first = (result[0][0], result[0][1])
        # second = (result[1][0], result[1][1])
        # print(f"Distance is {distance.distance(first, second).km} KM")

        airports = {}

        for ident, lat, lon in result:
            airports[ident] = (lat, lon)

        if first_airport not in airports or second_airport not in airports:
            print("One or both ICAO codes are not found!")
            return

        print(f"Distance is {distance.distance(airports[first_airport], airports[second_airport]).km} KM")




first_airport = input("Enter the ICAO of the first airport: ")
second_airport = input("Enter the ICAO of the second airport: ")

get_two_airports_distance(first_airport, second_airport)