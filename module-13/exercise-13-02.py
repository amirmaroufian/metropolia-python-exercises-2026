from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="flight_game",
    password="123456",
    autocommit=True
)


@app.route("/airport/<icao>")
def airport(icao):
    cursor = connection.cursor()

    sql = """
    SELECT ident, name, municipality
    FROM airport
    WHERE ident = %s
    """

    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    if result:
        response = {
            "ICAO": result[0],
            "Name": result[1],
            "Location": result[2]
        }
    else:
        response = {
            "Error": "Airport not found"
        }

    return jsonify(response)


if __name__ == "__main__":
    app.run()